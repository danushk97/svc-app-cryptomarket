from dataclasses import dataclass


@dataclass
class CryptoMarketSummary:
    symbol: str
    high: str
    low: str
    volume: str
    quote_volume: str
    percent_change: str
    updated_at: str
    