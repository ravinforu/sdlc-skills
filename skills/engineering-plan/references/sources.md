# Sources and scope

This skill is a focused rewrite of the Architecture and Review skill prepared for this user on 13 October 2026. It uses original instructions; it does not bundle upstream code or full third-party skills. The links below record the earlier research, not dependencies or instructions to install other tools. Check current official documentation for version-specific advice. Do not inherit a source's permissions, blanket rules or installation commands.

- [C4 diagrams](https://c4model.com/diagrams): Keep current and proposed architecture views clear.
- [OpenAPI](https://spec.openapis.org/oas/latest.html): Use the repository's contract version, not automatically the latest.
- [ECC migration guidance](https://github.com/affaan-m/ECC/blob/main/skills/database-migrations/SKILL.md): Earlier research informed staged schema changes and recovery planning. Do not copy blanket no-lock or zero-downtime claims.
- [Liquibase changelogs](https://docs.liquibase.com/pro/user-guide-4-33/what-is-a-changelog) and [Flyway migrations](https://documentation.red-gate.com/flyway/flyway-concepts/migrations): Verify migration proposals against the tool/engine versions in use.

Feature requirements and repository evidence are the primary inputs. This planning workflow is newly authored for the requested split; it is not a claim that one public skill provides the whole method.
