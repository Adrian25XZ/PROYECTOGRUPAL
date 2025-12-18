'''
Sistema de Gestion de Inventario - Interfaz Principal
Aplicacion Interactiva para gestionar productos
'''

from nuestroproyecto.models.producto import Categoria, Producto
from nuestroproyecto.repositories.inventario import Inventario, RepositorioMemoria
from nuestroproyecto.services.reportes import GenerarReportes
from nuestroproyecto.utils.validadores import Validadores
from nuestroproyecto.utils.formatters import Formateadores

class AplicacionInventario:
    
    ''''Aplicacion principal con interfaz de usuario'''
    
    def __init__(self):
        ''''Iniciar aplicacion '''
        
        self.repositorio = RepositorioMemoria()
        self.inventario = Inventario(self.repositorio)
        self.reportes = GenerarReportes(self.inventario)
        
    def mostrar_menu_principal(self) -> str:
        '''' Muestra el menu principal '''
        print('\n' + '=' * 50)
        print('........SISTEMA DE GESTION DE INVENTARIO')
        print('=' * 50)
        print('1. Agregar Producto')
        print('2. Ver Todos los Productos')
        print('3. Aumentar Stock')
        print('4. Disminuir Stock (ventas)')
        print('5. Productos con bajo stock')
        print('6. Ver reporte completo')
        print('7. Salir')
        print('=' * 50)
        
        return input('Seleccionar opcion')
    
    def agregar_producto_interactivo(self):
        ''''Permite agregar un producto de forma interactiva'''
        
        try:
            print('\n---Agregar Nuevo Producto---')
            nombre = input('Nombre del Producto: ')
            Validadores.validar_nombre_no_vacio(nombre)
            
            descripcion = input('Descripcion: ')
            
            precio = float(input('Precio: $'))
            Validadores.validar_precio_positivo(precio)
            
            cantidad = int(input('Cantidad inicial: '))
            Validadores.validar_cantidad_no_negativa(cantidad)
            
            print('\n categoria disponible:')
            for cat in Categoria:
                print(f'- {cat.value}')
                
            cat_str = input('categoria:')
            categoria = Categoria[cat_str.upper().replace(' ', '_')]
            
            producto = self.inventario.agregar_producto(nombre, descripcion, precio, cantidad, categoria)
            print(f'\nProducto agregado: {producto}')
            
        except(ValueError, KeyError) as e:
            print(f'Error: {e}')
            
    def ver_todos_productos(self):
            '''Muestra todos los productos'''
            productos = self.repositorio.obtener_todos()
            print(Formateadores.formatear_lista_productos(productos))
            
    def aumentar_stock(self):
            '''Aumenta el stock de un producto'''
            
            try:
                id_prod = int(input('\nID del producto:'))
                cantidad = int(input('Cantidad a aumentar:'))
                
                self.inventario.aumentar_stock(id_prod, cantidad)
                print('OK - Stock aumentado exitosamente')
                
            except(ValueError, KeyError) as e:
                print(f'Error: {e}')
                
    def disminuir_stock_interactivo(self):
            '''Disminuye el stock de un producto (simula venta)'''
            try:
                id_prod = int(input('\nID del producto:'))
                cantidad = int(input('cantidad vendida:'))
                
                self.inventario.disminuir_stock(id_prod, cantidad)
                print('Ok - Venta registrada exitosamente')

            except(ValueError, KeyError) as e:
                print(f'ERROR: {e}')
                
    def ver_bajo_stock(self):
            '''Muestra productos con bajo stock'''
            limite = int(input('\nLimite de stock bajo(default 10):') or '10')
            productos = self.inventario.obtener_productos_bajo_stock(limite)
            print(Formateadores.formatear_lista_productos(productos))
            
    def ver_reporte(self):
            '''Muestra el reporte completo'''
            reporte = self.reportes.reporte_completo()
            print(Formateadores.formatear_reporte(reporte))
            
    def ejecutar(self):
            '''Ejecuta la aplicacion principal'''
            self._cargar_datos_prueba()
            
            while True:
                opcion = self.mostrar_menu_principal()
                
                if opcion == '1':
                    self.agregar_producto_interactivo()
                elif opcion == '2':
                    self.ver_todos_productos()
                elif opcion == '3':
                    self.aumentar_stock()
                elif opcion == '4':
                    self.disminuir_stock_interactivo()
                elif opcion == '5':
                    self.ver_bajo_stock()
                elif opcion == '6':
                    self.ver_reporte()
                elif opcion == '7':
                    print('\nHasta luego!')
                    break
                else:
                    print('\nERROR - opcion invalida')
                
    def _cargar_datos_prueba(self):
        '''Carga datos de prueba en el inventario'''
        
        productos_prueba = [
            ('Laptop', 'Laptop HP Core i7', 899.99, 5, Categoria.ELECTRONICA),
            ('Mouse', 'Mouse inalambrico', 25.50, 50, Categoria.ELECTRONICA),
            ('Teclado', 'Teclado mecanico', 120.00, 15, Categoria.ELECTRONICA),
            ('Pan', 'Pan blanco artesanal', 3.50, 100, Categoria.ALIMENTOS),
            ('Queso', 'Queso fresco', 12.00, 30, Categoria.ALIMENTOS),
            ('Camiseta', 'Camiseta de algodon', 45.00, 20, Categoria.ROPA),
            ('Python pro', 'Libro de Python avanzado', 89.99, 8, Categoria.LIBROS),
        ]
        
        for nombre, descripcion, precio, cantidad, categoria in productos_prueba:
            self.inventario.agregar_producto(nombre, descripcion, precio, cantidad, categoria)
            
        print('OK - Datos de prueba cargados')
            
if __name__ == '__main__':
    app = AplicacionInventario()
    app.ejecutar()