from behave import given, when, then
from transporte.exceptions import EstudianteError, EstudianteAgregadoError
from transporte.models import Estudiante, ColaDeEspera


@given('que comenzé a recoger los carnets')
def step_impl(context):
	context.cola = ColaDeEspera()


# Agregar primer estudiante

@given('que "{nombre} {apellido}" llegó')
def step_impl(context, nombre, apellido):

	context.engel = Estudiante(
			nombre=nombre,
			apellido=apellido
		)


@given('no ha llegado ningún otro estudiante')
def step_impl(context):

	assert context.cola.esta_vacia()


@when('lo agregue a la cola')
def step_impl(context):

	context.cola.add(context.engel)


@then('será el primero')
def step_impl(context):
	primer_estudiante = context.cola.primero()
	
	assert context.engel is primer_estudiante


# Agregar varios estudiantes

@given('que llegaron estos estudiantes')
def step_impl(context):
	context.listado = list()

	for row in context.table:
		context.listado.append(Estudiante(
					nombre=row['nombre'],
					apellido=row['apellido']
				)
			)


@given('sólo estaba "{nombre} {apellido}"')
def step_impl(context, nombre, apellido):
	context.jose = Estudiante(
			nombre=nombre,
			apellido=apellido
		)

	context.cola.add(context.jose)


@when('los agregue en la cola')
def step_impl(context):

	for estudiante in context.listado:
		context.cola.add(estudiante)


@then('el primero será "José Aguirre"')
def step_impl(context):
	
	primer_estudiante = context.cola.primero()

	assert context.jose is primer_estudiante


@then('el último será "Andrés Salazar"')
def step_impl(context):
	
	andres_salazar = context.cola.ultimo()
	ultimo_del_listado = context.listado[-1]

	assert andres_salazar is ultimo_del_listado


# Agregar estudiante más de una vez	

@given('que "{nombre} {apellido}" ya está en la cola')
def step_impl(context, nombre, apellido):
	
	context.alonzo = Estudiante(
				nombre=nombre,
				apellido=apellido
			)
	context.cola.add(context.alonzo)


@when('yo intente agregarlo nuevamente')
def step_impl(context):
	try:
		
		context.cola.add(context.alonzo)
	
	except EstudianteAgregadoError as e:
		
		context.msj = str(e)
		

@then('debe decir "{msj}"')
def step_impl(context, msj):
	
	assert msj == context.msj


# Intentar agregar a ningún estudiante

@when('intente agregar a ningún estudiante')
def step_impl(context):
	try:
		
		context.cola.add()

	except EstudianteError as e:
		context.msj = str(e)


@then('dará un error como "{msj}"')
def step_impl(context, msj):

	assert msj == context.msj