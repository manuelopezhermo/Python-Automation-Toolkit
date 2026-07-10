"""
Esta clase crea un objeto session que contiene los parámetros de configuración almacenados en config.py, aunque se pueden
modificar en la creación de un objeto de calse SessionManager. El método create_session crea el objeto y verifica que no haya
más de uno creado para evitar duplicidades. Todos los cambios que se quieran añadir se pueden introducir en ese método y ya
serán parte del objeto session
"""

import requests
from core.config import HttpConfig

class SessionManager:
    def __init__(self, config: HttpConfig):
        self.config = config
        self._session = None

    def create_session(self):
        if self._session is None:
            self._session = requests.Session()
            self._session.verify = self.config.verify_ssl
        return self._session
    
