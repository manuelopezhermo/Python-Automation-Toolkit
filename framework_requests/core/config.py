"""
Esta clase se utiliza básicamente para almacenar parámetros que luego serivrán como configuración al objeto session, la
utilidad de esta clase es poder añadir los parámetros que se deseen aquí y serán visibles por el objeto sin necesidad de
modificar nada más
"""

from dataclasses import dataclass

@dataclass
class HttpConfig:
    timeout: int = 30
    verify_ssl: bool = True
    retries: int = 5

    