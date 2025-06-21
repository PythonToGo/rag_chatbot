#!/usr/bin/env python3
"""
PDF RAG Chatbot - Main Entry Point

A Streamlit-based chatbot that uses RAG (Retrieval-Augmented Generation)
to answer questions about uploaded PDF documents.
"""

import os
from dotenv import load_dotenv

# Load environment variables first
load_dotenv()

from src.ui.streamlit_app import main

if __name__ == "__main__":
    main()
