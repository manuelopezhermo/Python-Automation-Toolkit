import unidecode
import re

def normalizar(texto):
        """
        Método que normaliza texto, quitando mayúsculas, acentos ortográficos, espacios, separadores...
        """
        if texto is None:
            return ""
        texto = str(texto)
        texto = unidecode.unidecode(texto)
        texto = texto.lower()
        texto = texto.strip()
        texto = re.sub(r"[-_/]", " ", texto)
        texto = re.sub(r"\s+", " ", texto)
        return texto
