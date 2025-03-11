from abc import ABC, abstractmethod
import random
import time

# 🎯 Interfaz para estrategias de combate (Patrón Strategy)
class EstrategiaCombate(ABC):
    def __init__(self, vida):
        self.vida = vida

    @abstractmethod
    def atacar(self):
        pass

    @abstractmethod
    def esquivar(self):
        pass

    def recibir_daño(self, daño):
        if self.esquivar():
            return f"{self.__class__.__name__} esquivó el ataque!"
        else:
            self.vida -= daño
            return f"{self.__class__.__name__} recibió {daño} de daño. Vida restante: {self.vida}"

    def esta_vivo(self):
        return self.vida > 0


class WolverineEstrategia(EstrategiaCombate):
    def atacar(self):
        return random.randint(10, 120)

    def esquivar(self):
        return random.random() <= 0.20


class DeadpoolEstrategia(EstrategiaCombate):
    def atacar(self):
        return random.randint(10, 100)

    def esquivar(self):
        return random.random() <= 0.25


class CombateLogger:
    def __init__(self):
        self.eventos = []

    def registrar_evento(self, mensaje):
        self.eventos.append(mensaje)
        print(mensaje)
        time.sleep(1)


class Combate:
    def __init__(self, jugador, enemigo, logger):
        self.jugador = jugador
        self.enemigo = enemigo
        self.logger = logger

    def iniciar(self):
        turno = 1
        aturdido_jugador = False
        aturdido_enemigo = False

        self.logger.registrar_evento("¡Comienza la pelea! ⚔️")

        while self.jugador.esta_vivo() and self.enemigo.esta_vivo():
            self.logger.registrar_evento(f"\n🔹 Turno {turno} 🔹")

            if not aturdido_jugador:
                daño = self.jugador.atacar()
                resultado = self.enemigo.recibir_daño(daño)
                self.logger.registrar_evento(f"👊 {self.jugador.__class__.__name__} ataca con {daño} de daño.")
                self.logger.registrar_evento(resultado)

                if daño == 120 or daño == 100:
                    self.logger.registrar_evento(f"😵 {self.enemigo.__class__.__name__} está aturdido y pierde su turno!")
                    aturdido_enemigo = True
            else:
                self.logger.registrar_evento(f"⚠️ {self.jugador.__class__.__name__} estaba aturdido y pierde el turno.")
                aturdido_jugador = False

            if not self.enemigo.esta_vivo():
                self.logger.registrar_evento(f"🏆 {self.jugador.__class__.__name__} GANA LA PELEA!")
                break

            if not aturdido_enemigo:
                daño = self.enemigo.atacar()
                resultado = self.jugador.recibir_daño(daño)
                self.logger.registrar_evento(f"💥 {self.enemigo.__class__.__name__} ataca con {daño} de daño.")
                self.logger.registrar_evento(resultado)

                if daño == 120 or daño == 100:
                    self.logger.registrar_evento(f"😵 {self.jugador.__class__.__name__} está aturdido y pierde su turno!")
                    aturdido_jugador = True
            else:
                self.logger.registrar_evento(f"⚠️ {self.enemigo.__class__.__name__} estaba aturdido y pierde el turno.")
                aturdido_enemigo = False

            
            if not self.jugador.esta_vivo():
                self.logger.registrar_evento(f"🏆 {self.enemigo.__class__.__name__} GANA LA PELEA!")
                break

            turno += 1 
            time.sleep(1)  

    def mostrar_resultado(self):
        if self.jugador.esta_vivo():
            print("🎉 ¡Ganaste el combate!")
        else:
            print("💀 Has sido derrotado...")


def menu():
    print("\n🔥 Bienvenido a Deadpool vs Wolverine 🔥")
    print("Elige tu personaje:")
    print("(1) Deadpool")
    print("(2) Wolverine")

    while True:
        try:
            eleccion = int(input("Tu elección: "))
            if eleccion in [1, 2]:
                break
            print("❌ Opción inválida. Elige 1 o 2.")
        except ValueError:
            print("❌ Ingresa un número válido.")

    vida_inicial = 200  

    if eleccion == 1:
        jugador = DeadpoolEstrategia(vida_inicial)
        enemigo = WolverineEstrategia(vida_inicial)
        print("\n🤠 Elegiste a DEADPOOL. La máquina usará a WOLVERINE.")
    else:
        jugador = WolverineEstrategia(vida_inicial)
        enemigo = DeadpoolEstrategia(vida_inicial)
        print("\n🦸 Elegiste a WOLVERINE. La máquina usará a DEADPOOL.")

    logger = CombateLogger()
    combate = Combate(jugador, enemigo, logger)

    combate.iniciar()
    combate.mostrar_resultado()


# 🚀 Ejecutar el menú
menu()
