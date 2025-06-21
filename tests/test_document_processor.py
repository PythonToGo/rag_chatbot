"""
Tests for the DocumentProcessor class.
"""

import pytest
from unittest.mock import Mock, patch
from src.core.document_processor import DocumentProcessor


class TestDocumentProcessor:
    """Test cases for DocumentProcessor."""
    
    def test_init(self):
        """Test DocumentProcessor initialization."""
        processor = DocumentProcessor()
        assert processor is not None
        assert processor.embeddings is not None
        assert processor.text_splitter is not None
    
    def test_save_uploaded_file(self, tmp_path):
        """Test saving uploaded file."""
        processor = DocumentProcessor()
        
        # Mock uploaded file
        mock_file = Mock()
        mock_file.name = "test.pdf"
        mock_file.read.return_value = b"test content"
        
        # Test file saving
        with patch('src.core.document_processor.TEMP_PDFS_DIR', tmp_path):
            result = processor.save_uploaded_file(mock_file)
            assert result == str(tmp_path / "test.pdf")
            assert (tmp_path / "test.pdf").exists() 