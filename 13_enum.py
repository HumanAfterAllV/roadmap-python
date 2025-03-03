from enum import Enum
import random

class EstadoPedido(Enum):
    PENDIENTE = "Pendiente"
    ENVIADO = "Enviado"
    ENTREGADO = "Entregado"
    CANCELADO= "Cancelado"

class Pedido:
    def __init__(self, id):
        self.id = id
        self.estado = EstadoPedido.PENDIENTE

    def cambiar_estado(self, nuevo_estado):

        if isinstance(nuevo_estado, EstadoPedido):
            self.estado = nuevo_estado
            print(f"Pedido {self.id} actualizado a: {self.estado.value}")
        else:
            print("Error: Estado inválido")
    
    def __repr__(self):
        return f"Pedido (ID: {self.id} - Estado: {self.estado.value}"
    
class PedidoBuilder:
    def __init__(self):
        self.id = None

    def dar_id(self):
        digito1 = random.randint(0, 9)
        digito2 = random.randint(0, 9)

        self.id = digito1 * 10 + digito2

        return self
    
    def construir(self):
        if self.id is None:
            raise ValueError("Error: El pedido debe contener un ID")
        return Pedido(self.id)
    
class GestorPedidos:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GestorPedidos, cls).__new__(cls)
            cls._instance.pedidos = {}
        return cls._instance

    def agregar_pedido(self, pedido):
        if pedido.id in self.pedidos:
            print(f"Error: El pedido con ID:{pedido.id} ya existe")
        else:
            self.pedidos[pedido.id] = pedido
            print(f"Pedido {pedido.id} añadido al gestor.")
    
    def obtener_pedido(self, id):
        return self.pedidos.get(id, "Pedido no encontrado")
    
    def listas_pedidos(self):
        if not self.pedidos:
            print("No hay pedidos")
        else:
            
            for pedido in self.pedidos.values():
                print(pedido)

gestor = GestorPedidos()  # Singleton: Una única instancia del gestor

while True:
    print("\n--- Menú ---")
    print("1 - Crear un nuevo pedido")
    print("2 - Listar pedidos")
    print("3 - Modificar estado de un pedido")
    print("4 - Salir")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        
        builder = PedidoBuilder()
        pedido = builder.dar_id().construir()
        gestor.agregar_pedido(pedido)  

    elif opcion == "2":
        gestor.listas_pedidos()  

    elif opcion == "3":
        try:
            id_pedido = int(input("Ingrese el ID del pedido a modificar: ").strip())
            pedido = gestor.obtener_pedido(id_pedido)
            if isinstance(pedido, Pedido):
                print("\nSeleccione el nuevo estado:")
                print("1 - Enviado")
                print("2 - Entregado")
                print("3 - Cancelado")

                estado_opcion = input("Seleccione una opción: ").strip()
                if estado_opcion == "1":
                    pedido.cambiar_estado(EstadoPedido.ENVIADO)
                elif estado_opcion == "2":
                    if pedido.estado == EstadoPedido.PENDIENTE:
                        print("Error: No se puede cambiar directamente de Pendiente a Entregado.")
                    else:
                        pedido.cambiar_estado(EstadoPedido.ENTREGADO)
                elif estado_opcion == "3":
                    pedido.cambiar_estado(EstadoPedido.CANCELADO)
                else:
                    print("Opción inválida.")
            else:
                print("Pedido no encontrado.")
        except ValueError:
            print("Error: Debe ingresar un número válido.")

    elif opcion == "4":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción inválida, intente de nuevo.")

