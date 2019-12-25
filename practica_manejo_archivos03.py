import pickle
class persona:
    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se ha crfeado una persona nueva con el nombre de ", self.nombre)
    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class listapersonas:
    personas=[]
    def __init__(self):
        fichero_persona=open("Archivo_binario_personas", "ab+") #--> ab+=agregar informacion binaria
        fichero_persona.seek(0)
        try:
            self.personas=pickle.load(listapersonas)
            print("Se cargaron {} personas del fichero externo".format(len(listapersonas)))
        except:
            print("El fichero esta vacio")
        finally:
            fichero_persona.close()
            del (fichero_persona)

    def agregarpersona(self, p):
        self.personas.append(p)
        self.guardar_personas_en_fichero_externo()
    def mostrarpersonas(self):
        for i in self.personas:
            print(i)
    def guardar_personas_en_fichero_externo(self):
        fichero_persona = open("Archivo_binario_personas", "wb")  # -->
        pickle.dump(self.personas, fichero_persona)
        fichero_persona.close()
        del (fichero_persona)
    def mostar_informacion_fichero_externo(self):
        print("La informacion del fichero externo es: ")
        for p in self.personas:
            print(p)

listap=listapersonas()
persona01=persona("Ana", "Femenino", 21)
listap.agregarpersona(persona01)
listap.mostar_informacion_fichero_externo()
'''
p=
listap.agregarpersona(p)
p=persona("Antonio", "Masculino", 27)
listap.agregarpersona(p)
p=persona("Anthony", "Masculino", 26)
listap.agregarpersona(p)
listap.mostrarpersonas()
'''