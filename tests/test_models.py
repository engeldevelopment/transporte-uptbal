import unittest
from exceptions import ColaVaciaError, EstudianteAgregadoError
from exceptions import EstudianteError
from models import ColaDeEspera, Estudiante


class ColaTest(unittest.TestCase):

	def setUp(self):
		self.cola =  ColaDeEspera()
		self.engel = Estudiante(nombre="Engel", apellido="Pinto") 
	
	def test_la_cola_empienza_vacia(self):

		self.assertTrue(self.cola.esta_vacia())

	def test_el_primer_estudiante_en_la_cola_sera_el_primero_en_pasar(self):

		self.cola.add(self.engel)

		self.estudiante_a_pasar = self.cola.pasar()

		self.assertEqual("Engel", self.estudiante_a_pasar.nombre)

	def test_si_intento_agregar_a_ningun_estudiante_da_error(self):

		with self.assertRaises(EstudianteError):
			self.cola.add()

	def test_da_error_pasar_un_estudiante_cuando_esta_vacia_la_cola(self):

		self.assertRaises(ColaVaciaError, self.cola.pasar)

	def test_da_error_consultar_el_primer_estudiante_con_la_cola_vacia(self):

		self.assertRaises(ColaVaciaError, self.cola.primero)

	def test_da_error_intentar_agregar_un_estudiante_mas_de_una_vez(self):
		
		self.cola.add(self.engel)

		self.assertRaises(EstudianteAgregadoError, self.cola.add, self.engel)