# UNA VEZ AQUÍ. ASEGURATE DE QUE TODOS LOS PRINTS ANTERIORES ESTAN COMENTADOS... ¡COMENZAMOS!
# EJERCICIO EXTRA --VENCER AL RIVAL--
# Tenemos dos diccionarios. Uno nuestro personaje y otro el monstruo.

personaje = {'nombre' : 'AshKetchup', 'fuerza' : 20, 'Pokemon' : ['Pikachu', 'Bulbasaur', 'Charmander', 'Squirtle']}

rival = {'nombre' : 'Brook', 'vida' : 60, 'Pokemon' : ['Geodude', 'Vulpix', 'Onix', 'Zubat']}


# En este momento. El Rival saca su primer pokemon
# Crea una variable que contenga el Pokemon y printeala

Pokemon1 = rival.get('Pokemon')[0]

print(Pokemon1)

# Al detectar que su primer pokemon. La Ash se pone manos a la obra.
# De esta manera al saber la tabla de tipos y tener tipos ventajosos, obtienen +50 de fuerza.  (Haz que el valor de fuerza de tú personaje suba 50)

personaje["fuerza"] +=50

# Printea la fuerza de tu personaje para comprobar que ha subido

print(personaje["fuerza"])

# En este momento tú personaje realiza su elección de pokemon
# Crea una variable que contenga el pokemon Bulbasaur o Squirtle y printeala
Pokemon2 = personaje.get('Pokemon')[3]

print(Pokemon2)

# Crea una variable que compare si la fuerza de tu personaje es MAYOR que la vida del rival

combate = personaje["fuerza"] > rival["vida"]

# Printea la variable. En caso de ser True habremos obtenido la VICTORIA!!
print(combate)
