<!-- ABOUTME: Reference for how real agent tool descriptions appear — for the context-engineering slide. -->
<!-- ABOUTME: Anthropic tool-use / MCP tool definition shape; the description field is what the model reads. -->

# How agent tool descriptions actually appear (for slide: Context engineering)

A tool the model can call is defined by **name + description + input_schema** (Anthropic tool-use; MCP maps to the same shape — Anthropic uses `input_schema`, OpenAI uses `parameters`). The **`description` is load-bearing**: the model reads the name + one-line description to decide *when* and *how* to call it.

Real example (Anthropic docs / Bedrock):
```json
{
  "name": "get_weather",
  "description": "Get the current weather in a given location",
  "input_schema": {
    "type": "object",
    "properties": {
      "location": { "type": "string", "description": "The city and state, e.g. San Francisco, CA" },
      "unit": { "type": "string", "enum": ["celsius","fahrenheit"], "description": "Temperature unit" }
    },
    "required": ["location"]
  }
}
```
- `name` must match `^[a-zA-Z0-9_-]{1,64}$`.
- For the slide, show each tool compactly as **`name` — one-line description** (that's the part the model sees first). E.g.:
  - `get_weather` — Get the current weather in a given location
  - `create_ticket` — Open a ticket with title, priority, labels
  - `semantic_tool_search` — Find the most relevant tools for a query
- This mirrors a **skill** (folder + SKILL.md: name + one-line description) and a **memory index** (one line per fact) — all three feed the context as *name + short description*, with the full detail loaded on demand.

**On-demand / "context being assembled":** Anthropic's advanced tool use supports `defer_loading: true` + a tool-search tool, so hundreds of tools exist but only the *relevant* name+descriptions get pulled into the context window when needed (source: anthropic.com/engineering/advanced-tool-use). This is the concrete mechanism behind "context is assembled, not dumped" — perfect for the assembly animation.

Sources: Anthropic Tool use docs / Bedrock Anthropic tool-use; anthropic.com/engineering/advanced-tool-use.
