
class Productor:

    def __init__(self, nombre: str, apellidos: str, dni_nif: str, direccion: str, tlfn: str, email: str):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni_nif = dni_nif
        self.direccion = direccion
        self.tlfn = tlfn
        self.email = email

    def __str__(self):
        return f"{self.nombre} {self.apellidos} | {self.dni_nif}"