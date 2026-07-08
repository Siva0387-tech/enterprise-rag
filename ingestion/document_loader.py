from pathlib import Path

from ingestion.pdf_loader import PDFLoader
from ingestion.docx_loader import DOCXLoader
from ingestion.text_loader import TextLoader
from ingestion.excel_loader import ExcelLoader
from ingestion.image_loader import ImageLoader


class DocumentLoader:
    """
    Master document loader that automatically routes
    files to the appropriate loader based on file extension.
    """

    def __init__(self):

        # Register all supported loaders
        self.loaders = {
            ".pdf": PDFLoader(),
            ".docx": DOCXLoader(),
            ".txt": TextLoader(),
            ".rtf": TextLoader(),
            ".csv": ExcelLoader(),
            ".xlsx": ExcelLoader(),
            ".png": ImageLoader(),
            ".jpg": ImageLoader(),
            ".jpeg": ImageLoader(),
        }

    def load(self, file_path: str):
        """
        Load a document using the appropriate loader.

        Args:
            file_path (str): Path to the document.

        Returns:
            List[Document]: LangChain Document objects.
        """

        extension = Path(file_path).suffix.lower()

        loader = self.loaders.get(extension)

        if loader is None:
            raise ValueError(
                f"Unsupported document type: {extension}"
            )

        return loader.load(file_path)