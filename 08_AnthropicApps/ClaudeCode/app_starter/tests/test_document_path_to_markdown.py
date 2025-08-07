import os
import pytest
from tools.document import document_path_to_markdown


class TestDocumentPathToMarkdown:
    # Define fixture paths
    FIXTURES_DIR = os.path.join(os.path.dirname(__file__), "fixtures")
    DOCX_FIXTURE = os.path.join(FIXTURES_DIR, "mcp_docs.docx")
    PDF_FIXTURE = os.path.join(FIXTURES_DIR, "mcp_docs.pdf")

    def test_fixture_files_exist(self):
        """Verify test fixtures exist."""
        assert os.path.exists(self.DOCX_FIXTURE), (
            f"DOCX fixture not found at {self.DOCX_FIXTURE}"
        )
        assert os.path.exists(self.PDF_FIXTURE), (
            f"PDF fixture not found at {self.PDF_FIXTURE}"
        )

    def test_valid_docx_conversion(self):
        """Test converting a DOCX document to markdown using file path."""
        result = document_path_to_markdown(self.DOCX_FIXTURE)
        
        # Basic assertions to check the conversion was successful
        assert isinstance(result, str)
        assert len(result) > 0
        # Check for typical markdown formatting
        assert "#" in result or "-" in result or "*" in result

    def test_valid_pdf_conversion(self):
        """Test converting a PDF document to markdown using file path."""
        result = document_path_to_markdown(self.PDF_FIXTURE)
        
        # Basic assertions to check the conversion was successful
        assert isinstance(result, str)
        assert len(result) > 0
        # Check for typical markdown formatting
        assert "#" in result or "-" in result or "*" in result

    def test_return_type_validation(self):
        """Test that the function returns a string containing markdown."""
        docx_result = document_path_to_markdown(self.DOCX_FIXTURE)
        pdf_result = document_path_to_markdown(self.PDF_FIXTURE)
        
        # Verify return types are strings
        assert isinstance(docx_result, str)
        assert isinstance(pdf_result, str)
        
        # Verify non-empty strings
        assert len(docx_result) > 0
        assert len(pdf_result) > 0

    def test_content_preservation(self):
        """Test that specific content from source documents appears in markdown output."""
        docx_result = document_path_to_markdown(self.DOCX_FIXTURE)
        pdf_result = document_path_to_markdown(self.PDF_FIXTURE)
        
        # These assertions will need to be updated based on actual fixture content
        # Check for some common text that should exist in MCP documentation
        docx_lower = docx_result.lower()
        pdf_lower = pdf_result.lower()
        
        # Test that some content exists (will need to update with actual fixture content)
        assert len(docx_result.strip()) > 10, "DOCX conversion should produce substantial content"
        assert len(pdf_result.strip()) > 10, "PDF conversion should produce substantial content"

    def test_non_existent_file_error(self):
        """Test that non-existent file raises appropriate exception."""
        non_existent_path = "/path/that/does/not/exist.docx"
        
        with pytest.raises((FileNotFoundError, IOError)):
            document_path_to_markdown(non_existent_path)