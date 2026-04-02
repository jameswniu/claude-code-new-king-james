# Chapter 01: Workspace Context

The workspace context is the system's representation of the environment in which it operates. It is constructed at startup and carries the following information throughout a session:

The **current working directory** is determined by the standard method of querying the operating system for the process's working directory. This is the root from which all relative file operations are resolved.

The system maintains a list of **additional directories** that the user may have added to the workspace scope. These are directories beyond the current working directory that the agent is permitted to read and modify.

A boolean flag records whether the current working directory is a **git repository**. This is determined by checking for the presence of a ".git" directory within the current working directory.

If the directory is a git repository, the **current branch name** is recorded.

A **project directory** may also be set, which corresponds to the location of project-level configuration files (such as CLAUDE.md).

The workspace context is constructed through a factory method that examines the current working directory. It checks for the presence of a ".git" directory to set the git repository flag. The remaining fields are populated as the session progresses and more information becomes available about the user's project structure.

This context object is passed through the system and is available to tools, services, and the query loop whenever they need to understand the environment in which they are operating.
