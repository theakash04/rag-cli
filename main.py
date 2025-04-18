from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.text import Text
from core.cli import main_loop
from core.embedder import embedd_chunks
from core.scraper import scrape_content
from core.vectorStore import build_index
from shared.config import CHUNK_SIZE
from shared.utils import chunk_text
from rich.panel import Panel

console = Console()

panel_text = Text()
panel_text.append("🤖 Welcome to your AI CLI thingy!\n\n", style="bold magenta")
panel_text.append("🌐 Got a link you want me to pull context from?\n", style="bold cyan")
panel_text.append("Paste the full URL below — blog post, article, docs page, whatever.\n", style="italic white")
panel_text.append("I'll scrape it, read it, and use it in all your chats.\n\n", style="italic green")
panel_text.append("💡 Type '.exit' or 'bye' anytime to quit.\n", style="dim")
console.print(Panel(panel_text, title="Let's get contextual 📚", border_style="bright_magenta"))


if __name__ == "__main__":
    console.print("[bold yellow]Paste the URL here[/bold yellow]")
    url = input("> ")
    if url:
        console.print(f"\n✅ Got it! I'll use context from [underline blue]{url}[/underline blue] in our convo.\n", style="bold green")

        with Progress(SpinnerColumn(style="cyan"), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
            progress.add_task("Scraping content...", total=None)
            title, content = scrape_content(url)

            progress.add_task("Chunking text...", total=None)
            chunks = chunk_text(content, CHUNK_SIZE)

            progress.add_task("Creating embeddings...", total=None)
            embeddings = embedd_chunks(chunks)

            progress.add_task("Building index...", total=None)
            index, _ = build_index(embeddings)

        main_loop(index, chunks)
    else:
        console.print("[dim][bold red]No link Pasted[/bold red][/dim]")
        quit()
