class FakeHashlib:
    def __init__(self) -> None:
        self.value = None

    def new(self, *args):
        self.value = args[1]
        return self

    def hexdigest(self):
        return self.value

    def update(self, value):
        self.value = value

    def sha512(self, *args):
        return self
