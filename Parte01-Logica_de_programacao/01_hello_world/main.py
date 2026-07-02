# Este é um comentário de linha simples.

'''
Este é um comentário de linha simples.
Início do curso de Python no SENAI
'''
curso = "PYTHON"
data_nascimento = "22/06/2026"
idade_minima = 18
valor_unitario = 10
numero_flutuante = 10,5
valor_buleano = True

print ("Alô, mundo!")

"""
Este é um comentário de linha simples.
Comentários com linhas multiplas
"""

#TODO - Fazer este trexo de código

#FIXME - Corrija este trecho de código

#REVIEW - Reviar este trecho de cógido
print ("texto1")     
print ("texto1")
print (curso)

"""
Tipando variáveis
"""

nome_usuario: str = "Maria teste"
idade: int = 20
salario_base: float = 1.5
comissao: float = 2.5
print (idade, nome_usuario, salario_base)

print(type(nome_usuario))
print(type(idade))
print(type(salario_base))
print(type(valor_buleano))

print(idade + idade)
comissao1: float = 2.5
int(comissao1)
print("Olá, {}, meu nome é {}, e tenho {}.".format(nome_usuario, nome_usuario, idade))
