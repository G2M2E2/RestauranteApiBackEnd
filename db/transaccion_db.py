from typing import Dict
from datetime import datetime
from pydantic import BaseModel


class TransaccionInDB(BaseModel):
    transaccion_id: int
    producto_id: int
    venta_id: int
    cant_pedido: int
    tran_subtotal: int

database_transacciones = {
    "01": TransaccionInDB(**{"transaccion_id:":1,
                        "producto_id":1,
                        "venta_id:":1,
                        "cant_pedido":2,
                        "tran_subtotal": 15000
                        }),

    "02": TransaccionInDB(**{"transaccion_id:":2,
                        "producto_id":2,
                        "venta_id:":2,
                        "cant_pedido":1,
                        "tran_subtotal": 10000
                        }),
}


def get_all_transacciones():
    return database_transacciones


database_transacciones = []
generator = {"id":0}


def save_transaccion(transacciones_in_db: TransaccionInDB):
    generator["id"] = generator["id"] + 1
    transacciones_in_db.transaccion_id = generator["id"]
    database_transacciones.append(transacciones_in_db)
    return transacciones_in_db


def get_transaccion(id: int):
    if id in database_transacciones:
        return database_transacciones[id]
    else:
        return None
