# Chapter 19: File Tools

Three tools handle file operations: Read, Write, and Edit. Together they provide the agent's primary means of interacting with the filesystem.

## The Read Tool

The Read tool reads files from the local filesystem and returns their contents with line numbers. Its key behaviors:

- The file path must be an absolute path, not relative.
- By default, it reads up to two thousand lines starting from the beginning of the file.
- The caller may specify an offset (starting line number) and a limit (number of lines to read) to read specific portions of large files.
- Results are returned in "cat -n" format, with each line prefixed by its one-based line number followed by a tab character.
- If the file does not exist, an error is returned stating "File not found" followed by the path.
- The tool can read images (PNG, JPG, and similar formats), which are presented visually since the model is multimodal.
- It can read PDF files, though large PDFs (more than ten pages) require specifying a page range.
- It can read Jupyter notebooks, returning all cells with their outputs.

## The Write Tool

The Write tool creates or overwrites files on the filesystem. Its key behaviors:

- The file path must be absolute.
- If the file already exists, it is overwritten entirely. The agent is required to have read the file first before writing to it, to avoid accidentally destroying content.
- Parent directories are created automatically if they do not exist.
- On success, it returns a message stating the number of bytes written and the file path.

## The Edit Tool

The Edit tool performs exact string replacements within files. It is more surgical than Write, as it modifies only the specific portion of a file that matches. Its key behaviors:

- The caller provides an "old string" to find and a "new string" to replace it with.
- The edit fails if the old string is not found in the file.
- The edit fails if the old string appears more than once in the file, unless the caller explicitly sets the "replace all" flag. This uniqueness requirement prevents accidental modifications to the wrong location.
- When "replace all" is set, every occurrence of the old string is replaced.
- On success, it reports whether one occurrence or all occurrences were replaced.

The Edit tool is preferred over the Write tool for modifications to existing files because it sends only the changed portion rather than the entire file, making it easier for users to review what was changed.
