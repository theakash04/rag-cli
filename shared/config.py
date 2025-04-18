from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.environ["MISTRAL_API"]
GEN_MODEL = "mistral-large-latest"
EMBEDD_MODEL = "mistral-embed"
CHUNK_SIZE = 2048
