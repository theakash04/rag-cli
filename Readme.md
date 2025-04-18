# 🧠 RAG-CLI

Chat with an AI about any webpage — from your terminal.


---

## ✨ What it does

- Scrapes article content from a URL (`goose3`)
- Chunks and embeds the text (`mistral-embed`)
- Stores it in a FAISS vector index
- Lets you ask context-aware questions via Mistral's chat API
- Runs fully in your CLI, styled with `rich`

---

## 🚀 Quickstart

```bash
git clone https://github.com/your-username/cli-article-chat
cd cli-article-chat

# Install dependencies
pip install -r requirements.txt

# Set your API key
export MISTRAL_API=your-api-key

# Run it
python main.py
```

---

## ⚙️ Stack

| Tech         | Purpose                            |
|--------------|------------------------------------|
| `goose3`     | Article scraping                   |
| `mistralai`  | Embeddings + LLM chat              |
| `faiss`      | Fast vector similarity search      |
| `rich`       | CLI styling & progress spinners    |
| `dotenv`     | API key management                 |

