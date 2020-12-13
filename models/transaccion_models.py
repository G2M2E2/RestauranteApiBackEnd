from pydantic import BaseModel

class TransaccionIn(BaseModel):
    cant_pedido: int
    producto_id: str

class TransaccionOut(BaseModel):
    transaccion_id: int
    producto_id: str
    venta_id: int
    cant_pedido: int
    #tran_subtotal: int
