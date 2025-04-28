from persona import Persona
from alieno import Alieno

p: Persona = Persona("Damien","Rebong", 19)
print(p)

et: Alieno = Alieno("Milky Way")
print("\n",et,"\n")

p.speak()
et.speak()