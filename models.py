from collections import deque
from exceptions import ColaVaciaError, EstudianteAgregadoError
from exceptions import EstudianteError


class ColaDeEspera:

	def __init__(self):
		self.lista = deque()

	def add(self, estudiante=None):
		if estudiante is None:
			raise EstudianteError("Es obligatorio agregar el estudiante!")
		
		if self.esta_agregado(estudiante):
			raise EstudianteAgregadoError("Ya se encuentra en la cola!")
		
		self.lista.append(estudiante)

	def esta_agregado(self, estudiante):
		return estudiante in self.lista

	def pasar(self):
		self._lanzar_error_si_no_hay_gente_esperando()

		return self.lista.popleft()		

	def primero(self):
		self._lanzar_error_si_no_hay_gente_esperando()

		return self.lista[0]

	def ultimo(self):
		self._lanzar_error_si_no_hay_gente_esperando()

		return self.lista[-1]

	def _lanzar_error_si_no_hay_gente_esperando(self):
		
		if self.esta_vacia():
			raise ColaVaciaError("No hay nadie esperando en la cola!")	

	def esta_vacia(self):
		return len(self.lista) == 0


class Estudiante:

	def __init__(self, **kwargs):
		self.nombre = kwargs['nombre']
		self.apellido = kwargs['apellido']