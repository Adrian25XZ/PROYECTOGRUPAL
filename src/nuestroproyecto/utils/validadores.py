"""
Modulo de utilidades - Validadores 
Define funciones para validar entrada de datos 
"""

from typing import List 
class Validadores:
    """Clase con metodos estaticos para validaciones."""
    
    @staticmethod
    def validar_precio_positivo(precio: float) -> bool:
        """Valida que el precio sea positivo."""
        if not isinstance(precio, (int, float)):
            raise ValueError("El precio debe ser un numero")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        return True
    
    @staticmethod
    def validar_cantidad_no_negativa(cantidad: int) -> bool:
        """Valida que la cantidad no sea negativa."""
        if not isinstance(cantidad, int):
            raise ValueError("La cantidad debe ser un numero entero.")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        return True
    
    @staticmethod
    def validar_nombre_no_vacio(nombre: str) -> bool:
        """Valida que el nombre no este vacio."""
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser texto")
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacio")
        return True
    
    @staticmethod
    def validar_categoria_valida(categoria: str, categoria_validas: List[str]) -> bool:
        """Valida que la categoria este en la lista de categorias validas."""
        if categoria not in categoria_validas:
            raise ValueError(f"Categoria invalida. Validas: {', '.join(categoria_validas)}")
        return True
     
        