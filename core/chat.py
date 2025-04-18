from mistralai import Mistral, models
import time
from rich import print
from rich.progress import Progress, SpinnerColumn, TextColumn
from shared.config import API_KEY, GEN_MODEL

client = Mistral(api_key=API_KEY)

def chat_with_ai(query: str, content: list[str]):
    attempt = 0
    while attempt < 5:
        with Progress(
            SpinnerColumn(style="cyan"),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
        ) as progress:
            task = progress.add_task("Thinking...", total=None)
            try:
                response = client.chat.complete(
                    model=GEN_MODEL,
                    messages=[{
                        'role': "user",
                        "content": f"""
                        Context information is below.
                        ---------------------
                        {content}
                        ---------------------
                        Given the context information and not prior knowledge, answer the query.
                        Query: {query}
                        Answer:"""
                    }]
                    )
                progress.remove_task(task)
                return response.choices[0].message.content
            except models.SDKError:
                progress.remove_task(task)
                print(f"[bold yellow]Rate limit exceeded. Retrying... (Attempt {attempt + 1})[/bold yellow]")
                attempt += 1
                time.sleep(2 ** attempt)  # Exponential backoff
    print("[bold red]Max retries reached. Please try again later.[/bold red]")

