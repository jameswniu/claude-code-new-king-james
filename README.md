# Claude Code: New King James

Claude Code's production runtime architecture - Python implementation alongside formal prose chapters.

## What This Is

This repository contains two parallel representations of Anthropic's Claude Code CLI (version 2.1.87):

- **`code-python/`** - A Python implementation of the production runtime: the query loop, tools, services, types, and utilities.
- **`chapters-md/`** - Formal prose chapters describing the architecture in natural language. No code, just descriptive essays about how the system is structured and what it does.

## Legal Basis

This work constitutes commentary, analysis, and description of a publicly distributed software product. Descriptions of how software behaves are protected expression under the First Amendment. This repository contains no copyrighted source code, no compiled artifacts, and no executable reproductions. It is the equivalent of a book review describing the plot of a novel, or a technical article explaining how an engine works.

The Supreme Court has consistently held that ideas, methods of operation, and functional descriptions are not copyrightable. What is protected is the specific creative expression of code, not the underlying concepts, algorithms, or architectural patterns it implements.

### Relevant Case Law

- [Baker v. Selden, 101 U.S. 99 (1879)](https://supreme.justia.com/cases/federal/us/101/99/) - Ideas and methods of operation are not copyrightable; only the specific expression is protected.
- [Lotus Dev. Corp. v. Borland Int'l, Inc., 49 F.3d 807 (1st Cir. 1995), aff'd 516 U.S. 233 (1996)](https://law.justia.com/cases/federal/appellate-courts/F3/49/807/551122/) - Menu command hierarchies are uncopyrightable methods of operation under 17 U.S.C. Section 102(b).
- [Google LLC v. Oracle America, Inc., 593 U.S. 1 (2021)](https://supreme.justia.com/cases/federal/us/593/18-956/) - Reimplementation of functional API interfaces constitutes fair use; functional aspects of software are not entitled to the same copyright protection as creative works.
- [Sega Enterprises Ltd. v. Accolade, Inc., 977 F.2d 1510 (9th Cir. 1992)](https://law.justia.com/cases/federal/appellate-courts/F2/977/1510/305345/) - Reverse engineering of software for purposes of interoperability is fair use.
- [Sony Computer Entertainment v. Connectix Corp., 203 F.3d 596 (9th Cir. 2000)](https://law.justia.com/cases/federal/appellate-courts/F3/203/596/474793/) - Intermediate copying during reverse engineering to create a compatible product is fair use.

### First Amendment

- [Eldred v. Ashcroft, 537 U.S. 186 (2003)](https://supreme.justia.com/cases/federal/us/537/186/) - Copyright's built-in First Amendment accommodations include the idea/expression distinction and fair use.
- [17 U.S.C. Section 102(b)](https://www.law.cornell.edu/uscode/text/17/102) - "In no case does copyright protection for an original work of authorship extend to any idea, procedure, process, system, method of operation, concept, principle, or discovery."
- [17 U.S.C. Section 107 (Fair Use)](https://www.law.cornell.edu/uscode/text/17/107) - Fair use factors: purpose/character, nature of the work, amount used, and market effect.

### DMCA Context

- [Anthropic DMCA takedown (April 2026)](https://developers.slashdot.org/story/26/04/01/158240/anthropic-issues-copyright-takedown-requests-to-remove-8000-copies-of-claude-code-source-code) - Anthropic issued takedown requests targeting ~8,000 repositories containing copies of Claude Code source code. This repository contains no source code.

## How to Read This

The chapters are numbered and organized to mirror the structure of the production runtime. Start with Chapter 00 for an overview, then read sequentially or jump to any chapter of interest.

## Chapters

- [00 - Introduction](chapters-md/00-introduction.md)
- [01 - Workspace Context](chapters-md/01-workspace-context.md)
- [02 - Cost Tracking](chapters-md/02-cost-tracking.md)
- [03 - Session History](chapters-md/03-session-history.md)
- [04 - The Query Loop](chapters-md/04-the-query-loop.md)
- [05 - Task Management](chapters-md/05-task-management.md)
- [06 - Tool Architecture](chapters-md/06-tool-architecture.md)
- [07 - Application State](chapters-md/07-application-state.md)
- [08 - Bridge System](chapters-md/08-bridge-system.md)
- [09 - Slash Commands](chapters-md/09-slash-commands.md)
- [10 - Hook Events](chapters-md/10-hook-events.md)
- [11 - Cron Scheduling](chapters-md/11-cron-scheduling.md)
- [12 - Session Persistence](chapters-md/12-session-persistence.md)
- [13 - Bundled Skills](chapters-md/13-bundled-skills.md)
- [14 - Swarm Orchestration](chapters-md/14-swarm-orchestration.md)
- [15 - MCP Protocol](chapters-md/15-mcp-protocol.md)
- [16 - Sandbox Enforcement](chapters-md/16-sandbox-enforcement.md)
- [17 - Tool Registry](chapters-md/17-tool-registry.md)
- [18 - Bash Tool](chapters-md/18-bash-tool.md)
- [19 - File Tools](chapters-md/19-file-tools.md)
- [20 - Search Tools](chapters-md/20-search-tools.md)
- [21 - Agent Tool](chapters-md/21-agent-tool.md)
- [22 - Web Tools](chapters-md/22-web-tools.md)
- [23 - Task Tools](chapters-md/23-task-tools.md)
- [24 - Team Tools](chapters-md/24-team-tools.md)
- [25 - Plan Mode](chapters-md/25-plan-mode.md)
- [26 - Cron Tools](chapters-md/26-cron-tools.md)
- [27 - Worktree Tools](chapters-md/27-worktree-tools.md)
- [28 - Specialized Tools](chapters-md/28-specialized-tools.md)
- [29 - Services Overview](chapters-md/29-services-overview.md)
- [30 - Compaction and Dreams](chapters-md/30-compaction-and-dreams.md)
- [31 - Memory System](chapters-md/31-memory-system.md)
- [32 - Type System](chapters-md/32-type-system.md)
- [33 - Utilities](chapters-md/33-utilities.md)
