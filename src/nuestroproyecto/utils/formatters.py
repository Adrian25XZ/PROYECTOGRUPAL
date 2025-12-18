"""
Modulo de Utilidades - Formateadores
Define funciones para formatear y presentar datos.
"""

from typing import List, Dict, Any
from ..models.productos import Producto

class Formateadores:
    """Clase con metodos estaticos para formatear datos."""
    
    @staticmethod 
    def formatear_precio(precio: float) -> str:
        """Formatea precio con simbolo de moneda."""
        return f"${precio:.2f}"
    
    @staticmethod
    def formatear_producto_tabla(producto: Producto) -> str:
        """Formatea producto para visualizacion en tabla."""
        return (f"│ {producto.id_producto:>6} │ {producto.nombre:<20} │ "
                f"${producto.precio:>8.2f} │ {producto.cantidad:>6} │ "
                f"${producto.calcular_valor_total():>10.2f} │")

    @staticmethod
    def formatear_lista_productos(productos: List[Producto]) -> str:
        """Formatea lista de productos para visualizacion"""
        if not productos:
            return "No hay productos para mostrar"
 
        encabezado = (
            "│   ID   │         Nombre        │   Precio   │ Stock │ Valor Total │"
        )
        separador = "-" * len(encabezado)
        filas = [Formateadores.formatear_producto_tabla(p) for p in productos]
 
        return (
            f"{separador}\n{encabezado}\n{separador}\n" +
            "\n".join(filas) +
            f"\n{separador}"
        )
    
    @staticmethod
    def formatear_reporte(reporte: Dict[str, Any]) -> str:
        """Formatea reporte para visualizacion."""
        output = "\n" + "=" * 60 + "\n"
        output += "                    REPORTE DE INVENTARIO\n"
        output += "=" * 60 + "\n"
        
        output += f"Fecha: {reporte['fecha_generacion']}\n\n"
        output += f"Total de Productos: {reporte['total_productos']}\n"
        output += f"Total de Items en Stock: {reporte['total_items']}\n"
        output += f"Valor total del Inventario: ${reporte['valor_total']:.2f}\n\n"
        
        if reporte["producto_mas_caro"]:
            p = reporte["producto_mas_caro"]
            output += f"Producto más caro: {p.nombre} (${p.precio:.2f})\n"
        
        if reporte["producto_mas_barato"]:
            p = reporte["producto_mas_barato"]
            output += f"Producto más barato: {p.nombre} (${p.precio:.2f})\n"
        
        output += f"\nProductos bajo stock: {len(reporte['productos_bajo_stock'])}\n"
        output += "=" * 60 + "\n"
        
        return output