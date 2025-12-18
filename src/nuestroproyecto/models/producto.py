from datetime import datetime
from enum import Enum

class Categoria(Enum):
    
    ELECTRONICA = 'Electronica'
    ALIMENTOS = 'Alimentos'
    ROPA = 'Ropa'
    LIBROS = 'libros'
    OTROS = 'Otros'
    
class Producto:
    
    _contador = 1000
    
    def __init__(self, nombre: str, descripcion: str, precio: float, cantidad: int, categoria: Categoria):
        
        if not nombre or not nombre.strip():
            raise ValueError('El nombre no puede estar vacio')
        if precio < 0:
            raise ValueError('el precio no puede ser negativo')
        if cantidad < 0:
            raise ValueError('la cantidad no puede ser negativa')
        
        Producto._contador += 1
        self.id_producto = Producto._contador
        self.nombre = nombre.strip()
        self.descripcion = descripcion.strip()
        self.precio = precio
        self.cantidad = cantidad
        self.categoria = categoria
        self.fecha_creacion = datetime.now().strftime('%d-%m-%Y %H-%M%S')
        
    def actualizar_cantidad(self, cantidad: int) -> bool:
        
        if cantidad < 0:
            raise ValueError('la cantidad no puede ser negativa')
        self.cantidad = cantidad
        return True
    
    def actualizar_precio(self, precio: float) -> bool:
        
        if precio < 0:
            raise ValueError('el precio no puede ser negativo')
        self.precio = precio
        return True
    
    def calcular_valor_total(self) -> float:
        
        return self.precio * self.cantidad
    
    
    def __str__(self)-> str:
        
        return f'[{self.id_producto}]{self.nombre} - ${self.precio:.2f}(Stock: {self.cantidad})'
    
    def __repr__(self) -> str:
        return f'Producto(if={self.id_producto}, nombre={self.nombre}, precio={self.precio}, cantidad={self.cantidad})'
