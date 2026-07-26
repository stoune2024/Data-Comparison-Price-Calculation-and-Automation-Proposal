from app.services.processing_service import ProcessingService


def get_processing_service() -> ProcessingService:
    return ProcessingService()
