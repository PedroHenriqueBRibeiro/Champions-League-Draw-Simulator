



##           +--------------------------------------------------+
##           |         pip install -r requirements.txt          | 
##           +--------------------------------------------------+

import json
import time
import json
import os
import random
import numpy as np
import sys
import threading
import questionary
from questionary import Style

def reiniciar_aplicacao():
    print("\n\nA aplicação será reiniciada em 5 segundos...\n")
    for i in range(5, 0, -1):
        print(f"{i} segundo(s) restantes...", end='\r')
        time.sleep(1)  
    print("\nReiniciando a aplicação...")
    os.execv(sys.executable, ['python'] + sys.argv)


def resetar_aplicacao():
    arquivos_para_excluir = [
        "dados_times.json",
        "campeoes.json",
        "historico_gols.json",
        "historico_resultados.json",
        "configuracao_gols.json",
        "stats_personalizados.json"
    ]

    arquivos_excluidos = []
    arquivos_nao_encontrados = []

    confirmar = questionary.select(
        "\nDeseja Resetar todos os dados?\n\n",
        choices=["Sim", "Não", "Voltar"], style=custom_style
    ).ask()
    if confirmar == "Sim":
        confirma2 = questionary.text("\n\nEsta ação não poderá ser desfeita. Digite 'RESETAR' para dar continuidade.\n\n").ask()
        if confirma2 == 'RESETAR':

            for arquivo in arquivos_para_excluir:
                if os.path.exists(arquivo):
                    try:
                        os.remove(arquivo)
                        arquivos_excluidos.append(arquivo)
                    except Exception as e:
                        print(f"Erro ao excluir {arquivo}: {e}")
                else:
                    arquivos_nao_encontrados.append(arquivo)

            print("\n\nReset da aplicação concluído.\n\n")


            if arquivos_excluidos:
                print("\nArquivos excluídos:")
                for arquivo in arquivos_excluidos:
                    print(f"- {arquivo}")
            else:
                print("Nenhum arquivo excluído.")

            if arquivos_nao_encontrados:
                print("\nArquivos não encontrados:")
                for arquivo in arquivos_nao_encontrados:
                    print(f"- {arquivo}")
            reiniciar_aplicacao()

        else:
            print("\n\nOperação cancelada.\n\n")
    elif confirmar == 'Não':
        print("\n\nOperação cancelada.\n\n")
        return
    elif confirmar == 'Voltar':
        print("\n\nOperação cancelada.\n\n")
        return



def criar_json_predefinido():
    potes = [
        ["Barcelona", "Real Madrid", "Manchester City", "Bayern Munich", "PSG", "Juventus", "Aston Villa", "Liverpool", "Atletico Madrid"],
        ["Borussia Dortmund", "Internazionale", "Milan", "Girona", "Arsenal", "Bologna", "Leipzig", "Stuttgart", "Feyenoord"],
        ["Benfica", "Sporting", "Shakhtar", "PSV", "Estrela Vermelha", "Atalanta", "Lille", "Monaco", "Leverkusen"],
        ["Stade Brestois", "Sparta Praga", "Dinamo Zagreb", "RB Salzburg", "Celtic", "Young Boys", "Club Brugge", "Sturm", "Slovan Bratislava"]
    ]

    stats = {
        "Barcelona": {"ataque": 84, "defesa": 79, "meio_campo": 81},
        "Real Madrid": {"ataque": 88, "defesa": 84, "meio_campo": 85},
        "Manchester City": {"ataque":85, "defesa": 83, "meio_campo": 86},
        "Bayern Munich": {"ataque": 90, "defesa": 82, "meio_campo": 84},
        "PSG": {"ataque": 82, "defesa": 82, "meio_campo": 81},
        "Juventus": {"ataque": 84, "defesa": 79, "meio_campo": 79},
        "Aston Villa": {"ataque": 85, "defesa": 80, "meio_campo": 80},
        "Liverpool": {"ataque": 84, "defesa": 84, "meio_campo": 82},
        "Atletico Madrid": {"ataque": 84, "defesa": 81, "meio_campo": 82},
        "Borussia Dortmund": {"ataque": 84, "defesa": 80, "meio_campo": 81},
        "Internazionale": {"ataque": 86, "defesa": 83, "meio_campo": 83},
        "Milan": {"ataque": 80, "defesa": 80, "meio_campo": 82},
        "Girona": {"ataque": 76, "defesa": 79, "meio_campo": 79},
        "Arsenal": {"ataque": 83, "defesa": 83, "meio_campo": 84},
        "Bologna": {"ataque": 76, "defesa": 76, "meio_campo": 77},
        "Leipzig": {"ataque": 81, "defesa": 80, "meio_campo": 80},
        "Stuttgart": {"ataque": 75, "defesa": 75, "meio_campo": 77},
        "Feyenoord": {"ataque": 73, "defesa": 75, "meio_campo": 74},
        "Benfica": {"ataque": 79, "defesa": 78, "meio_campo": 78 },
        "Shakhtar": {"ataque": 73, "defesa": 73, "meio_campo": 74},
        "PSV": {"ataque": 78, "defesa": 74, "meio_campo": 78},
        "Sporting": {"ataque": 81, "defesa": 77, "meio_campo": 79},
        "Atalanta": {"ataque": 79, "defesa": 78, "meio_campo": 78},
        "Lille": {"ataque": 81, "defesa": 75, "meio_campo": 76},
        "Monaco": {"ataque": 74, "defesa": 77, "meio_campo": 77},
        "Leverkusen": {"ataque": 82, "defesa": 83, "meio_campo": 83},
        "Stade Brestois": {"ataque": 75, "defesa": 73, "meio_campo": 76},
        "Sparta Praga": {"ataque": 75, "defesa": 75, "meio_campo": 74},
        "Dinamo Zagreb": {"ataque": 77, "defesa": 71, "meio_campo": 71},
        "RB Salzburg": {"ataque": 70, "defesa": 71, "meio_campo": 73},
        "Celtic": {"ataque": 74, "defesa": 75, "meio_campo": 75},
        "Young Boys": {"ataque": 70, "defesa": 69, "meio_campo": 71},
        "Club Brugge": {"ataque": 71, "defesa": 65, "meio_campo": 68},
        "Estrela Vermelha": {"ataque": 68, "defesa": 66, "meio_campo": 64},
        "Sturm": {"ataque": 69, "defesa": 70, "meio_campo": 71},
        "Slovan Bratislava": {"ataque": 67, "defesa": 65, "meio_campo": 64}
    }


    dados = {
        "potes": potes,
        "stats": stats
    }


    with open("dados_times.json", "w") as file:
        json.dump(dados, file, indent=4)




criar_json_predefinido()


if os.path.exists("stats_personalizados.json"):
    with open("stats_personalizados.json", "r") as file:
        dados = json.load(file)
        print("Carregando times e stats personalizados...")
else:
    with open("dados_times.json", "r") as file:
        dados = json.load(file)
        print("Carregando configurações predefinidas...")


potes = dados["potes"]
stats = dados["stats"]



def get_pote(time):
    for idx, pote in enumerate(potes, start=1):
        if time in pote:
            return idx
    return None

def listar_times(potes, stats):
    print("\nLista de Times:")
    print("\n")


    tamanho_linha = 75

    print("┌" + "─" * tamanho_linha + "┐")  
    print("│" + f"{'Número':<10}{'Time':<25}{'Ataque':<15}{'Meio-campo':<15}{'Defesa':<10}│")  
    print("├" + "─" * tamanho_linha + "┤")  

    for i in range(len(potes)):
        for j in range(len(potes[i])):
            time = potes[i][j]
            ataque = stats.get(time, {}).get("ataque", "N/A")
            defesa = stats.get(time, {}).get("defesa", "N/A")
            meio_campo = stats.get(time, {}).get("meio_campo", "N/A")
            numero = i * 9 + j + 1  
            print("│" + f"{numero:<10}{time:<25}{ataque:<15}{meio_campo:<15}{defesa:<10}│")  

    print("└" + "─" * tamanho_linha + "┘")  







def salvar_times_stats_personalizados(potes, stats):
    configuracao_personalizada = {
        "potes": potes,
        "stats": stats
    }
    with open("stats_personalizados.json", "w") as file:
        json.dump(configuracao_personalizada, file, indent=4)




def excluir_stats_personalizados():
    global potes, stats, stats_atual
    print("\n")

    confirmacao = input("Digite 'EXCLUIR' para apagar os stats personalizados: \n\n")

    if confirmacao == "EXCLUIR":

        if os.path.exists("stats_personalizados.json"):
            os.remove("stats_personalizados.json")
            print("\n")
            print("Os times personalizados foram excluídos com sucesso.\n")
            with open("dados_times.json", "r") as file:
                dados = json.load(file)
                potes = dados["potes"]
                stats = dados["stats"]
            stats_atual = "Padrões"
        else:
            print("\n")
            print("Não existem times personalizados.\n")
    else:
        print("\n")
        print("Operação cancelada ou erro de digitação.")





stats_atual = ""


def carregar_stats_inicial():
    global potes, stats, stats_atual

    if os.path.exists("stats_personalizados.json"):
        with open("stats_personalizados.json", "r") as file:
            dados = json.load(file)
            potes = dados["potes"]
            stats = dados["stats"]
        stats_atual = "Personalizados"  
    else:
        with open("dados_times.json", "r") as file:
            dados = json.load(file)
            potes = dados["potes"]
            stats = dados["stats"]
        stats_atual = "Padrões"
        print("Stats padrão em uso.")



def alternar_stats():
    global potes, stats, stats_atual  


    print(f"\n\nTimes e stats atualmente em uso: {stats_atual}\n")


    escolha = questionary.select(
        "\nEscolha quais utilizar:\n\n",
        choices=[
            "Dados padrões",
            "Dados personalizados",
            "Voltar"
        ],
        style=custom_style
    ).ask()

    if escolha == 'Dados padrões':
        if os.path.exists("dados_times.json"):
            with open("dados_times.json", "r") as file:
                print("\n\nCarregando configurações predefinidas...")
                dados = json.load(file)
                potes = dados["potes"]
                stats = dados["stats"]  
            stats_atual = "Padrões"
            print("\n\nAgora, os times e stats padrões estão em uso.\n\n")
        else:
            print("Erro: O arquivo não foi encontrado.")

    elif escolha == 'Dados personalizados':
        if os.path.exists("stats_personalizados.json"):
            with open("stats_personalizados.json", "r") as file:
                print("\n\nCarregando times e stats personalizados...")
                dados = json.load(file)
                potes = dados["potes"]
                stats = dados["stats"]
            stats_atual = "Personalizados"
            print("\n\nAgora, os times e stats personalizados estão em uso.\n\n")
        else:
            print("\n\nErro: Não existem times e stats personalizados disponíveis.\n\n")

    elif escolha == 'Voltar':
        print("\nVoltando ao menu anterior...\n")
        return  
    else:
        print("\nEscolha inválida. Por favor, selecione uma opção válida.\n")





def carregar_times_stats2():
    """Função para carregar times e stats, verificando se existe um arquivo personalizado."""
    if os.path.exists("stats_personalizados.json"):
        with open("stats_personalizados.json", "r") as file:
            print("\n\nCarregando times e stats personalizados...")
            dados = json.load(file)
            potes = dados["potes"]
            stats = dados["stats"]
    else:
        with open("dados_times.json", "r") as file:
            print("\n\nCarregando configurações predefinidas...")
            dados = json.load(file)
            potes = dados["potes"]
            stats = dados["stats"]

    return potes, stats




def carregar_times_stats():
    if os.path.exists("stats_personalizados.json"):
        with open("stats_personalizados.json", "r") as file:
            configuracao = json.load(file)
            return configuracao["potes"], configuracao["stats"]
    else:
        with open("dados_times.json", "r") as file:
            configuracao = json.load(file)
            return configuracao["potes"], configuracao["stats"]





def substituir_time(potes, stats):
    if not os.path.exists("dados_times.json"):
        print("\n\nArquivo não encontrado.\n\n")
        return


    if os.path.exists("stats_personalizados.json"):
        with open("stats_personalizados.json", "r") as file:
            dados_personalizados = json.load(file)
            potes = dados_personalizados["potes"]
            stats = dados_personalizados["stats"]
    else:

        with open("dados_times.json", "r") as file:
            dados_normais = json.load(file)
            potes = dados_normais["potes"]
            stats = dados_normais["stats"]

    listar_times(potes, stats)


    while True:
        try:
            print("\n")
            entrada = questionary.text(
                "\nDigite o número do time que deseja substituir (1-36) ou 'S' para sair: ",
                validate=lambda val: val.isdigit() and 1 <= int(val) <= 36 or val.lower() == 's'
            ).ask().strip()

            if entrada.lower() == 's':
                break  

            numero_substituir = int(entrada)  

            if numero_substituir < 1 or numero_substituir > 36:
                print("\nNúmero inválido. Escolha um número entre 1 e 36.\n")
                continue  


            pote_indice = (numero_substituir - 1) // 9
            indice_no_pote = (numero_substituir - 1) % 9


            time_substituido = potes[pote_indice][indice_no_pote]

            print(f"\nVocê escolheu substituir o time: {time_substituido}")


            novo_time = questionary.text(f"\nDigite o nome do novo time:").ask()


            ataque = int(questionary.text(f"\nDigite o valor do ataque de {novo_time}:").ask())
            defesa = int(questionary.text(f"Digite o valor da defesa de {novo_time}:").ask())
            meio_campo = int(questionary.text(f"Digite o valor do meio-campo de {novo_time}:").ask())


            potes[pote_indice][indice_no_pote] = novo_time
            stats[novo_time] = {"ataque": ataque, "defesa": defesa, "meio_campo": meio_campo}


            if time_substituido in stats:
                del stats[time_substituido]

            print(f"\n\n{novo_time} foi adicionado com ataque {ataque}, meio-campo {meio_campo} e defesa {defesa}.\n\n")


            salvar_times_stats_personalizados(potes, stats)
            carregar_stats_inicial()


            if os.path.exists("stats_personalizados.json"):
                with open("stats_personalizados.json", "r") as file:
                    print("\n\nCarregando times e stats personalizados...")
                    dados = json.load(file)
                    potes = dados["potes"]
                    stats = dados["stats"]
                print("\n\nAgora, os times e stats personalizados estão em uso.\n\n")
            else:
                print("\n\nErro: Não existem times e stats personalizados disponíveis.\n\n")

        except ValueError:
            print("\nOpção inválida. Tente novamente.")












def calcula_media_desvio(ataque_time, defesa_adversario):

    configuracao = carregar_configuracao()
    nivel_gols = configuracao["nivel_gols"]
    params = configuracao["configuracoes"][nivel_gols]


    media = max(params["media_base"], (ataque_time - defesa_adversario) / params["media_divisor"] + params["soma"])
    desvio = max(params["desvio_base"], (60 - abs(ataque_time - defesa_adversario)) / params["desvio_divisor"])

    return media, desvio



def carregar_dados_json():

    if stats_atual == "Personalizados":
        caminho_arquivo = "stats_personalizados.json"
    else:
        caminho_arquivo = "dados_times.json"


    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        return json.load(f)


def salvar_dados_json(dados):

    if stats_atual == "Personalizados":
        caminho_arquivo = "stats_personalizados.json"
    else:
        caminho_arquivo = "dados_times.json"


    with open(caminho_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

def salvar_dados_json2(dados_times):
    with open("dados_times.json", "w") as file:
        json.dump(dados_times, file, indent=4)



momentos_aplicados = {}

def aplicar_momento(dados_times):
    nome_arquivo = "campeoes.json"
    ultimo_campeao = None

    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r', encoding='utf-8') as file:
            historico_finais = json.load(file)
            if historico_finais:
                ultimo_campeao = historico_finais[-1]["campeao"]["time"]


    for time, stats in dados_times['stats'].items():

        if time == ultimo_campeao:
            momento_ataque = random.choice(range(0, 6))
            momento_defesa = random.choice(range(0, 6))
            momento_meio_campo = random.choice(range(0, 6))
        else:
            if stats['ataque'] + stats['defesa'] >= 168:

                momento_ataque = random.choice(range(-1, 5))
                momento_defesa = random.choice(range(-1, 5))
                momento_meio_campo = random.choice(range(-1, 5))
            elif stats['ataque'] + stats['defesa'] < 168 and stats['ataque'] + stats['defesa'] >=160:
                momento_ataque = random.choice(range(-3, 6))
                momento_defesa = random.choice(range(-3, 6))
                momento_meio_campo = random.choice(range(-3, 6))

            elif stats['ataque'] + stats['defesa'] < 160 and stats['ataque'] + stats['defesa'] >=140:
                momento_ataque = random.choice(range(-3, 7))
                momento_defesa = random.choice(range(-3, 7))
                momento_meio_campo = random.choice(range(-3, 7))
            else:
                momento_ataque = random.choice(range(-4, 8))
                momento_defesa = random.choice(range(-4, 8))
                momento_meio_campo = random.choice(range(-4, 8))


        momentos_aplicados[time] = {
            "ataque": momento_ataque,
            "defesa": momento_defesa,
            "meio_campo": momento_meio_campo
        }


        stats['ataque'] += momento_ataque
        stats['defesa'] += momento_defesa
        stats['meio_campo'] += momento_meio_campo

    reordenar_potes(dados_times)


    salvar_dados_json2(dados_times)


def restaurar_stats_originais(dados_times):
    for time, stats in dados_times['stats'].items():
        if time in momentos_aplicados:
            momento_ataque = momentos_aplicados[time]['ataque']
            momento_defesa = momentos_aplicados[time]['defesa']
            momento_meio_campo = momentos_aplicados[time]['meio_campo']


            stats['ataque'] -= momento_ataque
            stats['defesa'] -= momento_defesa
            stats['meio_campo'] -= momento_meio_campo


    reordenar_potes(dados_times)


    salvar_dados_json(dados_times)


    momentos_aplicados.clear()




def reordenar_potes(dados_times):
    times_somados = [(time, stats['ataque'] + stats['defesa'] + stats['meio_campo']) for time, stats in dados_times['stats'].items()]
    times_ordenados = sorted(times_somados, key=lambda x: x[1], reverse=True)

    novos_potes = [[], [], [], []]
    for i, (time, soma) in enumerate(times_ordenados):
        pote = i // 9 
        novos_potes[pote].append(time)


    dados_times['potes'] = novos_potes



def carregar_dados_times_2(caminho_arquivo="dados_times.json"):
    with open(caminho_arquivo, 'r', encoding='utf-8') as file:
        return json.load(file)

def carregar_dados_de_stats():

    if stats_atual == "Personalizados":
        caminho_arquivo = "stats_personalizados.json"
    else:
        caminho_arquivo = "dados_times.json"


    with open(caminho_arquivo, "r") as file:
        dados = json.load(file)

    return dados["stats"]



def gerar_gols(time_casa, time_fora):
    stats=carregar_dados_de_stats()

    if time_casa not in stats or time_fora not in stats:
        raise ValueError(f"Stats não definidos para {time_casa} ou {time_fora}")

    numero_aleatorio = random.uniform(0.01, 0.05)
    numero_aleatorio2 = random.uniform(0.01, 0.04)
    fator_casa = round(numero_aleatorio, 3)
    fator_fora = round(numero_aleatorio2, 3)

    meio_campo_ataque_casa = (stats[time_casa]["ataque"] + (stats[time_casa]["meio_campo"] // 2)) // 1.5
    meio_campo_ataque_fora = (stats[time_fora]["ataque"] + (stats[time_fora]["meio_campo"] // 2)) // 1.5
    meio_campo_defesa_casa = (stats[time_casa]["defesa"] + (stats[time_casa]["meio_campo"] // 2)) // 1.5
    meio_campo_defesa_fora = (stats[time_fora]["defesa"] + (stats[time_fora]["meio_campo"] // 2)) // 1.5
    ataque_casa = meio_campo_ataque_casa
    defesa_casa = meio_campo_defesa_casa
    ataque_fora = meio_campo_ataque_fora
    defesa_fora = meio_campo_defesa_fora
    ataque_casa += ataque_casa * fator_casa
    ataque_fora -= ataque_fora * fator_fora
    defesa_casa += defesa_casa * fator_casa
    defesa_fora -= defesa_fora * fator_casa



    soma_stats_casa = ataque_casa + defesa_casa
    soma_stats_fora = ataque_fora + defesa_fora



    if abs(soma_stats_casa - soma_stats_fora) <= 20:
        if np.random.rand() <= 0.3:
            ataque_casa, ataque_fora = ataque_fora, ataque_casa
            defesa_casa, defesa_fora = defesa_fora, defesa_casa
        #    print(f"Inversão! O ataque do time da casa ({time_casa}) foi trocado com a defesa do time visitante ({time_fora}).")

    if abs(ataque_casa - defesa_fora) > 5 or abs(ataque_fora - defesa_casa) > 5:
        chance = np.random.rand()


        if chance <= 0.333:
            pass


        elif 0.333 < chance <= 0.666:
            if soma_stats_casa > soma_stats_fora:
                incremento = random.randint(5, 13)
                incremento2 = random.randint(5, 13)
                ataque_casa += incremento
                defesa_casa += incremento2
            else:
                incremento = random.randint(5, 13)
                incremento2 = random.randint(5, 13)
                ataque_fora += incremento
                defesa_fora += incremento2


        else:
            if soma_stats_casa > soma_stats_fora:
                decremento = random.randint(1, 3)
                ataque_casa = max(0, ataque_casa - decremento)
                defesa_casa = max(0, defesa_casa - decremento)
            else:
                decremento = random.randint(1, 3)
                ataque_fora = max(0, ataque_fora - decremento)
                defesa_fora = max(0, defesa_fora - decremento)

    diferenca_ataque_defesa = abs((ataque_casa + defesa_casa) - (ataque_fora + defesa_fora))

    if diferenca_ataque_defesa > 20:
        if np.random.rand() <= 0.25:
            incremento = np.random.randint(5, 11)  
            if ataque_casa + defesa_casa < ataque_fora + defesa_fora:
                ataque_casa += incremento
                defesa_casa += incremento
            else:
                ataque_fora += incremento
                defesa_fora += incremento





    media_casa, desvio_casa = calcula_media_desvio(ataque_casa, defesa_fora)
    media_fora, desvio_fora = calcula_media_desvio(ataque_fora, defesa_casa)


    gols_casa = max(0, int(np.random.normal(media_casa, desvio_casa)))
    gols_fora = max(0, int(np.random.normal(media_fora, desvio_fora)))

    return gols_casa, gols_fora

def gerar_gols_sem_fator_casa(time_casa, time_fora):
    stats=carregar_dados_de_stats()

    if time_casa not in stats or time_fora not in stats:
        raise ValueError(f"Stats não definidos para {time_casa} ou {time_fora}")


    meio_campo_ataque_casa = stats[time_casa]["ataque"] + (stats[time_casa]["meio_campo"] // 2) // 1.5
    meio_campo_ataque_fora = stats[time_fora]["ataque"] + (stats[time_fora]["meio_campo"] // 2) // 1.5
    meio_campo_defesa_casa = stats[time_casa]["defesa"] + (stats[time_casa]["meio_campo"] // 2) // 1.5
    meio_campo_defesa_fora = stats[time_fora]["defesa"] + (stats[time_fora]["meio_campo"] // 2) // 1.5
    ataque_casa = meio_campo_ataque_casa
    defesa_casa = meio_campo_defesa_casa
    ataque_fora = meio_campo_ataque_fora
    defesa_fora = meio_campo_defesa_fora


    soma_stats_casa = ataque_casa + defesa_casa
    soma_stats_fora = ataque_fora + defesa_fora


    if abs(soma_stats_casa - soma_stats_fora) <= 20:
        if np.random.rand() <= 0.12:
            ataque_casa, ataque_fora = ataque_fora, ataque_casa
            defesa_casa, defesa_fora = defesa_fora, defesa_casa
    #        print(f"Inversão! O ataque do time da casa ({time_casa}) foi trocado com a defesa do time visitante ({time_fora}).")

    if abs(ataque_casa - defesa_fora) > 20 or abs(ataque_fora - defesa_casa) > 20:
        chance = np.random.rand()


        if chance <= 0.333:
            pass


        elif 0.333 < chance <= 0.666:
            if soma_stats_casa > soma_stats_fora:
                incremento = random.randint(5, 13)
                ataque_casa += incremento
                defesa_casa += incremento
            else:
                incremento = random.randint(5, 13)
                ataque_fora += incremento
                defesa_fora += incremento


        else:
            if soma_stats_casa > soma_stats_fora:
                decremento = random.randint(1,7)
                ataque_casa = max(0, ataque_casa - decremento)
                defesa_casa = max(0, defesa_casa - decremento)
            else:
                decremento = random.randint(1, 7)
                ataque_fora = max(0, ataque_fora - decremento)
                defesa_fora = max(0, defesa_fora - decremento)

    diferenca_ataque_defesa = abs((ataque_casa + defesa_casa) - (ataque_fora + defesa_fora))

    if diferenca_ataque_defesa > 20:
        if np.random.rand() <= 0.25:
            incremento = np.random.randint(5, 11)  
            if ataque_casa + defesa_casa < ataque_fora + defesa_fora:
                ataque_casa += incremento
                defesa_casa += incremento
            else:
                ataque_fora += incremento
                defesa_fora += incremento



    media_casa, desvio_casa = calcula_media_desvio(ataque_casa, defesa_fora)
    media_fora, desvio_fora = calcula_media_desvio(ataque_fora, defesa_casa)


    gols_casa = max(0, int(np.random.normal(media_casa, desvio_casa)))
    gols_fora = max(0, int(np.random.normal(media_fora, desvio_fora)))

    return gols_casa, gols_fora






def simular_penaltis(time1, time2):

    gols_time1 = 0
    gols_time2 = 0
    total_cobranças = 5


    for i in range(total_cobranças):

        if random.random() < 0.72:
            gols_time1 += 1


        if random.random() < 0.72:
            gols_time2 += 1


        if abs(gols_time1 - gols_time2) > total_cobranças - (i + 1):
            return gols_time1, gols_time2



    while True:

        if random.random() < 0.72:
            gols_time1 += 1


        if random.random() < 0.72:
            gols_time2 += 1


        if gols_time1 != gols_time2:
            return gols_time1, gols_time2










def inicializa_confrontos(potes):
    return {time: set() for pote in potes for time in pote}


def assign_internal_rivals(pot, confrontos):
    shuffled_pot = pot.copy()
    random.shuffle(shuffled_pot)
    n = len(shuffled_pot)
    for i in range(n):
        team_a = shuffled_pot[i]
        team_b = shuffled_pot[(i + 1) % n]
        team_c = shuffled_pot[(i - 1) % n]
        confrontos[team_a].add(team_b)
        confrontos[team_b].add(team_a)
        confrontos[team_a].add(team_c)
        confrontos[team_c].add(team_a)

def assign_all_internal_rivals(potes, confrontos):
    for pot in potes:
        assign_internal_rivals(pot, confrontos)

def assign_external_rivals_between_pots(potA, potB, confrontos, max_attempts=1000):
    slotsA = potA.copy() * 2
    slotsB = potB.copy() * 2
    attempts = 0
    while attempts < max_attempts:
        attempts += 1
        random.shuffle(slotsA)
        random.shuffle(slotsB)
        temp_confrontos = {time: set(rivals) for time, rivals in confrontos.items()}
        sucesso = True
        for teamA, teamB in zip(slotsA, slotsB):
            if teamB in temp_confrontos[teamA]:
                found = False
                for idx, candidateB in enumerate(slotsB):
                    if candidateB not in temp_confrontos[teamA] and teamA not in temp_confrontos[candidateB]:

                        slotsB[idx], slotsB[slotsB.index(teamB)] = slotsB[slotsB.index(teamB)], slotsB[idx]
                        teamB = slotsB[slotsB.index(teamB)]
                        if teamB not in temp_confrontos[teamA]:
                            found = True
                            break
                if not found:
                    sucesso = False
                    break
            temp_confrontos[teamA].add(teamB)
            temp_confrontos[teamB].add(teamA)
        if sucesso:
            confrontos.update(temp_confrontos)
            return True
    print(f"Falha ao atribuir rivalidades entre {potA} e {potB} após {max_attempts} tentativas.")
    return False

def assign_all_external_rivals(potes, confrontos):
    NUM_POTS = len(potes)
    for i in range(NUM_POTS):
        for j in range(i + 1, NUM_POTS):
            potA = potes[i]
            potB = potes[j]
            success = assign_external_rivals_between_pots(potA, potB, confrontos)
            if not success:
                print(f"Falha ao atribuir rivalidades entre Pote {i+1} e Pote {j+1}")
                return False
    return True

def assign_home_away(confrontos):
    home_away = {time: {"home": [], "away": []} for time in confrontos}
    for time in confrontos:
        rivals = list(confrontos[time])
        random.shuffle(rivals)
        half = len(rivals) // 2
        home_away[time]["home"] = rivals[:half]
        home_away[time]["away"] = rivals[half:]
    return home_away

def agrupar_rivais_por_pote_intercalados(confrontos, time):
    rivais_por_pote = {i: [] for i in range(1, len(potes) + 1)}


    for rival in confrontos[time]:
        pote = get_pote(rival)
        if pote is not None:
            rivais_por_pote[pote].append(rival)


    rivais_intercalados = []
    max_length = max(len(rivais_por_pote[i]) for i in range(1, len(potes) + 1))

    for i in range(max_length):
        for pote in range(1, len(potes) + 1):
            if i < len(rivais_por_pote[pote]):
                rivais_intercalados.append(rivais_por_pote[pote][i])

    return rivais_intercalados





gols_acumulados = {
    "gols": {},
    "gols_sofridos": {},
    "partidas_jogadas": {},
    "vitorias": {},  
    "empates": {},  
    "derrotas": {}  
}

def inicializar_gols_acumulados(classificacao):
    """Inicializa o dicionário que armazena os gols acumulados com base na classificação."""
    for time in classificacao.keys():
        gols_acumulados["gols"][time] = classificacao[time]['gols_marcados']
        gols_acumulados["gols_sofridos"][time] = 0  
        gols_acumulados["partidas_jogadas"][time] = 0  
        gols_acumulados["vitorias"][time] = 0  
        gols_acumulados["empates"][time] = 0  
        gols_acumulados["derrotas"][time] = 0  

def atualizar_gols_acumulados(time, gols, tipo):
    """Atualiza o total de gols de um time, seja marcados ou sofridos."""
    if time in gols_acumulados[tipo]:
        gols_acumulados[tipo][time] += gols
    else:
        gols_acumulados[tipo][time] = gols

def atualizar_partidas_jogadas(time):
    """Atualiza o total de partidas jogadas de um time no arquivo JSON."""
    dados_atualizados = carregar_gols_acumulados()  


    if time in dados_atualizados["partidas_jogadas"]:
        dados_atualizados["partidas_jogadas"][time] += 1
    else:
        dados_atualizados["partidas_jogadas"][time] = 1

    salvar_gols_acumulados(dados_atualizados)  

def atualizar_vitoria(time):
    """Atualiza o total de vitórias de um time no arquivo JSON."""
    dados_atualizados = carregar_gols_acumulados()
    if time in dados_atualizados["vitorias"]:
        dados_atualizados["vitorias"][time] += 1
    else:
        dados_atualizados["vitorias"][time] = 1
    salvar_gols_acumulados(dados_atualizados)

def atualizar_empate(time):
    """Atualiza o total de empates de um time no arquivo JSON."""
    dados_atualizados = carregar_gols_acumulados()
    if time in dados_atualizados["empates"]:
        dados_atualizados["empates"][time] += 1
    else:
        dados_atualizados["empates"][time] = 1
    salvar_gols_acumulados(dados_atualizados)

def atualizar_derrota(time):
    """Atualiza o total de derrotas de um time no arquivo JSON."""
    dados_atualizados = carregar_gols_acumulados()

    if time not in dados_atualizados["derrotas"]:
        dados_atualizados["derrotas"][time] = 0


    dados_atualizados["derrotas"][time] += 1
    salvar_gols_acumulados(dados_atualizados)

nome_arquivo_gols = "gols_simulacao_atual.json"

def carregar_gols_acumulados():
    """Carrega o arquivo de gols acumulados. Se o arquivo não existir ou estiver incompleto, retorna um dicionário inicializado corretamente."""
    if os.path.exists(nome_arquivo_gols):
        with open(nome_arquivo_gols, 'r') as file:
            dados = json.load(file)


            if "vitorias" not in dados:
                dados["vitorias"] = {}
            if "empates" not in dados:
                dados["empates"] = {}
            if "derrotas" not in dados:
                dados["derrotas"] = {}
            if "gols" not in dados:
                dados["gols"] = {}
            if "gols_sofridos" not in dados:
                dados["gols_sofridos"] = {}
            if "partidas_jogadas" not in dados:
                dados["partidas_jogadas"] = {}

            return dados


    dados_iniciais = {
        "vitorias": {},
        "empates": {},
        "derrotas": {},
        "gols": {},
        "gols_sofridos": {},
        "partidas_jogadas": {}
    }


    for pote in potes:
        for time in pote:
            dados_iniciais["vitorias"][time] = 0
            dados_iniciais["empates"][time] = 0
            dados_iniciais["derrotas"][time] = 0
            dados_iniciais["gols"][time] = 0
            dados_iniciais["gols_sofridos"][time] = 0
            dados_iniciais["partidas_jogadas"][time] = 0

    return dados_iniciais



def salvar_gols_acumulados(gols_acumulados):
    """Salva o dicionário de gols acumulados no arquivo JSON."""
    with open(nome_arquivo_gols, 'w') as file:
        json.dump(gols_acumulados, file, indent=4)

def atualizar_gols_acumulados_json(time, gols_marcados, gols_sofridos):
    """Atualiza o total de gols marcados e sofridos de um time no arquivo JSON."""
    dados_atualizados = carregar_gols_acumulados()


    if time in dados_atualizados["gols"]:
        dados_atualizados["gols"][time] += gols_marcados
    else:
        dados_atualizados["gols"][time] = gols_marcados


    if time in dados_atualizados["gols_sofridos"]:
        dados_atualizados["gols_sofridos"][time] += gols_sofridos
    else:
        dados_atualizados["gols_sofridos"][time] = gols_sofridos


    atualizar_partidas_jogadas(time)  

    salvar_gols_acumulados(dados_atualizados)

nome_arquivo_historico = "historico_gols.json"

def carregar_historico_gols():
    if os.path.exists(nome_arquivo_historico_gols):
        with open(nome_arquivo_historico_gols, 'r') as file:
            try:

                return json.load(file)
            except json.JSONDecodeError:


                print(f"Arquivo vazio ou corrompido.")
                print("\n")
                return []
    else:

        print(f"Arquivo não encontrado.")
        print("\n")
        return []


def salvar_historico_gols(historico_gols):
    """Salva o histórico de gols no arquivo JSON."""
    with open(nome_arquivo_historico, 'w') as file:
        json.dump(historico_gols, file, indent=4)

def resetar_arquivo_gols():
    """Remove o arquivo de gols acumulados, iniciando uma nova simulação."""
    if os.path.exists(nome_arquivo_gols):
        os.remove(nome_arquivo_gols)
    maiores_goleadas.clear()
    criar_json_predefinido()

def finalizar_simulacao(vencedor_final, gols_vencedor, vice_final, gols_vice):
    """Transfere os gols marcados e sofridos da simulação atual para o histórico e reseta o arquivo de gols acumulados."""
    print("Finalização da simulação...")


    gols_acumulados = carregar_gols_acumulados()


    if len(gols_acumulados["gols"]) < 25:
        print("Erro: Não foi salvo no histórico!")
        return

    configuracao_atual = carregar_configuracao()
    nivel_gols_simulacao = configuracao_atual["nivel_gols"]


    historico_gols = carregar_historico_gols()


    historico_gols.append({
        "simulacao": len(historico_gols) + 1,
        "nivel_simulacao": nivel_gols_simulacao,
        "gols": gols_acumulados["gols"],
        "gols_sofridos": gols_acumulados["gols_sofridos"],
        "partidas_jogadas": gols_acumulados["partidas_jogadas"],  
        "vitorias": gols_acumulados["vitorias"],
        "empates": gols_acumulados["empates"],
        "derrotas": gols_acumulados["derrotas"]
    })
    salvar_resultado_final(vencedor_final, gols_vencedor, vice_final, gols_vice)


    salvar_historico_gols(historico_gols)


    resetar_arquivo_gols()

    print(f"Simulação finalizada! Os dados foram movidos para o histórico.")


def resetar_arquivo_resultados():
    """Remove o arquivo de resultados das partidas, iniciando uma nova simulação."""
    if os.path.exists('resultados_partidas_atual.json'):
        os.remove('resultados_partidas_atual.json')













def historico_melhores_ataques():
    """Lista o histórico de melhores ataques, somando todos os gols e partidas jogadas de cada time."""

    historico_gols = carregar_historico_gols()


    totais_gols = {}
    totais_partidas = {}


    for simulacao in historico_gols:
        for time, gols in simulacao["gols"].items():
            if time not in totais_gols:
                totais_gols[time] = 0
            totais_gols[time] += gols

        for time, partidas in simulacao["partidas_jogadas"].items():
            if time not in totais_partidas:
                totais_partidas[time] = 0
            totais_partidas[time] += partidas


    melhores_ataques = sorted(totais_gols.items(), key=lambda x: x[1], reverse=True)

    print("Histórico de Melhores Ataques:")
    print("┌" + "─" * 50 + "┐")
    print(f"│{'Time'.ljust(20)}│ {'Gols'.ljust(10)}│{'Partidas Jogadas'.ljust(15)} │")
    print("├" + "─" * 50 + "┤")

    for time, gols in melhores_ataques:
        partidas_jogadas = totais_partidas.get(time, 0)  
        print(f"│{time.ljust(20)}│ {str(gols).ljust(10)}│ {str(partidas_jogadas).ljust(15)} │")

    print("└" + "─" * 50 + "┘")


def historico_melhores_defesas():
    """Lista o histórico de melhores defesas, somando todos os gols sofridos e partidas jogadas de cada time."""

    historico_gols = carregar_historico_gols()


    totais_gols_sofridos = {}
    totais_partidas = {}


    for simulacao in historico_gols:
        for time, gols_sofridos in simulacao["gols_sofridos"].items():
            if time not in totais_gols_sofridos:
                totais_gols_sofridos[time] = 0
            totais_gols_sofridos[time] += gols_sofridos

        for time, partidas in simulacao["partidas_jogadas"].items():
            if time not in totais_partidas:
                totais_partidas[time] = 0
            totais_partidas[time] += partidas


    melhores_defesas = sorted(totais_gols_sofridos.items(), key=lambda x: x[1])

    print("Histórico de Melhores Defesas:")
    print("┌" + "─" * 55 + "┐")
    print(f"│{'Time'.ljust(20)}│ {'Gols Sofridos'.ljust(15)}│{'Partidas Jogadas'.ljust(15)} │")
    print("├" + "─" * 55 + "┤")

    for time, gols_sofridos in melhores_defesas:
        partidas_jogadas = totais_partidas.get(time, 0)  
        print(f"│{time.ljust(20)}│ {str(gols_sofridos).ljust(15)}│ {str(partidas_jogadas).ljust(15)} │")

    print("└" + "─" * 55 + "┘\n")







def historico_mais_vitorias():
    """Exibe uma tabela com os times ordenados por vitórias, empates ou derrotas, conforme a escolha do usuário."""
    while True:
        historico_gols = carregar_historico_gols()


        totais_vitorias = {}
        totais_empates = {}
        totais_derrotas = {}
        totais_partidas = {}


        for simulacao in historico_gols:
            if "vitorias" in simulacao:
                for time, vitorias in simulacao["vitorias"].items():
                    if time not in totais_vitorias:
                        totais_vitorias[time] = 0
                    totais_vitorias[time] += vitorias

            if "empates" in simulacao:
                for time, empates in simulacao["empates"].items():
                    if time not in totais_empates:
                        totais_empates[time] = 0
                    totais_empates[time] += empates

            if "derrotas" in simulacao:
                for time, derrotas in simulacao["derrotas"].items():
                    if time not in totais_derrotas:
                        totais_derrotas[time] = 0
                    totais_derrotas[time] += derrotas

            if "partidas_jogadas" in simulacao:
                for time, partidas in simulacao["partidas_jogadas"].items():
                    if time not in totais_partidas:
                        totais_partidas[time] = 0
                    totais_partidas[time] += partidas


        escolha = questionary.select(
            "\nOrdenar por:",
            choices=[
                "Vitórias",
                "Empates",
                "Derrotas",
                "VOLTAR"
            ], style=custom_style
        ).ask()

        if escolha == 'Empates':

            tabela_ordenada = sorted(totais_empates.items(), key=lambda x: x[1], reverse=True)
            criterio = "empates"
        elif escolha == 'Derrotas':

            tabela_ordenada = sorted(totais_derrotas.items(), key=lambda x: x[1], reverse=True)
            criterio = "derrotas"
        elif escolha == 'Vitórias':

            tabela_ordenada = sorted(totais_vitorias.items(), key=lambda x: x[1], reverse=True)
            criterio = "vitórias"
        elif escolha == 'VOLTAR':
            break


        print(f"\nTimes com mais {criterio}:")
        print("\n")


        tamanho_linha = 47

        print("┌" + "─" * tamanho_linha + "┐")  
        print("│" + f"{'Pos':<4} {'Time':<20} {criterio.capitalize():<10} {'Partidas':<10}│")  
        print("├" + "─" * tamanho_linha + "┤")  


        for i, (time, valor) in enumerate(tabela_ordenada, start=1):
            partidas_jogadas = totais_partidas.get(time, 0)
            print("│" + f"{i:<4} {time:<20} {valor:<10} {partidas_jogadas:<10}│")  

        print("└" + "─" * tamanho_linha + "┘")  
        print("\n")











def media_gols_feitos():
    """Calcula e lista as médias de gols feitos por time, ordenando do melhor para o pior."""

    historico_gols = carregar_historico_gols()


    totais_gols_feitos = {}
    partidas_jogadas = {}


    for simulacao in historico_gols:
        if "gols" in simulacao and "partidas_jogadas" in simulacao:
            for time, gols in simulacao["gols"].items():
                if time not in totais_gols_feitos:
                    totais_gols_feitos[time] = 0
                    partidas_jogadas[time] = 0
                totais_gols_feitos[time] += gols
                partidas_jogadas[time] += simulacao["partidas_jogadas"].get(time, 0)


    medias_gols_feitos = {time: totais_gols_feitos[time] / partidas_jogadas[time] 
                           for time in totais_gols_feitos}


    melhores_gols_feitos = sorted(medias_gols_feitos.items(), key=lambda x: x[1], reverse=True)


    print("Média de Gols Feitos por Time:")
    print("┌" + "─" * 44 + "┐")
    print(f"│{'Time'.ljust(20)}│ {'Média de Gols Feitos'.ljust(22)}│")
    print("├" + "─" * 44 + "┤")

    for time, media in melhores_gols_feitos:
        print(f"│{time.ljust(20)}│ {media:.2f}                  │".ljust(22))

    print("└" + "─" * 44 + "┘")




def media_gols_sofridos():
    """Calcula e lista as médias de gols sofridos por time, ordenando do melhor para o pior."""

    historico_gols = carregar_historico_gols()


    totais_gols_sofridos = {}
    partidas_jogadas = {}


    for simulacao in historico_gols:
        if "gols_sofridos" in simulacao and "partidas_jogadas" in simulacao:
            for time, gols_sofridos in simulacao["gols_sofridos"].items():
                if time not in totais_gols_sofridos:
                    totais_gols_sofridos[time] = 0
                    partidas_jogadas[time] = 0
                totais_gols_sofridos[time] += gols_sofridos
                partidas_jogadas[time] += simulacao["partidas_jogadas"].get(time, 0)


    medias_gols_sofridos = {time: totais_gols_sofridos[time] / partidas_jogadas[time] 
                             for time in totais_gols_sofridos}


    melhores_defesas = sorted(medias_gols_sofridos.items(), key=lambda x: x[1])


    print("Média de Gols Sofridos por Time:")
    print("┌" + "─" * 44 + "┐")
    print(f"│{'Time'.ljust(20)}│ {'Média de Gols Sofridos'.ljust(22)}│")
    print("├" + "─" * 44 + "┤")

    for time, media in melhores_defesas:
        print(f"│{time.ljust(20)}│ {media:.2f}                  │".ljust(22))

    print("└" + "─" * 44 + "┘")





























def exibir_playoffs(classificacao):

    classificados = sorted(classificacao.items(), key=lambda x: (x[1]['pontos'], x[1]['saldo_gols'], x[1]['gols_marcados']), reverse=True)

    print("\nConfrontos dos playoffs:")
    print("\n")

    confrontos_playoffs = [
        (classificados[8][0], classificados[23][0]),  
        (classificados[9][0], classificados[22][0]),  
        (classificados[10][0], classificados[21][0]),  
        (classificados[11][0], classificados[20][0]),  
        (classificados[12][0], classificados[19][0]),  
        (classificados[13][0], classificados[18][0]),  
        (classificados[14][0], classificados[17][0]),  
        (classificados[15][0], classificados[16][0]),  
    ]


    max_len_time = max(len(time1) + len(time2) for time1, time2 in confrontos_playoffs)
    if max_len_time % 2 == 0:
        max_len_time += 1
    tamanho_linha = max_len_time + 28  
    metade = (tamanho_linha - 5) // 2


    print("┌" + "─" * tamanho_linha + "┐")
    print("├" + "─" * tamanho_linha + "┤")

    for time1, time2 in confrontos_playoffs:
        print("| {:>{}} x {:<{}} |".format(time1, metade, time2, metade))

    print("└" + "─" * tamanho_linha + "┘")


def simular_playoff(classificacao):
    global maiores_goleadas_mata_mata  
    maiores_goleadas_mata_mata = []  


    classificados = sorted(classificacao.items(), key=lambda x: (x[1]['pontos'], x[1]['saldo_gols'], x[1]['gols_marcados']), reverse=True)

    confrontos_playoffs = [
        (classificados[8][0], classificados[23][0]),  
        (classificados[9][0], classificados[22][0]),  
        (classificados[10][0], classificados[21][0]),  
        (classificados[11][0], classificados[20][0]),  
        (classificados[12][0], classificados[19][0]),  
        (classificados[13][0], classificados[18][0]),  
        (classificados[14][0], classificados[17][0]),  
        (classificados[15][0], classificados[16][0]),  
    ]


    max_len_time = max(len(time1) + len(time2) for time1, time2 in confrontos_playoffs)
    if max_len_time % 2 == 0:
        max_len_time += 1
    tamanho_linha = max_len_time + 28  
    metade = (tamanho_linha - 13) //2 

    resultados_ida = {}
    print("\nJogo de ida - Playoffs:")
    print("\n")
    print("┌" + "─" * tamanho_linha + "┐")
    print("| {:^{}} | {:^1} x {:^1} | {:^{}} |".format("Casa", metade, "", "", "Fora", metade))
    print("├" + "─" * tamanho_linha + "┤")

    for time1, time2 in confrontos_playoffs:

        gols_time1, gols_time2 = gerar_gols(time1, time2)


        resultados_ida[(time1, time2)] = (gols_time1, gols_time2)


        diferenca_gols = abs(gols_time1 - gols_time2)
        if len(maiores_goleadas_mata_mata) == 0 or diferenca_gols > maiores_goleadas_mata_mata[0]['diferenca']:
            maiores_goleadas_mata_mata = [{
                "time1": time1,
                "gols_time1": gols_time1,
                "time2": time2,
                "gols_time2": gols_time2,
                "diferenca": diferenca_gols
            }]
        elif diferenca_gols == maiores_goleadas_mata_mata[0]['diferenca']:
            maiores_goleadas_mata_mata.append({
                "time1": time1,
                "gols_time1": gols_time1,
                "time2": time2,
                "gols_time2": gols_time2,
                "diferenca": diferenca_gols
            })


        atualizar_gols_acumulados_json(time1, gols_time1, gols_time2)
        atualizar_gols_acumulados_json(time2, gols_time2, gols_time1)
        atualizar_partidas_jogadas(time1)
        atualizar_partidas_jogadas(time2)
        if gols_time1 > gols_time2:
            atualizar_vitoria(time1)
            atualizar_derrota(time2)
        elif gols_time2 > gols_time1:
            atualizar_vitoria(time2)
            atualizar_derrota(time1)
        else:
            atualizar_empate(time1)
            atualizar_empate(time2)
        salvar_resultados_json(time1, gols_time1, time2, gols_time2, "playoffs")
        print("| {:>{}} | {:<1} x {:<1} | {:<{}} |".format(time1, metade, gols_time1, gols_time2, time2, metade))

    print("└" + "─" * tamanho_linha + "┘")

    resultados_volta = {}
    print("\n")
    print("\nJogo de volta - Playoffs:")
    print("\n")
    print("┌" + "─" * tamanho_linha + "┐")
    print("| {:^{}} | {:^1} x {:^1} | {:^{}} |".format("Casa", metade, "", "", "Fora", metade))
    print("├" + "─" * tamanho_linha + "┤")

    for time2, time1 in confrontos_playoffs:
        gols_time1, gols_time2 = gerar_gols(time1, time2)

        resultados_volta[(time1, time2)] = (gols_time1, gols_time2)


        diferenca_gols = abs(gols_time1 - gols_time2)
        if len(maiores_goleadas_mata_mata) == 0 or diferenca_gols > maiores_goleadas_mata_mata[0]['diferenca']:
            maiores_goleadas_mata_mata = [{
                "time1": time1,
                "gols_time1": gols_time1,
                "time2": time2,
                "gols_time2": gols_time2,
                "diferenca": diferenca_gols
            }]
        elif diferenca_gols == maiores_goleadas_mata_mata[0]['diferenca']:
            maiores_goleadas_mata_mata.append({
                "time1": time1,
                "gols_time1": gols_time1,
                "time2": time2,
                "gols_time2": gols_time2,
                "diferenca": diferenca_gols
            })


        atualizar_gols_acumulados_json(time1, gols_time1, gols_time2)
        atualizar_gols_acumulados_json(time2, gols_time2, gols_time1)
        atualizar_partidas_jogadas(time1)
        atualizar_partidas_jogadas(time2)
        if gols_time1 > gols_time2:
            atualizar_vitoria(time1)
            atualizar_derrota(time2)
        elif gols_time2 > gols_time1:
            atualizar_vitoria(time2)
            atualizar_derrota(time1)
        else:
            atualizar_empate(time1)
            atualizar_empate(time2)
        salvar_resultados_json(time1, gols_time1, time2, gols_time2, "playoffs")
        print("| {:>{}} | {:<1} x {:<1} | {:<{}} |".format(time1, metade, gols_time1, gols_time2, time2, metade))

    print("└" + "─" * tamanho_linha + "┘")

    return resultados_ida, resultados_volta




def placar_final_playoffs(classificacao):
    resultados_ida, resultados_volta = simular_playoff(classificacao)
    vencedores = []


    confrontos_playoffs = [(time1, time2) for (time1, time2), _ in resultados_ida.items()]
    max_len_time = max(len(time1) + len(time2) for time1, time2 in confrontos_playoffs)
    if max_len_time % 2 == 0:
        max_len_time += 1
    tamanho_linha = max_len_time + 28  
    metade = (tamanho_linha - 13) // 2
    print("\n")
    print("\nPlacar Agregado - Playoffs:")
    print("\n")
    print("┌" + "─" * tamanho_linha + "┐")
    print("├" + "─" * tamanho_linha + "┤")

    for (time1, time2), (gols_ida1, gols_ida2) in resultados_ida.items():
        gols_volta2, gols_volta1 = resultados_volta[(time2, time1)]  
        total_time1 = gols_ida1 + gols_volta1
        total_time2 = gols_ida2 + gols_volta2

        print("| {:>{}} | {:<5} | {:<{}} |".format(time1, metade, f"{total_time1} x {total_time2}", time2, metade))

        if total_time1 == total_time2:
            gols_penaltis1, gols_penaltis2 = simular_penaltis(time1, time2)
            print("| {:>{}}  {:^5}  {:<{}} |".format("Pen", metade, f"({gols_penaltis1} - {gols_penaltis2})", "", metade))
            vencedor = time1 if gols_penaltis1 > gols_penaltis2 else time2
            vencedores.append(vencedor)
        else:
            vencedor = time1 if total_time1 > total_time2 else time2
            vencedores.append(vencedor)

    print("└" + "─" * tamanho_linha + "┘")

    print("\nVencedores dos Playoffs:\n")
    for vencedor in vencedores:
        print("{:<16}".format(vencedor)) 

    return vencedores










def exibir_oitavas(classificacao, vencedores):

    primeiros_colocados = sorted(classificacao.items(), key=lambda x: (x[1]['pontos'], x[1]['saldo_gols'], x[1]['gols_marcados']), reverse=True)[:8]

    print("\nConfrontos das Oitavas de Final:")
    print("\n")

    confrontos_oitavas = [
        (primeiros_colocados[0][0], vencedores[0]),  
        (primeiros_colocados[1][0], vencedores[1]),  
        (primeiros_colocados[2][0], vencedores[2]),  
        (primeiros_colocados[3][0], vencedores[3]),  
        (primeiros_colocados[4][0], vencedores[4]),  
        (primeiros_colocados[5][0], vencedores[5]),  
        (primeiros_colocados[6][0], vencedores[6]),  
        (primeiros_colocados[7][0], vencedores[7]),  
    ]

    max_len_time = max(len(time1) + len(time2) for time1, time2 in confrontos_oitavas)
    if max_len_time % 2 == 0:
        max_len_time += 1
    tamanho_linha = max_len_time + 28  
    metade = (tamanho_linha - 5) // 2


    print("┌" + "─" * tamanho_linha + "┐")
    print("├" + "─" * tamanho_linha + "┤")

    for time1, time2 in confrontos_oitavas:
        print("| {:>{}} x {:<{}} |".format(time1, metade, time2, metade))

    print("└" + "─" * tamanho_linha + "┘")




def simular_oitavas(classificacao, vencedores):
    global maiores_goleadas_mata_mata  


    primeiros_colocados = sorted(classificacao.items(), key=lambda x: (x[1]['pontos'], x[1]['saldo_gols'], x[1]['gols_marcados']), reverse=True)


    confrontos_oitavas = [
        (primeiros_colocados[0][0], vencedores[0]),  
        (primeiros_colocados[1][0], vencedores[1]),  
        (primeiros_colocados[2][0], vencedores[2]),  
        (primeiros_colocados[3][0], vencedores[3]),  
        (primeiros_colocados[4][0], vencedores[4]),  
        (primeiros_colocados[5][0], vencedores[5]),  
        (primeiros_colocados[6][0], vencedores[6]),  
        (primeiros_colocados[7][0], vencedores[7]),  
    ]

    max_len_time = max(len(time1) + len(time2) for time1, time2 in confrontos_oitavas)
    if max_len_time % 2 == 0:
        max_len_time += 1
    tamanho_linha = max_len_time + 28  
    metade = (tamanho_linha - 13) //2 

    resultados_ida = {}
    print("\nJogo de ida - Oitavas de Final:")
    print("\n")
    print("┌" + "─" * tamanho_linha + "┐")
    print("| {:^{}} | {:^1} x {:^1} | {:^{}} |".format("Casa", metade, "", "", "Fora", metade))
    print("├" + "─" * tamanho_linha + "┤")
    for time1, time2 in confrontos_oitavas:

        gols_time1, gols_time2 = gerar_gols(time1, time2)


        resultados_ida[(time1, time2)] = (gols_time1, gols_time2)


        atualizar_gols_acumulados_json(time1, gols_time1, gols_time2)
        atualizar_gols_acumulados_json(time2, gols_time2, gols_time1)
        atualizar_partidas_jogadas(time1)
        atualizar_partidas_jogadas(time2)
        if gols_time1 > gols_time2:
            atualizar_vitoria(time1)
            atualizar_derrota(time2)
        elif gols_time2 > gols_time1:
            atualizar_vitoria(time2)
            atualizar_derrota(time1)
        else:
            atualizar_empate(time1)
            atualizar_empate(time2)
        salvar_resultados_json(time1, gols_time1, time2, gols_time2, "oitavas")

        print("| {:>{}} | {:<1} x {:<1} | {:<{}} |".format(time1, metade, gols_time1, gols_time2, time2, metade))


        diferenca_gols = abs(gols_time1 - gols_time2)
        if len(maiores_goleadas_mata_mata) == 0 or diferenca_gols > maiores_goleadas_mata_mata[0]['diferenca']:
            maiores_goleadas_mata_mata = [{
                "time1": time1,
                "gols_time1": gols_time1,
                "time2": time2,
                "gols_time2": gols_time2,
                "diferenca": diferenca_gols
            }]
        elif diferenca_gols == maiores_goleadas_mata_mata[0]['diferenca']:
            maiores_goleadas_mata_mata.append({
                "time1": time1,
                "gols_time1": gols_time1,
                "time2": time2,
                "gols_time2": gols_time2,
                "diferenca": diferenca_gols
            })
    print("└" + "─" * tamanho_linha + "┘")

    resultados_volta = {}
    print("\n")
    print("\nJogo de volta - Oitavas de Final:")
    print("\n")
    print("┌" + "─" * tamanho_linha + "┐")
    print("| {:^{}} | {:^1} x {:^1} | {:^{}} |".format("Casa", metade, "", "", "Fora", metade))
    print("├" + "─" * tamanho_linha + "┤")
    for time2, time1 in confrontos_oitavas:

        gols_time1, gols_time2 = gerar_gols(time1, time2)


        resultados_volta[(time1, time2)] = (gols_time1, gols_time2)


        atualizar_gols_acumulados_json(time1, gols_time1, gols_time2)
        atualizar_gols_acumulados_json(time2, gols_time2, gols_time1)
        atualizar_partidas_jogadas(time1)
        atualizar_partidas_jogadas(time2)
        if gols_time1 > gols_time2:
            atualizar_vitoria(time1)
            atualizar_derrota(time2)
        elif gols_time2 > gols_time1:
            atualizar_vitoria(time2)
            atualizar_derrota(time1)
        else:
            atualizar_empate(time1)
            atualizar_empate(time2)       
        salvar_resultados_json(time1, gols_time1, time2, gols_time2, "oitavas")


        print("| {:>{}} | {:<1} x {:<1} | {:<{}} |".format(time1, metade, gols_time1, gols_time2, time2, metade))


        diferenca_gols = abs(gols_time1 - gols_time2)
        if len(maiores_goleadas_mata_mata) == 0 or diferenca_gols > maiores_goleadas_mata_mata[0]['diferenca']:
            maiores_goleadas_mata_mata = [{
                "time1": time1,
                "gols_time1": gols_time1,
                "time2": time2,
                "gols_time2": gols_time2,
                "diferenca": diferenca_gols
            }]
        elif diferenca_gols == maiores_goleadas_mata_mata[0]['diferenca']:
            maiores_goleadas_mata_mata.append({
                "time1": time1,
                "gols_time1": gols_time1,
                "time2": time2,
                "gols_time2": gols_time2,
                "diferenca": diferenca_gols
            })

    print("└" + "─" * tamanho_linha + "┘")
    return resultados_ida, resultados_volta



def placar_final_oitavas(classificacao, vencedores):
    resultados_ida, resultados_volta = simular_oitavas(classificacao, vencedores)
    vencedores_oitavas = []
    confrontos_oitavas = [(time1, time2) for (time1, time2), _ in resultados_ida.items()]
    max_len_time = max(len(time1) + len(time2) for time1, time2 in confrontos_oitavas)
    if max_len_time % 2 == 0:
        max_len_time += 1
    tamanho_linha = max_len_time + 28  
    metade = (tamanho_linha - 13) // 2
    print("\n")
    print("\nPlacar Agregado - Oitavas de Final:")
    print("\n")
    print("┌" + "─" * tamanho_linha + "┐")
    print("├" + "─" * tamanho_linha + "┤")


    for (time1, time2), (gols_ida1, gols_ida2) in resultados_ida.items():
        gols_volta2, gols_volta1 = resultados_volta[(time2, time1)]  
        total_time1 = gols_ida1 + gols_volta1
        total_time2 = gols_ida2 + gols_volta2
        print("| {:>{}} | {:<5} | {:<{}} |".format(time1, metade, f"{total_time1} x {total_time2}", time2, metade))

        if total_time1 == total_time2:
            gols_penaltis1, gols_penaltis2 = simular_penaltis(time1, time2)
            print("| {:>{}}  {:^5}  {:<{}} |".format("Pen", metade, f"({gols_penaltis1} - {gols_penaltis2})", "", metade))
            vencedor_oitavas = time1 if gols_penaltis1 > gols_penaltis2 else time2
            vencedores_oitavas.append(vencedor_oitavas)
        else:
            vencedor_oitavas = time1 if total_time1 > total_time2 else time2
            vencedores_oitavas.append(vencedor_oitavas)

    print("└" + "─" * tamanho_linha + "┘")

    print("\nVencedores das oitavas:\n")
    for vencedor_oitavas in vencedores_oitavas:
        print("{:<16}".format(vencedor_oitavas)) 
    return vencedores_oitavas





def sortear_quartas(vencedores_oitavas):

    random.shuffle(vencedores_oitavas)


    quartas_de_final = [(vencedores_oitavas[i], vencedores_oitavas[i + 1]) for i in range(0, len(vencedores_oitavas), 2)]

    return quartas_de_final

def exibir_confrontos_quartas(quartas_de_final):
    print("\nConfrontos das Quartas de Final:")
    print("\n")
    max_len_time = max(len(time1) + len(time2) for time1, time2 in quartas_de_final)
    tamanho_linha = max_len_time + 28
    if tamanho_linha % 2 == 0:
        tamanho_linha += 1
    metade = (tamanho_linha - 5) // 2


    print("┌" + "─" * tamanho_linha + "┐")
    print("├" + "─" * tamanho_linha + "┤")

    for time1, time2 in quartas_de_final:
        print("| {:>{}} x {:<{}} |".format(time1, metade, time2, metade))

    print("└" + "─" * tamanho_linha + "┘")



def simular_quartas(quartas_de_final):
    global maiores_goleadas_mata_mata  

    max_len_time = max(len(time1) + len(time2) for time1, time2 in quartas_de_final)
    if max_len_time % 2 == 0:
        max_len_time += 1
    tamanho_linha = max_len_time + 28  
    metade = (tamanho_linha - 13) // 2

    resultados_ida = {}
    print("\nJogo de ida - Quartas de Final:")
    print("\n")
    print("┌" + "─" * tamanho_linha + "┐")
    print("| {:^{}} | {:^1} x {:^1} | {:^{}} |".format("Casa", metade, "", "", "Fora", metade))
    print("├" + "─" * tamanho_linha + "┤")


    for time1, time2 in quartas_de_final:
        gols_time1, gols_time2 = gerar_gols(time1, time2)


        resultados_ida[(time1, time2)] = (gols_time1, gols_time2)


        atualizar_gols_acumulados_json(time1, gols_time1, gols_time2)  
        atualizar_gols_acumulados_json(time2, gols_time2, gols_time1)  
        atualizar_partidas_jogadas(time1)
        atualizar_partidas_jogadas(time2)
        if gols_time1 > gols_time2:
            atualizar_vitoria(time1)
            atualizar_derrota(time2)
        elif gols_time2 > gols_time1:
            atualizar_vitoria(time2)
            atualizar_derrota(time1)
        else:
            atualizar_empate(time1)
            atualizar_empate(time2)
        salvar_resultados_json(time1, gols_time1, time2, gols_time2, "quartas")

        print("| {:>{}} | {:<1} x {:<1} | {:<{}} |".format(time1, metade, gols_time1, gols_time2, time2, metade))

        diferenca_gols = abs(gols_time1 - gols_time2)
        if diferenca_gols > 0:
            maior_goleada = {
                'time1': time1,
                'gols_time1': gols_time1,
                'time2': time2,
                'gols_time2': gols_time2,
                'diferenca': diferenca_gols
            }
            if not maiores_goleadas_mata_mata or diferenca_gols > maiores_goleadas_mata_mata[0]['diferenca']:
                maiores_goleadas_mata_mata = [maior_goleada]
            elif diferenca_gols == maiores_goleadas_mata_mata[0]['diferenca']:
                maiores_goleadas_mata_mata.append(maior_goleada)

    print("└" + "─" * tamanho_linha + "┘")

    resultados_volta = {}
    print("\n")
    print("\nJogo de volta - Quartas de Final:")
    print("\n")
    print("┌" + "─" * tamanho_linha + "┐")
    print("| {:^{}} | {:^1} x {:^1} | {:^{}} |".format("Casa", metade, "", "", "Fora", metade))
    print("├" + "─" * tamanho_linha + "┤")


    for time2, time1 in quartas_de_final:
        gols_time1, gols_time2 = gerar_gols(time1, time2)


        resultados_volta[(time1, time2)] = (gols_time1, gols_time2)


        atualizar_gols_acumulados_json(time1, gols_time1, gols_time2)  
        atualizar_gols_acumulados_json(time2, gols_time2, gols_time1)  
        atualizar_partidas_jogadas(time1)
        atualizar_partidas_jogadas(time2)
        if gols_time1 > gols_time2:
            atualizar_vitoria(time1)
            atualizar_derrota(time2)
        elif gols_time2 > gols_time1:
            atualizar_vitoria(time2)
            atualizar_derrota(time1)
        else:
            atualizar_empate(time1)
            atualizar_empate(time2)
        salvar_resultados_json(time1, gols_time1, time2, gols_time2, "quartas")

        print("| {:>{}} | {:<1} x {:<1} | {:<{}} |".format(time1, metade, gols_time1, gols_time2, time2, metade))

        diferenca_gols = abs(gols_time1 - gols_time2)
        if diferenca_gols > 0:
            maior_goleada = {
                'time1': time1,
                'gols_time1': gols_time1,
                'time2': time2,
                'gols_time2': gols_time2,
                'diferenca': diferenca_gols
            }
            if not maiores_goleadas_mata_mata or diferenca_gols > maiores_goleadas_mata_mata[0]['diferenca']:
                maiores_goleadas_mata_mata = [maior_goleada]
            elif diferenca_gols == maiores_goleadas_mata_mata[0]['diferenca']:
                maiores_goleadas_mata_mata.append(maior_goleada)

    print("└" + "─" * tamanho_linha + "┘")

    return resultados_ida, resultados_volta




def placar_final_quartas(quartas_de_final):
    resultados_ida, resultados_volta = simular_quartas(quartas_de_final)
    vencedores_quartas = []
    confrontos_quartas = [(time1, time2) for (time1, time2), _ in resultados_ida.items()]
    max_len_time = max(len(time1) + len(time2) for time1, time2 in confrontos_quartas)
    if max_len_time % 2 == 0:
        max_len_time += 1
    tamanho_linha = max_len_time + 28  
    metade = (tamanho_linha - 13) // 2
    print("\n")
    print("\nPlacar Agregado - Quartas de Final:")
    print("\n")
    print("┌" + "─" * tamanho_linha + "┐")
    print("├" + "─" * tamanho_linha + "┤")



    for (time1, time2), (gols_ida1, gols_ida2) in resultados_ida.items():
        gols_volta2, gols_volta1 = resultados_volta[(time2, time1)]  
        total_time1 = gols_ida1 + gols_volta1
        total_time2 = gols_ida2 + gols_volta2
        print("| {:>{}} | {:<5} | {:<{}} |".format(time1, metade, f"{total_time1} x {total_time2}", time2, metade))


        if total_time1 == total_time2:
            gols_penaltis1, gols_penaltis2 = simular_penaltis(time1, time2)
            print("| {:>{}}  {:^5}  {:<{}} |".format("Pen", metade, f"({gols_penaltis1} - {gols_penaltis2})", "", metade))
            vencedor_quartas = time1 if gols_penaltis1 > gols_penaltis2 else time2
            vencedores_quartas.append(vencedor_quartas)
        else:
            vencedor_quartas = time1 if total_time1 > total_time2 else time2
            vencedores_quartas.append(vencedor_quartas)

    print("└" + "─" * tamanho_linha + "┘")


    print("\nVencedores das Quartas de Final:\n")
    for vencedor_quartas in vencedores_quartas:
        print("{:<16}".format(vencedor_quartas)) 
    return vencedores_quartas


def exibir_semi_final(vencedores_quartas):
    print("\nConfrontos das Semifinais:")
    print("\n")    
    confrontos_semis = [(vencedores_quartas[i], vencedores_quartas[i + 1]) for i in range(0, len(vencedores_quartas), 2)]
    max_len_time = max(len(time1) + len(time2) for time1, time2 in confrontos_semis)
    if max_len_time % 2 == 0:
        max_len_time += 1
    tamanho_linha = max_len_time + 28  
    metade = (tamanho_linha - 5) // 2

    print("┌" + "─" * tamanho_linha + "┐")
    print("├" + "─" * tamanho_linha + "┤")


    print("| {:>{}} x {:<{}} |".format(vencedores_quartas[0], metade, vencedores_quartas[1], metade))


    print("| {:>{}} x {:<{}} |".format(vencedores_quartas[2], metade, vencedores_quartas[3], metade))

    print("└" + "─" * tamanho_linha + "┘")



def simular_semifinais(vencedores_quartas):
    global maiores_goleadas_mata_mata  


    confrontos_semis = [(vencedores_quartas[i], vencedores_quartas[i + 1]) for i in range(0, len(vencedores_quartas), 2)]
    max_len_time = max(len(time1) + len(time2) for time1, time2 in confrontos_semis)
    if max_len_time % 2 == 0:
        max_len_time += 1
    tamanho_linha = max_len_time + 28  
    metade = (tamanho_linha - 13) // 2

    resultados_ida = {}
    resultados_volta = {}


    print("\nJogos de ida - Semi-final:")
    print("\n")
    print("┌" + "─" * tamanho_linha + "┐")
    print("| {:^{}} | {:^1} x {:^1} | {:^{}} |".format("Casa", metade, "", "", "Fora", metade))
    print("├" + "─" * tamanho_linha + "┤")

    for i in range(0, len(vencedores_quartas), 2):  
        time1 = vencedores_quartas[i]
        time2 = vencedores_quartas[i + 1]
        gols_time1, gols_time2 = gerar_gols(time1, time2)


        resultados_ida[(time1, time2)] = (gols_time1, gols_time2)


        atualizar_gols_acumulados_json(time1, gols_time1, gols_time2)
        atualizar_gols_acumulados_json(time2, gols_time2, gols_time1)
        atualizar_partidas_jogadas(time1)
        atualizar_partidas_jogadas(time2)
        if gols_time1 > gols_time2:
            atualizar_vitoria(time1)
            atualizar_derrota(time2)
        elif gols_time2 > gols_time1:
            atualizar_vitoria(time2)
            atualizar_derrota(time1)
        else:
            atualizar_empate(time1)
            atualizar_empate(time2)
        salvar_resultados_json(time1, gols_time1, time2, gols_time2, "semis")


        print("| {:>{}} | {:<1} x {:<1} | {:<{}} |".format(time1, metade, gols_time1, gols_time2, time2, metade))


        diferenca_gols = abs(gols_time1 - gols_time2)
        if diferenca_gols > 0:
            maior_goleada = {
                'time1': time1,
                'gols_time1': gols_time1,
                'time2': time2,
                'gols_time2': gols_time2,
                'diferenca': diferenca_gols
            }
            if not maiores_goleadas_mata_mata or diferenca_gols > maiores_goleadas_mata_mata[0]['diferenca']:
                maiores_goleadas_mata_mata = [maior_goleada]
            elif diferenca_gols == maiores_goleadas_mata_mata[0]['diferenca']:
                maiores_goleadas_mata_mata.append(maior_goleada)

    print("└" + "─" * tamanho_linha + "┘")


    print("\n")
    print("\nJogos de volta - Semi-Final:")
    print("\n")
    print("┌" + "─" * tamanho_linha + "┐")
    print("| {:^{}} | {:^1} x {:^1} | {:^{}} |".format("Casa", metade, "", "", "Fora", metade))
    print("├" + "─" * tamanho_linha + "┤")

    for i in range(0, len(vencedores_quartas), 2):
        time1 = vencedores_quartas[i]
        time2 = vencedores_quartas[i + 1]
        gols_time2, gols_time1 = gerar_gols(time2, time1)

        resultados_volta[(time2, time1)] = (gols_time2, gols_time1)

        atualizar_gols_acumulados_json(time1, gols_time1, gols_time2)
        atualizar_gols_acumulados_json(time2, gols_time2, gols_time1)
        atualizar_partidas_jogadas(time1)
        atualizar_partidas_jogadas(time2)
        if gols_time1 > gols_time2:
            atualizar_vitoria(time1)
            atualizar_derrota(time2)
        elif gols_time2 > gols_time1:
            atualizar_vitoria(time2)
            atualizar_derrota(time1)
        else:
            atualizar_empate(time1)
            atualizar_empate(time2)
        salvar_resultados_json(time2, gols_time2, time1, gols_time1, "semis")

        print("| {:>{}} | {:<1} x {:<1} | {:<{}} |".format(time2, metade, gols_time2, gols_time1, time1, metade))

        diferenca_gols = abs(gols_time1 - gols_time2)
        if diferenca_gols > 0:
            maior_goleada = {
                'time1': time1,
                'gols_time1': gols_time1,
                'time2': time2,
                'gols_time2': gols_time2,
                'diferenca': diferenca_gols
            }
            if not maiores_goleadas_mata_mata or diferenca_gols > maiores_goleadas_mata_mata[0]['diferenca']:
                maiores_goleadas_mata_mata = [maior_goleada]
            elif diferenca_gols == maiores_goleadas_mata_mata[0]['diferenca']:
                maiores_goleadas_mata_mata.append(maior_goleada)

    print("└" + "─" * tamanho_linha + "┘")
    return resultados_ida, resultados_volta




def placar_final_semis(vencedores_quartas):
    resultados_ida, resultados_volta = simular_semifinais(vencedores_quartas)
    vencedores_semis = []
    confrontos_semis = [(time1, time2) for (time1, time2), _ in resultados_ida.items()]
    max_len_time = max(len(time1) + len(time2) for time1, time2 in confrontos_semis)
    if max_len_time % 2 == 0:
        max_len_time += 1
    tamanho_linha = max_len_time + 28  
    metade = (tamanho_linha - 13) // 2
    print("\n")
    print("\nPlacar Agregado - Semifinais:")
    print("\n")
    print("┌" + "─" * tamanho_linha + "┐")
    print("├" + "─" * tamanho_linha + "┤")



    for (time1, time2), (gols_ida1, gols_ida2) in resultados_ida.items():
        gols_volta2, gols_volta1 = resultados_volta[(time2, time1)]  
        total_time1 = gols_ida1 + gols_volta1
        total_time2 = gols_ida2 + gols_volta2
        print("| {:>{}} | {:<5} | {:<{}} |".format(time1, metade, f"{total_time1} x {total_time2}", time2, metade))


        if total_time1 == total_time2:
            gols_penaltis1, gols_penaltis2 = simular_penaltis(time1, time2)
            print("| {:>{}}  {:^5}  {:<{}} |".format("Pen", metade, f"({gols_penaltis1} - {gols_penaltis2})", "", metade))
            vencedor_semis = time1 if gols_penaltis1 > gols_penaltis2 else time2
            vencedores_semis.append(vencedor_semis)
        else:
            vencedor_semis = time1 if total_time1 > total_time2 else time2
            vencedores_semis.append(vencedor_semis)

    print("└" + "─" * tamanho_linha + "┘")


    print("\n")
    print("\nVencedores das semifinais:\n")
    print("\n")
    for vencedor_semis in vencedores_semis:
        print("{:<16}".format(vencedor_semis))
    return vencedores_semis






def exibir_final(vencedores_semis):
    print("\n")
    print("\nFinal:\n")
    print("\n")

    max_len_time = max(len(vencedores_semis[0]), len(vencedores_semis[1]))
    if max_len_time % 2 == 0:
        max_len_time += 1
    tamanho_linha = max_len_time + 28  
    metade = (tamanho_linha - 5) // 2
    print("┌" + "─" * tamanho_linha + "┐")
    print("├" + "─" * tamanho_linha + "┤")

    print("| {:>{}} x {:<{}} |".format(vencedores_semis[0], metade, vencedores_semis[1], metade))
    print("└" + "─" * tamanho_linha + "┘")


def simular_final(vencedores_semis):
    resultado = {}

    time1 = vencedores_semis[0]
    time2 = vencedores_semis[1]


    gols_time1, gols_time2 = gerar_gols_sem_fator_casa(time1, time2)
    resultado[(time1, time2)] = (gols_time1, gols_time2)

    return resultado


def placar_final_final(vencedores_semis):
    global maiores_goleadas_mata_mata
    resultado = simular_final(vencedores_semis)
    vencedor_final = []
    vice_final = []
    gols_vencedor = ""
    gols_vice = ""


    confronto = [(time1, time2) for (time1, time2), _ in resultado.items()]
    max_len_time = max(len(time1) + len(time2) + 3 for time1, time2 in confronto)  

    if max_len_time % 2 == 0:
        max_len_time += 1


    tamanho_linha = max_len_time + 28  
    metade = (tamanho_linha - 13) // 2 

    print("\nResultado Final:\n")
    print("\n")
    print("┌" + "─" * tamanho_linha + "┐")
    print("├" + "─" * tamanho_linha + "┤")


    for (time1, time2), (gols_time1, gols_time2) in resultado.items():
        atualizar_gols_acumulados_json(time1, gols_time1, gols_time2)
        atualizar_gols_acumulados_json(time2, gols_time2, gols_time1)
        atualizar_partidas_jogadas(time1)
        atualizar_partidas_jogadas(time2)


        if gols_time1 > gols_time2:
            atualizar_vitoria(time1)
            atualizar_derrota(time2)
        elif gols_time2 > gols_time1:
            atualizar_vitoria(time2)
            atualizar_derrota(time1)
        else:
            atualizar_empate(time1)
            atualizar_empate(time2)

        salvar_resultados_json(time1, gols_time1, time2, gols_time2, "final")
        print("| {:>{}} | {:<1} x {:<1} | {:<{}} |".format(time1, metade, gols_time1, gols_time2, time2, metade))


        diferenca_gols = abs(gols_time1 - gols_time2)
        if diferenca_gols > 0:
            maior_goleada = {
                'time1': time1,
                'gols_time1': gols_time1,
                'time2': time2,
                'gols_time2': gols_time2,
                'diferenca': diferenca_gols
            }
            if not maiores_goleadas_mata_mata or diferenca_gols > maiores_goleadas_mata_mata[0]['diferenca']:
                maiores_goleadas_mata_mata = [maior_goleada]
            elif diferenca_gols == maiores_goleadas_mata_mata[0]['diferenca']:
                maiores_goleadas_mata_mata.append(maior_goleada)


        if gols_time1 == gols_time2:
            gols_penaltis1, gols_penaltis2 = simular_penaltis(time1, time2)
            print("| {:>{}}  {:^5}  {:<{}} |".format("Pen", metade, f"({gols_penaltis1} - {gols_penaltis2})", "", metade))

            if gols_penaltis1 > gols_penaltis2:
                vencedor = time1
                vice = time2
                gols_vencedor = f"{gols_time1} ({gols_penaltis1} PEN)"
                gols_vice = f"{gols_time2} ({gols_penaltis2} PEN)"
            else:
                vencedor = time2
                vice = time1
                gols_vencedor = f"{gols_time2} ({gols_penaltis2} PEN)"
                gols_vice = f"{gols_time1} ({gols_penaltis1} PEN)"
        else:
            vencedor = time1 if gols_time1 > gols_time2 else time2
            vice = time2 if vencedor == time1 else time1
            gols_vencedor = gols_time1 if vencedor == time1 else gols_time2
            gols_vice = gols_time2 if vencedor == time1 else gols_time1

        vencedor_final.append(vencedor)
        vice_final.append(vice)

    print("└" + "─" * tamanho_linha + "┘")

    if vencedor_final and vice_final:
        return vencedor_final[0], gols_vencedor, vice_final[0], gols_vice
    else:
        return None, None, None, None











def atualizar_classificacao(time_casa, gols_casa, time_fora, gols_fora, classificacao):
    if gols_casa > gols_fora:
        classificacao[time_casa]['pontos'] += 3
        classificacao[time_casa]['vitorias'] += 1
        classificacao[time_fora]['derrotas'] += 1  
    elif gols_casa < gols_fora:
        classificacao[time_fora]['pontos'] += 3
        classificacao[time_fora]['vitorias'] += 1
        classificacao[time_casa]['derrotas'] += 1  
    else:
        classificacao[time_casa]['pontos'] += 1
        classificacao[time_fora]['pontos'] += 1
        classificacao[time_casa]['empates'] += 1  
        classificacao[time_fora]['empates'] += 1 


    classificacao[time_casa]['gols_marcados'] += gols_casa
    classificacao[time_fora]['gols_marcados'] += gols_fora
    classificacao[time_casa]['gols_sofridos'] += gols_fora  
    classificacao[time_fora]['gols_sofridos'] += gols_casa  

    classificacao[time_casa]['saldo_gols'] = classificacao[time_casa]['gols_marcados'] - classificacao[time_casa]['gols_sofridos']
    classificacao[time_fora]['saldo_gols'] = classificacao[time_fora]['gols_marcados'] - classificacao[time_fora]['gols_sofridos']

def inicializar_classificacao(potes):
    classificacao = {}
    for pot in potes:
        for time in pot:
            classificacao[time] = {'pontos': 0, 'gols_marcados': 0, 'gols_sofridos': 0, 'vitorias': 0, 'derrotas': 0, 'empates': 0}
    return classificacao













def salvar_resultados_json(time_casa, gols_casa, time_fora, gols_fora, fase):

    try:
        with open('resultados_partidas_atual.json', 'r') as file:
            resultados = json.load(file)
    except FileNotFoundError:
        resultados = {}


    if time_casa not in resultados:
        resultados[time_casa] = {
            "jogos": []
        }

    if time_fora not in resultados:
        resultados[time_fora] = {
            "jogos": []
        }


    resultados[time_casa]["jogos"].append({
        "adversario": time_fora,
        "gols_marcados": gols_casa,
        "gols_sofridos": gols_fora,
        "fase": fase  
    })


    resultados[time_fora]["jogos"].append({
        "adversario": time_casa,
        "gols_marcados": gols_fora,
        "gols_sofridos": gols_casa,
        "fase": fase  
    })


    with open('resultados_partidas_atual.json', 'w') as file:
        json.dump(resultados, file, indent=4)




def transferir_para_historico():

    try:
        with open('resultados_partidas_atual.json', 'r') as file:
            resultados = json.load(file)
    except FileNotFoundError:
        print("Arquivo de resultados não encontrado.")
        return


    for time, dados in resultados.items():
        jogos_grupos = [jogo for jogo in dados["jogos"] if jogo["fase"].lower() == "grupos"]
        if len(jogos_grupos) > 8:
            print(f"Erro: Dados anormais detectados. Dados não salvos no histórico.")
            return


    try:
        with open('historico_resultados.json', 'r') as file:
            historico = json.load(file)
    except FileNotFoundError:
        historico = []


    simulacao_numero = len(historico) + 1


    nova_simulacao = {
        "simulacao": simulacao_numero,
        "resultados": resultados
    }


    historico.append(nova_simulacao)


    with open('historico_resultados.json', 'w') as file:
        json.dump(historico, file, indent=4)


    if os.path.exists('resultados_partidas_atual.json'):
        os.remove('resultados_partidas_atual.json')
    else:
        print("O arquivo do histórico não foi encontrado.")













def listar_simulacoes():

    if not all(os.path.exists(arquivo) for arquivo in ["campeoes.json", "historico_gols.json", "historico_resultados.json"]):
        print("\nArquivo(s) não encontrado(s).\n")
        return
    try:

        with open("campeoes.json", "r") as file:
            campeoes = json.load(file)
    except FileNotFoundError:
        campeoes = []

    if not campeoes:
        print("\n\nNenhuma simulação encontrada.\n\n")
        return


    sim_data = []
    for final in campeoes:
        simulacao = str(final.get("simulacao"))
        vencedor = final["campeao"]["time"]
        placar_vencedor = str(final["campeao"]["gols"])
        vice = final["vice"]["time"]
        placar_vice = str(final["vice"]["gols"])
        nivel = final.get("nivel_simulacao", "Desconhecido")
        sim_data.append(f"{simulacao}│ {vencedor}│ {placar_vencedor} x {placar_vice}│ {vice}│ {nivel}")

    if not sim_data:
        print("\n\nNenhuma simulação disponível para exibir.\n\n")
        return



    tamanho_linha = 97


    print(f"{'┌' + '─' * tamanho_linha + '┐'}")
    print(f"│{'Simulação'.ljust(10)}│{'Vencedor'.ljust(20)}│{'Placar'.ljust(21)}│{'Vice-Campeão'.ljust(18)}│{'Nível da Simulação'.ljust(24)}│")
    print(f"{'├' + '─' * tamanho_linha + '┤'}")

    for final in campeoes:
        simulacao = str(final.get("simulacao")).ljust(10)
        vencedor = final["campeao"]["time"].ljust(20)
        placar_vencedor = str(final["campeao"]["gols"])
        placar_vice = str(final["vice"]["gols"])
        placar = f"{placar_vencedor} x {placar_vice}".ljust(21)
        vice = final["vice"]["time"].ljust(18)
        nivel = final.get("nivel_simulacao", "Desconhecido").ljust(10)


        linha_formatada = f"│{simulacao}│{vencedor}│{placar}│{vice}│{nivel}              │"
        print(linha_formatada)


    print(f"{'└' + '─' * tamanho_linha + '┘'}")


def excluir_simulacao_por_numero(simulacao_numero):
    arquivos = ["campeoes.json", "historico_gols.json", "historico_resultados.json"]

    def remover_simulacao_arquivo(nome_arquivo):
        if os.path.exists(nome_arquivo):
            with open(nome_arquivo, 'r') as file:
                dados = json.load(file)

          
            dados_filtrados = [simulacao for simulacao in dados if simulacao.get("simulacao") != simulacao_numero]

           
            for i, simulacao in enumerate(dados_filtrados, start=1):
                simulacao["simulacao"] = i


            with open(nome_arquivo, 'w') as file:
                json.dump(dados_filtrados, file, indent=4)

    for arquivo in arquivos:
        remover_simulacao_arquivo(arquivo)

    print(f"\nSimulação {simulacao_numero} removida dos arquivos!\n")


def excluir_simulacao():
    if not all(os.path.exists(arquivo) for arquivo in ["campeoes.json", "historico_gols.json", "historico_resultados.json"]):
        print("\nArquivo(s) não encontrado(s).\n")
        return
    else:

        while True:

            listar_simulacoes()


            entrada = questionary.text("\n\nDigite o número da simulação que deseja excluir ou 'S' para voltar:\n\n").ask()


            if entrada.lower() == 's':
                print("\nVoltando...\n")
                return


            try:
                simulacao_numero = int(entrada)


                with open("campeoes.json", "r") as file:
                    campeoes = json.load(file)

                if simulacao_numero < 1 or simulacao_numero > len(campeoes):
                    print(f"\n\nSimulação {simulacao_numero} não existe. Tente novamente.\n\n")
                else:


                    confirmacao = questionary.select(
                        f"\nDeseja excluir a simulação {simulacao_numero}?\n\n".upper(),
                        choices=["Sim", "Não", "Voltar"], style=custom_style
                    ).ask()
                    if confirmacao == 'Sim':
                        excluir_simulacao_por_numero(simulacao_numero)
                    elif confirmacao == 'Não':
                        print("\n\nExclusão cancelada.\n\n")
                    elif confirmacao == 'Voltar':
                        continue

            except ValueError:

                print("\n\nEntrada inválida! Por favor, insira um número de simulação válido.\n\n")












def exibir_classificacao(classificacao):

    classificacao_ordenada = sorted(classificacao.items(), key=lambda x: (x[1]['pontos'], x[1]['saldo_gols'], x[1]['gols_marcados']), reverse=True)

    print("\nTabela de Classificação Final:")


    tamanho_linha = 90
    print("\n")

    print("|" + "─" * tamanho_linha + "|")
    print("┌" + "─" * tamanho_linha + "┐")  
    print("│" + "{:<4} | {:<20} | {:<6} | {:<6} | {:<6} | {:<6} | {:<6} | {:<6} | {:<6}".format("Pos", "Time", "Pts", "GM", "GS", "SG", "V", "E", "D") + "│")  
    print("├" + "─" * tamanho_linha + "┤")  

    for i, (time, dados) in enumerate(classificacao_ordenada, start=1):
        time = time.upper()

        if i <= 8:
            posicao_nome = f"\033[32m{i:<4} | {time:<20}\033[0m"

        elif 9 <= i <= 24:
            posicao_nome = f"\033[34m{i:<4} | {time:<20}\033[0m"

        else:
            posicao_nome = f"\033[31m{i:<4} | {time:<20}\033[0m"


        linha = f"{posicao_nome} | {dados['pontos']:<6} | {dados['gols_marcados']:<6} | {dados['gols_sofridos']:<6} | {dados['saldo_gols']:<6} | {dados['vitorias']:<6} | {dados['empates']:<6} | {dados['derrotas']:<6}"
        print("│" + linha + "│")
        print("├" + "─" * tamanho_linha + "┤")  

    print("└" + "─" * tamanho_linha + "┘")  
    print("\n")
    print(f"\033[32m●\033[0m - Classificados para oitavas\n")
    print(f"\033[34m●\033[0m - Classificados para playoffs\n")
    print(f"\033[31m●\033[0m - Eliminados\n")






def exibir_primeiros_confrontos(home_away):

    max_len_time = max(len(time.upper()) + len(adversario.upper()) for time in home_away for adversario in home_away[time]["home"] + home_away[time]["away"])


    if max_len_time % 2 == 0:
        max_len_time += 1
    tamanho_linha = max_len_time + 28  
    metade = (tamanho_linha - 5) // 2  

    confrontos_partidas = []

    for time in sorted(home_away.keys()):
        espacos_finais = 1 if len(time.upper()) % 2 == 0 else 0

        linha_superior_time = "┌" + "─" * tamanho_linha + "┐"  
        resultado_time = f"|{' ' * ((tamanho_linha - len(time.upper())) // 2)}\033[32m{time.upper()}\033[0m{' ' * ((tamanho_linha - len(time.upper())) // 2 + espacos_finais)}|"
        linha_inferior_time = "└" + "─" * tamanho_linha + "┘"  


        confrontos_partidas.append(f"\n\n\n{linha_superior_time}\n{resultado_time}\n{linha_inferior_time}")


        confrontos_partidas.append("┌" + "─" * tamanho_linha + "┐")  


        for adversario in home_away[time]["home"]:
            time1 = time.upper()
            time2 = adversario
            confronto_formatado = f"| {time1:>{metade}}  x  {time2:<{metade-2}} |"
            confrontos_partidas.append(confronto_formatado)

        for adversario in home_away[time]["away"]:
            time1 = adversario
            time2 = time.upper()
            confronto_formatado = f"| {time1:>{metade}}  x  {time2:<{metade-2}} |"
            confrontos_partidas.append(confronto_formatado)


        confrontos_partidas.append("└" + "─" * tamanho_linha + "┘")

    return confrontos_partidas






def delay(seconds):

    threading.Event().wait(seconds)


def simular_confrontos(home_away, resultados, classificacao):
    largura_total = 64  
    resultados_partidas = []

    print("\n")
    print("\nResultados das partidas:")
    print("\n")

    for time in sorted(home_away.keys()):

        espacos_antes_time = (largura_total - len(time.upper()) - 4) // 2  
        linha_superior_time = "┌" + "─" * (largura_total - 2) + "┐"  
        resultado_time = f"|{' ' * espacos_antes_time}\033[32m{time.upper()}\033[0m{' ' * (largura_total - 2 - len(time.upper()) - espacos_antes_time)}|"
        linha_inferior_time = "└" + "─" * (largura_total - 2) + "┘"  


        resultados_partidas.append(f"\n\n\n{linha_superior_time}\n{resultado_time}\n{linha_inferior_time}")


        linha_superior_partidas = "┌" + "─" * (largura_total - 2) + "┐"  
        linha_inferior_partidas = "└" + "─" * (largura_total - 2) + "┘"  
        resultados_partidas.append(linha_superior_partidas)


        for adversario in home_away[time]["home"]:
            resultado = simular_partida(time, adversario, resultados, classificacao)
            resultado = resultado.replace(time, time.upper())  
            espacos_antes_resultado = (largura_total - len(resultado) - 4) // 2  
            resultado_formatado = f"|{' ' * espacos_antes_resultado}{resultado}{' ' * (largura_total - 2 - len(resultado) - espacos_antes_resultado)}|"
            resultados_partidas.append(resultado_formatado)

        for adversario in home_away[time]["away"]:
            resultado = simular_partida(adversario, time, resultados, classificacao)
            resultado = resultado.replace(time, time.upper())  
            espacos_antes_resultado = (largura_total - len(resultado) - 4) // 2  
            resultado_formatado = f"|{' ' * espacos_antes_resultado}{resultado}{' ' * (largura_total - 2 - len(resultado) - espacos_antes_resultado)}|"
            resultados_partidas.append(resultado_formatado)


        resultados_partidas.append(linha_inferior_partidas)




        for linha in resultados_partidas:
            print(linha)


        delay(0.01)


        resultados_partidas = []


    return resultados_partidas


maiores_goleadas = []

def simular_partida(time_casa, time_fora, resultados, classificacao):
    global maiores_goleadas

    if (time_casa, time_fora) in resultados:
        return resultados[(time_casa, time_fora)]
    if (time_fora, time_casa) in resultados:
        return resultados[(time_fora, time_casa)]


    gols_casa, gols_fora = gerar_gols_sem_fator_casa(time_casa, time_fora)


    atualizar_classificacao(time_casa, gols_casa, time_fora, gols_fora, classificacao)


    atualizar_gols_acumulados_json(time_casa, gols_casa, gols_fora)  
    atualizar_gols_acumulados_json(time_fora, gols_fora, gols_casa)  
    atualizar_partidas_jogadas(time_casa)
    atualizar_partidas_jogadas(time_fora)


    if gols_casa > gols_fora:
        atualizar_vitoria(time_casa)
        atualizar_derrota(time_fora)
    elif gols_fora > gols_casa:
        atualizar_vitoria(time_fora)
        atualizar_derrota(time_casa)
    else:
        atualizar_empate(time_casa)
        atualizar_empate(time_fora)

    salvar_resultados_json(time_casa, gols_casa, time_fora, gols_fora, "grupos")

    resultado = "{:>20} {:<1} x {:<1} {:<20}".format(time_casa, gols_casa, gols_fora, time_fora)
    resultados[(time_casa, time_fora)] = resultado


    diferenca_gols = abs(gols_casa - gols_fora)


    if len(maiores_goleadas) == 0 or diferenca_gols > maiores_goleadas[0]['diferenca']:
        maiores_goleadas = [{
            "time1": time_casa,
            "gols_time1": gols_casa,
            "time2": time_fora,
            "gols_time2": gols_fora,
            "diferenca": diferenca_gols
        }]

    elif diferenca_gols == maiores_goleadas[0]['diferenca']:
        maiores_goleadas.append({
            "time1": time_casa,
            "gols_time1": gols_casa,
            "time2": time_fora,
            "gols_time2": gols_fora,
            "diferenca": diferenca_gols
        })

    return resultado










def print_trophy(vencedorFinal):

    amarelo = "\033[33m"  
    laranja = "\033[38;5;214m"  
    reset = "\033[0m"  

    print("\n")
    print("\n")
    print(f"""{amarelo}
             ___________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ){laranja}{vencedorFinal}{reset}´´´´
               _.' '._
          `"""""""`
    """)



def salvar_resultado_final(vencedor_final, gols_vencedor, vice_final, gols_vice):
    try:
        nome_arquivo = "campeoes.json"


        if os.path.exists(nome_arquivo):
            with open(nome_arquivo, 'r') as file:
                historico_finais = json.load(file)
        else:
            historico_finais = []


        numero_simulacao = len(historico_finais) + 1

        configuracao_atual = carregar_configuracao()
        nivel_gols_simulacao = configuracao_atual["nivel_gols"]


        final = {
            "simulacao": numero_simulacao,
            "nivel_simulacao": nivel_gols_simulacao,
            "campeao": {
                "time": vencedor_final,
                "gols": gols_vencedor
            },
            "vice": {
                "time": vice_final,
                "gols": gols_vice
            }
        }

        historico_finais.append(final)


        with open(nome_arquivo, 'w') as file:
            json.dump(historico_finais, file, indent=4)

    except Exception as e:
        print(f"Erro ao salvar o resultado final: {e}")





def exibir_finais():
    nome_arquivo = "campeoes.json"
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r') as file:
            historico_finais = json.load(file)
            print("\nHistórico de Finais:")
            print("\n")
            print(f"{'Nº'.ljust(4)}│ {'Campeão'.ljust(20)}│ {'Gols Campeão'.ljust(15)}│ {'Vice'.ljust(20)}│ {'Gols Vice'.ljust(15)}")
            print("─" * 80)

            for i, final in enumerate(historico_finais, start=1):
                campeao = final['campeao']['time'].upper()
                gols_campeao = final['campeao']['gols']
                vice = final['vice']['time']
                gols_vice = final['vice']['gols']

                print(f"{str(i).ljust(4)}│ {campeao.ljust(20)}│ {str(gols_campeao).ljust(15)}│ {vice.ljust(20)}│ {str(gols_vice).ljust(15)}")
    else:
        print("Nenhum campeão registrado ainda.")


def contar_campeoes():
    nome_arquivo = "campeoes.json"
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r') as file:
            historico_finais = json.load(file)


            contador_titulos = {}


            for final in historico_finais:
                campeao = final['campeao']['time']


                if campeao in contador_titulos:
                    contador_titulos[campeao] += 1
                else:

                    contador_titulos[campeao] = 1

            return contador_titulos
    else:
        return {}

def listar_campeoes_ordenados():

    campeoes = contar_campeoes()

    if campeoes:

        total_simulacoes = sum(campeoes.values())


        campeoes_ordenados = sorted(campeoes.items(), key=lambda item: item[1], reverse=True)


        print(f"\nLista de campeões após {total_simulacoes} simulação(ões):")
        print("\n")
        print(f"{'Nº'.ljust(4)}│ {'Time'.ljust(30)}│ {'Títulos'.ljust(10)}")
        print("─" * 50)


        for i, (time, titulos) in enumerate(campeoes_ordenados, start=1):
            print(f"{str(i).ljust(4)}│ {time.ljust(30)}│ {str(titulos).ljust(10)}")
    else:
        print("\nNenhum campeão registrado ainda.")




def contar_vices():
    nome_arquivo = "campeoes.json"
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r') as file:
            historico_finais = json.load(file)


            contador_vices = {}


            for final in historico_finais:
                vice = final['vice']['time']


                if vice in contador_vices:
                    contador_vices[vice] += 1
                else:

                    contador_vices[vice] = 1

            return contador_vices
    else:
        return {}

def listar_vices_ordenados():

    vices = contar_vices()

    if vices:

        total_simulacoes = sum(vices.values())


        vices_ordenados = sorted(vices.items(), key=lambda item: item[1], reverse=True)


        print(f"\nLista de vice-campeões após {total_simulacoes} simulação(ões):")
        print("\n")
        print(f"{'Nº'.ljust(4)}│ {'Time'.ljust(30)}│ {'Vice-Campeonatos'.ljust(18)}")
        print("─" * 50)


        for i, (time, vices_count) in enumerate(vices_ordenados, start=1):
            print(f"{str(i).ljust(4)}│ {time.ljust(30)}│ {str(vices_count).ljust(18)}")
    else:
        print("\nNenhum vice-campeão registrado ainda.")





def verificar_time_no_historico(nome_time):
    """Verifica se o time existe no histórico de resultados."""

    nome_time = nome_time.lower()


    try:
        with open('historico_resultados.json', 'r') as file:
            historico = json.load(file)
    except FileNotFoundError:
        print("Arquivo de histórico não encontrado.")
        return False


    for simulacao in historico:
        resultados = simulacao['resultados']
        for time in resultados:

            if nome_time == time.lower():
                return True

    return False



nome_arquivo_campeoes = "campeoes.json"
nome_arquivo_historico_gols = "historico_gols.json"


def pesquisar_campeao_por_time(nome_time):
    contador_campeao = 0
    contador_vice = 0


    if not verificar_time_no_historico(nome_time):
        print(f"\nO time {nome_time.upper()} não existe nos registros.")
        return 0


    if os.path.exists(nome_arquivo_campeoes):
        with open(nome_arquivo_campeoes, 'r') as file:
            historico_finais = json.load(file)


            for final in historico_finais:
                campeao_time = final['campeao']['time'].lower()  
                vice_time = final['vice']['time'].lower()  


                if campeao_time == nome_time.lower():
                    contador_campeao += 1  



                if vice_time == nome_time.lower():
                    contador_vice += 1  


    historico_gols = carregar_historico_gols()
    gols_feitos = 0
    gols_sofridos = 0
    partidas_jogadas = 0
    participacoes = 0  
    vitorias = 0
    empates = 0
    derrotas = 0


    eliminacoes_por_fase = {
        "grupos": 0,
        "playoffs": 0,
        "oitavas": 0,
        "quartas": 0,
        "semis": 0,
    }


    nome_time_min = nome_time.lower()
    for simulacao in historico_gols:
        for time in simulacao['gols']:
            if time.lower() == nome_time_min:  
                gols_feitos += simulacao['gols'][time]
                gols_sofridos += simulacao['gols_sofridos'][time]
                partidas_jogadas += simulacao['partidas_jogadas'][time]
                participacoes += 1
                vitorias += simulacao.get('vitorias', {}).get(time, 0)
                empates += simulacao.get('empates', {}).get(time, 0)
                derrotas += simulacao.get('derrotas', {}).get(time, 0)
                break  


    eliminacoes_por_fase = {
        "grupos": 0,
        "playoffs": 0,
        "oitavas": 0,
        "quartas": 0,
        "semis": 0,
    }

    nome_time_min = nome_time.lower()  


    if not os.path.exists('historico_resultados.json'):
        print("\n")
        print("Sem informações salvas. O histórico pode estar com informações faltantes.")
        print("\n")
    else:
        try:
            with open('historico_resultados.json', 'r') as file:
                historico_resultados = json.load(file)


                if not historico_resultados:
                    print("Histórico vazio")
                else:
                    for simulacao in historico_resultados:

                        resultados = {time.lower(): jogos for time, jogos in simulacao['resultados'].items()}


                        if nome_time_min in resultados:
                            jogos = resultados[nome_time_min]['jogos']
                            ultima_fase = None

                            for jogo in jogos:
                                ultima_fase = jogo['fase']  


                            if ultima_fase == "grupos":
                                if "playoffs" not in [jogo['fase'] for jogo in jogos]:
                                    eliminacoes_por_fase["grupos"] += 1
                            elif ultima_fase == "playoffs":
                                if "oitavas" not in [jogo['fase'] for jogo in jogos]:
                                    eliminacoes_por_fase["playoffs"] += 1
                            elif ultima_fase == "oitavas":
                                if "quartas" not in [jogo['fase'] for jogo in jogos]:
                                    eliminacoes_por_fase["oitavas"] += 1
                            elif ultima_fase == "quartas":
                                if "semis" not in [jogo['fase'] for jogo in jogos]:
                                    eliminacoes_por_fase["quartas"] += 1
                            elif ultima_fase == "semis":
                                if "final" not in [jogo['fase'] for jogo in jogos]:
                                    eliminacoes_por_fase["semis"] += 1

        except json.JSONDecodeError:
            print("Erro ao ler o histórico. O arquivo pode estar corrompido.")



    media_gols_feitos = gols_feitos / partidas_jogadas if partidas_jogadas > 0 else 0
    media_gols_sofridos = gols_sofridos / partidas_jogadas if partidas_jogadas > 0 else 0




    if contador_campeao == 0 and contador_vice == 0:
        print(f"\n{'─' * 44}")
        print("\n")
        print(f"Time: {nome_time.upper()}")
        print(f"{'Participações:'.ljust(30)}{participacoes}\n")
        print(f"\nO time {nome_time.upper()} não chegou à nenhuma final.")
        print(f"\n{'─' * 44}")
    else:
        print(f"\n{'─' * 44}")
        print("\n")
        print(f"Time: {nome_time.upper()}")
        print(f"{'Participações:'.ljust(30)}{participacoes}\n")  
        print(f"{'Campeão:'.ljust(30)}{contador_campeao} vez(es)")
        print(f"{'Vice-campeão:'.ljust(30)}{contador_vice} vez(es)")
        print(f"{'─' * 44}")
    print("\n")

    print("Mais informações:")
    print("┌" + "─" * 44 + "┐")

    print(f"│ {'Gols Feitos:'.ljust(30)}{gols_feitos:<10}   │")
    print(f"│ {'Gols Sofridos:'.ljust(30)}{gols_sofridos:<10}   │")
    print(f"│ {'Partidas Jogadas:'.ljust(30)}{partidas_jogadas:<10}   │")
    print(f"│ {'Vitórias:'.ljust(30)}{vitorias:<10}   │")
    print(f"│ {'Empates:'.ljust(30)}{empates:<10}   │")
    print(f"│ {'Derrotas:'.ljust(30)}{derrotas:<10}   │")
    print("└" + "─" * 44 + "┘")


    print("┌" + "─" * 44 + "┐")
    print(f"│ {'Média de Gols Feitos:'.ljust(30)}{media_gols_feitos:.2f}         │")
    print(f"│ {'Média de Gols Sofridos:'.ljust(30)}{media_gols_sofridos:.2f}         │")
    print("└" + "─" * 44 + "┘\n")


    print("\nEliminações por fase:")
    print("┌" + "─" * 44 + "┐")
    for fase, eliminacoes in eliminacoes_por_fase.items():
        print(f"│ {fase.capitalize().ljust(30)} {eliminacoes:<10}  │")
    print("└" + "─" * 44 + "┘\n")

    return contador_campeao, contador_vice, gols_feitos, gols_sofridos, partidas_jogadas, participacoes, vitorias, empates, derrotas















def menu_principal():
    print("""  ____ _                           _                         
 / ___| |__   __ _ _ __ ___  _ __ (_) ___  _ __  ___         
| |   | '_ \ / _` | '_ ` _ \| '_ \| |/ _ \| '_ \/ __|        
| |___| | | | (_| | | | | | | |_) | | (_) | | | \__ \        
 \____|_| |_|\__,_|_| |_| |_| .__/|_|\___/|_| |_|___/        
| |    ___  __ _  __ _ _   _|_|__  |  _ \ _ __ __ ___      __
| |   / _ \/ _` |/ _` | | | |/ _ \ | | | | '__/ _` \ \ /\ / /
| |__|  __/ (_| | (_| | |_| |  __/ | |_| | | | (_| |\ V  V / 
|_____\___|\__,_|\__, |\__,_|\___| |____/|_|  \__,_| \_/\_/  
/ ___|(_)_ __ ___|___/ _| | __ _| |_ ___  _ __               
\___ \| | '_ ` _ \| | | | |/ _` | __/ _ \| '__|              
 ___) | | | | | | | |_| | | (_| | || (_) | |                 
|____/|_|_| |_| |_|\__,_|_|\__,_|\__\___/|_|        """) 
    print("\n")

    return





def carregar_configuracao():
    with open("configuracao_gols.json", "r") as file:
        configuracao = json.load(file)
    return configuracao


def salvar_configuracao(nivel_gols):
    configuracao = carregar_configuracao()
    configuracao["nivel_gols"] = nivel_gols
    with open("configuracao_gols.json", "w") as file:
        json.dump(configuracao, file, indent=4)


def configurar_nivel_gols():
    if not os.path.exists("configuracao_gols.json"):
        print("\n\nArquivo não encontrado.\n\n")
    else:
        config_atual = carregar_configuracao()

        print("\n")
        print("\n")
        print(f"Nível de gols atual: {config_atual['nivel_gols'].replace('_', ' ').upper()}")
        print("\n")


        escolha = questionary.select(
            "Escolha o nível da média de gols para as simulações:\n\n",
            choices=[
                "Média de gols baixa",
                "Média de gols média (recomendado)",
                "Média de gols alta",
                "Média de gols muito alta",
                "Exibir detalhes",
                "Voltar"
            ],
            style=custom_style
        ).ask()

        print("\n")


        if escolha == "Média de gols baixa":
            nivel_gols = "baixa"
        elif escolha == "Média de gols média (recomendado)":
            nivel_gols = "media"
        elif escolha == "Média de gols alta":
            nivel_gols = "alta"
        elif escolha == "Média de gols muito alta":
            nivel_gols = "muito_alta"
        elif escolha == 'Exibir detalhes':

            print("\n")
            print("Configurações disponíveis:")
            print("\n")
            for nivel, config in config_atual["configuracoes"].items():
                print(f"\nNível: {nivel.capitalize()}")
                print(f"  Média Base: {config['media_base']}")
                print(f"  Divisor da Média: {config['media_divisor']}")
                print(f"  Desvio Base: {config['desvio_base']}")
                print(f"  Divisor do Desvio: {config['desvio_divisor']}")
                print(f"  Soma: {config['soma']}")
                print("\n")


            return configurar_nivel_gols()

        elif escolha == "Voltar":
            print("\nVoltando ao menu anterior...\n")
            return  

        else:
            print("\n")
            print(f"Opção inválida. Usando configuração atual ({config_atual['nivel_gols']}).")
            print("\n")
            return configurar_nivel_gols()


        salvar_configuracao(nivel_gols)
        print("\n\n")
        print(f"Configuração do nível de gols ajustada para {nivel_gols.replace('_', ' ').upper()} com sucesso!")
        print("\n\n")




def criar_configuracao_padrao():
    configuracao_padrao = {
        "nivel_gols": "media",
        "configuracoes": {
            "baixa": {
                "media_base": 0.3,
                "media_divisor": 15,
                "desvio_base": 0.4,
                "desvio_divisor": 60,
                "soma": 1
            },
            "media": {
                "media_base": 0.5,
                "media_divisor": 10,
                "desvio_base": 0.5,
                "desvio_divisor": 50,
                "soma": 1.2
            },
            "alta": {
                "media_base": 0.7,
                "media_divisor": 10,
                "desvio_base": 0.6,
                "desvio_divisor": 40,
                "soma": 1.5
            },
            "muito_alta": {
                "media_base": 2.0,
                "media_divisor": 5,
                "desvio_base": 1.0,
                "desvio_divisor": 30,
                "soma": 1.8
            }
        }
    }

    with open("configuracao_gols.json", "w") as file:
        json.dump(configuracao_padrao, file, indent=4)







def buscar_partidas_por_time():

    try:
        with open('resultados_partidas_atual.json', 'r') as file:
            resultados = json.load(file)
    except FileNotFoundError:
        print("Arquivo de resultados não encontrado.")
        return


    nome_time = questionary.text("Digite o nome do time: "
    ).ask().strip()
    print("\n")



    resultados_normalizados = {time.lower(): partidas for time, partidas in resultados.items()}


    if nome_time not in resultados_normalizados:
        print(f"Time '{nome_time}' não encontrado.")
        return


    partidas_por_fase = {
        "grupos": [],
        "playoffs": [],
        "oitavas": [],
        "quartas": [],
        "semis": [],
        "final": []
    }


    for partida in resultados_normalizados[nome_time]["jogos"]:  
        fase = partida["fase"]
        adversario = partida["adversario"]
        gols_marcados = partida["gols_marcados"]
        gols_sofridos = partida["gols_sofridos"]


        resultado = "{:>20} {:<1} x {:<1} {:<20}".format(nome_time.capitalize(), gols_marcados, gols_sofridos, adversario)


        if fase in partidas_por_fase:
            partidas_por_fase[fase].append(resultado)
        else:
            print(f"Fase desconhecida: {fase}")


    print(f"\nPartidas jogadas pelo {nome_time.capitalize()}:\n")

    for fase, partidas in partidas_por_fase.items():
        if partidas:  

            max_len_time = max(len(nome_time), max(len(partida) for partida in partidas))
            if max_len_time % 2 == 0:
                max_len_time += 1
            tamanho_linha = max_len_time + 28  
            metade = (tamanho_linha - 5) // 2

            print(f"Fase {fase.capitalize()}:\n")
            print("┌" + "─" * tamanho_linha + "┐")
            print("├" + "─" * tamanho_linha + "┤")

            for partida in partidas:
                print("| {:^{}} |".format(partida, tamanho_linha - 2))  

            print("└" + "─" * tamanho_linha + "┘\n")  










def buscar_partidas_historico():
    while True:

        try:
            with open('historico_resultados.json', 'r') as file:
                historico = json.load(file)
        except FileNotFoundError:
            print("Arquivo de histórico não encontrado.")
            return

        quantidade_simulacoes = len(historico)


        escolha = questionary.text(
            f"\nDigite o número da simulação ou 'A' para todas (total de {quantidade_simulacoes}):",
            validate=lambda val: val.lower() == 'a' or val.isdigit() or val == ''  
        ).ask()


        if escolha == '':
            return  


        nome_time = questionary.text("Digite o nome do time:").ask().strip().lower()


        partidas_por_fase = {
            "grupos": [],
            "playoffs": [],
            "oitavas": [],
            "quartas": [],
            "semis": [],
            "final": []
        }


        if escolha.lower() == 'a':
            time_encontrado = False
            for num_simulacao, simulacao in enumerate(historico, 1):
                resultados = simulacao["resultados"]


                resultados_normalizados = {time.lower(): dados for time, dados in resultados.items()}


                if nome_time in resultados_normalizados:
                    time_encontrado = True  
                    print(f"\nPartidas jogadas pelo {nome_time.capitalize()} na simulação {num_simulacao}:\n")


                    for partida in resultados_normalizados[nome_time]["jogos"]:
                        fase = partida["fase"]
                        adversario = partida["adversario"]
                        gols_marcados = partida["gols_marcados"]
                        gols_sofridos = partida["gols_sofridos"]


                        resultado = "{:>20} {:<1} x {:<1} {:<20}".format(nome_time.capitalize(), gols_marcados, gols_sofridos, adversario)


                        if fase in partidas_por_fase:
                            partidas_por_fase[fase].append(resultado)
                        else:
                            print(f"Fase desconhecida: {fase}")


                    for fase, partidas in partidas_por_fase.items():
                        if partidas:
                            max_len_time = max(len(nome_time), max(len(partida) for partida in partidas))
                            if max_len_time % 2 == 0:
                                max_len_time += 1
                            tamanho_linha = max_len_time + 28  

                            print(f"Fase {fase.capitalize()}:\n")
                            print("┌" + "─" * tamanho_linha + "┐")
                            print("├" + "─" * tamanho_linha + "┤")

                            for partida in partidas:
                                print("| {:^{}} |".format(partida, tamanho_linha - 2))  

                            print("└" + "─" * tamanho_linha + "┘\n")  
                    partidas_por_fase = {k: [] for k in partidas_por_fase}  
            if not time_encontrado:
                print(f"\nO time {nome_time} não existe nos registros.\n")
        else:

            try:
                num_simulacao = int(escolha)
            except ValueError:
                print("Entrada inválida. Digite um número ou 'A' para todas as simulações.")
                continue


            if num_simulacao > len(historico) or num_simulacao <= 0:
                print(f"Simulação {num_simulacao} não encontrada.")
                continue


            simulacao = historico[num_simulacao - 1]  
            resultados = simulacao["resultados"]


            resultados_normalizados = {time.lower(): dados for time, dados in resultados.items()}


            if nome_time not in resultados_normalizados:
                print(f"Time '{nome_time}' não encontrado na simulação {num_simulacao}.")
                continue


            for partida in resultados_normalizados[nome_time]["jogos"]:
                fase = partida["fase"]
                adversario = partida["adversario"]
                gols_marcados = partida["gols_marcados"]
                gols_sofridos = partida["gols_sofridos"]


                resultado = "{:>20} {:<1} x {:<1} {:<20}".format(nome_time.capitalize(), gols_marcados, gols_sofridos, adversario)


                if fase in partidas_por_fase:
                    partidas_por_fase[fase].append(resultado)
                else:
                    print(f"Fase desconhecida: {fase}")


            print(f"\nPartidas jogadas pelo {nome_time.capitalize()} na simulação {num_simulacao}:\n")

            for fase, partidas in partidas_por_fase.items():
                if partidas:  
                    max_len_time = max(len(nome_time), max(len(partida) for partida in partidas))
                    if max_len_time % 2 == 0:
                        max_len_time += 1
                    tamanho_linha = max_len_time + 28  

                    print(f"Fase {fase.capitalize()}:\n")
                    print("┌" + "─" * tamanho_linha + "┐")
                    print("├" + "─" * tamanho_linha + "┤")

                    for partida in partidas:
                        print("| {:^{}} |".format(partida, tamanho_linha - 2))  

                    print("└" + "─" * tamanho_linha + "┘\n")  


















def analisar_estatisticas():
    """Analisa o arquivo de gols acumulados e imprime estatísticas de ataque, defesa e maior goleada."""
    gols_acumulados = carregar_gols_acumulados()

    gols = gols_acumulados["gols"]
    gols_sofridos = gols_acumulados["gols_sofridos"]
    partidas_jogadas = gols_acumulados["partidas_jogadas"]


    melhores_ataques = []
    piores_ataques = []
    melhores_defesas = []
    piores_defesas = []


    melhor_media_gols = float('-inf')
    pior_media_gols = float('inf')
    melhor_media_defensiva = float('inf')
    pior_media_defensiva = float('-inf')


    time_melhor_media_gols = None
    time_pior_media_gols = None
    time_melhor_media_defensiva = None
    time_pior_media_defensiva = None


    for time in gols:

        if gols[time] > (melhores_ataques[0]['gols'] if melhores_ataques else -1):
            melhores_ataques = [{"time": time, "gols": gols[time], "partidas": partidas_jogadas.get(time, 0)}]
        elif gols[time] == (melhores_ataques[0]['gols'] if melhores_ataques else -1):
            melhores_ataques.append({"time": time, "gols": gols[time], "partidas": partidas_jogadas.get(time, 0)})


        if gols[time] < (piores_ataques[0]['gols'] if piores_ataques else float('inf')):
            piores_ataques = [{"time": time, "gols": gols[time], "partidas": partidas_jogadas.get(time, 0)}]
        elif gols[time] == (piores_ataques[0]['gols'] if piores_ataques else float('inf')):
            piores_ataques.append({"time": time, "gols": gols[time], "partidas": partidas_jogadas.get(time, 0)})


        if gols_sofridos[time] < (melhores_defesas[0]['gols_sofridos'] if melhores_defesas else float('inf')):
            melhores_defesas = [{"time": time, "gols_sofridos": gols_sofridos[time], "partidas": partidas_jogadas.get(time, 0)}]
        elif gols_sofridos[time] == (melhores_defesas[0]['gols_sofridos'] if melhores_defesas else float('inf')):
            melhores_defesas.append({"time": time, "gols_sofridos": gols_sofridos[time], "partidas": partidas_jogadas.get(time, 0)})


        if gols_sofridos[time] > (piores_defesas[0]['gols_sofridos'] if piores_defesas else -1):
            piores_defesas = [{"time": time, "gols_sofridos": gols_sofridos[time], "partidas": partidas_jogadas.get(time, 0)}]
        elif gols_sofridos[time] == (piores_defesas[0]['gols_sofridos'] if piores_defesas else -1):
            piores_defesas.append({"time": time, "gols_sofridos": gols_sofridos[time], "partidas": partidas_jogadas.get(time, 0)})


        if partidas_jogadas.get(time, 0) > 0:  
            media_gols = gols[time] / partidas_jogadas[time]
            media_defensiva = gols_sofridos[time] / partidas_jogadas[time]


            if media_gols > melhor_media_gols:
                melhor_media_gols = media_gols
                time_melhor_media_gols = time


            if media_gols < pior_media_gols:
                pior_media_gols = media_gols
                time_pior_media_gols = time


            if media_defensiva < melhor_media_defensiva:
                melhor_media_defensiva = media_defensiva
                time_melhor_media_defensiva = time


            if media_defensiva > pior_media_defensiva:
                pior_media_defensiva = media_defensiva
                time_pior_media_defensiva = time


    print(f"{'_' * 56}\n")
    print("Melhor(es) Ataque(s):")
    for ataque in melhores_ataques:
        print(f"{ataque['time']}: {' ' * (20 - len(ataque['time']))} {ataque['gols']} gols em {ataque['partidas']} partidas")
    print(f"{'_' * 56}\n")

    print("\nMelhor(es) Defesa(s):")
    for defesa in melhores_defesas:
        print(f"{defesa['time']}: {' ' * (20 - len(defesa['time']))} {defesa['gols_sofridos']} gols sofridos em {defesa['partidas']} partidas")
    print(f"{'_' * 56}\n")

    print("\nPior(es) Ataque(s):")
    for ataque in piores_ataques:
        print(f"{ataque['time']}: {' ' * (20 - len(ataque['time']))} {ataque['gols']} gols em {ataque['partidas']} partidas")
    print(f"{'_' * 56}\n")

    print("\nPior(es) Defesa(s):")
    for defesa in piores_defesas:
        print(f"{defesa['time']}: {' ' * (20 - len(defesa['time']))} {defesa['gols_sofridos']} gols sofridos em {defesa['partidas']} partidas")
    print(f"{'_' * 56}\n")

    print("\nMaior(es) Goleada(s) da fase de liga:")
    print("\n")
    for goleada in maiores_goleadas:
        print("{:>20} {:<1} x {:<1} {:<20}".format(goleada['time1'], goleada['gols_time1'], goleada['gols_time2'], goleada['time2']))
    print("\n")
    print(f"{'_' * 56}\n")
    print("\nMaior(s) goleada(s) da fase de mata-mata:")
    print("\n")
    for goleada in maiores_goleadas_mata_mata:
        print("{:>20} {:<1} x {:<1} {:<20}".format(goleada['time1'], goleada['gols_time1'], goleada['gols_time2'], goleada['time2']))


    print("\n")
    print(f"{'_' * 56}\n")


    print("\nMelhor média de gols:")
    print(f"{time_melhor_media_gols}: {' ' * (20 - len(time_melhor_media_gols))} {melhor_media_gols:.2f} gols por partida")

    print("\nMelhor média defensiva:")
    print(f"{time_melhor_media_defensiva}: {' ' * (20 - len(time_melhor_media_defensiva))} {melhor_media_defensiva:.2f} gols sofridos por partida")

    print("\nPior média de gols:")
    print(f"{time_pior_media_gols}: {' ' * (20 - len(time_pior_media_gols))} {pior_media_gols:.2f} gols por partida")

    print("\nPior média defensiva:")
    print(f"{time_pior_media_defensiva}: {' ' * (20 - len(time_pior_media_defensiva))} {pior_media_defensiva:.2f} gols sofridos por partida")
    print(f"{'_' * 56}\n")









custom_style = Style([
    ('question', "yellow"),          
    ('qmark', ''),        
    ('pointer', 'cyan bold'),             
    ('highlighted', 'cyan bold'),    
    ('selected', ''),     
    ('separator', 'white'),          
    ('instruction', ''),        
    ('text', 'white'),               
    ('answer', 'cyan'),        
])




class ExitLoops(Exception):
    pass
class ExitToMainMenu(Exception):
    pass


def main():
    global potes, stats
    try:
        if not os.path.exists("configuracao_gols.json"):
            criar_configuracao_padrao()
        carregar_stats_inicial()

        class ExitLoops(Exception):
            """Exceção personalizada para controlar a saída de múltiplos loops."""
            pass

        while True:
            try:
                menu_principal()

                escolha_menu = questionary.select(
                    "\n\nMenu Principal\n\n",
                    choices=[
                        "Entrar no simulador",
                        "Configurações",
                        "Sair"
                    ],
                    style=custom_style 
                ).ask()

                if escolha_menu == 'Sair':
                    print("\n")
                    print("\nSaindo do programa...\n\n")
                    break  

                if escolha_menu == "Configurações":
                    while True:  
                        print("\n")
                        configs = questionary.select(
                            "\n\nConfigurações\n\n",
                            choices=[
                                "Editar média de gols do jogo",
                                "Editar times",
                                "Trocar para configuração padrão ou personalizada",
                                "Excluir times personalizados",
                                "Excluir simulação",
                                "Voltar",
                                "RESETAR DADOS"
                            ],
                            style=custom_style
                        ).ask()

                        if configs == "RESETAR DADOS":
                            resetar_aplicacao()

                        elif configs == "Editar média de gols do jogo":
                            configurar_nivel_gols()

                        elif configs == "Editar times":
                            substituir_time(potes, stats)
                            continue

                        elif configs == "Excluir times personalizados":
                            if os.path.exists("stats_personalizados.json"):
                                confirma = questionary.select(
                                    "Tem certeza que deseja excluir os times personalizados e voltar para a configuração padrão?\n\n",
                                    choices=[
                                        "Sim",
                                        "Não"
                                    ],
                                    style=custom_style
                                ).ask()

                                if confirma == 'Sim':
                                    excluir_stats_personalizados()
                                    potes, stats = carregar_times_stats2()
                                    continue
                                elif confirma == 'Não':
                                    print("\nOperação cancelada.")
                                    continue
                            else:
                                print("\n\nArquivo não encontrado.\n\n")

                        elif configs == "Trocar para configuração padrão ou personalizada":
                            alternar_stats()
                            continue

                        elif configs == "Excluir simulação":
                            excluir_simulacao()
                            continue

                        elif configs == "Voltar":
                            raise ExitLoops  

                elif escolha_menu == "Entrar no simulador":  
                        dados_times = carregar_dados_json()

                        aplicar_momento(dados_times)
                        salvar_dados_json(dados_times)

                        escolha = ""

                        while True:

                            dados_times = carregar_dados_times_2()


                            potes = dados_times["potes"]
                            confrontos = inicializa_confrontos(potes)
                            assign_all_internal_rivals(potes, confrontos)
                            success = assign_all_external_rivals(potes, confrontos)

                            if not success:
                                print("Falha ao sortear os confrontos.")
                                continue

                            home_away = assign_home_away(confrontos)
                            classificacao = inicializar_classificacao(potes)


                            print("\nConfrontos sorteados:")
                            for time in sorted(confrontos.keys()):
                                rivais_ordenados = agrupar_rivais_por_pote_intercalados(confrontos, time)
                                print("{:<20}| {}".format(time.upper(), ', '.join(f"{rival:<2}" for rival in rivais_ordenados)))
                            if escolha != "Sortear novamente":

                                escolha = questionary.select(
                                    "\n\nSimulador\n\n".upper(),
                                    choices=[ 
                                        "Sortear novamente",
                                        "Exibir confrontos",                                        
                                        "Pesquisar dados",
                                        "Menu Principal"
                                    ],
                                    style=custom_style
                                ).ask()

                                if escolha == "Menu Principal":
                                    criar_json_predefinido()
                                    restaurar_stats_originais(dados_times)
                                    raise ExitLoops  

                                elif escolha == "Sortear novamente":
                                    escolha = ""
                                    continue  


                                elif escolha == "Exibir confrontos":

                                    print("\n")
                                    print("\nExibindo confrontos...")
                                    print("\n")

                                    confrontos_partidas = exibir_primeiros_confrontos(home_away)
                                    print("\n")
                                    print("\nConfrontos:")
                                    print("\n")
                                    print("\n".join(confrontos_partidas))
                                    print("\n")

                                    while True:
                                        escolha_simular = questionary.select(
                                            "\n\n",
                                            choices=[
                                                "Simular partidas",
                                                "Voltar"
                                            ], style=custom_style
                                        ).ask()


                                        if escolha_simular == "Simular partidas":
                                            resultados = {}
                                            print("\n")
                                            print("\nSimulando partidas...")
                                            print("\n")

                                            resultados_partidas = simular_confrontos(home_away, resultados, classificacao)
                                            inicializar_gols_acumulados(classificacao)
                                            print("\n".join(resultados_partidas))
                                            print("\n")


                                            while True:
                                                escolha_tabela = questionary.select(
                                                    "\n\n",
                                                    choices=[
                                                        "Exibir play-offs",
                                                        "Exibir tabela de classificação",
                                                        "Voltar ao menu"
                                                    ], style=custom_style
                                                ).ask()


                                                if escolha_tabela == 'Exibir tabela de classificação':
                                                    print("\n")
                                                    exibir_classificacao(classificacao)
                                                    print("\n")

                                                elif escolha_tabela == 'Voltar ao menu':
                                                    resetar_arquivo_gols()
                                                    resetar_arquivo_resultados()
                                                    restaurar_stats_originais(dados_times)
                                                    raise ExitLoops

                                                elif escolha_tabela == 'Exibir play-offs':
                                                    print("\n")
                                                    exibir_playoffs(classificacao)
                                                    print("\n")

                                                    while True:
                                                        continuar = questionary.select(
                                                            "\n\n",
                                                            choices=[
                                                                "Simular play-offs",
                                                                "Exibir tabela de classificação",
                                                                "Voltar ao menu"
                                                            ], style=custom_style
                                                        ).ask()

                                                        if continuar == 'Exibir tabela de classificação':        
                                                            print("\n")
                                                            exibir_classificacao(classificacao)
                                                            print("\n")

                                                        elif continuar == 'Voltar ao menu':
                                                            resetar_arquivo_gols()
                                                            resetar_arquivo_resultados()
                                                            restaurar_stats_originais(dados_times)
                                                            raise ExitLoops


                                                        elif continuar == 'Simular play-offs':
                                                            print("\n")
                                                            vencedores = placar_final_playoffs(classificacao)
                                                            print("\n")


                                                            while True:
                                                                continuar = questionary.select(
                                                                    "\n\n",
                                                                    choices=[
                                                                        "Exibir confrontos das oitavas",
                                                                        "Exibir tabela de classificação",
                                                                        "Voltar ao menu"
                                                                    ], style=custom_style
                                                                ).ask()

                                                                if continuar == 'Exibir tabela de classificação':        
                                                                    print("\n")
                                                                    exibir_classificacao(classificacao)
                                                                    print("\n")

                                                                elif continuar == 'Voltar ao menu':
                                                                    resetar_arquivo_gols()
                                                                    resetar_arquivo_resultados()
                                                                    restaurar_stats_originais(dados_times)
                                                                    raise ExitLoops

                                                                elif continuar == 'Exibir confrontos das oitavas':
                                                                    exibir_oitavas(classificacao, vencedores)
                                                                    print("\n")
                                                                    print("\n")
                                                                    while True:
                                                                        continuar = questionary.select(
                                                                            "\n\n",
                                                                            choices=[
                                                                                "Simular oitavas de final",
                                                                                "Exibir tabela de classificação",
                                                                                "Voltar ao menu"
                                                                            ], style=custom_style
                                                                        ).ask()

                                                                        if continuar == 'Exibir tabela de classificação':        
                                                                            print("\n")
                                                                            exibir_classificacao(classificacao)
                                                                            print("\n")

                                                                        elif continuar == 'Voltar ao menu':
                                                                            resetar_arquivo_gols()
                                                                            resetar_arquivo_resultados()
                                                                            raise ExitLoops

                                                                        elif continuar == 'Simular oitavas de final':
                                                                            vencedores_oitavas = placar_final_oitavas(classificacao, vencedores)
                                                                            print("\n")
                                                                            print("\n")
                                                                            while True:
                                                                                continuar = questionary.select(
                                                                                    "\n\n",
                                                                                    choices=[
                                                                                        "Sortear confrontos das quartas de final",
                                                                                        "Exibir tabela de classificação",
                                                                                        "Voltar ao menu"
                                                                                    ], style=custom_style
                                                                                ).ask()

                                                                                if continuar == 'Exibir tabela de classificação':        
                                                                                    print("\n")
                                                                                    exibir_classificacao(classificacao)
                                                                                    print("\n")

                                                                                elif continuar == 'Voltar ao menu':
                                                                                    resetar_arquivo_gols()
                                                                                    resetar_arquivo_resultados()
                                                                                    restaurar_stats_originais(dados_times)
                                                                                    raise ExitLoops


                                                                                elif continuar == 'Sortear confrontos das quartas de final':
                                                                                    quartas_de_final = sortear_quartas(vencedores_oitavas)
                                                                                    exibir_confrontos_quartas(quartas_de_final)
                                                                                    print("\n")
                                                                                    print("\n")
                                                                                    while True:
                                                                                        continuar = questionary.select(
                                                                                            "\n\n",
                                                                                            choices=[
                                                                                                "Simular quartas de final",
                                                                                                "Exibir tabela de classificação",
                                                                                                "Voltar ao menu"
                                                                                            ], style=custom_style
                                                                                        ).ask()

                                                                                        if continuar == 'Exibir tabela de classificação':        
                                                                                            print("\n")
                                                                                            exibir_classificacao(classificacao)
                                                                                            print("\n")

                                                                                        elif continuar == 'Voltar ao menu':
                                                                                            resetar_arquivo_gols()
                                                                                            resetar_arquivo_resultados()
                                                                                            restaurar_stats_originais(dados_times)
                                                                                            raise ExitLoops


                                                                                        elif continuar == 'Simular quartas de final':
                                                                                            vencedores_quartas = placar_final_quartas(quartas_de_final)
                                                                                            print("\n")
                                                                                            print("\n")
                                                                                            while True:
                                                                                                continuar = questionary.select(
                                                                                                    "\n\n",
                                                                                                    choices=[
                                                                                                        "Exibir confrontos das semifinais",
                                                                                                        "Exibir tabela de classificação",
                                                                                                        "Voltar ao menu"
                                                                                                    ], style=custom_style
                                                                                                ).ask()

                                                                                                if continuar == 'Exibir tabela de classificação':        
                                                                                                    print("\n")
                                                                                                    exibir_classificacao(classificacao)
                                                                                                    print("\n")

                                                                                                elif continuar == 'Voltar ao menu':
                                                                                                    resetar_arquivo_gols()
                                                                                                    resetar_arquivo_resultados()
                                                                                                    restaurar_stats_originais(dados_times)
                                                                                                    raise ExitLoops


                                                                                                elif continuar == 'Exibir confrontos das semifinais':
                                                                                                    exibir_semi_final(vencedores_quartas)
                                                                                                    print("\n")
                                                                                                    print("\n")
                                                                                                    while True:
                                                                                                        continuar = questionary.select(
                                                                                                            "\n\n",
                                                                                                            choices=[
                                                                                                                "Simular semifinais",
                                                                                                                "Exibir tabela de classificação",
                                                                                                                "Voltar ao menu"
                                                                                                            ], style=custom_style
                                                                                                        ).ask()

                                                                                                        if continuar == 'Exibir tabela de classificação':        
                                                                                                            print("\n")
                                                                                                            exibir_classificacao(classificacao)
                                                                                                            print("\n")

                                                                                                        elif continuar == 'Voltar ao menu':
                                                                                                            resetar_arquivo_gols()
                                                                                                            resetar_arquivo_resultados()
                                                                                                            restaurar_stats_originais(dados_times)
                                                                                                            raise ExitLoops


                                                                                                        elif continuar == 'Simular semifinais':
                                                                                                            vencedores_semis = placar_final_semis(vencedores_quartas)
                                                                                                            print("\n")
                                                                                                            print("\n")
                                                                                                            while True:
                                                                                                                continuar = questionary.select(
                                                                                                                    "\n\n",
                                                                                                                    choices=[
                                                                                                                        "Exibir final",
                                                                                                                        "Exibir tabela de classificação",
                                                                                                                        "Voltar ao menu"
                                                                                                                    ], style=custom_style
                                                                                                                ).ask()

                                                                                                                if continuar == 'Exibir tabela de classificação':        
                                                                                                                    print("\n")
                                                                                                                    exibir_classificacao(classificacao)
                                                                                                                    print("\n")

                                                                                                                elif continuar == 'Voltar ao menu':
                                                                                                                    resetar_arquivo_gols()
                                                                                                                    resetar_arquivo_resultados()
                                                                                                                    restaurar_stats_originais(dados_times)
                                                                                                                    raise ExitLoops


                                                                                                                elif continuar == 'Exibir final':
                                                                                                                    exibir_final(vencedores_semis)
                                                                                                                    print("\n")
                                                                                                                    print("\n")
                                                                                                                    while True:
                                                                                                                        continuar = questionary.select(
                                                                                                                            "\n\n",
                                                                                                                            choices=[
                                                                                                                                "Simular final",
                                                                                                                                "Exibir tabela de classificação",
                                                                                                                                "Voltar ao menu"
                                                                                                                            ], style=custom_style
                                                                                                                        ).ask()

                                                                                                                        if continuar == 'Exibir tabela de classificação':        
                                                                                                                            print("\n")
                                                                                                                            exibir_classificacao(classificacao)
                                                                                                                            print("\n")

                                                                                                                        elif continuar == 'Voltar ao menu':
                                                                                                                            resetar_arquivo_gols()
                                                                                                                            resetar_arquivo_resultados()
                                                                                                                            restaurar_stats_originais(dados_times)
                                                                                                                            raise ExitLoops

                                                                                                                        if continuar == 'Simular final':
                                                                                                                            vencedor_final, gols_vencedor, vice_final, gols_vice = placar_final_final(vencedores_semis)
                                                                                                                            print("\n{:>16}\nCampeão: {}".format('', vencedor_final))
                                                                                                                            print_trophy(vencedor_final)
                                                                                                                            print("\n")
                                                                                                                            print("\n")



                                                                                                                            while True:                                                                                                                            
                                                                                                                                escolha_finais2 = questionary.select(
                                                                                                                                    "\nEscolha uma opção:\n\n".upper(),
                                                                                                                                    choices=["Finalizar","Estatísticas", "Exibir tabela de classificação"], style=custom_style
                                                                                                                                ).ask()
                                                                                                                                print("\n")



                                                                                                                                if escolha_finais2 == 'Exibir tabela de classificação':
                                                                                                                                    print("\n")
                                                                                                                                    exibir_classificacao(classificacao)
                                                                                                                                    print("\n")
                                                                                                                                    while True:
                                                                                                                                        voltar_ao_sorteio = questionary.select(
                                                                                                                                            "\nEscolha uma opção:\n\n".upper(),
                                                                                                                                            choices=["Finalizar", "Voltar"], style=custom_style
                                                                                                                                        ).ask()
                                                                                                                                        print("\n")


                                                                                                                                        if voltar_ao_sorteio == 'Finalizar':
                                                                                                                                            while True:
                                                                                                                                                salvar_ou_nao = questionary.select(
                                                                                                                                                    "\nDeseja salvar a simulação?\n\n".upper(),
                                                                                                                                                    choices=["Sim", "Não", "Voltar"], style=custom_style
                                                                                                                                                ).ask()

                                                                                                                                                print("\n")
                                                                                                                                                if salvar_ou_nao == 'Sim':

                                                                                                                                                    finalizar_simulacao(vencedor_final, gols_vencedor, vice_final, gols_vice)
                                                                                                                                                    transferir_para_historico()
                                                                                                                                                    restaurar_stats_originais(dados_times)
                                                                                                                                                    raise ExitLoops

                                                                                                                                                elif salvar_ou_nao == 'Não':
                                                                                                                                                    resetar_arquivo_gols()
                                                                                                                                                    resetar_arquivo_resultados()
                                                                                                                                                    restaurar_stats_originais(dados_times)
                                                                                                                                                    print("\nSimulação não salva.\n\n")

                                                                                                                                                    raise ExitLoops

                                                                                                                                                elif salvar_ou_nao == 'Voltar':
                                                                                                                                                    break
                                                                                                                                        elif voltar_ao_sorteio == 'Voltar':
                                                                                                                                            break



                                                                                                                                        else:
                                                                                                                                            print("\n")
                                                                                                                                            print("\nOpção inválida. Por favor, tente novamente.\n\n")






                                                                                                                                elif escolha_finais2 == 'Finalizar':                                                                                                                        

                                                                                                                                    while True:
                                                                                                                                        salvar_ou_nao = questionary.select(
                                                                                                                                            "\nDeseja salvar a simulação?\n\n".upper(),
                                                                                                                                            choices=["Sim", "Não", "Voltar"], style=custom_style
                                                                                                                                        ).ask()

                                                                                                                                        print("\n")
                                                                                                                                        if salvar_ou_nao == 'Sim':

                                                                                                                                            finalizar_simulacao(vencedor_final, gols_vencedor, vice_final, gols_vice)
                                                                                                                                            transferir_para_historico()
                                                                                                                                            restaurar_stats_originais(dados_times)
                                                                                                                                            raise ExitLoops

                                                                                                                                        elif salvar_ou_nao == 'Não':
                                                                                                                                            resetar_arquivo_gols()
                                                                                                                                            resetar_arquivo_resultados()
                                                                                                                                            restaurar_stats_originais(dados_times)
                                                                                                                                            print("\nSimulação não salva.\n\n")

                                                                                                                                            raise ExitLoops

                                                                                                                                        elif salvar_ou_nao == 'Voltar':
                                                                                                                                            break




                                                                                                                                elif escolha_finais2 == 'Estatísticas':
                                                                                                                                        print("\n")
                                                                                                                                        analisar_estatisticas()
                                                                                                                                        print("\n")
                                                                                                                                        while True:
                                                                                                                                            voltar_ao_sorteio = questionary.select(
                                                                                                                                                "\nEscolha uma opção:\n\n".upper(),
                                                                                                                                                choices=["Finalizar", "Procurar trajeto do time", "Voltar"], style=custom_style
                                                                                                                                            ).ask()
                                                                                                                                            print("\n")

                                                                                                                                            if voltar_ao_sorteio == 'Finalizar':



                                                                                                                                                while True:
                                                                                                                                                    salvar_ou_nao = questionary.select(
                                                                                                                                                        "\nDeseja salvar a simulação?\n\n".upper(),
                                                                                                                                                        choices=["Sim", "Não", "Voltar"], style=custom_style
                                                                                                                                                    ).ask()

                                                                                                                                                    print("\n")
                                                                                                                                                    if salvar_ou_nao == 'Sim':

                                                                                                                                                        finalizar_simulacao(vencedor_final, gols_vencedor, vice_final, gols_vice)
                                                                                                                                                        transferir_para_historico()
                                                                                                                                                        restaurar_stats_originais(dados_times)
                                                                                                                                                        raise ExitLoops

                                                                                                                                                    elif salvar_ou_nao == 'Não':
                                                                                                                                                        resetar_arquivo_gols()
                                                                                                                                                        resetar_arquivo_resultados()
                                                                                                                                                        restaurar_stats_originais(dados_times)
                                                                                                                                                        print("\nSimulação não salva.\n\n")

                                                                                                                                                        raise ExitLoops

                                                                                                                                                    elif salvar_ou_nao == 'Voltar':
                                                                                                                                                        break



                                                                                                                                            elif voltar_ao_sorteio == 'Voltar':
                                                                                                                                                break
                                                                                                                                            elif voltar_ao_sorteio == 'Procurar trajeto do time':
                                                                                                                                                print("\n")
                                                                                                                                                buscar_partidas_por_time()


                                                                                                                                            else:
                                                                                                                                                print("\n")
                                                                                                                                                print("\nOpção inválida. Por favor, tente novamente.\n\n")


                                                                                                                                else:
                                                                                                                                    print("\n")
                                                                                                                                    print("\nOpção inválida. Por favor, tente novamente.\n\n")

                                                                                                                else:
                                                                                                                    print("\n")
                                                                                                                    print("\nOpção inválida. Por favor, tente novamente.\n\n")    


                                                                                                        else:
                                                                                                            print("\n")
                                                                                                            print("\nOpção inválida. Por favor, tente novamente.\n\n")    

                                                                                                else:
                                                                                                    print("\n")
                                                                                                    print("\nOpção inválida. Por favor, tente novamente.\n\n")    

                                                                                        else:
                                                                                            print("\n")
                                                                                            print("\nOpção inválida. Por favor, tente novamente.\n\n")                                           
                                                                                else:
                                                                                    print("\n")
                                                                                    print("\nOpção inválida. Por favor, tente novamente.\n\n")

                                                                        else:
                                                                            print("\n")
                                                                            print("\nOpção inválida. Por favor, tente novamente.\n\n")

                                                                else:
                                                                    print("\n")
                                                                    print("\nOpção inválida. Por favor, tente novamente.\n\n")

                                                        else:
                                                            print("\n")
                                                            print("\nOpção inválida. Por favor, tente novamente.\n\n")

                                                else:
                                                    print("\n")
                                                    print("\nOpção inválida. Por favor, tente novamente.\n\n")
                                        elif escolha_simular == 'Voltar':
                                            criar_json_predefinido()
                                            restaurar_stats_originais(dados_times)
                                            break




                                elif escolha == "Pesquisar dados":
                                    while True:  
                                        print("\n")


                                        procurar_dados = questionary.select(
                                            "\nPesquisa de Dados\n\n".upper(),
                                            choices=[
                                                "Exibir todas as finais",
                                                "Listar campeões",
                                                "Listar vice-campeões",
                                                "Melhores Ataques Histórico",
                                                "Melhores Defesas Histórico",
                                                "Exibir médias de ataque e defesa",
                                                "Ordem por vitórias",
                                                "Maiores goleadas",
                                                "Pesquisar por time",
                                                "Todas as partidas registradas",
                                                "Voltar para o sorteio"
                                            ], style=custom_style
                                        ).ask()

                                        print("\n")

                                        if procurar_dados == 'Exibir todas as finais':
                                            print("\n")
                                            exibir_finais()
                                            print("\n")
                                            voltar = questionary.select(
                                                "Escolha uma opção:\n\n".upper(),
                                                choices=["Voltar para pesquisa de dados", "voltar para sorteio"], style=custom_style
                                            ).ask()
                                            print("\n")

                                            if voltar == 'Voltar para pesquisa de dados':
                                                continue  
                                            elif voltar == 'Voltar para sorteio':
                                                break  

                                        elif procurar_dados == 'Listar campeões':
                                            print("\n")
                                            listar_campeoes_ordenados()
                                            print("\n")
                                            voltar = questionary.select(
                                                "Escolha uma opção:\n\n".upper(),
                                                choices=["Voltar para pesquisa de dados", "voltar para sorteio"], style=custom_style
                                            ).ask()
                                            print("\n")

                                            if voltar == 'Voltar para pesquisa de dados':
                                                continue  
                                            elif voltar == 'Voltar para sorteio':
                                                break  


                                        elif procurar_dados == 'Listar vice-campeões':
                                            print("\n")
                                            listar_vices_ordenados()
                                            print("\n")
                                            voltar = questionary.select(
                                                "Escolha uma opção:\n\n".upper(),
                                                choices=["Voltar para pesquisa de dados", "voltar para sorteio"], style=custom_style
                                            ).ask()
                                            print("\n")

                                            if voltar == 'Voltar para pesquisa de dados':
                                                continue  
                                            elif voltar == 'Voltar para sorteio':
                                                break  

                                        elif procurar_dados == 'Melhores Ataques Histórico':
                                            print("\n")
                                            historico_melhores_ataques()
                                            print("\n")
                                            voltar = questionary.select(
                                                "Escolha uma opção:\n\n".upper(),
                                                choices=["Voltar para pesquisa de dados", "voltar para sorteio"], style=custom_style
                                            ).ask()
                                            print("\n")

                                            if voltar == 'Voltar para pesquisa de dados':
                                                continue  
                                            elif voltar == 'Voltar para sorteio':
                                                break  

                                        elif procurar_dados == 'Melhores Defesas Histórico':
                                            print("\n")
                                            historico_melhores_defesas()
                                            print("\n")
                                            voltar = questionary.select(
                                                "Escolha uma opção:\n\n".upper(),
                                                choices=["Voltar para pesquisa de dados", "voltar para sorteio"], style=custom_style
                                            ).ask()
                                            print("\n")

                                            if voltar == 'Voltar para pesquisa de dados':
                                                continue  
                                            elif voltar == 'Voltar para sorteio':
                                                break  

                                        elif procurar_dados == 'Exibir médias de ataque e defesa':
                                            print("\n")
                                            media_gols_feitos()
                                            print("\n")
                                            media_gols_sofridos()
                                            print("\n")
                                            voltar = questionary.select(
                                                "Escolha uma opção:\n\n".upper(),
                                                choices=["Voltar para pesquisa de dados", "voltar para sorteio"], style=custom_style
                                            ).ask()
                                            print("\n")

                                            if voltar == 'Voltar para pesquisa de dados':
                                                continue  
                                            elif voltar == 'Voltar para sorteio':
                                                break  

                                        elif procurar_dados == 'Ordem por vitórias':
                                            print("\n")
                                            historico_mais_vitorias()
                                            print("\n")
                                            continue  

                                        elif procurar_dados == 'Pesquisar por time':
                                            while True:  
                                                print("\n")
                                                nome_time = questionary.text("Digite o nome do time que deseja pesquisar: "
                                                ).ask().strip()
                                                print("\n")
                                                pesquisar_campeao_por_time(nome_time)
                                                print("\n")

                                                voltar = questionary.select(
                                                    "\nEscolha uma opção:".upper(),
                                                    choices=["Voltar", "Pesquisar novamente"], style=custom_style
                                                ).ask()

                                                if voltar == 'Pesquisar novamente':
                                                    continue  
                                                elif voltar == 'Voltar':
                                                    break  

                                        elif procurar_dados == 'Todas as partidas registradas':
                                            print("\n")
                                            buscar_partidas_historico()
                                            print("\n")
                                            continue  

                                        elif procurar_dados == 'Voltar para o sorteio':
                                            break  

                                        else:
                                            print("\n")
                                            print("\nInsira uma opção válida\n\n")
                                            continue


            except ExitLoops:
                print("Voltando para o menu principal...")
                print("\n")
                continue  
    except KeyboardInterrupt:
        print("\n")
        resetar_arquivo_gols()
        resetar_arquivo_resultados()
        restaurar_stats_originais(dados_times)
        print("\nPrograma interrompido pelo usuário.")
        print("\n")


if __name__ == "__main__":
    main()