from requests import HTTPError

from tests.conftest import make_crypto_market_summary
from src.adapters.data_source.exception import ExternalServiceException


class FakeCryptoMarketSummaryService:
    def __init__(self, repo) -> None:
        self.repo = repo

    def retrieve_all(self):
        return [ make_crypto_market_summary() ]

class FakeCryptoMarketSummaryRaisesExceptionService(
    FakeCryptoMarketSummaryService
):
    def retrieve_all(self):
        raise ExternalServiceException() from HTTPError()
    