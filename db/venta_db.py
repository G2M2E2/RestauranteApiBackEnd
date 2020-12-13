from typing import Dict
from datetime import datetime
from pydantic import BaseModel



class VentaInDB(BaseModel):
    venta_id: int = 0
    venta_fecha: datetime = datetime.now()
    venta_total: int
    telefono: int
    username: str


database_ventas = [{
    "venta_id":1,
    "venta_fecha":"2020-12-13T11:45:41.154306",
    "venta_total":5000,
    "telefono":3214567890,
    "username": "Admin"
    },
    {"venta_id":2,
    "venta_fecha":"2020-12-13T11:45:41.154306",
    "venta_total":1000,
    "telefono":3212222220,
    "username": "Admin"
    },
]

def get_all_ventas():
    return database_ventas


#database_ventas = []
len_lista = len(database_ventas)
generator = {"id":len_lista}


def save_venta(ventas_in_db: VentaInDB):
    generator["id"] = generator["id"] + 1
    ventas_in_db.venta_id = generator["id"]
    database_ventas.append(ventas_in_db)
    return ventas_in_db


def get_venta(id: int):
    if (id != 0 and (id-1) < len(database_ventas)):
        return database_ventas[id-1]
    else:
        return "No existe la factura buscada"
