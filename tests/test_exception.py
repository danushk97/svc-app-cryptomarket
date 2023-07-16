from src.exception import AppException


def test_create_app_exception_returns_instance_with_deafault_init_values():
    exception = AppException()
    assert exception.title == "Internal Server Error"
    assert exception.detail == (
        "The server encountered an internal error and was unable to complete "
        "your request"
    )
    assert exception.type == "about:blank"
    assert exception.status == 500
    assert exception.__cause__ is None
