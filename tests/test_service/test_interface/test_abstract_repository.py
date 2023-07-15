import pytest

from src.service.interface.abstract_repository import AbstractRepository



class FakeRepo(AbstractRepository):
    def list(self):
        return super().list()

    def find_by_market(self, summary: str):
        return super().find_by_market(summary)


def test_abstract_repo_raises_non_implemented_error():
    fake_repo = FakeRepo()
    
    with pytest.raises(NotImplementedError):
        fake_repo.list()
    
    with pytest.raises(NotImplementedError):
        fake_repo.find_by_market('summary')
