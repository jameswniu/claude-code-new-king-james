# Chapter 18: Bash Tool

The Bash tool executes shell commands on the user's system and returns their output. It is one of the most powerful and frequently used tools in the system.

## Command Classification

The Bash tool classifies commands into categories that inform permission decisions:

**Search commands** are automatically allowed without any permission check. These include: find, grep, rg (ripgrep), ag (the silver searcher), ack, locate, which, and whereis.

**Read commands** are also automatically allowed. These include: cat, head, tail, less, more, wc, stat, file, strings, ls, tree, du, jq, awk, cut, sort, uniq, and tr.

**Passthrough commands** are trivial commands that produce no meaningful side effects: echo, printf, true, false, and the colon (a shell no-op).

**Mutation commands** require approval in the default permission mode because they modify the filesystem or environment: mv, cp, rm, mkdir, rmdir, chmod, chown, chgrp, touch, ln, cd, export, unset, and wait.

**Accept-edits-allowed commands** are a subset of mutation commands that are automatically approved when the user is in "accept edits" permission mode: mkdir, touch, rm, rmdir, mv, cp, and sed.

## Execution

When a command is executed, it runs as an asynchronous subprocess. The working directory defaults to the current session's working directory but can be overridden. Standard output and standard error are both captured. The default timeout is one hundred and twenty thousand milliseconds (two minutes).

If the command completes within the timeout, its combined output (stdout followed by stderr) is returned. If the exit code is non-zero, the result is flagged as an error. If the command exceeds the timeout, a timeout error is returned. Any other exception during execution is caught and returned as an error message.

## Design Note

The Bash tool is the primary vector for the security classifier's attention. While read and search commands are automatically allowed, any command that could modify state, access the network, or interact with external systems must pass through the permission and classification systems described in the intelligence layer.
