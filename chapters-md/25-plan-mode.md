# Chapter 25: Plan Mode

Plan mode is a special operational state in which the agent designs an implementation strategy before executing any changes. Two tools control this state: EnterPlanMode and ExitPlanMode.

**EnterPlanMode** transitions the session into plan mode. While in plan mode, the agent is restricted from making edits, running non-read-only tools, or otherwise modifying the system. It may only read files, search code, and write to a designated plan file. This constraint forces the agent to think through its approach before acting.

**ExitPlanMode** signals that the agent has finished writing its plan and is ready for user approval. The user reviews the plan file and either approves it (allowing the agent to proceed with execution) or provides feedback for revision.

Plan mode is designed for complex tasks where acting without a plan could lead to wasted effort, incorrect approaches, or unintended changes. It ensures alignment between the agent's intended approach and the user's expectations before any code is written or any system state is modified.

The plan file itself is a markdown document created at a path specified by the system. It typically includes context (why the change is needed), the recommended approach, file paths to be modified, and a verification section describing how to test the changes.
