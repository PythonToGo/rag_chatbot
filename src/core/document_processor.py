import os
from typing import List
from pathlib import Path

from langchain_openai import OpenAIEmbeddings
from langchain_core.documents.base import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyMuPDFLoader

from src.config.settings import (
    TEMP_PDFS_DIR, 
    VECTOR_STORE_DIR, 
    CHUNK_SIZE, 
    CHUNK_OVERLAP,
    EMBEDDING_MODEL
)


class DocumentProcessor:
    """Handles PDF document processing, chunking, and vector storage."""
    
    def __init__(self):
        self.embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE, 
            chunk_overlap=CHUNK_OVERLAP
        )
    
    def save_uploaded_file(self, uploaded_file) -> str:
        """Save uploaded file to temporary directory."""
        file_path = TEMP_PDFS_DIR / uploaded_file.name
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())
        return str(file_path)
    
    def pdf_to_documents(self, pdf_path: str) -> List[Document]:
        """Convert PDF file to Document objects."""
        documents = []
        loader = PyMuPDFLoader(pdf_path)
        doc = loader.load()
        for d in doc:
            d.metadata['file_path'] = pdf_path
        documents.extend(doc)
        return documents
    
    def chunk_documents(self, documents: List[Document]) -> List[Document]:
        """Split documents into smaller chunks."""
        return self.text_splitter.split_documents(documents)
    
    def save_to_vector_store(self, documents: List[Document]) -> None:
        """Save documents to FAISS vector store."""
        vector_store = FAISS.from_documents(documents, embedding=self.embeddings)
        vector_store.save_local(str(VECTOR_STORE_DIR))
    
    def load_vector_store(self):
        """Load existing vector store."""
        return FAISS.load_local(
            str(VECTOR_STORE_DIR), 
            self.embeddings, 
            allow_dangerous_deserialization=True
        ) 