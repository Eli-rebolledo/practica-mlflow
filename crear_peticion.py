import json, sys
sys.path.append("src")
from data import cargar_limpio, ajustar_preprocesador, aplicar_preprocesador

datos = cargar_limpio()
pre = ajustar_preprocesador(datos)
pos = int((datos["at_risk"] == 1).idxmax()); fila = aplicar_preprocesador(datos, pre).iloc[[pos]]
cuerpo = {"dataframe_split": {"columns": list(fila.columns), "data": fila.values.tolist()}}
json.dump(cuerpo, open("peticion.json", "w"))
print("Listo. at_risk real de ese estudiante:", datos["at_risk"].iloc[0])
