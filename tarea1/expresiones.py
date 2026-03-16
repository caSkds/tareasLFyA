#importamos la biblioteca para el uso de expresiones regulares
import re

#cada elemento de la variable ejercicios deberá ser la solución al ejercicio correspondiente
#es decir ejercicios["e03"]  es la solución al ejercicio [e03]
ejercicios = {
    "e08": re.compile('[aeiou][a-z]|[aeiou][a-z]*[aeiou][a-z]')
}
#cada elemento de la variable pruebas_match deberá ser un arreglo con las cadenas con las que DEBE hacer match la solución
#Por ejemplo pruebas_match["e03"] = ["cadena1","cadena2"...] significa que cadena1, cadena2, etc. deben hacer match con la ER del ejercicio e03
pruebas_match = {
    "e08": ["ab", "ii", "aab","alugbhwrfuz", "uaf"]
}
#cada elemento de la variable pruebas_nmatch deberá ser un arreglo con las cadenas con las que NO DEBE hacer match la solución
#Por ejemplo pruebas_nmatch["e03"] = ["cadena1","cadena2"...] significa que cadena1, cadena2, etc. no deben hacer match
pruebas_nmatch = {
    "e08": ["abc", "xyz", "aba", "ba", "a"]
}

#Ejemplo:
#ejercicios["CODIGO_DE_EJERCICIO"] = re.compile('ER_DE_LA_SOLUCION')
ejercicios["CODIGO_DE_EJERCICIO"] = re.compile('#[A-Z][A-Za-z0-9]+')
pruebas_match ["CODIGO_DE_EJERCICIO"] = ["#HolaMundo","#UNAMONOS","#Covid19","#SomosIngenieria","#UNAM2023"]
pruebas_nmatch ["CODIGO_DE_EJERCICIO"] = ["#HolaMundo","#UNAM ONOS","#Covid 19","##SomosIngenieria","#UNAM?","#Somos#Ingenieria"]

#NOTA: el CODIGO_DE_EJERCICIO es la cadena que se encuentra entre [ ] en el enunciado del ejercicio.
#Por ejemplo: [e03] Σ = {a, b,..., z}. Cadenas que no contienen tres consonantes consecutivas.

#e02
ejercicios["e02"] = re.compile(r'^([a-z0-9][^aeiou])([a-z0-9][^aeiou])*(?:[a-z0-9])?$')

pruebas_match["e02"] = [
"a1b2",
"b3c4",
"z9",
"m2n4",
"x5y"
]

pruebas_nmatch["e02"] = [
"ba",
"a2e",
"c4i",
"d8o",
"g2u"
]


#e12
ejercicios["e12"] = re.compile(r'^([a-z]+|[0-9]+)$')

pruebas_match["e12"] = [
"abc",
"xyz",
"hola",
"123",
"98765"
]

pruebas_nmatch["e12"] = [
"a1",
"b2c",
"hola3",
"4test",
"x9y"
]


#e24
ejercicios["e24"] = re.compile(r'^([a-z0-9]*[02468]){1,2}[a-z0-9]*$')

pruebas_match["e24"] = [
"a2",
"b4c",
"z8x6",
"hola2",
"test4a"
]

pruebas_nmatch["e24"] = [
"abc",
"135",
"7test",
"xyz",
"bdfg"
]

