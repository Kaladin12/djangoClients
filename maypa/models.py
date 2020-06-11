from django.db import models

# Create your models here.

class cliente(models.Model):
	IDCLIENTE = models.CharField(max_length=20 )
	NOMBRE = models.CharField(max_length = 200 )
	DIRECCION_FISICA = models.CharField(max_length = 150)
	COLONIA = models.CharField(max_length = 100 )
	CIUDAD = models.CharField(max_length = 50)
	ESTADO = models.CharField(max_length = 50)
	TELEFONO1 = models.CharField(max_length = 100 )
	TELEFONO2 = models.CharField(max_length = 100 )
	EMAIL = models.CharField(max_length = 100 )
	RECOLECCIONES_MENSUALES = models.CharField(max_length = 100 )
	MONTO = models.CharField(max_length = 100 )


	MONEDA = models.CharField(max_length = 10 )
	FECHA_REGISTRO = models.CharField(max_length = 20 )
	GIRO = models.CharField(max_length = 150 )
	CUOTA_MENSUAL_PESOS = models.CharField(max_length = 100 )
	CUOTA_MENSUAL_DLLS = models.CharField(max_length = 100 )
	CUOTA_SEMESTRAL = models.CharField(max_length = 100 )
	CUOTA_ANUAL = models.CharField(max_length = 100 )

	def __str__(self):
		return "ID: {0}, NOMBRE: {1}".format(self.IDCLIENTE, self.NOMBRE)




