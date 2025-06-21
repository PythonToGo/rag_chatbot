from typing import List, Tuple
from langchain_openai import ChatOpenAI
from langchain_core.documents.base import Document
from langchain.prompts import PromptTemplate
from langchain_core.runnables import Runnable
from langchain.schema.output_parser import StrOutputParser

from src.config.settings import CHAT_MODEL, RETRIEVER_K
from src.core.document_processor import DocumentProcessor


class RAGChain:
    """Handles RAG (Retrieval-Augmented Generation) processing."""
    
    def __init__(self):
        self.document_processor = DocumentProcessor()
        self.chain = self._create_rag_chain()
    
    def _create_rag_chain(self) -> Runnable:
        """Create the RAG processing chain."""
        template = """
        Use the following context to answer the question.
        - Provide a direct answer to the question
        - Keep the response concise (within 5 lines)
        - Give the answer immediately without preamble

        Context: {context}

        Question: {question}

        Answer:"""

        custom_rag_prompt = PromptTemplate.from_template(template)
        model = ChatOpenAI(model=CHAT_MODEL)

        return custom_rag_prompt | model | StrOutputParser()
    
    def process_question(self, user_question: str) -> Tuple[str, List[Document]]:
        """Process user question and return response with context documents."""
        # Load vector store
        vector_store = self.document_processor.load_vector_store()
        
        # Create retriever
        retriever = vector_store.as_retriever(search_kwargs={"k": RETRIEVER_K})
        
        # Retrieve relevant documents
        retrieved_docs = retriever.invoke(user_question)
        
        # Generate response
        response = self.chain.invoke({
            "question": user_question, 
            "context": retrieved_docs
        })

        return response, retrieved_docs 