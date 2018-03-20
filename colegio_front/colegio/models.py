from django.db import models

# Create your models here.

""" 
	Modelo Profesor
"""
class Profesor(models.Model):
	identificacion = models.CharField(max_length=200)
	nombres = models.CharField(max_length=200)
	apellidos = models.CharField(max_length=200)
	"""
		docstring for Profesor
	"""
	def __str__(self):
		return self.nombres + ' ' + self.apellidos

""" 
	Modelo Alumno
"""
class Alumno(models.Model):
	identificacion = models.CharField(max_length=200)
	nombres = models.CharField(max_length=200)
	apellidos = models.CharField(max_length=200)
	"""
		docstring for Alumno
	"""
	def __str__(self):
		return self.nombres + ' ' + self.apellidos



""" 
	Modelo Materia
"""
class Materia(models.Model):
	# id_profesor guarda al llave foránea del modelo Profesor
	id_profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=200)
	"""
	docstring for Alumno
	"""
	def __str__(self):
		return self.nombre


""" 
	Modelo Nota
"""
class Nota(models.Model):
	# id_materia guarda al llave foránea del modelo Materia
	id_materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
	# id_alumno guarda al llave foránea del modelo Alumno
	id_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
	valor_nota = models.IntegerField(default=0)
	"""
	docstring for Alumno
	"""
	def __str__(self):
		return self.id_alumno.nombres + ' - ' + self.id_materia.nombre


