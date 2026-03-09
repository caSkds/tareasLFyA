#importamos la biblioteca para el uso de expresiones regulares
import re

#cada elemento de la variable ejercicios deberá ser la solución al ejercicio correspondiente
#es decir ejercicios["e03"]  es la solución al ejercicio [e03]
ejercicios = {}
#cada elemento de la variable pruebas_match deberá ser un arreglo con las cadenas con las que DEBE hacer match la solución
#Por ejemplo pruebas_match["e03"] = ["cadena1","cadena2"...] significa que cadena1, cadena2, etc. deben hacer match con la ER del ejercicio e03
pruebas_match = {}
#cada elemento de la variable pruebas_nmatch deberá ser un arreglo con las cadenas con las que NO DEBE hacer match la solución
#Por ejemplo pruebas_nmatch["e03"] = ["cadena1","cadena2"...] significa que cadena1, cadena2, etc. no deben hacer match
pruebas_nmatch = {}

#Ejemplo:
#ejercicios["CODIGO_DE_EJERCICIO"] = re.compile('ER_DE_LA_SOLUCION')
ejercicios["CODIGO_DE_EJERCICIO"] = re.compile('#[A-Z][A-Za-z0-9]+')
pruebas_match ["CODIGO_DE_EJERCICIO"] = ["#HolaMundo","#UNAMONOS","#Covid19","#SomosIngenieria","#UNAM2023"]
pruebas_nmatch ["CODIGO_DE_EJERCICIO"] = ["#HolaMundo","#UNAM ONOS","#Covid 19","##SomosIngenieria","#UNAM?","#Somos#Ingenieria"]

#NOTA: el CODIGO_DE_EJERCICIO es la cadena que se encuentra entre [ ] en el enunciado del ejercicio.
#Por ejemplo: [e03] Σ = {a, b,..., z}. Cadenas que no contienen tres consonantes consecutivas.
