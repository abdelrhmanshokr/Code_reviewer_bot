# Smart Code Reviewer

A small FastAPI-based service that reviews short code snippets and returns
exactly three concrete improvements plus one positive note. The service includes
a deterministic, offline review stub so you can run and iterate locally without
an OpenAI key. Optional OpenAI integration can be enabled later to produce
LLM-generated reviews.

Contents
 - `src/main.py` — application entrypoint (starts Uvicorn)
 - `src/api/server.py` — exposes `app` (FastAPI) and includes the router
 - `src/api/routes.py` — API endpoints: `/health`, `/rules`, `/review`
 - `src/api/models.py` — Pydantic models for request/response payloads
 - `src/core/rule_engine.py` — loads authority and custom rules
 - `src/core/standards/*.py` — rule definitions (`authority_rules`, `custom_rules`)
 - `src/core/code_analyzer.py` — small heuristics used by the deterministic stub
 - `src/ai/review_generator.py` — deterministic review generator (3 improvements + positive note)

Quickstart (development)
1. Create and activate a Python virtual environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python3 -m src.main
```

The server will start with Uvicorn and listen on port 8000 by default.

API endpoints
- `GET /health` — basic health check, returns {"status":"ok"}
- `GET /rules` — returns the loaded rule dictionaries from the RuleEngine
- `POST /review` — review endpoint. Request JSON schema:

```json
{
	"language": "python",           // optional, default: python
	"intent": "count unique items", // optional
	"code": "<code string>"         // required
}
```

Response JSON schema:

```json
{
	"improvements": [
		{"title":"...","explanation":"...","suggested_change":"...","priority":"..."},
		... (3 items)
	],
	"positive_note": "..."
}
```

Examples

- Curl (inline snippet):

```bash
curl -sS -X POST http://127.0.0.1:8000/review \
	-H 'Content-Type: application/json' \
	-d '{"language":"python","intent":"count unique","code":"def f(a):\n    s=set()\n    for x in a:\n        if x not in s:\n            s.add(x)\n    return len(s)"}' | jq .
```

- Python client (requests):

```python
import requests

payload = {
		"language": "python",
		"intent": "count unique items",
		"code": "def f(a):\n    s = set()\n    for x in a:\n        if x not in s:\n            s.add(x)\n    return len(s)\n"
}

r = requests.post("http://127.0.0.1:8000/review", json=payload)
print(r.json())
```

Design notes
- The repository currently contains a deterministic review generator (`src/ai/review_generator.py`) that uses simple heuristics from `CodeAnalyzer` (line counts, indentation-based nesting estimate, presence of docstrings). This allows immediate offline reviews and rapid iteration.
- `RuleEngine` pulls in authority and custom rule sets from `src/core/standards` for future use when scoring or explaining violations.

Enabling OpenAI LLM-based reviews (optional)
1. Add your OpenAI API key to an environment variable: `export OPENAI_API_KEY=sk-...` or put it in a local `.env` file.
2. Replace or extend `src/ai/review_generator.py` with a function that calls the OpenAI API using the prompt template in `docs` or the `ai/prompt_templates.py` if present.
3. Restart the server.

Security & best practices
- Never commit real API keys. Keep `.env` in `.gitignore`.
- For production, use a secrets manager and run the app under a process manager (systemd / container orchestration). Consider rate-limiting, authentication, and logging.

Next steps (suggested)
- Add unit tests for the endpoints (pytest) — there is `tests/` in the repo ready for additions.
- Add OpenAI integration with careful rate/error handling.
- Add a CLI tool or GitHub Action to run quick snippet reviews.

If you want, I can:
- wire OpenAI integration now (I'll add code that reads `OPENAI_API_KEY` and calls the API),
- add a small `scripts/review.py` CLI to post files to the server,
- or create minimal pytest tests for `/review`.

