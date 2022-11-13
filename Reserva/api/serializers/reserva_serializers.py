from Reserva.models import Reserva
from rest_framework import serializers

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
          
    def to_internal_value(self, instance):
        a = super().to_internal_value(instance)
        if str(a['fecha_ingreso']) == '1900-01-01':
            a['fecha_salida'] = None
        return a

    fecha_ingreso = serializers.DateField(format="%d/%m/%Y", input_formats=['%d/%m/%Y', 'iso-8601'])
    fecha_salida = serializers.DateField(format="%d/%m/%Y", input_formats=['%d/%m/%Y', 'iso-8601',''])