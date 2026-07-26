from app.infrascructure.excel_reader import ExcelReader
from app.infrascructure.excel_writer import ExcelWriter
from app.infrascructure.fuzzy_matcher import FuzzyMatcher
from app.services.pricing_service import PricingService
from app.services.processing_service import ProcessingService


def get_processing_service() -> ProcessingService:
    return ProcessingService(
        writer=ExcelWriter(),
        matcher=FuzzyMatcher(),
        pricing=PricingService(),
    )
