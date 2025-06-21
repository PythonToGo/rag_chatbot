import streamlit as st
import os
from pathlib import Path

from src.config.settings import PAGE_TITLE, LAYOUT
from src.core.document_processor import DocumentProcessor
from src.core.rag_chain import RAGChain
from src.utils.pdf_converter import PDFConverter


class StreamlitApp:
    """Main Streamlit application for the PDF RAG Chatbot."""
    
    def __init__(self):
        self.document_processor = DocumentProcessor()
        self.rag_chain = RAGChain()
        self.pdf_converter = PDFConverter()
        self.setup_page()
    
    def setup_page(self):
        """Setup Streamlit page configuration."""
        st.set_page_config(
            page_title=PAGE_TITLE,
            layout=LAYOUT
        )
        st.title(PAGE_TITLE)
    
    def handle_pdf_upload(self):
        """Handle PDF file upload and processing."""
        pdf_doc = st.file_uploader("PDF Upload", type="pdf")
        button = st.button("Upload PDF")

        if pdf_doc and button:
            with st.spinner("Uploading PDF..."):
                st.write("Processing PDF...")
                
                # Save and process PDF
                pdf_path = self.document_processor.save_uploaded_file(pdf_doc)
                pdf_doc = self.document_processor.pdf_to_documents(pdf_path)
                smaller_docs = self.document_processor.chunk_documents(pdf_doc)
                self.document_processor.save_to_vector_store(smaller_docs)
            
            st.success("PDF upload completed successfully")
            
            # Convert to images
            with st.spinner("Converting PDF to images..."):
                images = self.pdf_converter.convert_pdf_to_images(pdf_path)
                st.session_state.images = images
    
    def handle_question_processing(self):
        """Handle user question processing."""
        user_question = st.text_input(
            "Ask me anything about the uploaded PDF",
            placeholder="Enter your question here..."
        )
        
        if user_question:
            response, context = self.rag_chain.process_question(user_question)
            st.text(response)
            
            # Display context documents
            for i, doc in enumerate(context):
                with st.expander(f"Related Document {i+1}"):
                    st.text(doc.page_content)
                    file_path = doc.metadata.get('source', '')
                    page_number = doc.metadata.get('page', 0) + 1
                    # Add unique index to prevent duplicate keys
                    button_key = f"link_{file_path}_{page_number}_{i}"
                    
                    reference_button = st.button(
                        f"View {Path(file_path).name} page {page_number}", 
                        key=button_key
                    )
                    if reference_button:
                        st.session_state.page_number = str(page_number)
    
    def display_pdf_page(self, image_path: str, page_number: int):
        """Display a specific PDF page as image."""
        with open(image_path, "rb") as f:
            image_bytes = f.read()
        st.image(image_bytes, caption=f"Page {page_number}", output_format="PNG", width=600)
    
    def handle_pdf_display(self):
        """Handle PDF page display in the right column."""
        page_number = st.session_state.get("page_number")
        if page_number:
            page_number = int(page_number)
            image_paths = self.pdf_converter.get_sorted_images()
            
            if image_paths and page_number <= len(image_paths):
                self.display_pdf_page(image_paths[page_number - 1], page_number)
    
    def run(self):
        """Run the main application."""
        left_col, right_col = st.columns([1, 1])
        
        with left_col:
            self.handle_pdf_upload()
            self.handle_question_processing()
        
        with right_col:
            self.handle_pdf_display()


def main():
    """Main entry point for the Streamlit application."""
    app = StreamlitApp()
    app.run()


if __name__ == "__main__":
    main() 