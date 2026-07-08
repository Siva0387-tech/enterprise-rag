from pathlib import Path
from datetime import datetime


def create_metadata(
    file_path: str,
    document_type: str,
    page: int = 1,
    sheet_name: str = None,
    version_id: str = "v1",
    department: str = "General"
):
    """
    Creates standardized metadata for every document.
    """

    metadata = {
        "source": Path(file_path).name,
        "page": page,
        "document_type": document_type,
        "version_id": version_id,
        "department": department,
        "updated_at": datetime.fromtimestamp(
            Path(file_path).stat().st_mtime
        ).isoformat()
    }

    if sheet_name:
        metadata["sheet_name"] = sheet_name

    return metadata