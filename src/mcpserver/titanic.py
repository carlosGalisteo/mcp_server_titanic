from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel
from typing import List
from pathlib import Path
import pandas as pd

#Ruta del archivo xls del Titanic
DATA_PATH = Path(r"C:\CURSOS\MCP\Datos\titanic.xls")

mcp = FastMCP(name = "Titanic Survival")

def load_titanic_df() -> pd.DataFrame:
    """Carga el DataFrame del Titanic desde un archivo xls.
    y normaliza nombre de columnas.
    """
    df = pd.read_excel(DATA_PATH)
    df.columns = [c.strip().lower() for c in df.columns]
    
    if "age" not in df.columns or "name" not in df.columns:
        raise ValueError("El archivo xls no contiene las columnas esperadas 'age' y 'name'.")
    return df

class Passenger(BaseModel):
    name: str
    age: float
    
class AgeFilterResult(BaseModel):
    count: int
    passengers: List[Passenger]
    
@mcp.tool()
def pasajeros_menores_de(edad_max: float) -> AgeFilterResult:
    """Devuelve los pasajeros menores de una edad dada.
    y sus nombres"""
    df = load_titanic_df()
    mask = (df["age"] < edad_max) & (df["age"].notna())
    resultados = df[mask]
    
    pasajeros = [
        Passenger(name=row["name"], age=row["age"])
        for _, row in resultados.iterrows()
    ]
    
    return AgeFilterResult(count=len(pasajeros), passengers=pasajeros)


