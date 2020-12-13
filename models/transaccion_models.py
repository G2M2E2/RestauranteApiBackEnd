from pydantic import BaseModel

class TransaccionIn(BaseModel):
    producto_id: int
    venta_id: int
    cant_pedido: int
    tran_subtotal: int

class TransaccionOut(BaseModel):
    transaccion_id: int
    producto_id: int
    venta_id: int
    cant_pedido: int
    tran_subtotal: int
