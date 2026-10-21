# Read the schema from migrations

## Establish the target

Find each engine/version, schema, owning service, migration tool/version, root or locations, target version, profile and placeholders. Redact secrets. Keep independent databases and environment variants separate. Record supplied migration history or snapshots; do not assume they exist.

Distinguish the expected schema from source, a schema replayed in an authorized disposable database, and an observed snapshot of a named environment. Use static analysis by default. Unknown custom/Java migrations, callbacks, SQL expressions, unresolved properties and conditions remain explicit gaps. Never run a migration or connect merely to fill a documentation gap.

## Liquibase

Follow configured root changelogs, nested include/includeAll, relative paths, search paths, filters and custom ordering. Read XML, YAML, JSON, formatted SQL and referenced SQL as applicable. File presence alone does not mean a changeset runs.

Track identity using ID, author and effective file/logical path; repeated IDs in different files need not be duplicates. Resolve contexts, labels, dbms and preconditions for the target. Account for onFail/onError, including changes marked ran without applying DDL. Do not assume all context-tagged changes are excluded when no filter is supplied. Check behavior against the detected version.

Account for runAlways, runOnChange, transaction settings, custom changes and object replacement. Carry create/alter/rename/drop operations, constraints, indexes and relevant data changes forward to the final expected state. Record old names and removed objects as history, not surviving schema. Compare DATABASECHANGELOG only when supplied or access is authorized; absent history cannot prove what ran.

## Flyway

Read locations, naming settings, target, schemas, placeholders, baselines, out-of-order settings, callbacks and SQL/Java/custom migration types. Sort versions by Flyway rules, not alphabetically: V2 comes before V10. Gaps in version numbers alone are not errors.

Distinguish a baseline history marker from a baseline migration script. Model a fresh installation and existing-environment upgrades separately where needed. Changed repeatable migrations follow pending versioned migrations in description order. Use their latest applicable object definitions. Do not treat undo migrations as forward migrations.

Account for conditional execution and transaction/version/edition differences. Compare flyway_schema_history only when available. Preserve uncertainty about deployed order, baselines and callbacks.

## Read the resulting objects

Track tables/views, columns/types, nullability/defaults, primary/foreign keys, delete/update actions, uniqueness/checks, ordered or filtered indexes, sequences, triggers/functions and partitions where present. Map tables to entity/query code. Use constraints to establish ERD cardinality. Flag unresolved object definitions; do not guess.

When there are no migrations, explain the actual schema source and its limits. When there is no database, mark the area not applicable. Verify version-sensitive behavior in official engine/tool documentation if needed. Do not substitute engine-specific advice from a different database.
