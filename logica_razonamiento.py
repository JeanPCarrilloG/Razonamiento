class Razonamiento:
    
    def __init__(self):
        self.entrada = ()
        self.base = []
        self.consulta = ""
    
    def perceptron(self):
        
        fechas_iguales = identificar_fecha(self.entrada[0])==identificar_fecha(self.entrada[1])
        fecha_texto_mayor = int(identificar_fecha(self.entrada[0]))>int(identificar_fecha(self.entrada[1]))
        #print("Texto fecha",identificar_fecha(self.entrada[0]))
        #print("Pregunta fecha",identificar_fecha(self.entrada[1]))
        
        partes_del_dia_iguales = identificar_parte_del_dia(self.entrada[0])[1]==identificar_parte_del_dia(self.entrada[1])[1]
        parte_del_dia_texto_mayor = identificar_parte_del_dia(self.entrada[0])[1]>identificar_parte_del_dia(self.entrada[1])[1]
        #print("Texto parte del dia",identificar_parte_del_dia(self.entrada[0]))
        #print("Pregunta parte del dia",identificar_parte_del_dia(self.entrada[1]))
        
        #print("[fechas_iguales,fecha_texto_mayor,partes_del_dia_iguales,parte_del_dia_texto_mayor]")
        return(fechas_iguales,fecha_texto_mayor,partes_del_dia_iguales,parte_del_dia_texto_mayor)
    
    def respuesta_perceptron(self):
        premisa = ""
        premisas = ["fechas_iguales","fecha_texto_mayor","partes_del_dia_iguales","parte_del_dia_texto_mayor"]
        respuestas = self.perceptron()
        contador = 0
        conjuncion = ""
        for validacion in respuestas:
            if contador != 0:
                conjuncion = "^"
            if respuestas[contador] == True:
                premisa = premisa+conjuncion+premisas[contador]
            elif respuestas[contador] == False:
                premisa = premisa+conjuncion+"¬"+premisas[contador]
            contador = contador + 1
        return(premisa)
    
    def regla(self):
        base = self.base
        clausula = {}
        for formula in base:
            cabeza = (formula[formula.find("->")+2:len(formula)])
            cuerpo = (formula[0:formula.find("->")])
            clausula[cuerpo]= cabeza
        return(clausula)
        
    def consultar(self):
        respuesta = self.regla().get(self.consulta)
        return(respuesta)
    
    def respuesta(self):
        orden = ["origen_de_vuelo","destino_de_vuelo"]
        ciudades = identificar_lugar(str(self.entrada))
        ruta_de_viaje = dict(zip(orden, ciudades))
        return ( "Estaba en " + ruta_de_viaje.get(self.consultar()))
         
def identificar_fecha(texto):
    fecha_numero = ""
    for caracter in texto:
        try:
            if type(int(caracter)) == int:
                fecha_numero = fecha_numero+caracter
        except:
            pass
    return(fecha_numero)

def identificar_parte_del_dia(texto):
    partes_del_dia = {"mañana":1,"mediodía":2,"tarde":3,"noche":4}
    for parte_del_dia in partes_del_dia.keys():
        if (parte_del_dia in texto) == True:
            numero = partes_del_dia.get(parte_del_dia)
            return(parte_del_dia,numero)
        
def identificar_lugar(texto):
    ruta_viaje = []
    lugares_visitados = []
    texto = texto.lower()
    lugares = ["bogotá","medellı́n","cali","barranquilla","cartagena","cucuta","bucaramanga","santa marta","villavicencio","ibagué"]
    for lugar in lugares:
        if (lugar in texto) == True:
            lugares_visitados.append(lugar)
    try:
        if (texto[(texto.find(lugares_visitados[0]))-2]) == "a":
            #print("Viajo de ",lugares_visitados[1]," a ",lugares_visitados[0])
            ruta_viaje = [lugares_visitados[1],lugares_visitados[0]]
        else:
            #print("Viajo de ",lugares_visitados[0]," a ",lugares_visitados[1])
            ruta_viaje = [lugares_visitados[0],lugares_visitados[1]]
    except:
        pass
    return(ruta_viaje)