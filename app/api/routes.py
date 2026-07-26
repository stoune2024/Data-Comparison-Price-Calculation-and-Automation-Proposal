from pathlib import Path
from tempfile import TemporaryDirectory

from fastapi import APIRouter, Depends, File, UploadFile
from fastapi.responses import FileResponse

from app.dependencies import get_processing_service
from app.services.processing_service import ProcessingService

router = APIRouter()


@router.get("/health")
def health():
    return {"status": "ok"}


@router.post("/process")
async def process_file(
    file: UploadFile = File(...),
    service: ProcessingService = Depends(get_processing_service),
):

    with TemporaryDirectory() as temp_dir:
        input_path = Path(temp_dir) / file.filename
        output_path = Path(temp_dir) / "result.xlsx"

        with input_path.open("wb") as buffer:
            buffer.write(await file.read())

        service.process(
            input_path=input_path,
            output_path=output_path,
        )

        return FileResponse(
            path=output_path,
            filename="result.xlsx",
            media_type=(
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            ),
        )
