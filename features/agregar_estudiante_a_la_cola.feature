Característica: Agregar estudiante a la cola
  Cómo coordinador de la cola para el transporte
  Quiero agregar a cada estudiante que llegue en la cola de espera
  Para poder tener un orden

  Antecedentes: Cola de espera preparada!
    Dado que comenzé a recoger los carnets


  Escenario: Agregar primer estudiante
    Dado que "Engel Pinto" llegó
    Y no ha llegado ningún otro estudiante
    Cuando lo agregue a la cola
    Entonces será el primero

  
  Escenario: Agregar estudiante más de una vez
    Dado que "Alonzo Gonzalez" ya está en la cola
    Cuando yo intente agregarlo nuevamente
    Entonces debe decir "Ya se encuentra en la cola!"


  Escenario: Intentar agregar a ningún estudiante
    Cuando intente agregar a ningún estudiante
    Entonces dará un error como "Es obligatorio agregar el estudiante!"
  
     
  Escenario: Agregar varios estudiantes
    Dado que llegaron estos estudiantes
    
    |nombre | apellido|
    |Raul   | Zamora  |
    |Carlos | Rangel  |
    |Andrés | Salazar |

    Y sólo estaba "José Aguirre"
    Cuando los agregue en la cola
    Entonces el primero será "José Aguirre"
    Pero el último será "Andrés Salazar"