from pathlib import Path
from datetime import datetime
from typing import List
from utils.metadata import create_metadata
from PIL import Image
import pytesseract
from langchain_core.documents import Document

# Configure Tesseract path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


class ImageLoader:
    """
    Loads image files and extracts text using OCR.
    """

    def load(self, file_path: str) -> List[Document]:

        image = Image.open(file_path)

        text = pytesseract.image_to_string(image)

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