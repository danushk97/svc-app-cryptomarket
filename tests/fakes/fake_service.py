from tests.conftest import make_crypto_market_summary


class FakeCryptoMarketSummaryService:
    def __init__(self, repo) -> None:
        self.repo = repo

    def retrieve_all(self):
        return [ make_crypto_market_summary() ]
    