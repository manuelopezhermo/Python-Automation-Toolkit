from openpyxl.utils import range_boundaries


class MergeManager:

    def __init__(self, workbook):
        self.workbook = workbook

    def get_merge_range(self, sheet_name: str):
        """
        Método que busca todos los rangos de celas con merge en una pestaña de un workbook
        """
        merge_map = {}
        for merged_range in self.workbook.wb[sheet_name].merged_cells.ranges:
            min_col, min_row, max_col, max_row = range_boundaries(str(merged_range))
            top_left_cell = self.workbook.wb[sheet_name].cell(min_row, min_col)
            for r in range(min_row, max_row + 1):
                for c in range(min_col, max_col + 1):
                    merge_map[(r, c)] = top_left_cell
        return merge_map


    def get_merge_real_position(self, merged_ranges, cell):
        """
        Método que comprueba si la celda en estudio pertenece a un rango merged, y en caso de ser así comprueba si esa celda
        pertenece a la posicción superior izquierda, que es la celda que tendrá el valor del rango merge
        """
        resultado = "No Merge"
        for merge_cell in merged_ranges:
            if cell.coordinate in merge_cell:
                resultado = "Merge"
                if cell.row == merge_cell.min_row and cell.column == merge_cell.min_col:
                    return cell
        if resultado == "No Merge":
            return resultado
        return resultado


    def get_merge_coordinate_value(self, cell, sheet_name: str):
            """
            Método que obtiene el valor de la celda, si esta celda pertenece a un rango merged cell
            esta función comprueba si la celda es la top left del merge, de ser así devuelve su valor,
            si no lo es la descarta, de este modo, solo se queda con las celdas que tienen valores
            """
            merged_ranges = self.get_merge_range(sheet_name)
            cell_coordinate = self.get_merge_real_position(merged_ranges, cell)
            return cell_coordinate
