from piston.handler import BaseHandler
from piston.utils import rc, require_mime


class Containers(BaseHandler):
    allowed_methods = ('GET', 'POST',)

    def read(self, request):
        pass

    def create(self, request):
        pass


class Container(BaseHandler):
    allowed_methods = ('GET', 'PUT', 'DELETE',)

    def read(self, request, id):
        pass

    def update(self, request, id):
        pass

    def delete(self, request, id):
        pass
