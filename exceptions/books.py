from rest_framework.exceptions import APIException


class NoBook(APIException):
    status = 400
    default_detail = "Todos exemplares estão emprestados"
    default_code = '4026'

class NotAvailable(APIException):
    status = 400
    default_detail = "Livro não disponível"
    default_code = '4026'
