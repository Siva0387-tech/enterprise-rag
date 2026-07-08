from pathlib import Path
from datetime import datetime
from typing import List
from utils.metadata import create_metadata
import pandas as pd
from langchain_core.documents import Document


class ExcelLoader:
    """
    Loads CSV and Excel files and returns
    LangChain Document objects.
    """

    def load(self, file_path: str) -> List[Document]:

        extension = Path(file_path).suffix.lower()

        if extension == ".csv":
            return self._load_csv(file_path)

        elif extension == ".xlsx":
            return self._load_xlsx(file_path)

        else:
            raise ValueError(f"Unsupported file type: {extension}")

    def _load_csv(self, file_path: str) -> List[Document]:

        df = pd.read_csv(file_path)

        text = df.to_string(index=False)

        metadata = {
            "source": Path(file_path).name,
            "page": 1,
            "sheet_name": "CSV",
            "document_type": "csv",
            "version_id": "v1",
            "department": "General",
            "updated_at": datetime.fromtimestamp(
                Path(file_path).stat().st_mtime
            ).isoformat()
        }

        return [
            Document(
                page_content=text,
                metadata=metadata
            )
        ]

    def _load_xlsx(self, file_path: str) -> List[Document]:

        excel = pd.ExcelFile(file_path)

        documents = []

        for sheet in excel.sheet_names:

            df = pd.read_excel(file_path, sheet_name=sheet)

            text = df.to_string(index=False)

            metadata = create_metadata(
                file_path=file_path,
                document_type="xlsx",
                sheet_name=sheet
            )

            documents.append(
                Document(
                    page_content=text,
                    metadata=metadata
                )
            )

        return documents