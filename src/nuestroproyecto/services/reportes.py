from typing import Dict, Any, Optional
from datetime import datetime
from ..models.producto import Producto
from ..repositories.inventario import Inventario


class GenerarReportes:
    
    def __init__(self, inventario: Inventario):
        self.inventario = inventario
        
    def valor_total_inventario(self) -> float:
        productos = self.inventario.repositorio.obtener_todos()
        return sum(p.calcular_valor_total() for p in productos)
    
    def cantidad_total_productos(self) -> int:
        return len(self.inventario.repositorio.obtener_todos())
    
    def total_items_stock(self) -> int:
        productos = self.inventario.repositorio.obtener_todos()
        return sum(p.cantidad for p in productos)
    
    def producto_mas_caro(self) -> Optional[Producto]:
        productos = self.inventario.repositorio.obtener_todos()
        return max(productos, key=lambda p: p.precio) if productos else None
    
    def productos_mas_baratos(self) -> Optional[Producto]:
        productos = self.inventario.repositorio.obtener_todos()
        return min(productos, key=lambda p: p.precio) if productos else None
    
    def reporte_completo(self) -> Dict[str, Any]:
        return {
            'fecha_generacion': datetime.now().strftime('%d-%m-%Y %H:%M:%S'),
            'total_productos': self.cantidad_total_productos(),
            'total_items': self.total_items_stock(),
            'valor_total': self.valor_total_inventario(),
            'producto_mas_caro': self.producto_mas_caro(),
            'producto_mas_barato': self.productos_mas_baratos(),
            'productos_bajo_stock': self.inventario.obtener_productos_bajo_stock()
            
        }