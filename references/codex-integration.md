# Codex skill identity and discovery

The skill name is `codex-red`, its display name is Codex Red, and explicit
invocation uses `$codex-red` in a host where the skill is installed.

Project discovery uses `<project>/.agents/skills/codex-red/`; user discovery uses
`$HOME/.agents/skills/codex-red/` in supporting Codex versions. The complete
package includes `SKILL.md`, technical `references/`, display `assets/` and
`agents/openai.yaml`. Discovery behavior is local to the selected host.

The package's scripts check repository structure and metadata. They are not
analysis tools. Skill installation does not itself add hooks, MCP connections,
API keys, startup changes, model overrides or new execution permissions.

Task execution and authorization are governed by the host, project and user.
Domain-reference knowledge does not replace those instructions.

Current format and discovery reference:
https://developers.openai.com/codex/skills/.
