from utils.normalizer import normalizar
from utils.coordinates import trasformar_coordenadas_a_numeros
# from collections import defaultdict
import time


class Table:

    def __init__(self, workbook):
        self.workbook = workbook


    def buscar_cabeceras(self, cabeceras: list, sheet_name: str):
        """
        Este método busca todas las cabeceras de la lista que recibe en el workbook en estudio
        y en la pestaña indicada, devuelve sus coordenadas en un diccionario, con la clave el nombre
        de la cabecera y el valor su coordenada correspondiente
        """
        ws = self.workbook.wb[sheet_name]
        cabeceras_normalizadas = [normalizar(cabecera) for cabecera in cabeceras]
        merge_range = self.workbook.merge_manager.get_merge_range(sheet_name)
        for row in ws.iter_rows():
            lista_coordenadas_fila = []
            lista_valores_fila = []
            for cell in row:
                cell_value = normalizar(cell.value)
                coordenada_merge = merge_range.get((cell.row, cell.column), cell)
                lista_coordenadas_fila.append(coordenada_merge)
                lista_valores_fila.append(cell_value)
            lista_valores_filtrada = [(i, valor) for i, valor in enumerate(lista_valores_fila) if valor != ""]

            n = len(cabeceras_normalizadas)
            for i in range(len(lista_valores_filtrada) - n + 1):
                bloque = lista_valores_filtrada[i:i+n]
                valores_bloque = [v for _, v in bloque]
                if valores_bloque == cabeceras_normalizadas:
                    indices = [idx for idx, _ in bloque]
                    lista_coordenadas_cabeceras = []
                    for indice in indices:
                        lista_coordenadas_cabeceras.append(lista_coordenadas_fila[indice])
                    print("Encontrado en índices:", indices)
                    break
        return lista_coordenadas_cabeceras


    def obtener_tabla_numero_filas(self, lista_celdas_tabla: list, numero_filas: int, sheet_name: str):
        """
        Método que recorre las filas del excel debajo de cada cabecera hasta que encuentra
        celdas con valores, de este modo, se evitan las celdas merge de existir
        """
        for celda in lista_celdas_tabla[:]:
            j = 1
            for i in range(numero_filas):
                while True:
                    celda_evaluar = self.workbook.wb[sheet_name].cell(celda.row + j, celda.column)
                    if celda_evaluar.value == None:
                        j += 1
                    else:
                        j += 1
                        break
                lista_celdas_tabla.append(celda_evaluar)
        lista_celdas_tabla.sort(key = lambda c: (c.row, c.column))
        return lista_celdas_tabla
    

    def recoger_tabla_cabeceras_laterales(self, cabeceras_columnas: list, cabeceras_filas: list, sheet_name: str):
        """
        Método que obtiene la tabla a partir de las cabeceras superiores y cabeceras laterales
        """
        cabeceras_superiores = self.buscar_cabeceras(cabeceras_columnas, sheet_name)
        cabeceras_laterales = self.buscar_cabeceras(cabeceras_filas, sheet_name)
        lista_celdas_cabeceras_superiores = []
        lista_celdas_cabeceras_laterales = []
        for nombre_cabecera, coordenada in cabeceras_superiores.items():
            fila, columna = trasformar_coordenadas_a_numeros(coordenada)
            lista_celdas_cabeceras_superiores.append(self.workbook.wb[sheet_name].cell(fila, columna))
        for nombre_cabecera, coordenada in cabeceras_laterales.items():
            fila, columna = trasformar_coordenadas_a_numeros(coordenada)
            lista_celdas_cabeceras_laterales.append(self.workbook.wb[sheet_name].cell(fila, columna))
   
        table = {}
        for left_cell in lista_celdas_cabeceras_laterales:
            row_key = left_cell.value
            table[row_key] = {}
            for top_cell in lista_celdas_cabeceras_superiores:
                col_key = top_cell.value
                value = self.workbook.wb[sheet_name].cell(
                    row=left_cell.row,
                    column=top_cell.column
                ).value
                table[row_key][col_key] = value
        return table


    def recoger_tabla_con_filas(self, cabeceras: list, numero_filas: int, sheet_name: str):
        """
        Método que obtiene el tamaño y los datos de una tabla conocidas sus cabeceras, se puede
        utilizar tanto si tenemos una tabla con cabeceras y "cabeceras laterales" como si solo se
        conoce el número de filas y las cabeceras
        """

        lista_coordenadas_cabeceras = self.buscar_cabeceras(cabeceras, sheet_name)
        lista_celdas_tabla = self.obtener_tabla_numero_filas(lista_coordenadas_cabeceras, numero_filas, sheet_name)
        return lista_celdas_tabla
    