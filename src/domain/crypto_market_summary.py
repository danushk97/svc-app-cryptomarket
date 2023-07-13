from dataclasses import dataclass, fields, asdict

from src.constants import Constants


@dataclass
class CryptoMarketSummary:
    symbol: str
    high: str
    low: str
    volume: str
    quote_volume: str
    percent_change: str
    updated_at: str

    @classmethod
    def from_dict(cls, summary_dict: dict):
        return cls(
            *[
                summary_dict[Constants.snake_to_camel_case(field.name)]
                for field in fields(cls)
            ]
        )
    
    def to_dict(self) -> dict:
        return asdict(self)
    