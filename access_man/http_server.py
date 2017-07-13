from eve import Eve
from eve.auth import BasicAuth

from access_man.utils import Singleton


class Auth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        pass


class RestApiServer(metaclass=Singleton):
    def __init__(self):
        self.__app = Eve(auth=Auth)

    def start(self):
        self.__app.run()
    pass
