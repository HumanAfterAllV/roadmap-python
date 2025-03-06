from abc import ABC, abstractmethod

class Notificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje):
        pass

class EmailNotificacion(Notificacion):
    def enviar(self, mensaje):
        print(f"📧 Enviando Email: {mensaje}")

class SMSNotificacion(Notificacion):
    def enviar(self, mensaje):
        print(f"📱 Enviando SMS: {mensaje}")

class GestorNotificaciones:
    def __init__(self):
        self.canales = {}  

    def registrar_canal(self, nombre, canal):
        self.canales[nombre] = canal

    def enviar_notificacion(self, tipo, mensaje):
        if tipo not in self.canales:
            print(f"❌ Error: El canal de notificación '{tipo}' no está registrado.")
            return
        for notificacion in self.canales:
            self.canales[tipo].enviar(mensaje)

gestor = GestorNotificaciones()
gestor.registrar_canal("email", EmailNotificacion())
gestor.registrar_canal("sms", SMSNotificacion())

gestor.enviar_notificacion("email", "Hola, tienes un nuevo mensaje!")
gestor.enviar_notificacion("sms", "Tu código de verificación es 123456")

class WhatsAppNotificacion(Notificacion):
    def enviar(self, mensaje):
        print(f"💬 Enviando WhatsApp: {mensaje}")

gestor.registrar_canal("whatsapp", WhatsAppNotificacion())
gestor.enviar_notificacion("whatsapp", "Hola! Te enviamos un mensaje por WhatsApp.")
