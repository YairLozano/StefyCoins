from beneficios import tutorias, puntosExtra, cambiarFecha
from usuario import profesor, estudiante
from tareas import trabajoPractico
from mailAutomation import EmailSender

estudiante1 = estudiante(nombre="hector",
                          apellido="vicente",
                            edad=22, 
                            legajo=1234, 
                            curso="4to A", 
                            correo="yaircinlozanito@gmail.com", 
                            password="ujmp kzkh dlmt gprw", 
                            id=1)

profesor1 = profesor(nombre="Juan", 
                     apellido="Perez", 
                     edad=40, 
                     especialidad="Matematica", 
                     correo="yaircinlozanito@gmail.com", 
                     password="ujmp kzkh dlmt gprw", 
                     id=1)

tarea1= trabajoPractico(consigna="esto es una consigna de Tarea1", 
                        fechaEntrega="12/10/2025", 
                        criterioEvaluacion="Hacer el trabajo Práctico")


profesor1.asignarTarea(estudiante1,tarea1)

print("visualizacion de tareas")
estudiante1.checkearTarea()

print("estudiante entrega tarea")
estudiante1.entregarTarea(tarea1)


estudiante1.checkearTarea()

print("aprobacion de tarea")
profesor1.aprobarTarea(estudiante1, tarea1)

estudiante1.checkearTarea()

usuario = "yaircinlozanito@gmail.com"
contraseña = "ujmp kzkh dlmt gprw" 

correo = EmailSender(usuario, contraseña)
correo.enviar_mail(
    destinatario="yairruiz7879@gmail.com",
    asunto="Prueba desde Python en ProA La Falda",
    mensaje="Hola! Este es el estado en el que se encuentran tus materias")
