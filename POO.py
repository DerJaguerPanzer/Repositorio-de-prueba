class Coche():
    largochasis = 250
    anchocasis = 120
    ruedas = 4
    enmarcha = False
    
    def arrancar(self, arrancamos): #Metodo
        self.enmarcha = arrancamos
        if (self.enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"
    
    def estado_general(self):
        print("El coche tiene ", self.ruedas, " ruedas. Un ancho de ", self.anchocasis, " y un largo de ", self.largochasis)

#Objeto 1        
micoche=Coche()
print(micoche.arrancar(True))
micoche.estado_general()

#Objeto 2
micoche2= Coche()
print(micoche2.arrancar(False))
micoche2.estado_general()