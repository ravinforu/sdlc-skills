# Sources and scope

Engineering Plan uses original instructions for feature design and implementation planning. It does not bundle upstream code or full third-party skills. The links below record background research, not dependencies or instructions to install other tools. Check current official documentation for version-specific advice. Do not inherit a source's permissions, blanket rules or installation commands.

- [C4 diagrams](https://c4model.com/diagrams): Keep current and proposed architecture views clear.
- [OpenAPI](https://spec.openapis.org/oas/latest.html): Use the repository's contract version, not automatically the latest.
- [ECC migration guidance](https://github.com/affaan-m/ECC/blob/main/skills/database-migrations/SKILL.md): Earlier research informed staged schema changes and recovery planning. Do not copy blanket no-lock or zero-downtime claims.
- [Liquibase changelogs](https://docs.liquibase.com/pro/user-guide-4-33/what-is-a-changelog) and [Flyway migrations](https://documentation.red-gate.com/flyway/flyway-concepts/migrations): Verify migration proposals against the tool/engine versions in use.

Feature requirements and repository evidence are the primary inputs. No single public skill is claimed to provide the whole method.

## Integration references checked on 14 October 2026

- [Spec Kit presets](https://github.github.io/spec-kit/reference/presets.html): command wrapping and template composition. The included preset was exercised with Spec Kit v1.1.3.
- [Spec Kit source](https://github.com/github/spec-kit/tree/v1.1.3): preset schema, integration commands and core stage behavior.

## Native extension checked on 15 October 2026

- [Spec Kit 1.2.0 extensions](https://github.com/github/spec-kit/blob/v1.2.0/docs/reference/extensions.md): local installation and extension lifecycle.
- [Extension API](https://github.com/github/spec-kit/blob/v1.2.0/extensions/EXTENSION-API-REFERENCE.md): command declarations and before/after hooks. The release validator accepts the metadata used by this package.
- [Core plan command](https://github.com/github/spec-kit/blob/v1.2.0/templates/commands/plan.md): agent-executed hook dispatch and malformed-configuration behavior.
- Tested release commit: `4ca46a0706a662b1edc07086ef16f021820c2db0` (Spec Kit v1.2.0). No upstream implementation is bundled in the extension.

## Standalone distribution checked on 16 October 2026

The standalone extension repository includes installation and release tools, without a dependency on the personal skill authoring checkout. Local checks cover separate target projects, explicit updates, runtime archives and all three tested agent integrations. No remote extension repository or release has been published by this package.
