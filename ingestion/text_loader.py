from pathlib import Path
from datetime import datetime
from typing import List
from utils.metadata import create_metadata
from langchain_core.documents import Document
from striprtf.striprtf import rtf_to_text


class TextLoader:
    """
    Loads TXT and RTF files.
    """

    def load(self, file_path: str) -> List[Document]:

        extension = Path(file_path).suffix.lower()

        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            text = file.read()

        if extension == ".rtf":
            text = rtf_to_text(text)

        document_type = extension.replace(".", "")

        metadata = create_metadata(
            file_path=file_path,
            document_type=document_type,
            page=1
        )

        return [
            Document(
                page_content=text,
                metadata=metadata
            )
        ]