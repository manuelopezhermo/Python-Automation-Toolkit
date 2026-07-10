import openpyxl

def trasformar_coordenadas_a_numeros(coordenada: str):
        """
        Esta función transforma coordenadas del excel, por ejemplo, A32 en enteros que es lo que utiliza openpyxl
        para identificar filas y columnas, en este ejemplo, fila 32 columna 1
        """
        column_letra, fila = openpyxl.utils.cell.coordinate_from_string(coordenada)
        columna = openpyxl.utils.cell.column_index_from_string(column_letra)
        return fila, columna
