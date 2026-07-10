import openpyxl
from pathlib import Path
from utils.logger_generico import get_logger
from core.merge_manager import MergeManager
from core.table import Table


class Workbook:

    def __init__(self, filepath: str):
        """
        Se crea un workbook y se carga el filepath y una configuración básica inicial
        """
        self.filepath = Path(filepath)
        self._validate_path()
        self.wb = openpyxl.load_workbook(filename = filepath, data_only = True)
        self.config = {
            "case_sensitive" : False,
            "normalize_headers" : True
        }
        self.logger = get_logger(self.__class__.__name__)
        self.merge_manager = MergeManager(self)
        self.table = Table(self)

    def _validate_path(self):
        if not self.filepath.exists():
            self.logger.error(f"El path {self.filepath} no se ha encontrado")
            raise FileNotFoundError(f"El path {self.filepath} no se ha encontrado")
        if not self.filepath.is_file():
            self.logger.error(f"El path {self.filepath} no contiene un archivo")
            raise FileNotFoundError(f"El path {self.filepath} no contiene un archivo")
        valid_extensions = [".xlsx", ".xlsm"]
        if self.filepath.suffix.lower() not in valid_extensions:
            self.logger.error(f"La extensión del archivo del path {self.filepath} no es correcta")
            raise FileNotFoundError(f"La extensión del archivo del path {self.filepath} no es correcta")
        
    def get_wb(self):
        """
        Método para obtener una hoja del workbook
        """
        # if sheet_name not in self.wb.sheetnames:
        #     self.logger.error(f"La hoja {sheet_name} no se ha encontrado en el workbook")
        #     raise ValueError(f"La hoja {sheet_name} no se ha encontrado en el workbook")
        return self.wb