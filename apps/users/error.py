from rest_framework import status
from rest_framework.exceptions import APIException


class EmailAlreadyExistsError(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = "이미 존재하는 email입니다."
    default_code = "email_already_exists_error"