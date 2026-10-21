# Review checks

## Review the code that supports each claim

These are prompts for investigation, not a list of defects to assume. Read the implementation, callers, configuration and tests. Look for counter-evidence. Apply only the checks relevant to the repository and its requirements.

| Area | Questions to investigate |
| --- | --- |
| Architecture/design | Are responsibilities clear? Do dependencies or shared data create harmful coupling? Trace complete cycles. Are process, transaction and plugin boundaries reliable? Do deployment definitions match documented assumptions? |
| Database | Do keys/types/nullability/uniqueness match business rules? Are queries and indexes aligned? Are tenant boundaries, isolation, locks, retention and migration upgrades handled safely? |
| API/events | Do contracts match handlers/consumers? Are inputs, object/field permissions, errors, pagination, retries, concurrency, idempotency and compatibility handled? Are event delivery and business completion distinguished? |
| Frontend | Are routes/components/state responsibilities clear? Are loading/error/empty states, cancellation/races, access feedback, keyboard/focus, semantic controls and shared components handled? |
| Security | Are identity and permission checks correct across entry points? Can untrusted data reach dangerous operations? Are secrets/sensitive outputs/logs protected? Are tenant controls, sessions, uploads and dependencies suitable? |
| Code/patterns/standards | Are domain rules repeated or scattered? Are side effects, errors, resources and concurrency managed? Do deviations from conventions cause actual trouble? Are abstractions useful or needless? |
| Tests | Do tests cover meaningful business, permission, failure, contract and integration behavior? Which gaps are demonstrated? Are test results/coverage reports available and current? |
| Build/dependencies | Are versions and builds reproducible? Are packaging, generation, CI quality checks, supported dependencies and supply-chain controls consistent with requirements? |
| Operations | Are timeouts, retries, capacity bounds, telemetry, redaction, configuration, health checks, deployment and recovery supported by evidence? What depends on an external platform? |

## Database detail

Reconstruct relevant objects before reviewing them. For an index recommendation, show the actual filter/join/sort path, existing indexes, likely selectivity and write/storage costs. A foreign key does not automatically require a separate index in every workload. Explain what a representative plan or measurement must show before claiming improvement. EXPLAIN ANALYZE runs statements; do not treat it as a harmless static check.

Check migration identity/order, later renames/drops, profiles/baselines, custom code and repeatable definitions. Separate actual schema/model drift from unresolved environment history. For a proposed change, include preflight checks, compatibility, staged rollout/backfill if needed, lock/rewrite risks, validation and irreversible data effects. Do not promise zero downtime or say a DOWN script restores deleted data. Engine/version determines behavior.

## API and UI detail

Check server middleware and downstream enforcement before declaring an endpoint unprotected. OpenAPI security metadata is not enforcement; hidden UI controls are not authorization. Compare response fields with real consumers. Consider GraphQL resolver authorization/complexity, gRPC compatibility/deadlines or webhook retries only when those protocols exist.

Inspect frontend data ownership, repeated requests, stale responses, optimistic rollback and API contracts. Separate source-detectable accessibility issues from browser/assistive checks not performed. React/Next rules do not automatically apply to Angular/Vue. Bundle/render/performance concerns require evidence or an explicit measurement request, not invented numbers.

## Structure and standards detail

Compare a proposed pattern with keeping the current design or a simpler change. Identify the practical problem, affected responsibilities, compatibility, adoption cost and enforcement check. Do not recommend microservices, new frameworks, blanket caching or memoization by default. Similar syntax alone is not duplicated business logic.

Check repository standards in configuration, policy and repeated code examples. A standards deviation should cite the rule and its effect. Label optional consistency improvements as such. Suggest targeted tests/lint rules that prevent the actual problem, not tests that merely repeat implementation details.
