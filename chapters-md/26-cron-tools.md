# Chapter 26: Cron Tools

Three tools manage scheduled execution: CronCreate, CronDelete, and CronList.

**CronCreate** schedules a prompt to run at a future time. It supports two modes: a one-time execution at a specific future timestamp, or recurring execution on a cron-style schedule. The created job is persisted to the durable job store described in Chapter 11.

**CronDelete** removes a previously scheduled job by its identifier.

**CronList** displays all currently scheduled jobs, including their schedules, next execution times, and associated prompts.

The cron system is governed by feature flags (described in the intelligence layer). The flags "tengu_kairos_cron" and "tengu_kairos_cron_durable" control whether the cron system is active and whether jobs are persisted durably, respectively. Both default to enabled.
