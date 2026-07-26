from pathlib import Path
from tempfile import NamedTemporaryFile

from fastapi import APIRouter, Depends, File, UploadFile
from fastapi.responses import FileResponse

from app.dependencies import get_processing_service
from app.services.processing_service import ProcessingService

router = APIRouter()


@router.post("/process")
async def process_file(
    file: UploadFile = File(...),
    service: ProcessingService = Depends(get_processing_service),
):
    with NamedTemporaryFile(suffix=".xlsx", delete=False) as input_tmp:
        input_tmp.write(await file.read())
        input_path = Path(input_tmp.name)

    with NamedTemporaryFile(suffix=".xlsx", delete=False) as output_tmp:
        output_path = Path(output_tmp.name)

    service.process(
        input_path=input_path,
        output_path=output_path,
    )

    return FileResponse(
        output_path,
        filename="result.xlsx",
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )