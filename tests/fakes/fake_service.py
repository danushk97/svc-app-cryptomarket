from requests import HTTPError

from tests.conftest import make_crypto_market_summary
from src.adapters.data_source.exception import ResourceNotFoundException


class FakeCryptoMarketSummaryService:
    def __init__(self, repo) -> None:
        self.repo = repo

    def retrieve_all(self):
        return [make_crypto_market_summary()]

    def retrieve_market_summary_for(self, market):
        return make_crypto_market_summary()


class FakeCryptoMarketSummaryServiceRaisesException(
    FakeCryptoMarketSummaryService
):
    def retrieve_all(self):
        raise Exception

    def retrieve_market_summary_for(self, market):
        raise ResourceNotFoundException() from HTTPError()
