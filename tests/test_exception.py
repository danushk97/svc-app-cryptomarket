from src.exception import AppException


def test_app_exception_construction_returns_instance_with_deafault_init_values():
    exception = AppException()
    assert exception.title.value == "Internal Server Error"
    assert exception.detail == "Unknown error has occured"
    assert exception.type == "about:blank"
    assert exception.status == 500
    assert exception.__cause__ == None
