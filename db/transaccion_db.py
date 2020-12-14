from typing import Dict
from datetime import datetime
from pydantic import BaseModel

class TransaccionInDB(BaseModel):
    transaccion_id: int = 0
    id: str #id producto
    venta_id: int
    cant_pedido: int
    tran_subtotal: int


database_transacciones =  [{
    "transaccion_id":1,
    "producto_id":"CA01",
    "venta_id:":1,
    "cant_pedido":2
    },
    {"transaccion_id":2,
    "producto_id":"CA01",
    "venta_id:":2,
    "cant_pedido":1
    },
]


def get_all_transacciones():
    return database_transacciones


#database_transacciones = []
generator_tr = {"id":0}


def save_transaccion(transacciones_in_db: TransaccionInDB):
    generator_tr["id"] = generator_tr["id"] + 1
    transacciones_in_db.transaccion_id = generator_tr["id"]
    database_transacciones.append(transacciones_in_db)
    return transacciones_in_db


def get_transaccion(id: int):
    if (id != 0 and (id-1) < len(database_transacciones)):
        return database_transacciones[id-1]
    else:
        return "No existe la transaccion buscada"

"""
def calcular_total(cant_pedido: int, precio: int):
    total = cant_pedido * precio
    return total
    """
