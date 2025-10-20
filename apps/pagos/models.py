from django.db import models

# Create your models here.

class Pago(models.Model):
    #paciente = models.ForeignKey('pacientes.Paciente', on_delete=models.CASCADE)
    fecha = models.DateField()
    #servicio = models.ForeignKey('servicios.Servicio', on_delete=models.CASCADE)
    medio = models.CharField(max_length=50)  
    monto_total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Monto total')
    monto_pendiente = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Monto pendiente')
    estado = models.CharField(max_length=20)

    def __str__(self):
        return f"Pago de {self.paciente} - {self.servicio} ({self.estado})"