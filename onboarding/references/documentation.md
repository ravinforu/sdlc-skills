# Documentation guide

## Give each topic one home

Use docs/onboarding/ unless another destination is requested. Keep the guide detailed but easy to navigate.

| Page | Owns this information |
| --- | --- |
| README.md | Short system introduction, reading order, links, reviewed commit, scope and incomplete areas |
| architecture.md | Component categories, system/runtime/deployment views, boundaries, shared concerns |
| modules.md or modules/name.md | Detailed module responsibilities and internal design; use one form, not both |
| flows.md | End-to-end sequences, state transitions and failure paths |
| database.md | Schema dictionary, migration target/order, data ownership and ERDs |
| api.md | API groups, operations, contracts, inputs/outputs, errors and examples |
| frontend.md | Screens, components, state, forms and browser behavior |
| standards.md | Existing structure/conventions, extension workflow, setup/testing/debugging and glossary |

Combine pages for small repositories. Split very large schema/API sections by domain only when needed and link them directly from the overview. Keep module navigation one level deep. Do not create a separate general evidence catalogue that repeats every citation: put sources beside the facts they support. List documentation coverage once in README.md.

When another skill uses the same guide, link to this existing information after checking freshness. It should add proposed changes or findings in its own output, not copy the guide.

## Explain a module

Use a few short headings: Purpose; How it works; Dependencies and data; Errors and tests. Include entry/public interfaces, key symbols/files, initialization/lifecycle, internal branches, mutable state, configuration and extension points under these headings. Show how pieces collaborate, including background jobs or plugins. Add a diagram where it helps.

A module can own an API operation without repeating its full request schema. Link to API for the contract, Database for stored fields and Flows for the full sequence. Record internal module behavior here only. Group trivial helpers with their owner and name the files; do not silently omit them.

## Draw diagrams people can read

Use Mermaid inside the relevant Markdown page. Use a system context view for external users/systems, a runtime view for applications and stores, a component view for one module, sequences for ordered behavior and ERDs for tables. A C4 container means an application or store; it does not necessarily mean Docker.

Show one question and one level per diagram. Use short labels, quoted punctuation, clear boundaries and labeled arrows. Prefer top-down layout when broad. Keep at most five nodes across; split a view with roughly more than twelve nodes. Add one sentence explaining what to notice and a short source note for important nodes/relationships. Do not repeat the whole diagram in prose.

Use separate “Current” and “Proposed” views only when a proposal is explicitly requested. Mark uncertain relationships. An ORM association or similarly named column does not establish a database foreign key. Draw database cardinality from actual constraints, including nullability and uniqueness. Never add an integration or network hop because it seems likely.

## Finish the guide

Confirm every meaningful module is explained or listed as incomplete with a reason. Confirm API/UI inventories and schema objects have the detail supported by available source. Explain acronyms on first use and preserve exact technical names. Remove repeated summaries and duplicated diagrams. Check relative links and source paths. Keep known facts separate from uncertainty and report checks that were not run.
