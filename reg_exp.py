#EJEMPLO DE COMO USAR LA EXPRESIONES REGULARES EN PYTHON

import re #esto debe ser en minúsculas

line = "Beautiful is better tha ugly"
matches = re.findall("Beautiful", line)
#^ el findall acepta una expresión regular e imprime lo que concuerda
#si queremos ignorar las mayúsculas usamos:
#matches = re.findall("Beautiful", line, re.IGNORECASE)
print(matches)


##otra forma de usar las expresiones 

zen = """Although never is often better than *right* now.
If the implementation is hard to explain,
it's a bad idea.
If the implementation is easy to explain,
it may be a good idea.Namespaces are
one honking great idea -- let's do more of those!"""
#para todo el texto hay que poner 3 sets de comillas """ """

m= re.findall("^If", zen, re.MULTILINE)
print(m)

#en un string multilinea, podemos hacer match con varias palabras
#si las ponemos entre brackets [], como [abc]


#### OTRO EJEMPLO CON []
string = "Two too"
n = re.findall("t[ow]o", string, re.IGNORECASE)
#andaba olvidando la ultima o, el output salía diferente

print(n)


##### EJEMPLO PARA LOS DIGITOS
digi = "123?34 hello?"
p = re.findall("\d", digi, re.IGNORECASE)
print(p)


## EJEMPLO DE ASTERISCO EN PYTHON
t = "__one__ __two__ __three__"
results = re.findall("__.*?__", t)
for match in results:
    print(match)

#gracias a que pusimos el *? Python no regresó un solo string
#sino que nos dio todos los que concordaban

#En otra pestaña hay otro ejemplo de este simbolo
