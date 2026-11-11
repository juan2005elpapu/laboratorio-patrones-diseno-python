"""2.3. Facade: Una fachada simple sobre un subsistema complejo."""


class Projector:
    def on(self):  print("Proyector encendido")
    def off(self): print("Proyector apagado")


class SoundSystem:
    def set_volume(self, level): print(f"Volumen en {level}")
    def off(self): print("Sonido apagado")

class StreamingPlayer:
    def play(self, movie): print(f"Reproduciendo '{movie}'")
    def stop(self): print("Reproducción detenida")

class HomeTheaterFacade:
    def __init__(self, projector, sound, player):
        self.projector = projector
        self.sound = sound
        self.player = player

    def ver_pelicula(self, movie):
        self.projector.on()
        self.sound.set_volume(7)
        self.player.play(movie)

    def terminar(self):
        self.player.stop()
        self.sound.off()
        self.projector.off()


def main():
    theater = HomeTheaterFacade(Projector(), SoundSystem(), StreamingPlayer())
    theater.ver_pelicula("Interstellar")
    theater.terminar()


if __name__ == "__main__":
    main()
