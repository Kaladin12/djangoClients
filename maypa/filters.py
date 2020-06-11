import django_filters
from .models import * 

class clientFilter(django_filters.FilterSet):
	class Meta:
		model = cliente
		fields = ('IDCLIENTE',	'NOMBRE', 'DIRECCION_FISICA', 'COLONIA', 'CIUDAD', 'ESTADO', 'TELEFONO1', 'TELEFONO2', 'EMAIL', 'RECOLECCIONES_MENSUALES',
					'MONTO', 'MONEDA', 'FECHA_REGISTRO', 'GIRO', 'CUOTA_MENSUAL_PESOS', 'CUOTA_MENSUAL_DLLS', 'CUOTA_SEMESTRAL', 'CUOTA_ANUAL')
		