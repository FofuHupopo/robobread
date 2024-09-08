from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

from . import exceptions


class ServiceResponseExceptionMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        if isinstance(exception, exceptions.ServiceResponseException):
            return JsonResponse(
                exception.response or {'error': str(exception)},
                status=exception.status_code
            )

        return None


class NoObjectExceptionMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        if isinstance(exception, exceptions.NoObjectException):
            return JsonResponse(
                exception.response or {'error': str(exception)},
                status=404
            )

        return None
