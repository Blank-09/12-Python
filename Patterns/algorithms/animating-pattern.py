from time import sleep
from os import system

def createPattern(sym, spacing=' ', terminate=' '):
  for i in range(9):
    for j in range(9):
      if j < (13  - i) and j >= (i - 4) and j >= (4 - i) and j <= (4 + i):
        j = sym
      else: j = spacing
      print(j, end= terminate)
    print()

symbols = ['|', '/', '_', '\\']
times = 10

for i in range(times):
  for symbol in symbols:
    system('cls')
    createPattern(symbol)
    sleep(0.1)
