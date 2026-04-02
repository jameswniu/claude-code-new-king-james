# Chapter 22: Web Tools

Two tools provide web access: WebFetch for retrieving and processing web page content, and WebSearch for performing web searches.

## The WebFetch Tool

The WebFetch tool fetches content from a specified URL, converts HTML to markdown, and processes the content using a small, fast AI model. It accepts a URL and a prompt describing what information to extract from the page.

Key behaviors:

- The URL must be fully formed and valid
- HTTP URLs are automatically upgraded to HTTPS
- The content is summarized if it exceeds size limits
- A self-cleaning cache with a fifteen-minute lifetime provides faster responses for repeated accesses to the same URL
- When a URL redirects to a different host, the tool informs the caller and provides the redirect URL
- The tool will fail for authenticated or private URLs; specialized MCP tools should be used for those

## The WebSearch Tool

The WebSearch tool performs web searches and returns results. It enables the agent to find information, documentation, and resources on the internet when local knowledge is insufficient.

Both web tools require runtime integration to function, as they depend on network access and external service communication that is not available in a standalone context.
