#Regular expression to match digits on a string

import re

digi = "Arizona 479, 501, 870. California 209, 213, 650"
m = re.findall("\d",digi, re.IGNORECASE) #la "\d" es importante

print(m)


########################
###Create a regular expression that matches any word
##that starts with any character and is followed by two o's.
##Then use Python's re module to match boo and loo in the
##sentence "The ghost that says boo haunts the loo". Save
##the result in a variable and print it.

line = "The ghost that says boo haunts the loo"
n = re.findall("\w[o]o", line)
#la secuencia \w permite ir separando letra por letra
#en este caso, agregué [o]o para que coincida con las 2 o
print(n)
