#--------------------------------------------
# Algoritmo de Minimização
# Grupo:
# - Beatriz Alves
# - Bianca Mayra
# - Lucelho Silva
# - Renato Noronha
# - Túlio Inácio
#
# Data: 07/10/2025
# Disciplina: Análise e Estrutura de Dados
# Professor: Edyene Oliveira
#--------------------------------------------

import pulp
import pandas as pd

# Criar modelo de minimização
modelo = pulp.LpProblem("Problema_Transporte", pulp.LpMinimize)

# Variáveis de decisão
x1A = pulp.LpVariable("x1A", lowBound=0)
x1B = pulp.LpVariable("x1B", lowBound=0)
x1C = pulp.LpVariable("x1C", lowBound=0)
x2A = pulp.LpVariable("x2A", lowBound=0)
x2B = pulp.LpVariable("x2B", lowBound=0)
x2C = pulp.LpVariable("x2C", lowBound=0)

# Função objetivo: custo total
modelo += 8*x1A + 6*x1B + 10*x1C + 9*x2A + 12*x2B + 13*x2C

# Restrições de oferta
modelo += x1A + x1B + x1C <= 20   # Fábrica 1
modelo += x2A + x2B + x2C <= 30   # Fábrica 2

# Restrições de demanda
modelo += x1A + x2A == 10   # Centro A
modelo += x1B + x2B == 15   # Centro B
modelo += x1C + x2C == 25   # Centro C

# Resolver
modelo.solve()

# Criar tabela com resultados
resultado = pd.DataFrame({
    "Loja A": [pulp.value(x1A), pulp.value(x2A)],
    "Loja B": [pulp.value(x1B), pulp.value(x2B)],
    "Loja C": [pulp.value(x1C), pulp.value(x2C)],
}, index=["Fábrica 1", "Fábrica 2"])

# Adicionar custo mínimo
custo_total = pulp.value(modelo.objective)

print("Status:", pulp.LpStatus[modelo.status])
print("\nTabela de envio (unidades):")
print(resultado)
print("\nCusto mínimo =", custo_total)
