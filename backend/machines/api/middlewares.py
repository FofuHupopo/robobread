import logging

from django.core import exceptions

from api.synchronizer import models


class MachineTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger(__name__)

    def __call__(self, request):
        request.machine = None

        token = request.headers.get('Machine-Token')
        if token:
            try:
                machine = models.MachineModel.objects.get(token=token)
                request.machine = machine
            except models.MachineModel.DoesNotExist:
                self.logger.warning(f"Machine with token {token} not found")
            except exceptions.ValidationError:
                self.logger.warning(f"Incorrect token {token} format")

        return self.get_response(request)
