from django.db import models

class Usuario(models.Model):
    usuario = models.CharField(max_length=20, primary_key=True)
    contraseña = models.CharField(max_length=20,primary_key=True)
    correo = models.CharField(max_length=100,primary_key=True)
    edad = models.CharField(max_length=3,primary_key=True)
    apodo = models.Charfield(max_length=20, primary_key=True)

    def infouser(self):
        txt = "{0},{1},{2},{3},{4}"
        return txt.format(self.usuario, self.contraseña, self.correo, self.correo, self.apodo )

