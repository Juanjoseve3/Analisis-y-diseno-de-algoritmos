# -*- coding: utf-8 -*-
"""Ejercicio_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UdyKP3sweaTXD26jGkJwOCub1N4vk1QV
"""

import random
def crear_matriz(n, matriz = []):  
  for i in range(n): 
    matriz.append([])
    for j in range(n): matriz[i].append(random.randint(0,10))
  return matriz
def mostrar_matriz(matriz):(print(matriz))
def sumatoria(matriz, c = 0):
  for i in range(len(matriz)): a = sum(matriz[i]);c += a
  return c
sumatoria(crear_matriz(3))
