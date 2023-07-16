from src.service.crypto_market_summary_service import \
    CryptoMarketSummaryService
from src.adapters.repository.crypto_market_summary_http_repository import \
    CryptoMarketSummaryHttpRepository


def retrieve_all():
    repository = CryptoMarketSummaryHttpRepository()
    service = CryptoMarketSummaryService(repository)
    data = service.retrieve_all()

    return [row.to_dict() for row in data]


def retrieve_market_summary_for(market: str):
    repository = CryptoMarketSummaryHttpRepository()
    service = CryptoMarketSummaryService(repository)
    data = service.retrieve_market_summary_for(market)

    return data
