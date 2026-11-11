"""2.2. Decorator: Añadir funcionalidades dinámicamente."""


class Notifier:
    def send(self, message: str) -> None:
        raise NotImplementedError

class EmailNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"[Email] {message}")

class NotifierDecorator(Notifier):
    def __init__(self, wrapped: Notifier):
        self._wrapped = wrapped

    def send(self, message: str) -> None:
        self._wrapped.send(message)

class SMSDecorator(NotifierDecorator):
    def send(self, message: str) -> None:
        super().send(message)
        print(f"[SMS] {message}")

class SlackDecorator(NotifierDecorator):
    def send(self, message: str) -> None:
        super().send(message)
        print(f"[Slack] {message}")


def main():
    notifier = SlackDecorator(SMSDecorator(EmailNotifier()))
    notifier.send("Servidor caído")


if __name__ == "__main__":
    main()
