from rich import print
from rich.console import Console
from core.chat import chat_with_ai
import numpy as np
from core.embedder import get_text_embedding
from core.vectorStore import searchIndex

console = Console()

def main_loop(index, chunks):
    while True:
        console.print("[bold cyan]Say something:[/bold cyan]")
        user_input = input("> ")

        if user_input == ".exit" or user_input == "bye":
            console.print("[bold green] Byee![/bold green]")
            break

        query_embedding = get_text_embedding(user_input)
        I = searchIndex(index, np.array([query_embedding]))
        relevant_chunks = [chunks[i] for i in I]

        answer = chat_with_ai(user_input, relevant_chunks)
        print(f"[green]AI:[/green] {answer} \n")

