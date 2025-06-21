#!/usr/bin/env python3
"""
Simple runner script for the PDF RAG Chatbot.
This script ensures proper setup before running the application.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables first
load_dotenv()

# Add src to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

# Check for .env file
env_file = Path(__file__).parent / ".env"
if not env_file.exists():
    print("Warning: .env file not found. Please create one with your OPENAI_API_KEY")
    print("Example: echo 'OPENAI_API_KEY=your_key_here' > .env")

# Import and run the application
from src.ui.streamlit_app import main

if __name__ == "__main__":
    main() 