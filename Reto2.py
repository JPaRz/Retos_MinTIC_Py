def compra_producto(valor_producto: int, nro_cuotas:int)->dict:
   dic_vacio= {}
   
   if nro_cuotas<1 or nro_cuotas>18:
       return dic_vacio
   if nro_cuotas>=1 and nro_cuotas<=18:
       cuota_inicial= valor_producto*0.15
       valor_deuda= valor_producto-cuota_inicial
       
       if nro_cuotas<=6:
           valor_cuota= (valor_deuda*1.10)/nro_cuotas
       elif nro_cuotas<=12:
           valor_cuota= (valor_deuda*1.12)/nro_cuotas
       else:
           valor_cuota= (valor_deuda*1.15)/nro_cuotas
           
   valor_final_producto= cuota_inicial+(valor_cuota*nro_cuotas)
   dic_compra= {
       "valor_producto":valor_producto,
       "cuota_inicial":int(cuota_inicial),
       "nro_cuotas":nro_cuotas,
       "valor_cuota":int(valor_cuota),
       "valor_final_producto":int(valor_final_producto)
   }
   return dic_compra
   
       