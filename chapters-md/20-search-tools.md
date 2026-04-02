# Chapter 20: Search Tools

Two tools provide search capabilities: Glob for finding files by name patterns, and Grep for searching file contents.

## The Glob Tool

The Glob tool performs file pattern matching using glob syntax (such as "**/*.js" or "**/*.py"). Its behaviors:

- It accepts a pattern and an optional directory path (defaulting to the current directory).
- Matching files are sorted by modification time, with the most recently modified files appearing first.
- Results are limited to two hundred and fifty matches.
- It returns the full paths of matching files, one per line.

Glob is used when the agent needs to discover files by name or extension without knowing their exact locations. It is faster than using the Bash tool to run "find" or "ls" commands.

## The Grep Tool

The Grep tool searches file contents using regular expressions. It is built on ripgrep (rg), a high-performance search tool. Its behaviors:

- It accepts a pattern (regular expression), a path to search, and optional filters.
- The **glob filter** limits the search to files matching a glob pattern (such as "*.js").
- The **output mode** controls what is returned:
  - "files_with_matches" (the default) returns only the paths of files that contain matches
  - "content" returns the matching lines themselves
  - "count" returns the number of matches per file
- A **head limit** caps the output at two hundred and fifty entries by default.
- The **case insensitive** flag enables case-insensitive matching.

If ripgrep is not installed on the system, the tool returns an error message suggesting installation.

The Grep tool is used when the agent needs to find specific content within files, such as searching for function definitions, variable references, error messages, or configuration values.
