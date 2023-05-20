from rest_framework import status
from rest_framework.exceptions import APIException


class UsernameAlreadyExistsError(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = "이미 존재하는 username입니다."
    default_code = "username_already_exists_error"