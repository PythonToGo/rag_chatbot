import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Base paths
BASE_DIR = Path(__file__).parent.parent.parent
DATA_DIR = BASE_DIR / "data"
TEMP_PDFS_DIR = DATA_DIR / "temp_pdfs"
VECTOR_STORE_DIR = DATA_DIR / "vector_store"
PDF_IMAGES_DIR = DATA_DIR / "pdf_images"

# Ensure directories exist
TEMP_PDFS_DIR.mkdir(parents=True, exist_ok=True)
VECTOR_STORE_DIR.mkdir(parents=True, exist_ok=True)
PDF_IMAGES_DIR.mkdir(parents=True, exist_ok=True)

# Model settings
EMBEDDING_MODEL = "text-embedding-3-small"
CHAT_MODEL = "gpt-4o-mini"

# Document processing settings
CHUNK_SIZE = 800
CHUNK_OVERLAP = 100
RETRIEVER_K = 3

# Image conversion settings
DEFAULT_DPI = 250

# Streamlit settings
PAGE_TITLE = "PDF RAG Chatbot"
LAYOUT = "wide" 