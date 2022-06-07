from rest_framework.exceptions import APIException


class CantGet(APIException):
    status = 401
    default_detail = "Atingiu quantidade máxima de empréstimos"
    default_code = '4026'