from pathlib import Path
from typing import List
from datetime import datetime
from langchain_core.documents import Document
from pypdf import PdfReader
from utils.metadata import create_metadata


class PDFLoader:
    """
    Loads PDF files and returns a list of LangChain Document objects.
    Each page is represented as a separate Document.
    """

    def load(self, file_path: str) -> List[Document]:

        reader = PdfReader(file_path)

        documents = []

        for page_number, page in enumerate(reader.pages, start=1):

            text = page.extract_text()

            if not text:
                continue

            metadata = create_metadata(
                file_path=file_path,
                document_type="pdf",
                page=page_number
            )

            documents.append(
                Document(
                    page_content=text,
                    metadata=metadata
                )
            )

        return documents