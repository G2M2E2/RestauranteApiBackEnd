from pydantic import BaseModel

class TransaccionIn(BaseModel):
    cant_pedido: int
    id: str
    #venta_id: int
    

class TransaccionOut(BaseModel):
    transaccion_id: int
    id: str #producto id
    venta_id: int
    cant_pedido: int
    tran_subtotal: int
