from rest_framework.exceptions import APIException

class AlreadyExistsException(APIException):
    status_code = 400
    default_detail = "Object already exists"
    
class InvalidCredentialsException(APIException):
    status_code = 401
    default_detail = "Invalid credentials"
    
class NotFoundException(Exception):
    pass
    
class PermissionDeniedException(Exception):
    pass