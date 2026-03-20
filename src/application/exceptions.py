from rest_framework.exceptions import APIException

class AlreadyExistsException(APIException):
    status_code = 400
    default_detail = "Object already exists"