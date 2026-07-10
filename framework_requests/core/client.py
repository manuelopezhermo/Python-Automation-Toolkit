"""
Clase que crea directamente en el init un objeto que tiene referencia a un objeto de la clase HttpConfig y a un objeto de la
clase SessionManager. Al hacer cualquier llamada a una de las funciones que definen los métodos (get, post...) éstas a su vez
llaman al método _request_methods que es la que contiene toda la lógica, que además, en un futuro si se quiere aumentar tan
solo se debe modificar el método _request_methods
"""

from core.config import HttpConfig
from core.session_manager import SessionManager
from urllib.parse import urlparse


class HttpClient:

    def __init__(self, config: HttpConfig):
        self.config = config
        self.session = SessionManager(config).create_session()

    def _request_methods(self, method: str, url: str, **Kwargs):
        """
        Este es el método principal de la clase, todos los métodos de llamada de request (get, post...) pasan por este método,
        de este modo, si en el futuro se introducen cambios o nueva lógica tan solo se debe cambiar este método y los demás lo
        recibirán automáticamente
        """
        url_val = urlparse(url)
        if not url_val.scheme or not url_val.netloc:
            raise ValueError(f"La URL introducida {url} no es válida, revisar")
        return self.session.request(method = method, url = url, timeout = self.config.timeout, **Kwargs)
    
    def get(self, url: str, **Kwargs):
        return self._request_methods("GET", url, **Kwargs)
    def post(self, url: str, **Kwargs):
        return self._request_methods("POST", url, **Kwargs)
    def put(self, url: str, **Kwargs):
        return self._request_methods("PUT", url, **Kwargs)
    def patch(self, url: str, **Kwargs):
        return self._request_methods("PATCH", url, **Kwargs)
    def delete(self, url: str, **Kwargs):
        return self._request_methods("DELETE", url, **Kwargs)