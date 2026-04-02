# Chapter 04: The Query Loop

The query loop is the central mechanism of Claude Code. It is the agentic cycle that drives the entire system: sending messages to the Anthropic API, interpreting the model's responses, executing tool calls, and repeating until completion. This chapter describes its operation in full.

## Parameters

The query loop is invoked with a set of parameters that govern its behavior:

- A **message history** containing all prior messages in the conversation
- A **system prompt** assembled from multiple sections (identity, system, doing tasks, executing actions, tone, output efficiency)
- A **user context** and **system context** providing environment-specific information
- A **tool use context** that carries the available tools, permission mode, and model configuration
- A **query source** indicating where the query originated (typically "repl" for interactive use)
- An optional **fallback model** to use if the primary model fails
- An optional **maximum output tokens override**
- An optional **maximum turns limit** (defaulting to two hundred)
- A flag indicating whether to **skip cache writes**
- An optional **task budget** that constrains token usage

## Configuration Resolution

Before the loop begins, the parameters are resolved into a concrete configuration. The model is determined from the tool use context, defaulting to "claude-sonnet-4-6" if none is specified. The maximum output tokens default to thirty-two thousand unless overridden.

## The Loop

The loop proceeds as follows, repeating for up to two hundred turns (or whatever limit was specified):

**Step 1: Call the API.** The system sends the accumulated message history, system prompt, available tools, and output token limit to the Anthropic API using the streaming interface. The call is awaited asynchronously.

**Step 2: Handle API errors.** If the API call fails, the error message is examined. If it contains the phrase "Prompt is too long," the system logs a warning about prompt length and yields an error message to the caller, then terminates the loop. For all other API errors, the error is similarly surfaced and the loop terminates.

**Step 3: Record the response.** The elapsed time of the API call is recorded in milliseconds. The assistant's message is appended to the message history and yielded to the caller for display.

**Step 4: Examine the stop reason.** The model's response includes a stop reason that determines what happens next:

- If the stop reason is **"end_turn"**, the model has finished speaking. The loop terminates.
- If the stop reason is **"max_output_tokens"**, the model ran out of output space. The system increments a recovery counter. If this counter exceeds three (the maximum output tokens recovery limit), the loop terminates. Otherwise, the system appends a user message saying "Please continue from where you left off" and continues the loop.
- For any other stop reason, the system proceeds to check for tool calls.

**Step 5: Dispatch tool calls.** The assistant's response content is examined for blocks of type "tool_use." If none are found and the stop reason was not "end_turn," the loop terminates (the model produced text but neither ended its turn nor requested tools).

If tool use blocks are present, each one is executed sequentially. For each tool call:

1. The tool name and input are extracted from the block.
2. The tool is looked up in the tool registry by name.
3. If the tool is not found, an error result is generated saying "Unknown tool" followed by the tool name.
4. If the tool is found, it is called with its input and the tool use context. The call may be asynchronous. If the tool raises an exception, the error is caught and logged, and an error result is returned.
5. The tool's result is wrapped in a "tool_result" message and appended to the message history.
6. If the tool produced additional messages beyond its primary result, those are also appended.

All tool result messages are yielded to the caller and the loop continues from Step 1.

**Step 6: Budget exhaustion.** If the loop reaches the maximum turn limit (two hundred by default), a warning is logged and the loop terminates.

## Key Constants

The system defines a **maximum output tokens recovery limit** of three. This means the model may hit its output ceiling at most three times in a single query loop before the system gives up on continuation.

The **"Prompt is too long" error message** is the sentinel string used to detect when the conversation has exceeded the model's context window. When detected, the system signals that compaction is needed (see Chapter 30).

## Design Philosophy

The query loop is deliberately simple in its control flow. It is a while loop with sequential tool execution. It does not parallelize tool calls within a single turn (though the model may request multiple tools, they are executed one after another). Error handling is defensive: any exception from a tool is caught and converted to an error message that the model can read and react to, rather than crashing the loop. The loop trusts the model to eventually produce an "end_turn" signal, but defends against infinite loops through the turn limit.
