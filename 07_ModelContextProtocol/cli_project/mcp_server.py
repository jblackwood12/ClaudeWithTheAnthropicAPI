from pydantic import Field
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("DocumentMCP", log_level="ERROR")


docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}


@mcp.tool(
    name="read_doc_contents", 
    description="Read the contents of a document and return it as a string."
)
def read_document(
    doc_id: str = Field(description="Id of the document to read")
):
    if doc_id not in docs:
        raise ValueError(f"Document with id '{doc_id}' not found.")
    return docs[doc_id]


@mcp.tool(
    name="edit_document",
    description="Edit a document by replacing a string in the documents content with a new string."
)
def edit_document(
    doc_id: str = Field(description="Id of the document to edit"),
    old_str: str = Field(description="String to replace in the document"),
    new_str: str = Field(description="String to replace with in the document")
):
    if doc_id not in docs:
        raise ValueError(f"Document with id '{doc_id}' not found.")
    if old_str not in docs[doc_id]:
        raise ValueError(f"String '{old_str}' not found in document '{doc_id}'.")
    
    docs[doc_id] = docs[doc_id].replace(old_str, new_str)


@mcp.resource("docs://documents",
              mime_type="application/json"
)
def list_docs() -> list[str]:
    return list(docs.keys()) # the SDK will turn this into JSON automatically


@mcp.resource("docs://documents/{doc_id}",
              mime_type="text/plain"
)
def fetch_doc(doc_id: str) -> list[str]:        # parameter here must also be listed on the resource definition.
    if doc_id not in docs:
        raise ValueError(f"Document with id '{doc_id}' not found.")
    return docs[doc_id]





# TODO: Write a resource to return the contents of a particular doc
# TODO: Write a prompt to rewrite a doc in markdown format
# TODO: Write a prompt to summarize a doc


if __name__ == "__main__":
    mcp.run(transport="stdio")
