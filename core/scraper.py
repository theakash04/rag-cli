from goose3 import Goose
from rich  import print

g = Goose()

def scrape_content(url: str):
    article = g.extract(url)
    title = article.title
    content = article.cleaned_text
    if not (title and content):
        print("[bold red]⚠️  No data found from the URL. Scraping failed.[/bold red]")
        exit(1)
    return title, content
