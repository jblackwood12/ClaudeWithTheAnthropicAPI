# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python package that implements document-related tools through a Model Context Protocol (MCP) server interface. The server provides tools for document processing and mathematical operations that can be consumed by AI assistants.

## Architecture

The project follows a simple MCP server architecture:

- **main.py**: Entry point that creates a FastMCP server instance and registers tools
- **tools/**: Contains tool implementations that are exposed via the MCP server
  - Each tool is a Python function with proper type annotations using Pydantic Field descriptors
  - Tools are automatically discovered and registered with the server using `mcp.tool()` decorator
- **tests/**: Test suite with fixtures for document processing validation

The MCP server is built using FastMCP from the `mcp` library and runs as a standalone server that can be consumed by AI assistants.

## Development Commands

### Setup
```bash
# Create and activate virtual environment
uv venv
source .venv/bin/activate

# Install in development mode
uv pip install -e .
```

### Running
```bash
# Start the MCP server
uv run main.py
```

### Testing
```bash
# Run all tests
uv run pytest

# Run specific test file
uv run pytest tests/test_document.py

# Run specific test class or method
uv run pytest tests/test_document.py::TestBinaryDocumentToMarkdown::test_binary_document_to_markdown_with_docx
```

## Tool Development Guidelines

### Tool Registration
Tools are registered by importing them in main.py and using the decorator:
```python
from tools.my_tool import my_function
mcp.tool()(my_function)
```

### Tool Function Structure
Follow this pattern when creating new tools:

```python
from pydantic import Field

def my_tool(
    param1: str = Field(description="Detailed description of this parameter"),
    param2: int = Field(description="Explain what this parameter does")
) -> ReturnType:
    """Comprehensive docstring here.
    
    Takes specific inputs and explains what it returns. This tool handles
    specific use cases and behaviors.
    
    When to use:
    - When you need to perform specific operation
    - When you need particular functionality
    
    When not to use:
    - When alternative approach is better
    - When input doesn't match expected format
    
    Examples:
    >>> my_tool("example", 42)
    expected_output
    >>> my_tool("another", 100) 
    another_expected_output
    """
    # Implementation
    return result
```

### Tool Documentation Requirements
- Begin with a one-line summary in the docstring
- Provide detailed explanation of functionality
- Explain when to use (and not use) the tool
- Include usage examples with expected input/output
- Use Pydantic Field descriptions for all parameters
- Always apply appropriate types to function arguments (str, int, float, bool, list, dict, etc.)
- Use specific return type annotations for all functions

## Key Dependencies

- **mcp[cli]==1.8.0**: Model Context Protocol server framework
- **markitdown[docx,pdf]>=0.1.1**: Document conversion library for DOCX and PDF files
- **pydantic>=2.11.3**: Data validation and type annotations
- **pytest>=8.3.5**: Testing framework

## Testing Strategy

Tests use fixtures located in `tests/fixtures/` directory. The test structure validates:
- Tool functionality with real document samples
- Expected output formats and types
- Error handling for various input types

Test fixtures include sample documents (mcp_docs.docx, mcp_docs.pdf) for integration testing of document processing tools.