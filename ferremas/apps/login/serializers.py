from rest_framework import serializers
from apps.usuario.models import Usuario

class LoginSerializer(serializers.Serializer):
    correo = serializers.EmailField()
    contrasena = serializers.CharField(write_only=True)

    def validate(self, data):
        correo = data.get('correo')
        contrasena = data.get('contrasena')

        if not correo or not contrasena:
            raise serializers.ValidationError("Correo y contraseña son requeridos.")

        try:
            user = Usuario.objects.get(correo=correo)
        except Usuario.DoesNotExist:
            raise serializers.ValidationError("Usuario no encontrado.")

        if user.contrasena != contrasena:
            raise serializers.ValidationError("Contraseña incorrecta.")

        data['user'] = user
        return data
