# Chatbot Project

> A hands-on learning project to explore how local AI chatbots work — from basic conversation memory to Retrieval-Augmented Generation (RAG).

A local AI chatbot built with [Ollama](https://ollama.com) and [LangChain](https://www.langchain.com/) — no cloud API, no costs, runs entirely on your machine.

## Included Chatbots

### `chatbot.py` — Conversational Chatbot
Simple chatbot with conversation memory. It remembers the entire chat history within a session.

### `rag_chatbot.py` — RAG Chatbot
Chatbot with custom knowledge from `wissen.txt`. Uses Retrieval-Augmented Generation (RAG): the user's question is enriched with relevant text chunks from the knowledge file before the model responds.

## Requirements

- Python 3.10+
- [Ollama](https://ollama.com) installed and running
- Model downloaded: `ollama pull llama3.1:8b`

## Installation

```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

pip install -r requirements.txt
```

## Usage

### Add your knowledge (RAG chatbot only)

Open `wissen.txt` and replace the example content with your own information:

```
John Doe is a software developer at Company XYZ.
He works with Python, Docker and PostgreSQL.
```

### Start a chatbot

```bash
# Simple conversational chatbot
python chatbot.py

# RAG chatbot with custom knowledge
python rag_chatbot.py
```

Type `quit` to exit.

## Switch models

Edit the model line in `chatbot.py` or `rag_chatbot.py`:

```python
chatmodel = "llama3.1:8b"  # e.g. "mistral", "gemma3", "phi4"
```

Browse available models at [ollama.com/library](https://ollama.com/library)
