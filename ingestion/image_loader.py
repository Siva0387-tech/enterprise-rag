from pathlib import Path
from typing import List

import easyocr
from langchain_core.documents import Document

from utils.metadata import create_metadata


class ImageLoader:
    """
    Loads image files and extracts text using EasyOCR.
    """

    def __init__(self):
        # Initialize EasyOCR reader once
        self.reader = easyocr.Reader(['en'], gpu=False)

    def load(self, file_path: str) -> List[Document]:

        # Read text from image
        results = self.reader.readtext(file_path)

        # Combine detected text
        text = "\n".join([result[1] for result in results])

        # Debug output (remove after testing)
        print("\n===== OCR OUTPUT =====")
        print(text)
        print("======================\n")

        document_type = Path(file_path).suffix.replace(".", "")

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