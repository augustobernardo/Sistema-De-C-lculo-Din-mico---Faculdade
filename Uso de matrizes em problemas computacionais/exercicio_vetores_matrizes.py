# -*- coding: utf-8 -*-
"""exercicio_vetores_matrizes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T_oRWVnpD0vG_5DJ90ogqjImam-iOcrz
"""

pergunta = int(input("Digite quantas notas serão inseridas\n>> "))
soma = 0
vetor = []

for i in range(pergunta):
  nota = float(input('Digite a nota do aluno: '))
  vetor.append(nota)
  soma = soma + vetor[i]

media = soma / pergunta
print(f'A média das notas desse alunos foi de {media:.2f}')