# Chapter 30: Compaction and Dreams

Two services manage the system's relationship with its context window: the compaction engine that summarizes conversations when they grow too long, and the dream system that consolidates memories during idle periods.

## Compaction

The compaction engine monitors the token count of the current conversation against the model's effective context window. It uses three threshold offsets:

- **Warning threshold**: the effective context window minus twenty thousand tokens. When the conversation reaches this point, the system considers auto-compaction.
- **Error threshold**: the effective context window minus thirteen thousand tokens. At this point, compaction becomes urgent.
- **Blocking limit**: the effective context window minus three thousand tokens. At this point, the system can no longer proceed without compaction.

The system permits up to three consecutive compaction failures before giving up.

When compaction is triggered, the model is given a detailed prompt instructing it to create a thorough summary. The compaction prompt directs the model to:

First, chronologically analyze each message and section of the conversation, identifying the user's explicit requests and intents, the agent's approach to addressing those requests, key decisions, technical concepts and code patterns, specific details like file names, full code snippets and function signatures, errors encountered and their fixes, and specific user feedback. The model is asked to double-check for technical accuracy and completeness.

The summary must include nine sections: (1) Primary Request and Intent, capturing all explicit user requests in detail; (2) Key Technical Concepts, listing important technologies and frameworks; (3) Files and Code Sections, enumerating specific files examined, modified, or created; (4) Errors and Fixes, listing all errors and their resolutions; (5) Problem Solving, documenting problems solved and ongoing troubleshooting; (6) All User Messages, listing every user message that is not a tool result; (7) Pending Tasks, outlining work explicitly requested; (8) Current Work, describing in detail what was being worked on immediately before the summary; (9) Optional Next Step, listing the next step related to the most recent work.

## Dreams

The dream system performs memory consolidation during idle periods. It is a four-phase reflective process:

**Phase 1, Orient**: The system reads the memory directory listing and the MEMORY.md index to understand what memories already exist. It skims existing topic files to avoid creating duplicates.

**Phase 2, Gather Recent Signal**: The system looks for new information worth persisting, checking daily logs, identifying existing memories that have drifted from reality, and searching session transcripts for specific terms using narrow, targeted searches rather than exhaustive reading.

**Phase 3, Consolidate**: For each piece of information worth remembering, the system writes or updates a memory file. It prioritizes merging new information into existing files over creating near-duplicates, converts relative dates to absolute dates, and deletes facts that have been contradicted by more recent observations.

**Phase 4, Prune and Index**: The system updates the MEMORY.md index to stay under two hundred lines and approximately twenty-five kilobytes. It removes pointers to stale memories, demotes verbose entries, adds pointers to newly important memories, and resolves contradictions between files.

The dream system is controlled by the feature flag "tengu_onyx_plover," which specifies the minimum hours between dream cycles.
