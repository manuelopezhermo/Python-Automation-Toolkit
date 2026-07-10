import core.workbook

wb = core.workbook.Workbook(r"C:\Users\manuel.d.lopez\Downloads\New folder\399877_4633131_V00.xlsx")
ws = wb.get_wb()


# tabla = wb.table.recoger_tabla_con_filas(["Sector", "MODELO ANTENA", "ARRAYS FRECUENCIA", "Horizont. Haz", "Tamaño", "Azimuth",
#                                    "Azimut Físico", "Altura Antena", "Altura Total", "M-tilt"], 4, "Solución Propuesta")
# print(tabla)



# tabla = wb.table.recoger_tabla_con_filas(["Tipo cable", "Longitud", "Cable", "Longitud", "Fibra", "Splitter", "Modelo", "Splitter", "TMA", "Modelo TMA", "PASIVO", "MATRIZ 1", "MATRIZ 2"],
#                                                    ["GSM 900", "UMTS 900", "UMTS 2100", "LTE 700", "LTE 800", "LTE 1800", "LTE 2100"], "Solución Propuesta")
# print(tabla)


tabla = wb.table.recoger_tabla_con_filas(["OSP", "G9", "D18", "U21", "U9", "L8", "L18", "L26", "L21"], 4, "Solución Propuesta")
print(tabla)

tabla = wb.table.recoger_tabla_con_filas(["vFe", "G9", "D18", "U21", "U9", "L8", "L18", "L26", "L21"], 4, "Solución Propuesta")
print(tabla)
																												
