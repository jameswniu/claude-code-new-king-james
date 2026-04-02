# Chapter 12: Session Persistence

Session transcripts are stored as JSONL (JSON Lines) files, where each line represents a single message or event in the conversation. This format allows efficient append-only writing during a session and line-by-line reading for retrieval or analysis.

The default retention period for session transcripts is **thirty days**. After this period, transcripts may be cleaned up to conserve disk space. The session identifier (described in Chapter 03) serves as the key for locating transcript files.

The JSONL format is chosen for its simplicity and streaming-friendliness: new messages can be appended without reading or rewriting the entire file, and transcripts can be searched using standard text tools like grep without requiring a JSON parser to load the complete file into memory.
