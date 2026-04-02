# Chapter 11: Cron Scheduling

The cron scheduling subsystem allows jobs to be scheduled for future or recurring execution. Jobs fire while the REPL is idle, meaning they execute during periods when the user is not actively interacting with the system.

Durable jobs are persisted to a JSON file located at ".claude/scheduled_tasks.json" within the user's configuration directory. This persistence ensures that scheduled jobs survive session restarts and are re-loaded when Claude Code starts up.

The cron system supports both one-time scheduled execution (run a task at a specific future time) and recurring execution on a cron-style schedule. The scheduling interface is exposed through three tools: CronCreate, CronDelete, and CronList, described in Chapter 26.
