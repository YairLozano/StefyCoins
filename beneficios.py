class beneficios():
    def __init__(self, nombre, costo):
        self.nombre=nombre
        self.costo=costo
    

class cambiarFecha(beneficios):
    def __init__(self, nombre="cambiar fecha de entrega" , costo=50,):
        super().__init__(nombre,costo)
        self.descripcion="permite extender la fecha de entrega de una tarea"

    

class puntosExtra(beneficios):
    def __init__(self, nombre="puntos extra", costo=30):
        super().__init__(nombre, costo)
        self.descripcion="suma puntos adicionales en una evaluacion"

class tutorias(beneficios):
    def __init__(self, nombre="personalizar tutoria", costo=40):
        super().__init__(nombre, costo)
        self.descripcion="faltar a tutoria"
