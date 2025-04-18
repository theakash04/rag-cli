# 🧠 RAG-CLI

Chat with an AI about any webpage — from your terminal.

![cli-rag](https://github.com/user-attachments/assets/d5a3263c-be23-479e-ab29-d613347f0aa3)

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
git clone https://github.com/theakash04/rag-cli.git
cd rag-cli

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

