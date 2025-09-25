# Funcionalidades
# Adicionar hábitos, listar hábitos, marcar hábitos concluídos do dia, ver progresso nos hábitos
# Salvar em arquivo JSON

import json # Para salvar e carregar dados
from datetime import date # Para registrar a data de conclusão
import os # Para verificar se o arquivo existe


# -- FUNÇÕES AUXILIARES -- #
def adicionar_habito(habitos, nome):
    if nome not in habitos:
        habitos[nome] = []
        print(f"Hábito '{nome}' adicionado!")
    else:
        print("Esse hábito já existe!")

def listar_habitos(habitos):
    if not habitos:
        print("Nenhum hábito cadastrado!")
        return
    for nome, dias in habitos.items():
        print(f"- {nome} | Dias concluídos: {len(dias)}")

def marcar_habitos(habitos, nome):
    hoje = str(date.today())
    if nome in habitos:
        if hoje not in habitos[nome]:
            habitos[nome].append(hoje)
            print(f"Hábito '{nome}' marcado como concluído para hoje!")
        else:
            print(f"Hábito '{nome}' já foi marcado como concluído hoje!")
    else:
        print("Hábito não encontrado!")

def ver_progresso(habitos, nome):
    if nome in habitos:
        dias_concluidos = habitos[nome]
        print(f"Progresso do hábito '{nome}': {len(dias_concluidos)} dias concluídos.")
    else:
        print("Hábito não encontrado!")


# -- PROGRAMA PRINCIPAL -- #
habitos = {}  # Inicializa o dicionário de hábitos
while True:
    print("------------------------------------------------")
    print("Bem-vindo ao Rastreador de Hábitos!")
    print("1. Adicionar hábito")
    print("2. Listar hábitos") 
    print("3. Marcar hábito como concluído")
    print("4. Ver progresso")
    print("5. Limpar tela")
    print("6. Sair")

    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        nome = str(input("Digite o nome do hábito que deseja adicionar: "))
        adicionar_habito(habitos, nome)
        print("")
    elif escolha == 2:
        listar_habitos(habitos)
    elif escolha == 3:
        nome = input("Digite o nome do hábito que deseja marcar como concluido: ")
        marcar_habitos(habitos, nome)
    elif escolha == 4:
        nome = input("Digite o nome do hábito que deseja ver o progresso: ")
        ver_progresso(habitos, nome)
    elif escolha == 5:
        os.system('cls')
    elif escolha == 6:
        print("Progresso salvo. Até mais!")
        break
    else:
        print("Opção inválida, tente novamente!")
    
