# -*- coding: utf-8 -*-
"""Untitled20.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17OE3Q8myqOh_gyfyLneLskqRd_5fVzCg
"""

def combinaciones(valor, listica):
  temp = []
  def retroceso(residuo, posibilidad, inicio):
    if residuo == 0:
      temp.append(list(posibilidad))
      return
    elif residuo < 0:
      return
    for i in range(inicio, len(listica)):
      posibilidad.append(listica[i])
      retroceso(residuo - listica[i], posibilidad, i)
      posibilidad.pop()
  retroceso(valor, [], 0)
  return temp

listica = [1,2,3]
valor = 3
lista_combinaciones = combinaciones(valor, listica)
for i in  lista_combinaciones:
  print(i)