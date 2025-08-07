from markitdown import MarkItDown, StreamInfo
from io import BytesIO
from pydantic import Field
import os


def binary_document_to_markdown(binary_data: bytes, file_type: str) -> str:
    """Converts binary document data to markdown-formatted text."""
    md = MarkItDown()
    file_obj = BytesIO(binary_data)
    stream_info = StreamInfo(extension=file_type)
    result = md.convert(file_obj, stream_info=stream_info)
    return result.text_content


def document_path_to_markdown(
    file_path: str = Field(description="Path to a PDF or DOCX file to convert to markdown")
) -> str:
    """Converts a PDF or DOCX file to markdown-formatted text.
    
    Takes a file path to a PDF or DOCX document, reads the file, and converts 
    its contents to markdown format using the MarkItDown library.
    
    When to use:
    - When you need to convert PDF or DOCX documents to markdown
    - When you have a file path and want markdown output
    - When you need to process document content as text
    
    When not to use:
    - When you already have binary document data (use binary_document_to_markdown instead)
    - When working with unsupported file types
    - When the file doesn't exist or isn't accessible
    
    Examples:
    >>> document_path_to_markdown("/path/to/document.docx")
    "# Document Title\n\nContent in markdown format..."
    >>> document_path_to_markdown("/path/to/report.pdf") 
    "# Report\n\n- Item 1\n- Item 2..."
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    if not os.path.isfile(file_path):
        raise ValueError(f"Path is not a file: {file_path}")
    
    # Determine file extension
    _, ext = os.path.splitext(file_path.lower())
    ext = ext.lstrip('.')
    
    if ext not in ['pdf', 'docx']:
        raise ValueError(f"Unsupported file type: {ext}. Only PDF and DOCX files are supported.")
    
    # Read the file as binary data
    with open(file_path, 'rb') as f:
        binary_data = f.read()
    
    # Use existing binary_document_to_markdown function
    return binary_document_to_markdown(binary_data, ext)
