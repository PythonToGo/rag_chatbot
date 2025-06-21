# PDF RAG Chatbot

A Streamlit-based chatbot that uses RAG (Retrieval-Augmented Generation) to answer questions about uploaded PDF documents.

## Features

- **PDF Upload & Processing**: Upload PDF files and automatically process them for RAG
- **Vector Storage**: Uses FAISS for efficient document retrieval
- **RAG Integration**: Leverages OpenAI's GPT models for intelligent question answering
- **PDF Visualization**: View PDF pages as images alongside responses
- **Context Display**: See the source documents used to generate answers

## Project Structure

```
chatbot/
├── src/
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py          # Configuration and constants
│   ├── core/
│   │   ├── __init__.py
│   │   ├── document_processor.py # PDF processing and vector storage
│   │   └── rag_chain.py         # RAG chain implementation
│   ├── utils/
│   │   ├── __init__.py
│   │   └── pdf_converter.py     # PDF to image conversion
│   ├── ui/
│   │   ├── __init__.py
│   │   └── streamlit_app.py     # Streamlit UI implementation
│   └── __init__.py
├── data/
│   ├── temp_pdfs/              # Temporary PDF storage
│   ├── vector_store/           # FAISS vector database
│   └── pdf_images/             # Converted PDF images
├── tests/                      # Test files
├── docs/                       # Documentation
├── main.py                     # Application entry point
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd chatbot
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory with your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

1. Run the application:
```bash
streamlit run main.py
```

2. Open your browser and navigate to the provided URL (usually `http://localhost:8501`)

3. Upload a PDF file using the file uploader

4. Ask questions about the uploaded PDF in the text input field

5. View the generated responses and related document context

## Configuration

You can modify the application settings in `src/config/settings.py`:

- **Model Settings**: Change the embedding and chat models
- **Document Processing**: Adjust chunk size and overlap
- **Retrieval Settings**: Modify the number of retrieved documents
- **Image Conversion**: Change DPI settings for PDF to image conversion

## Dependencies

- **Streamlit**: Web application framework
- **LangChain**: RAG framework and document processing
- **OpenAI**: Language models and embeddings
- **FAISS**: Vector similarity search
- **PyMuPDF**: PDF processing and image conversion

## Development

### Running Tests
```bash
# Add test files to the tests/ directory
python -m pytest tests/
```

### Code Structure

The application follows a modular architecture:

- **DocumentProcessor**: Handles PDF loading, chunking, and vector storage
- **RAGChain**: Manages the RAG pipeline and question processing
- **PDFConverter**: Converts PDF pages to images for display
- **StreamlitApp**: Main UI application with clean separation of concerns

### Adding New Features

1. Create new modules in the appropriate directory (`core/`, `utils/`, `ui/`)
2. Update configuration in `src/config/settings.py` if needed
3. Add tests in the `tests/` directory
4. Update this README with new features

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here] 