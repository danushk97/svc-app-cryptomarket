from http import HTTPStatus

from src.error_codes import ErrorCode


class AppException(Exception):
    def __init__(
        self, 
        title=ErrorCode.INTERNAL_SERVER_ERROR,
        detail="Unknown error has occured",
        status=HTTPStatus.INTERNAL_SERVER_ERROR,
        type="about:blank"
    ) -> None:
        self.title = title
        self.detail = detail
        self.status = status
        self.type = type
    