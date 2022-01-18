import pandas as pd
df= pd.read_excel("Fallecidos.xls") 

value= df[["DNI", "NOMBRE", "APELLIDO", "Fecha Fallecimiento"]]
value['NOMBRE Y APELLIDO'] = value["NOMBRE"]+ "," +value["APELLIDO"]
resultado= value[["DNI", "NOMBRE Y APELLIDO", "Fecha Fallecimiento"]]
resultado['Fecha Fallecimiento']=resultado['Fecha Fallecimiento'].dt.strftime('%d/%m/%Y')

resultado.to_excel("resultados.xlsx")


