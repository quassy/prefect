---
sidebarDepth: 0
---

# Contents

**Prefect Improvement Notices** are used to propose, discuss, accept, and memorialize any major architectural decisions for Prefect Core.

## [PIN-1: Introduce Prefect Improvement Notices](/core/PINs/PIN-01-Introduce-PINs/)

Introducing PINs for recording Prefect decisions.

**Status:** Approved

## [PIN-2: Implementation of Result Handlers and State Metadata](/core/PINs/PIN-02-Result-Handlers/)

Adding metadata to `States` in order to track task results and serialization methods.

**Status:** Approved

## [PIN-3: Agent-Environment Model for Flow Execution](/core/PINs/PIN-03-Agent-Environment/)

A description of a more complex and executable `Environment` object.

**Status:** Approved

## [PIN-4: Result Objects for Tracking and Serializing Task Outputs](/core/PINs/PIN-04-Result-Objects/)

A new `Result` object that clarifies the logic introduced by [PIN-2](/core/PINs/PIN-02-Result-Handlers/).

**Status:** Approved

## [PIN-5: Ability to Combine Tasks](/core/PINs/PIN-05-Combining-Tasks/)

A proposal for automatically combining tasks to ensure data locality; ultimately declined as a general approach.

**Status:** Declined

## [PIN-6: Remove Constant Tasks](/core/PINs/PIN-06-Remove-Constant-Tasks/)

A proposal for removing auto-converting non-task objects into `Constant` Tasks; ultimately declined as the benefits outweigh the costs.

**Status:** Declined

## [PIN-7: Storage and Execution](/core/PINs/PIN-07-Storage-Execution/)

A proposal for refactoring environments into `Storage` classes and execution `Environment` classes with specific, loosely coupled interfaces.

**Status:** Approved

## [PIN-8: Event-Driven / Listener Flows](/core/PINs/PIN-08-Listener-Flows/)

A proposal for event-driven or long-running flows that run in response to events that arrive in an irregular stream.

**Status:** Proposed

## [PIN-9: Prefect CLI](/core/PINs/PIN-09-CLI/)

A proposal for a flexible and live-updating Prefect Cloud command line client.

**Status:** Approved

## [PIN-10: Flexible Schedules](/core/PINs/PIN-10-Schedules/)

A proposal for a new way of building schedules that captures a wider variety of use cases.

**Status:** Proposed

## [PIN-11: Single-Task Loops](/core/PINs/PIN-11-Task-Loops/)

A proposal for a way to loop over single tasks with arbitrary control logic and all Prefect semantics intact

**Status:** Proposed

## [PIN 12: Environment Callbacks](/core/PINs/PIN-12-Environment-Callbacks/)

A proposal to introduce user-provided callbacks for `Environments` which users can use to specify additional behavior before a Flow is run and after a FlowRun has ended.

**Status:** Accepted

## [PIN 13: Universal Cloud Deploys](/core/PINs/PIN-13-Universal-Deploy/)

A proposal to run Flows from Prefect Cloud with local Python resources and packages.

**Status:** Accepted

## [PIN-14: Event-Driven Flow Execution via Listeners](/core/PINs/PIN-14-Listener-Flows-2/)

A proposal to enable starting a Flow based on events from user provided sources by leveraging the existing Schedule features.

**Status:** Proposed; supersedes [PIN 8](/core/PINs/PIN-08-Listener-Flows.html).

## [PIN-15: Skip state as Finished + Control Flow Conditional](/core/PINs/PIN-15-Skip-as-Finished-and-Conditionals/)

A proposal to interpret `Skip` states as `Finished` instead of `Success`ful while also introducing more conditional control flow constructs.

**Status:** Proposed
