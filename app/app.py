class App:
    def __init__(self, a: str, b: int):
        if not isinstance(a, str):
            raise TypeError("a must be a string")
        if not isinstance(b, int):
            raise TypeError("b must be an integer")
        self.a = a
        self.b = b
