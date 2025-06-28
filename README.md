# PromptFable

PromptFable is a local Generative AI (GenAI) storytelling web application that transforms user prompts into complete, creative stories using the LLaMA 3 model powered by Ollama. It features a minimal, elegant user interface, story history/prompt tracking, and chat-style story generation, all without relying on cloud APIs or internet access.

---

## What It Does

PromptFable allows users to:

- Enter a one-line story prompt
- Generate a full story using a locally running LLaMA 3 GenAI model
- View and manage their story history
- Experience fast, private, offline AI story generation

---

## Unique Features

- **Runs Entirely Offline**: No internet or API keys required. Powered locally via the LLaMA 3 model through Ollama.
- **Generative AI Integration**: Utilizes LLaMA 3 for high-quality story generation from short prompts.
- **Persistent Story History**: Automatically saves stories to a local SQLite database for later viewing or deletion.
- **Modern UI/UX**: Chat-style interface with theme toggle, loading animations, and responsive design.
- **No External AI APIs**: PromptFable uses local inference for full control and privacy.

---

## Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python with Flask
- **Generative AI Model:** LLaMA 3 (via Ollama CLI)
- **Database:** SQLite
- **Deployment:** Runs locally, can be self-hosted

---

## Data Flow

1. User enters a short prompt in the input box.
2. The form sends a POST request to the Flask backend.
3. Flask uses `subprocess` to invoke Ollama and generate a story with the LLaMA 3 GenAI model.
4. The story is captured and returned as a response.
5. The prompt and story are stored in a local SQLite database.
6. The story is displayed in the interface.
7. Users can visit the History page to view or delete previously generated stories.

---


