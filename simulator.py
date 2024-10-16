import json
import os
import random
import numpy as np
import sys
import time

def reiniciar_aplicacao():
    print("\n\nA aplicação será reiniciada em 5 segundos...\n")
    for i in range(5, 0, -1):
        print(f"{i} segundo(s) restantes...", end='\r')
        time.sleep(1)  # Espera 1 segundo
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

    confirmar = input("\n\nDeseja excluir permanentemente todos os dados? (S/N).\n\n")
    if confirmar == 'S' or confirmar == 's':
        confirma2 = input("\n\nEsta ação não poderá ser desfeita. Digite 'RESETAR' para dar continuidade.\n\n")
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
    elif confirmar == 'N' or confirmar == 'n':
        print("\n\nOperação cancelada.\n\n")
        return
    else:
        print("\n\nOperação cancelada.\n\n")
        return



def criar_json_predefinido():
    potes = [
        ["Barcelona", "Real Madrid", "Manchester City", "Bayern Munich", "PSG", "Juventus", "Chelsea", "Liverpool", "Atlético Madrid"],
        ["Borussia Dortmund", "Inter de Milão", "Milan", "Tottenham", "Arsenal", "Napoli", "Leipzig", "Sevilla", "Ajax"],
        ["Benfica", "Porto", "Shakhtar", "Zenit", "Sporting", "Atalanta", "Lyon", "Monaco", "Leverkusen"],
        ["Fenerbahçe", "Galatasaray", "Olympiacos", "Red Bull Salzburg", "Celtic", "Rangers", "Club Brugge", "Dynamo Kiev", "Anderlecht"]
    ]

    stats = {
        "Barcelona": {"ataque": 90, "defesa": 85},
        "Real Madrid": {"ataque": 88, "defesa": 83},
        "Manchester City": {"ataque": 92, "defesa": 86},
        "Bayern Munich": {"ataque": 91, "defesa": 84},
        "PSG": {"ataque": 89, "defesa": 80},
        "Juventus": {"ataque": 86, "defesa": 82},
        "Chelsea": {"ataque": 87, "defesa": 81},
        "Liverpool": {"ataque": 90, "defesa": 84},
        "Atlético Madrid": {"ataque": 85, "defesa": 88},
        "Borussia Dortmund": {"ataque": 84, "defesa": 79},
        "Inter de Milão": {"ataque": 82, "defesa": 80},
        "Milan": {"ataque": 81, "defesa": 78},
        "Tottenham": {"ataque": 83, "defesa": 77},
        "Arsenal": {"ataque": 85, "defesa": 76},
        "Napoli": {"ataque": 84, "defesa": 78},
        "Leipzig": {"ataque": 82, "defesa": 76},
        "Sevilla": {"ataque": 80, "defesa": 79},
        "Ajax": {"ataque": 81, "defesa": 75},
        "Benfica": {"ataque": 78, "defesa": 74},
        "Porto": {"ataque": 77, "defesa": 76},
        "Shakhtar": {"ataque": 75, "defesa": 72},
        "Zenit": {"ataque": 76, "defesa": 73},
        "Sporting": {"ataque": 76, "defesa": 71},
        "Atalanta": {"ataque": 79, "defesa": 74},
        "Lyon": {"ataque": 78, "defesa": 72},
        "Monaco": {"ataque": 77, "defesa": 70},
        "Leverkusen": {"ataque": 79, "defesa": 73},
        "Fenerbahçe": {"ataque": 72, "defesa": 69},
        "Galatasaray": {"ataque": 71, "defesa": 68},
        "Olympiacos": {"ataque": 70, "defesa": 67},
        "Red Bull Salzburg": {"ataque": 73, "defesa": 70},
        "Celtic": {"ataque": 71, "defesa": 66},
        "Rangers": {"ataque": 70, "defesa": 65},
        "Club Brugge": {"ataque": 72, "defesa": 68},
        "Dynamo Kiev": {"ataque": 69, "defesa": 66},
        "Anderlecht": {"ataque": 67, "defesa": 65}
    }

    # Estrutura do JSON
    dados = {
        "potes": potes,
        "stats": stats
    }

    # Salvando no arquivo JSON
    with open("dados_times.json", "w") as file:
        json.dump(dados, file, indent=4)



# Chamar a função para criar o JSON predefinido
criar_json_predefinido()

# Verificar se existe o arquivo de personalização
if os.path.exists("stats_personalizados.json"):
    with open("stats_personalizados.json", "r") as file:
        dados = json.load(file)
        print("Carregando times e stats personalizados...")
else:
    with open("dados_times.json", "r") as file:
        dados = json.load(file)
        print("Carregando configurações predefinidas...")

# Carregar os potes e stats
potes = dados["potes"]
stats = dados["stats"]


# Função para determinar o pote do time
def get_pote(time):
    for idx, pote in enumerate(potes, start=1):
        if time in pote:
            return idx
    return None

def listar_times(potes, stats):
    print("\nLista de Times:")
    print("\n")
    
    # Define o tamanho da linha baseado nos cabeçalhos
    tamanho_linha = 65
    
    print("┌" + "─" * tamanho_linha + "┐")  # Início da borda superior
    print("│" + f"{'Número':<10}{'Time':<25}{'Ataque':<15}{'Defesa':<15}│")  # Cabeçalho
    print("├" + "─" * tamanho_linha + "┤")  # Linha horizontal após o cabeçalho

    for i in range(len(potes)):
        for j in range(len(potes[i])):
            time = potes[i][j]
            ataque = stats.get(time, {}).get("ataque", "N/A")
            defesa = stats.get(time, {}).get("defesa", "N/A")
            numero = i * 9 + j + 1  # Número do time baseado no índice
            print("│" + f"{numero:<10}{time:<25}{ataque:<15}{defesa:<15}│")  # Dados da tabela

    print("└" + "─" * tamanho_linha + "┘")  # Borda inferior







def salvar_times_stats_personalizados(potes, stats):
    configuracao_personalizada = {
        "potes": potes,
        "stats": stats
    }
    with open("stats_personalizados.json", "w") as file:
        json.dump(configuracao_personalizada, file, indent=4)




def excluir_stats_personalizados():
    print("\n")
   
    confirmacao = input("Digite 'EXCLUIR' para apagar os stats personalizados: \n\n")
    
    if confirmacao == "EXCLUIR":
        # Verificar se o arquivo existe antes de tentar excluir
        if os.path.exists("stats_personalizados.json"):
            os.remove("stats_personalizados.json")
            print("\n")
            print("Os times personalizados foram excluídos com sucesso.\n")
        else:
            print("\n")
            print("Não existem times personalizados.\n")
    else:
        print("\n")
        print("Operação cancelada ou erro de digitação.")





stats_atual = ""

# Função para carregar os stats com base no arquivo existente (executada uma vez no início)
def carregar_stats_inicial():
    global potes, stats, stats_atual
    # Verifica se o arquivo personalizado existe e carrega os dados correspondentes
    if os.path.exists("stats_personalizados.json"):
        with open("stats_personalizados.json", "r") as file:
            dados = json.load(file)
            potes = dados["potes"]
            stats = dados["stats"]
        stats_atual = "Personalizados"  # Atualiza a variável para indicar que os stats personalizados estão em uso
    else:
        with open("dados_times.json", "r") as file:
            dados = json.load(file)
            potes = dados["potes"]
            stats = dados["stats"]
        stats_atual = "Padrões"
        print("Stats padrão em uso.")

        

def alternar_stats():
    global potes, stats, stats_atual  # Usar as variáveis globais
        # Verifica se existe o arquivo personalizado e define qual usar
    #if not os.path.exists("stats_personalizados.json"):


    # Exibe qual está em uso atualmente
    print(f"\n\nTimes e stats atualmente em uso: {stats_atual}\n")

    # Solicita que o usuário escolha entre os stats padrões ou personalizados
    escolha = input("\nEscolha quais utilizar:\n1 - Dados padrões\n2 - Dados personalizados\n\n").strip()

    if escolha == '1':
        if os.path.exists("dados_times.json"):
            with open("dados_times.json", "r") as file:
                print("\n\nCarregando configurações predefinidas...")
                dados = json.load(file)
                potes = dados["potes"]
                stats = dados["stats"]  # Carregar os dados predefinidos
            stats_atual = "Padrões"
            print("\n\nAgora, os times e stats padrões estão em uso.\n\n")
        else:
            print("Erro: O arquivo não foi encontrado.")
    
    elif escolha == '2':
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
    
    else:
        print("\nEscolha inválida. Por favor, selecione 1 ou 2.\n")





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



# Função para carregar o arquivo personalizado ou, caso não exista, o predefinido
def carregar_times_stats():
    if os.path.exists("stats_personalizados.json"):
        with open("stats_personalizados.json", "r") as file:
            configuracao = json.load(file)
            return configuracao["potes"], configuracao["stats"]
    else:
        with open("dados_times.json", "r") as file:
            configuracao = json.load(file)
            return configuracao["potes"], configuracao["stats"]





# Função para substituir o time e salvar no arquivo personalizado
def substituir_time(potes, stats):
    if not os.path.exists("dados_times.json"):
        print("\n\nArquivo não encontrado.\n\n")
    else:

        # Verifica se existe um arquivo de stats personalizados
        if os.path.exists("stats_personalizados.json"):
            with open("stats_personalizados.json", "r") as file:
                dados_personalizados = json.load(file)
                potes = dados_personalizados["potes"]
                stats = dados_personalizados["stats"]
        else:
            # Se não existir, carrega o arquivo de dados normais
            with open("dados_times.json", "r") as file:
                dados_normais = json.load(file)
                potes = dados_normais["potes"]
                stats = dados_normais["stats"]
        
        listar_times(potes, stats)
        while True:
            try:
                print("\n")
                entrada = input("\n\nDigite o número do time que deseja substituir (1-36):\nS - sair\n\n").strip()
                
                if entrada.lower() == 's':
                    break  # Sai do loop se o usuário digitar 's' ou 'S'

                numero_substituir = int(entrada)  # Tenta converter a entrada para inteiro

                if numero_substituir < 1 or numero_substituir > 36:
                    print("\nNúmero inválido. Escolha um número entre 1 e 36.\n")
                    continue  # Volta para o início do loop para nova tentativa
                
                # Identificar o pote e o índice do time com base no número
                pote_indice = (numero_substituir - 1) // 9
                indice_no_pote = (numero_substituir - 1) % 9
                
                # Time que será substituído
                time_substituido = potes[pote_indice][indice_no_pote]
                
                print(f"\nVocê escolheu substituir o time: {time_substituido}")
                
                # Nome do novo time
                novo_time = input("\nDigite o nome do novo time: \n\n")
                
                # Stats do novo time
                ataque = int(input(f"\nDigite o valor do ataque de {novo_time}: "))
                defesa = int(input(f"Digite o valor da defesa de {novo_time}: "))
                
                # Substitui o time no pote e atualiza os stats
                potes[pote_indice][indice_no_pote] = novo_time
                stats[novo_time] = {"ataque": ataque, "defesa": defesa}
                
                # Remove os stats do time substituído
                if time_substituido in stats:
                    del stats[time_substituido]
                
                print(f"\n\n{novo_time} foi adicionado com ataque {ataque} e defesa {defesa}.\n\n")

                
                # Salvar a alteração no arquivo personalizado
                salvar_times_stats_personalizados(potes, stats)
                carregar_stats_inicial()
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

            except ValueError:
                print("\n")
                print("Opção inválida. Tente novamente.")











# Função para calcular a média de gols e o desvio padrão com base nos stats
def calcula_media_desvio(ataque_time, defesa_adversario):
    # Carregar a configuração atual
    configuracao = carregar_configuracao()
    nivel_gols = configuracao["nivel_gols"]
    params = configuracao["configuracoes"][nivel_gols]

    # Aplicar os parâmetros configuráveis
    media = max(params["media_base"], (ataque_time - defesa_adversario) / params["media_divisor"] + params["soma"])
    desvio = max(params["desvio_base"], (60 - abs(ataque_time - defesa_adversario)) / params["desvio_divisor"])

    return media, desvio




def momento():
    # Gera uma lista de números de -10 a 10 pulando de 2 em 2
    numeros = list(range(-10, 11, 1))
    return random.choice(numeros)

def print_stats_com_momento():
    for time in stats:
        # Obter os stats de ataque e defesa do time atual
        ataque_time = stats[time]["ataque"]
        defesa_time = stats[time]["defesa"]

        # Gerar valores de momento para o ataque e defesa
        momento_ataque = momento()
        momento_defesa = momento()

        # Aplicar o momento aos stats
        ataque_time_com_momento = ataque_time + momento_ataque
        defesa_time_com_momento = defesa_time + momento_defesa

        # Printar os stats com o momento aplicado
        print(f"Time: {time}")
        print(f"Ataque com momento: {ataque_time_com_momento}")
        print(f"Defesa com momento: {defesa_time_com_momento}")
        print("-" * 30)  # Separador para melhor visualização


# Chamar a função para imprimir os stats de todos os times



# Função para gerar gols usando o cálculo automático de médias e desvios
def gerar_gols(time_casa, time_fora):
    # Obter pote dos times
    pote_fora = get_pote(time_fora)
    pote_casa = get_pote(time_casa)

    # Verificar se os stats estão definidos para os times
    if time_casa not in stats or time_fora not in stats:
        raise ValueError(f"Stats não definidos para {time_casa} ou {time_fora}")

    # Obter stats de ataque e defesa
    ataque_casa = stats[time_casa]["ataque"]
    defesa_fora = stats[time_fora]["defesa"]
    ataque_fora = stats[time_fora]["ataque"]
    defesa_casa = stats[time_casa]["defesa"]

    momento_casa_ataque = momento()
    momento_fora_defesa = momento()
    momento_fora_ataque = momento()
    momento_casa_defesa = momento()

    ataque_casa = ataque_casa + momento_casa_ataque
    defesa_fora = defesa_fora + momento_fora_defesa
    ataque_fora = ataque_fora + momento_fora_ataque
    defesa_casa = defesa_casa + momento_casa_defesa


    # Calcular médias e desvios
    media_casa, desvio_casa = calcula_media_desvio(ataque_casa, defesa_fora)
    media_fora, desvio_fora = calcula_media_desvio(ataque_fora, defesa_casa)

    # Gerar gols usando uma distribuição normal e arredondar para garantir que não seja negativo
    gols_casa = max(0, int(np.random.normal(media_casa, desvio_casa)))
    gols_fora = max(0, int(np.random.normal(media_fora, desvio_fora)))

    return gols_casa, gols_fora



def simular_penaltis(time1, time2):
    # Placar inicial
    gols_time1 = 0
    gols_time2 = 0
    total_cobranças = 5

    # Primeiras 5 cobranças alternadas
    for i in range(total_cobranças):
        # Time A bate
        if random.random() < 0.75:
            gols_time1 += 1

        # Time B bate
        if random.random() < 0.75:
            gols_time2 += 1

        # Verifica se há um vencedor após ambas as cobranças
        if abs(gols_time1 - gols_time2) > total_cobranças - (i + 1):
            return gols_time1, gols_time2

    # Se chegar aqui, os placares estão empatados ou a disputa continua
    # Disputa de pênaltis em morte súbita
    while True:
        # Time A bate
        if random.random() < 0.75:
            gols_time1 += 1
        
        # Time B bate
        if random.random() < 0.75:
            gols_time2 += 1

        # Verifica se há um vencedor
        if gols_time1 != gols_time2:
            return gols_time1, gols_time2









# Função para inicializar os confrontos
def inicializa_confrontos(potes):
    return {time: set() for pote in potes for time in pote}

# Atribuição das rivalidades internas e externas permanece a mesma
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
                        # Trocar as posições
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
    
    # Preenche o dicionário com os rivais
    for rival in confrontos[time]:
        pote = get_pote(rival)
        if pote is not None:
            rivais_por_pote[pote].append(rival)

    # Exibe os rivais na ordem intercalada
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
    "vitorias": {},  # Novo dicionário para contabilizar vitórias
    "empates": {},  # Novo dicionário para contabilizar empates
    "derrotas": {}  # Novo dicionário para contabilizar derrotas
}

def inicializar_gols_acumulados(classificacao):
    """Inicializa o dicionário que armazena os gols acumulados com base na classificação."""
    for time in classificacao.keys():
        gols_acumulados["gols"][time] = classificacao[time]['gols_marcados']
        gols_acumulados["gols_sofridos"][time] = 0  # Inicializa os gols sofridos como 0
        gols_acumulados["partidas_jogadas"][time] = 0  # Inicializa partidas jogadas como 0
        gols_acumulados["vitorias"][time] = 0  # Inicializa vitórias como 0
        gols_acumulados["empates"][time] = 0  # Inicializa empates como 0
        gols_acumulados["derrotas"][time] = 0  # Inicializa derrotas como 0

def atualizar_gols_acumulados(time, gols, tipo):
    """Atualiza o total de gols de um time, seja marcados ou sofridos."""
    if time in gols_acumulados[tipo]:
        gols_acumulados[tipo][time] += gols
    else:
        gols_acumulados[tipo][time] = gols

def atualizar_partidas_jogadas(time):
    """Atualiza o total de partidas jogadas de um time no arquivo JSON."""
    dados_atualizados = carregar_gols_acumulados()  # Carrega os dados atuais

    # Atualiza a contagem de partidas jogadas
    if time in dados_atualizados["partidas_jogadas"]:
        dados_atualizados["partidas_jogadas"][time] += 1
    else:
        dados_atualizados["partidas_jogadas"][time] = 1

    salvar_gols_acumulados(dados_atualizados)  # Salva os dados atualizados

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
    # Verifica se o time já existe nas derrotas; se não, inicializa com 0
    if time not in dados_atualizados["derrotas"]:
        dados_atualizados["derrotas"][time] = 0
    
    # Incrementa o total de derrotas
    dados_atualizados["derrotas"][time] += 1
    salvar_gols_acumulados(dados_atualizados)

nome_arquivo_gols = "gols_simulacao_atual.json"

def carregar_gols_acumulados():
    """Carrega o arquivo de gols acumulados. Se o arquivo não existir ou estiver incompleto, retorna um dicionário inicializado corretamente."""
    if os.path.exists(nome_arquivo_gols):
        with open(nome_arquivo_gols, 'r') as file:
            dados = json.load(file)
            
            # Garante que todas as chaves necessárias existam
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

    # Se o arquivo não existir, inicializa com a estrutura completa
    dados_iniciais = {
        "vitorias": {},
        "empates": {},
        "derrotas": {},
        "gols": {},
        "gols_sofridos": {},
        "partidas_jogadas": {}
    }
    
    # Inicializa estatísticas para todos os times nos potes
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
    
    # Atualiza os gols marcados
    if time in dados_atualizados["gols"]:
        dados_atualizados["gols"][time] += gols_marcados
    else:
        dados_atualizados["gols"][time] = gols_marcados
    
    # Atualiza os gols sofridos
    if time in dados_atualizados["gols_sofridos"]:
        dados_atualizados["gols_sofridos"][time] += gols_sofridos
    else:
        dados_atualizados["gols_sofridos"][time] = gols_sofridos

    # Atualiza a contagem de partidas jogadas
    atualizar_partidas_jogadas(time)  # Atualiza partidas jogadas

    salvar_gols_acumulados(dados_atualizados)

nome_arquivo_historico = "historico_gols.json"

def carregar_historico_gols():
    if os.path.exists(nome_arquivo_historico_gols):
        with open(nome_arquivo_historico_gols, 'r') as file:
            try:
                # Tenta carregar o arquivo JSON
                return json.load(file)
            except json.JSONDecodeError:
                # Se o arquivo estiver vazio ou inválido, retorna uma lista vazia
                
                print(f"Arquivo vazio ou corrompido.")
                print("\n")
                return []
    else:
        # Se o arquivo não existir, retorna uma lista vazia
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

def finalizar_simulacao(vencedor_final, gols_vencedor, vice_final, gols_vice):
    """Transfere os gols marcados e sofridos da simulação atual para o histórico e reseta o arquivo de gols acumulados."""
    print("Finalização da simulação...")

    # Carrega os dados de gols acumulados
    gols_acumulados = carregar_gols_acumulados()
    
    # Verifica se há pelo menos 25 times
    if len(gols_acumulados["gols"]) < 25:
        print("Erro: Não foi salvo no histórico!")
        return
    
    configuracao_atual = carregar_configuracao()
    nivel_gols_simulacao = configuracao_atual["nivel_gols"]

    # Carrega o histórico de gols
    historico_gols = carregar_historico_gols()

    # Adiciona os dados da simulação atual ao histórico
    historico_gols.append({
        "simulacao": len(historico_gols) + 1,
        "nivel_simulacao": nivel_gols_simulacao,
        "gols": gols_acumulados["gols"],
        "gols_sofridos": gols_acumulados["gols_sofridos"],
        "partidas_jogadas": gols_acumulados["partidas_jogadas"],  # Adiciona partidas jogadas
        "vitorias": gols_acumulados["vitorias"],
        "empates": gols_acumulados["empates"],
        "derrotas": gols_acumulados["derrotas"]
    })
    salvar_resultado_final(vencedor_final, gols_vencedor, vice_final, gols_vice)

    # Salva o novo histórico de gols
    salvar_historico_gols(historico_gols)

    # Remove o arquivo de gols acumulados (reset)
    resetar_arquivo_gols()

    print(f"Simulação finalizada! Os dados foram movidos para o histórico.")


def resetar_arquivo_resultados():
    """Remove o arquivo de resultados das partidas, iniciando uma nova simulação."""
    if os.path.exists('resultados_partidas_atual.json'):
        os.remove('resultados_partidas_atual.json')













def historico_melhores_ataques():
    """Lista o histórico de melhores ataques, somando todos os gols e partidas jogadas de cada time."""
    # Carrega o histórico de gols
    historico_gols = carregar_historico_gols()

    # Inicializa um dicionário para armazenar os totais de gols e partidas jogadas
    totais_gols = {}
    totais_partidas = {}

    # Soma todos os gols e partidas jogadas de cada simulação
    for simulacao in historico_gols:
        for time, gols in simulacao["gols"].items():
            if time not in totais_gols:
                totais_gols[time] = 0
            totais_gols[time] += gols

        for time, partidas in simulacao["partidas_jogadas"].items():
            if time not in totais_partidas:
                totais_partidas[time] = 0
            totais_partidas[time] += partidas

    # Ordena os times com base nos gols totais
    melhores_ataques = sorted(totais_gols.items(), key=lambda x: x[1], reverse=True)

    print("Histórico de Melhores Ataques:")
    print("┌" + "─" * 50 + "┐")
    print(f"│{'Time'.ljust(20)}│ {'Gols'.ljust(10)}│{'Partidas Jogadas'.ljust(15)} │")
    print("├" + "─" * 50 + "┤")

    for time, gols in melhores_ataques:
        partidas_jogadas = totais_partidas.get(time, 0)  # Obtém o número de partidas jogadas
        print(f"│{time.ljust(20)}│ {str(gols).ljust(10)}│ {str(partidas_jogadas).ljust(15)} │")

    print("└" + "─" * 50 + "┘")


def historico_melhores_defesas():
    """Lista o histórico de melhores defesas, somando todos os gols sofridos e partidas jogadas de cada time."""
    # Carrega o histórico de gols sofridos
    historico_gols = carregar_historico_gols()

    # Inicializa um dicionário para armazenar os totais de gols sofridos e partidas jogadas
    totais_gols_sofridos = {}
    totais_partidas = {}

    # Soma todos os gols sofridos e partidas jogadas de cada simulação
    for simulacao in historico_gols:
        for time, gols_sofridos in simulacao["gols_sofridos"].items():
            if time not in totais_gols_sofridos:
                totais_gols_sofridos[time] = 0
            totais_gols_sofridos[time] += gols_sofridos

        for time, partidas in simulacao["partidas_jogadas"].items():
            if time not in totais_partidas:
                totais_partidas[time] = 0
            totais_partidas[time] += partidas

    # Ordena os times com base nos gols sofridos, do menor para o maior
    melhores_defesas = sorted(totais_gols_sofridos.items(), key=lambda x: x[1])

    print("Histórico de Melhores Defesas:")
    print("┌" + "─" * 55 + "┐")
    print(f"│{'Time'.ljust(20)}│ {'Gols Sofridos'.ljust(15)}│{'Partidas Jogadas'.ljust(15)} │")
    print("├" + "─" * 55 + "┤")

    for time, gols_sofridos in melhores_defesas:
        partidas_jogadas = totais_partidas.get(time, 0)  # Obtém o número de partidas jogadas
        print(f"│{time.ljust(20)}│ {str(gols_sofridos).ljust(15)}│ {str(partidas_jogadas).ljust(15)} │")

    print("└" + "─" * 55 + "┘\n")







def historico_mais_vitorias():
    """Exibe uma tabela com os times ordenados por vitórias, empates ou derrotas, conforme a escolha do usuário."""
    # Carrega o histórico de gols, vitórias, empates e derrotas
    while True:
        historico_gols = carregar_historico_gols()

        # Inicializa dicionários para armazenar os totais
        totais_vitorias = {}
        totais_empates = {}
        totais_derrotas = {}
        totais_partidas = {}

        # Soma as vitórias, empates e derrotas de cada time em todas as simulações
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

        # Solicita que o usuário escolha o critério de ordenação
        escolha = input("\nOrdenar por:\n\n1 - Vitórias\n2 - Empates\n3 - Derrotas\n4 - VOLTAR\n\n")

        if escolha == '2':
            # Ordena por empates em ordem decrescente
            tabela_ordenada = sorted(totais_empates.items(), key=lambda x: x[1], reverse=True)
            criterio = "empates"
        elif escolha == '3':
            # Ordena por derrotas em ordem decrescente
            tabela_ordenada = sorted(totais_derrotas.items(), key=lambda x: x[1], reverse=True)
            criterio = "derrotas"
        elif escolha == '1':
            # Ordena por vitórias em ordem decrescente
            tabela_ordenada = sorted(totais_vitorias.items(), key=lambda x: x[1], reverse=True)
            criterio = "vitórias"
        elif escolha == '4':
            break
        else:
            print("\nOpção inválida. Por favor, tente novamente.\n")
            continue

# Exibição da tabela com a formatação desejada
        print(f"\nTimes com mais {criterio}:")
        print("\n")

        # Define o tamanho da linha baseado nos cabeçalhos
        tamanho_linha = 47

        print("┌" + "─" * tamanho_linha + "┐")  # Início da borda superior
        print("│" + f"{'Pos':<4} {'Time':<20} {criterio.capitalize():<10} {'Partidas':<10}│")  # Cabeçalho
        print("├" + "─" * tamanho_linha + "┤")  # Linha horizontal após o cabeçalho

        # Exibição dos times e suas estatísticas
        for i, (time, valor) in enumerate(tabela_ordenada, start=1):
            partidas_jogadas = totais_partidas.get(time, 0)
            print("│" + f"{i:<4} {time:<20} {valor:<10} {partidas_jogadas:<10}│")  # Dados da tabela

        print("└" + "─" * tamanho_linha + "┘")  # Borda inferior
        print("\n")










def media_gols_feitos():
    """Calcula e lista as médias de gols feitos por time, ordenando do melhor para o pior."""
    # Carrega o histórico de gols
    historico_gols = carregar_historico_gols()

    # Inicializa um dicionário para armazenar os totais e partidas jogadas
    totais_gols_feitos = {}
    partidas_jogadas = {}

    # Soma todos os gols feitos e partidas jogadas de cada simulação
    for simulacao in historico_gols:
        if "gols" in simulacao and "partidas_jogadas" in simulacao:
            for time, gols in simulacao["gols"].items():
                if time not in totais_gols_feitos:
                    totais_gols_feitos[time] = 0
                    partidas_jogadas[time] = 0
                totais_gols_feitos[time] += gols
                partidas_jogadas[time] += simulacao["partidas_jogadas"].get(time, 0)

    # Calcula a média de gols feitos
    medias_gols_feitos = {time: totais_gols_feitos[time] / partidas_jogadas[time] 
                           for time in totais_gols_feitos}

    # Ordena os times pela média de gols feitos
    melhores_gols_feitos = sorted(medias_gols_feitos.items(), key=lambda x: x[1], reverse=True)

    # Impressão das médias de gols feitos
    print("Média de Gols Feitos por Time:")
    print("┌" + "─" * 44 + "┐")
    print(f"│{'Time'.ljust(20)}│ {'Média de Gols Feitos'.ljust(22)}│")
    print("├" + "─" * 44 + "┤")

    for time, media in melhores_gols_feitos:
        print(f"│{time.ljust(20)}│ {media:.2f}                  │".ljust(22))

    print("└" + "─" * 44 + "┘")




def media_gols_sofridos():
    """Calcula e lista as médias de gols sofridos por time, ordenando do melhor para o pior."""
    # Carrega o histórico de gols
    historico_gols = carregar_historico_gols()

    # Inicializa um dicionário para armazenar os totais e partidas jogadas
    totais_gols_sofridos = {}
    partidas_jogadas = {}

    # Soma todos os gols sofridos e partidas jogadas de cada simulação
    for simulacao in historico_gols:
        if "gols_sofridos" in simulacao and "partidas_jogadas" in simulacao:
            for time, gols_sofridos in simulacao["gols_sofridos"].items():
                if time not in totais_gols_sofridos:
                    totais_gols_sofridos[time] = 0
                    partidas_jogadas[time] = 0
                totais_gols_sofridos[time] += gols_sofridos
                partidas_jogadas[time] += simulacao["partidas_jogadas"].get(time, 0)

    # Calcula a média de gols sofridos
    medias_gols_sofridos = {time: totais_gols_sofridos[time] / partidas_jogadas[time] 
                             for time in totais_gols_sofridos}

    # Ordena os times pela média de gols sofridos (menor média é melhor)
    melhores_defesas = sorted(medias_gols_sofridos.items(), key=lambda x: x[1])

    # Impressão das médias de gols sofridos
    print("Média de Gols Sofridos por Time:")
    print("┌" + "─" * 44 + "┐")
    print(f"│{'Time'.ljust(20)}│ {'Média de Gols Sofridos'.ljust(22)}│")
    print("├" + "─" * 44 + "┤")

    for time, media in melhores_defesas:
        print(f"│{time.ljust(20)}│ {media:.2f}                  │".ljust(22))

    print("└" + "─" * 44 + "┘")





























def exibir_playoffs(classificacao):
    # Obtém os classificados para os playoffs (9º a 24º)
    classificados = sorted(classificacao.items(), key=lambda x: (x[1]['pontos'], x[1]['saldo_gols'], x[1]['gols_marcados']), reverse=True)

    print("\nConfrontos dos playoffs:")
    print("\n")
    
    confrontos_playoffs = [
        (classificados[8][0], classificados[23][0]),  # 9º x 24º
        (classificados[9][0], classificados[22][0]),  # 10º x 23º
        (classificados[10][0], classificados[21][0]),  # 11º x 22º
        (classificados[11][0], classificados[20][0]),  # 12º x 21º
        (classificados[12][0], classificados[19][0]),  # 13º x 20º
        (classificados[13][0], classificados[18][0]),  # 14º x 19º
        (classificados[14][0], classificados[17][0]),  # 15º x 18º
        (classificados[15][0], classificados[16][0]),  # 16º x 17º
    ]
    
    # Determina o maior comprimento de nomes de times para formatação
    max_len_time = max(len(time1) + len(time2) for time1, time2 in confrontos_playoffs)
    if max_len_time % 2 == 0:
        max_len_time += 1
    tamanho_linha = max_len_time + 28  # Adiciona uma margem de 28 caracteres
    metade = (tamanho_linha - 5) // 2

    # Exibe os confrontos formatados
    print("┌" + "─" * tamanho_linha + "┐")
    print("├" + "─" * tamanho_linha + "┤")
    
    for time1, time2 in confrontos_playoffs:
        print("| {:>{}} x {:<{}} |".format(time1, metade, time2, metade))
    
    print("└" + "─" * tamanho_linha + "┘")


def simular_playoff(classificacao):
    global maiores_goleadas_mata_mata  # Para garantir que a variável seja acessível
    maiores_goleadas_mata_mata = []  # Inicializa ou limpa a lista

    # Obtém os classificados para os playoffs (9º a 24º)
    classificados = sorted(classificacao.items(), key=lambda x: (x[1]['pontos'], x[1]['saldo_gols'], x[1]['gols_marcados']), reverse=True)

    confrontos_playoffs = [
        (classificados[8][0], classificados[23][0]),  # 9º x 24º
        (classificados[9][0], classificados[22][0]),  # 10º x 23º
        (classificados[10][0], classificados[21][0]),  # 11º x 22º
        (classificados[11][0], classificados[20][0]),  # 12º x 21º
        (classificados[12][0], classificados[19][0]),  # 13º x 20º
        (classificados[13][0], classificados[18][0]),  # 14º x 19º
        (classificados[14][0], classificados[17][0]),  # 15º x 18º
        (classificados[15][0], classificados[16][0]),  # 16º x 17º
    ]

    # Calcula o comprimento máximo das linhas baseado no tamanho dos nomes dos times
    max_len_time = max(len(time1) + len(time2) for time1, time2 in confrontos_playoffs)
    if max_len_time % 2 == 0:
        max_len_time += 1
    tamanho_linha = max_len_time + 28  # Adiciona uma margem de 8 caracteres
    metade = (tamanho_linha - 13) //2 

    resultados_ida = {}
    print("\nJogo de ida - Playoffs:")
    print("\n")
    print("┌" + "─" * tamanho_linha + "┐")
    print("| {:^{}} | {:^1} x {:^1} | {:^{}} |".format("Casa", metade, "", "", "Fora", metade))
    print("├" + "─" * tamanho_linha + "┤")

    for time1, time2 in confrontos_playoffs:
        # Gera os gols para ambos os times
        gols_time1, gols_time2 = gerar_gols(time1, time2)

        # Salva o resultado da partida de ida
        resultados_ida[(time1, time2)] = (gols_time1, gols_time2)

        # Atualiza as maiores goleadas da fase de mata-mata
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
        
        # Atualiza o JSON e exibe o resultado
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
        
        # Atualiza as maiores goleadas da fase de mata-mata para o jogo de volta
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
        
        # Atualiza o JSON e exibe o resultado
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

    # Calcula o comprimento máximo das linhas baseado no tamanho dos nomes dos times
    confrontos_playoffs = [(time1, time2) for (time1, time2), _ in resultados_ida.items()]
    max_len_time = max(len(time1) + len(time2) for time1, time2 in confrontos_playoffs)
    if max_len_time % 2 == 0:
        max_len_time += 1
    tamanho_linha = max_len_time + 28  # Adiciona uma margem de 28 caracteres
    metade = (tamanho_linha - 13) // 2
    print("\n")
    print("\nPlacar Agregado - Playoffs:")
    print("\n")
    print("┌" + "─" * tamanho_linha + "┐")
    print("├" + "─" * tamanho_linha + "┤")

    for (time1, time2), (gols_ida1, gols_ida2) in resultados_ida.items():
        gols_volta2, gols_volta1 = resultados_volta[(time2, time1)]  # Usar o par correto
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
    # Obtém os 8 primeiros colocados
    primeiros_colocados = sorted(classificacao.items(), key=lambda x: (x[1]['pontos'], x[1]['saldo_gols'], x[1]['gols_marcados']), reverse=True)[:8]
    
    print("\nConfrontos das Oitavas de Final:")
    print("\n")
    
    confrontos_oitavas = [
        (primeiros_colocados[0][0], vencedores[0]),  # 1º x Vencedor 1
        (primeiros_colocados[1][0], vencedores[1]),  # 2º x Vencedor 2
        (primeiros_colocados[2][0], vencedores[2]),  # 3º x Vencedor 3
        (primeiros_colocados[3][0], vencedores[3]),  # 4º x Vencedor 4
        (primeiros_colocados[4][0], vencedores[4]),  # 5º x Vencedor 5
        (primeiros_colocados[5][0], vencedores[5]),  # 6º x Vencedor 6
        (primeiros_colocados[6][0], vencedores[6]),  # 7º x Vencedor 7
        (primeiros_colocados[7][0], vencedores[7]),  # 8º x Vencedor 8
    ]
    
    max_len_time = max(len(time1) + len(time2) for time1, time2 in confrontos_oitavas)
    if max_len_time % 2 == 0:
        max_len_time += 1
    tamanho_linha = max_len_time + 28  # Adiciona uma margem de 28 caracteres
    metade = (tamanho_linha - 5) // 2

    # Exibe os confrontos formatados
    print("┌" + "─" * tamanho_linha + "┐")
    print("├" + "─" * tamanho_linha + "┤")
    
    for time1, time2 in confrontos_oitavas:
        print("| {:>{}} x {:<{}} |".format(time1, metade, time2, metade))
    
    print("└" + "─" * tamanho_linha + "┘")




def simular_oitavas(classificacao, vencedores):
    global maiores_goleadas_mata_mata  # Certifica-se de que a variável é acessível

    # Ordena os primeiros colocados pela pontuação, saldo de gols e gols marcados
    primeiros_colocados = sorted(classificacao.items(), key=lambda x: (x[1]['pontos'], x[1]['saldo_gols'], x[1]['gols_marcados']), reverse=True)

    # Define os confrontos das oitavas de final
    confrontos_oitavas = [
        (primeiros_colocados[0][0], vencedores[0]),  # 1º x Vencedor 1
        (primeiros_colocados[1][0], vencedores[1]),  # 2º x Vencedor 2
        (primeiros_colocados[2][0], vencedores[2]),  # 3º x Vencedor 3
        (primeiros_colocados[3][0], vencedores[3]),  # 4º x Vencedor 4
        (primeiros_colocados[4][0], vencedores[4]),  # 5º x Vencedor 5
        (primeiros_colocados[5][0], vencedores[5]),  # 6º x Vencedor 6
        (primeiros_colocados[6][0], vencedores[6]),  # 7º x Vencedor 7
        (primeiros_colocados[7][0], vencedores[7]),  # 8º x Vencedor 8
    ]

    max_len_time = max(len(time1) + len(time2) for time1, time2 in confrontos_oitavas)
    if max_len_time % 2 == 0:
        max_len_time += 1
    tamanho_linha = max_len_time + 28  # Adiciona uma margem de 8 caracteres
    metade = (tamanho_linha - 13) //2 

    resultados_ida = {}
    print("\nJogo de ida - Oitavas de Final:")
    print("\n")
    print("┌" + "─" * tamanho_linha + "┐")
    print("| {:^{}} | {:^1} x {:^1} | {:^{}} |".format("Casa", metade, "", "", "Fora", metade))
    print("├" + "─" * tamanho_linha + "┤")
    for time1, time2 in confrontos_oitavas:
        # Gera os gols para o jogo de ida
        gols_time1, gols_time2 = gerar_gols(time1, time2)
        
        # Salva o resultado do jogo de ida
        resultados_ida[(time1, time2)] = (gols_time1, gols_time2)
        
        # Atualiza os gols marcados e sofridos no arquivo JSON
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
        # Exibe o resultado
        print("| {:>{}} | {:<1} x {:<1} | {:<{}} |".format(time1, metade, gols_time1, gols_time2, time2, metade))
    
        # Atualiza as maiores goleadas
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
        # Gera os gols para o jogo de volta
        gols_time1, gols_time2 = gerar_gols(time1, time2)
        
        # Salva o resultado do jogo de volta
        resultados_volta[(time1, time2)] = (gols_time1, gols_time2)
        
        # Atualiza os gols marcados e sofridos no arquivo JSON
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
        
        # Exibe o resultado
        print("| {:>{}} | {:<1} x {:<1} | {:<{}} |".format(time1, metade, gols_time1, gols_time2, time2, metade))

        # Atualiza as maiores goleadas
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
    tamanho_linha = max_len_time + 28  # Adiciona uma margem de 28 caracteres
    metade = (tamanho_linha - 13) // 2
    print("\n")
    print("\nPlacar Agregado - Oitavas de Final:")
    print("\n")
    print("┌" + "─" * tamanho_linha + "┐")
    print("├" + "─" * tamanho_linha + "┤")


    for (time1, time2), (gols_ida1, gols_ida2) in resultados_ida.items():
        gols_volta2, gols_volta1 = resultados_volta[(time2, time1)]  # Usar o par correto
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
    # Embaralhar aleatoriamente os vencedores
    random.shuffle(vencedores_oitavas)
    
    # Formar 4 pares (confrontos) com os 8 times
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

    # Exibe os confrontos formatados
    print("┌" + "─" * tamanho_linha + "┐")
    print("├" + "─" * tamanho_linha + "┤")
    
    for time1, time2 in quartas_de_final:
        print("| {:>{}} x {:<{}} |".format(time1, metade, time2, metade))
    
    print("└" + "─" * tamanho_linha + "┘")



def simular_quartas(quartas_de_final):
    global maiores_goleadas_mata_mata  # Certifica-se de que a variável global é acessível

    max_len_time = max(len(time1) + len(time2) for time1, time2 in quartas_de_final)
    if max_len_time % 2 == 0:
        max_len_time += 1
    tamanho_linha = max_len_time + 28  # Adiciona uma margem de 28 caracteres para formatação
    metade = (tamanho_linha - 13) // 2

    resultados_ida = {}
    print("\nJogo de ida - Quartas de Final:")
    print("\n")
    print("┌" + "─" * tamanho_linha + "┐")
    print("| {:^{}} | {:^1} x {:^1} | {:^{}} |".format("Casa", metade, "", "", "Fora", metade))
    print("├" + "─" * tamanho_linha + "┤")
    
    # Simula jogos de ida
    for time1, time2 in quartas_de_final:
        gols_time1, gols_time2 = gerar_gols(time1, time2)
        
        # Salva os resultados
        resultados_ida[(time1, time2)] = (gols_time1, gols_time2)
        
        # Atualiza os gols marcados e sofridos
        atualizar_gols_acumulados_json(time1, gols_time1, gols_time2)  # Time1 marcou gols_time1 e sofreu gols_time2
        atualizar_gols_acumulados_json(time2, gols_time2, gols_time1)  # Time2 marcou gols_time2 e sofreu gols_time1
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
        # Exibe o resultado
        print("| {:>{}} | {:<1} x {:<1} | {:<{}} |".format(time1, metade, gols_time1, gols_time2, time2, metade))
    
    print("└" + "─" * tamanho_linha + "┘")

    resultados_volta = {}
    print("\n")
    print("\nJogo de volta - Quartas de Final:")
    print("\n")
    print("┌" + "─" * tamanho_linha + "┐")
    print("| {:^{}} | {:^1} x {:^1} | {:^{}} |".format("Casa", metade, "", "", "Fora", metade))
    print("├" + "─" * tamanho_linha + "┤")
    
    # Simula jogos de volta
    for time2, time1 in quartas_de_final:
        gols_time1, gols_time2 = gerar_gols(time1, time2)
        
        # Salva os resultados
        resultados_volta[(time1, time2)] = (gols_time1, gols_time2)
        
        # Atualiza os gols marcados e sofridos
        atualizar_gols_acumulados_json(time1, gols_time1, gols_time2)  # Time1 marcou gols_time1 e sofreu gols_time2
        atualizar_gols_acumulados_json(time2, gols_time2, gols_time1)  # Time2 marcou gols_time2 e sofreu gols_time1
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
        # Exibe o resultado
        print("| {:>{}} | {:<1} x {:<1} | {:<{}} |".format(time1, metade, gols_time1, gols_time2, time2, metade))
    
    print("└" + "─" * tamanho_linha + "┘")
    
    return resultados_ida, resultados_volta




def placar_final_quartas(quartas_de_final):
    resultados_ida, resultados_volta = simular_quartas(quartas_de_final)
    vencedores_quartas = []
    confrontos_quartas = [(time1, time2) for (time1, time2), _ in resultados_ida.items()]
    max_len_time = max(len(time1) + len(time2) for time1, time2 in confrontos_quartas)
    if max_len_time % 2 == 0:
        max_len_time += 1
    tamanho_linha = max_len_time + 28  # Adiciona uma margem de 28 caracteres
    metade = (tamanho_linha - 13) // 2
    print("\n")
    print("\nPlacar Agregado - Quartas de Final:")
    print("\n")
    print("┌" + "─" * tamanho_linha + "┐")
    print("├" + "─" * tamanho_linha + "┤")


    # Calcula o placar agregado e determina os vencedores
    for (time1, time2), (gols_ida1, gols_ida2) in resultados_ida.items():
        gols_volta2, gols_volta1 = resultados_volta[(time2, time1)]  # Usar o par correto
        total_time1 = gols_ida1 + gols_volta1
        total_time2 = gols_ida2 + gols_volta2
        print("| {:>{}} | {:<5} | {:<{}} |".format(time1, metade, f"{total_time1} x {total_time2}", time2, metade))

        # Caso de empate no placar agregado, simula pênaltis
        if total_time1 == total_time2:
            gols_penaltis1, gols_penaltis2 = simular_penaltis(time1, time2)
            print("| {:>{}}  {:^5}  {:<{}} |".format("Pen", metade, f"({gols_penaltis1} - {gols_penaltis2})", "", metade))
            vencedor_quartas = time1 if gols_penaltis1 > gols_penaltis2 else time2
            vencedores_quartas.append(vencedor_quartas)
        else:
            vencedor_quartas = time1 if total_time1 > total_time2 else time2
            vencedores_quartas.append(vencedor_quartas)

    print("└" + "─" * tamanho_linha + "┘")

    # Exibe os vencedores das quartas de final
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
    tamanho_linha = max_len_time + 28  # Adiciona uma margem de 28 caracteres
    metade = (tamanho_linha - 5) // 2
    
    print("┌" + "─" * tamanho_linha + "┐")
    print("├" + "─" * tamanho_linha + "┤")
    
    # Confronto 1: [0] vs [1]
    print("| {:>{}} x {:<{}} |".format(vencedores_quartas[0], metade, vencedores_quartas[1], metade))
    
    # Confronto 2: [2] vs [3]
    print("| {:>{}} x {:<{}} |".format(vencedores_quartas[2], metade, vencedores_quartas[3], metade))

    print("└" + "─" * tamanho_linha + "┘")



def simular_semifinais(vencedores_quartas):
    global maiores_goleadas_mata_mata  # Variável global para armazenar as maiores goleadas

    # Calcula o tamanho da linha com base no comprimento dos nomes dos times
    confrontos_semis = [(vencedores_quartas[i], vencedores_quartas[i + 1]) for i in range(0, len(vencedores_quartas), 2)]
    max_len_time = max(len(time1) + len(time2) for time1, time2 in confrontos_semis)
    if max_len_time % 2 == 0:
        max_len_time += 1
    tamanho_linha = max_len_time + 28  # Adiciona uma margem de 28 caracteres
    metade = (tamanho_linha - 13) // 2

    resultados_ida = {}
    resultados_volta = {}

    # Jogo de ida
    print("\nJogos de ida - Semi-final:")
    print("\n")
    print("┌" + "─" * tamanho_linha + "┐")
    print("| {:^{}} | {:^1} x {:^1} | {:^{}} |".format("Casa", metade, "", "", "Fora", metade))
    print("├" + "─" * tamanho_linha + "┤")
    
    for i in range(0, len(vencedores_quartas), 2):  # Percorre a lista de 2 em 2
        time1 = vencedores_quartas[i]
        time2 = vencedores_quartas[i + 1]
        gols_time1, gols_time2 = gerar_gols(time1, time2)
        
        # Salva os resultados
        resultados_ida[(time1, time2)] = (gols_time1, gols_time2)
        
        # Atualiza os gols marcados e sofridos
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
        
        # Exibe o resultado
        print("| {:>{}} | {:<1} x {:<1} | {:<{}} |".format(time1, metade, gols_time1, gols_time2, time2, metade))

        # Atualiza as maiores goleadas
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

    # Jogo de volta
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
        
        # Salva os resultados
        resultados_volta[(time2, time1)] = (gols_time2, gols_time1)
        
        # Atualiza os gols marcados e sofridos
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
        
        # Exibe o resultado
        print("| {:>{}} | {:<1} x {:<1} | {:<{}} |".format(time1, metade, gols_time1, gols_time2, time2, metade))

        # Atualiza as maiores goleadas
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
    tamanho_linha = max_len_time + 28  # Adiciona uma margem de 28 caracteres
    metade = (tamanho_linha - 13) // 2
    print("\n")
    print("\nPlacar Agregado - Semifinais:")
    print("\n")
    print("┌" + "─" * tamanho_linha + "┐")
    print("├" + "─" * tamanho_linha + "┤")


    # Calcula o placar agregado e determina os vencedores
    for (time1, time2), (gols_ida1, gols_ida2) in resultados_ida.items():
        gols_volta2, gols_volta1 = resultados_volta[(time2, time1)]  # Usar o par correto
        total_time1 = gols_ida1 + gols_volta1
        total_time2 = gols_ida2 + gols_volta2
        print("| {:>{}} | {:<5} | {:<{}} |".format(time1, metade, f"{total_time1} x {total_time2}", time2, metade))

        # Caso de empate no placar agregado, simula pênaltis
        if total_time1 == total_time2:
            gols_penaltis1, gols_penaltis2 = simular_penaltis(time1, time2)
            print("| {:>{}}  {:^5}  {:<{}} |".format("Pen", metade, f"({gols_penaltis1} - {gols_penaltis2})", "", metade))
            vencedor_semis = time1 if gols_penaltis1 > gols_penaltis2 else time2
            vencedores_semis.append(vencedor_semis)
        else:
            vencedor_semis = time1 if total_time1 > total_time2 else time2
            vencedores_semis.append(vencedor_semis)
    
    print("└" + "─" * tamanho_linha + "┘")

    # Exibe os vencedores das semifinais
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
    tamanho_linha = max_len_time + 28  # Adiciona uma margem de 28 caracteres
    metade = (tamanho_linha - 5) // 2
    print("┌" + "─" * tamanho_linha + "┐")
    print("├" + "─" * tamanho_linha + "┤")
    # Confronto 1: [0] vs [1]
    print("| {:>{}} x {:<{}} |".format(vencedores_semis[0], metade, vencedores_semis[1], metade))
    print("└" + "─" * tamanho_linha + "┘")
    

def simular_final(vencedores_semis):
    resultado = {}
    
    time1 = vencedores_semis[0]
    time2 = vencedores_semis[1]
    
    # Simula o único jogo da final
    gols_time1, gols_time2 = gerar_gols(time1, time2)
    resultado[(time1, time2)] = (gols_time1, gols_time2)

    return resultado


def placar_final_final(vencedores_semis):
    global maiores_goleadas_mata_mata
    resultado = simular_final(vencedores_semis)
    vencedor_final = []
    vice_final = []
    gols_vencedor = ""
    gols_vice = ""

    # Combina o comprimento dos dois times em um confronto
    confronto = [(time1, time2) for (time1, time2), _ in resultado.items()]
    max_len_time = max(len(time1) + len(time2) + 3 for time1, time2 in confronto)  # +3 para o " x " no placar

    if max_len_time % 2 == 0:
        max_len_time += 1

    # Tamanho da linha com margem para espaçamento e formatação
    tamanho_linha = max_len_time + 28  
    metade = (tamanho_linha - 13) // 2 

    print("\nResultado Final:\n")
    print("\n")
    print("┌" + "─" * tamanho_linha + "┐")
    print("├" + "─" * tamanho_linha + "┤")

    # Calcula o placar final e determina o vencedor
    for (time1, time2), (gols_time1, gols_time2) in resultado.items():
        atualizar_gols_acumulados_json(time1, gols_time1, gols_time2)
        atualizar_gols_acumulados_json(time2, gols_time2, gols_time1)
        atualizar_partidas_jogadas(time1)
        atualizar_partidas_jogadas(time2)

        # Verifica o resultado da partida e atualiza vitórias, empates ou derrotas
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

        # Verifica a maior goleada
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

        # Caso de empate no tempo normal
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










# Função para atualizar a pontuação da tabela de classificação
def atualizar_classificacao(time_casa, gols_casa, time_fora, gols_fora, classificacao):
    if gols_casa > gols_fora:
        classificacao[time_casa]['pontos'] += 3
        classificacao[time_casa]['vitorias'] += 1
        classificacao[time_fora]['derrotas'] += 1  # Incrementa derrotas do time visitante
    elif gols_casa < gols_fora:
        classificacao[time_fora]['pontos'] += 3
        classificacao[time_fora]['vitorias'] += 1
        classificacao[time_casa]['derrotas'] += 1  # Incrementa derrotas do time da casa
    else:
        classificacao[time_casa]['pontos'] += 1
        classificacao[time_fora]['pontos'] += 1
        classificacao[time_casa]['empates'] += 1  # Incrementa empates do time da casa
        classificacao[time_fora]['empates'] += 1 

        # Atualiza os gols marcados
    classificacao[time_casa]['gols_marcados'] += gols_casa
    classificacao[time_fora]['gols_marcados'] += gols_fora
    classificacao[time_casa]['gols_sofridos'] += gols_fora  # Gols sofridos pelo time da casa
    classificacao[time_fora]['gols_sofridos'] += gols_casa  # Gols sofridos pelo time visitante

    classificacao[time_casa]['saldo_gols'] = classificacao[time_casa]['gols_marcados'] - classificacao[time_casa]['gols_sofridos']
    classificacao[time_fora]['saldo_gols'] = classificacao[time_fora]['gols_marcados'] - classificacao[time_fora]['gols_sofridos']

def inicializar_classificacao(potes):
    classificacao = {}
    for pot in potes:
        for time in pot:
            classificacao[time] = {'pontos': 0, 'gols_marcados': 0, 'gols_sofridos': 0, 'vitorias': 0, 'derrotas': 0, 'empates': 0}
    return classificacao








maiores_goleadas = []

def simular_partida(time_casa, time_fora, resultados, classificacao):
    global maiores_goleadas
    # Verifica se o resultado já existe, para evitar recalcular
    if (time_casa, time_fora) in resultados:
        return resultados[(time_casa, time_fora)]
    if (time_fora, time_casa) in resultados:
        return resultados[(time_fora, time_casa)]

    # Gera os gols para os dois times
    gols_casa, gols_fora = gerar_gols(time_casa, time_fora)

    # Atualiza a classificação com os resultados dos gols
    atualizar_classificacao(time_casa, gols_casa, time_fora, gols_fora, classificacao)

    # Atualiza o arquivo JSON com os gols marcados e sofridos
    atualizar_gols_acumulados_json(time_casa, gols_casa, gols_fora)  # Time da casa marcou e sofreu
    atualizar_gols_acumulados_json(time_fora, gols_fora, gols_casa)  # Time visitante marcou e sofreu
    atualizar_partidas_jogadas(time_casa)
    atualizar_partidas_jogadas(time_fora)

    # Verifica o resultado da partida e atualiza vitórias, empates ou derrotas
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
    # Formata o resultado da partida e o salva nos resultados
    resultado = "{:>20} {:<1} x {:<1} {:<20}".format(time_casa, gols_casa, gols_fora, time_fora)
    resultados[(time_casa, time_fora)] = resultado

    # Calcula a diferença de gols
    diferenca_gols = abs(gols_casa - gols_fora)
    
    # Se a diferença de gols é maior que a maior existente, reinicia a lista
    if len(maiores_goleadas) == 0 or diferenca_gols > maiores_goleadas[0]['diferenca']:
        maiores_goleadas = [{
            "time1": time_casa,
            "gols_time1": gols_casa,
            "time2": time_fora,
            "gols_time2": gols_fora,
            "diferenca": diferenca_gols
        }]
    # Se a diferença de gols é igual à maior, adiciona à lista
    elif diferenca_gols == maiores_goleadas[0]['diferenca']:
        maiores_goleadas.append({
            "time1": time_casa,
            "gols_time1": gols_casa,
            "time2": time_fora,
            "gols_time2": gols_fora,
            "diferenca": diferenca_gols
        })

    return resultado
    



def salvar_resultados_json(time_casa, gols_casa, time_fora, gols_fora, fase):
    # Carrega os dados existentes do arquivo, ou cria uma estrutura vazia
    try:
        with open('resultados_partidas_atual.json', 'r') as file:
            resultados = json.load(file)
    except FileNotFoundError:
        resultados = {}

    # Inicializa a estrutura para o time da casa se não existir
    if time_casa not in resultados:
        resultados[time_casa] = {
            "jogos": []
        }
    # Inicializa a estrutura para o time de fora se não existir
    if time_fora not in resultados:
        resultados[time_fora] = {
            "jogos": []
        }

    # Adiciona os novos resultados para o time da casa
    resultados[time_casa]["jogos"].append({
        "adversario": time_fora,
        "gols_marcados": gols_casa,
        "gols_sofridos": gols_fora,
        "fase": fase  # Adiciona a fase do jogo
    })

    # Adiciona os novos resultados para o time de fora
    resultados[time_fora]["jogos"].append({
        "adversario": time_casa,
        "gols_marcados": gols_fora,
        "gols_sofridos": gols_casa,
        "fase": fase  # Adiciona a fase do jogo
    })

    # Salva os dados atualizados de volta no arquivo
    with open('resultados_partidas_atual.json', 'w') as file:
        json.dump(resultados, file, indent=4)




def transferir_para_historico():
    # Carrega os dados do arquivo de resultados
    try:
        with open('resultados_partidas_atual.json', 'r') as file:
            resultados = json.load(file)
    except FileNotFoundError:
        print("Arquivo de resultados não encontrado.")
        return

    # Verifica se algum time tem mais de 8 jogos na fase "grupos"
    for time, dados in resultados.items():
        jogos_grupos = [jogo for jogo in dados["jogos"] if jogo["fase"].lower() == "grupos"]
        if len(jogos_grupos) > 8:
            print(f"Erro: Dados anormais detectados. Dados não salvos no histórico.")
            return

    # Carrega o histórico ou cria um novo
    try:
        with open('historico_resultados.json', 'r') as file:
            historico = json.load(file)
    except FileNotFoundError:
        historico = []

    # Determina o número da próxima simulação
    simulacao_numero = len(historico) + 1

    # Cria um novo registro para a simulação
    nova_simulacao = {
        "simulacao": simulacao_numero,
        "resultados": resultados
    }

    # Adiciona a nova simulação ao histórico
    historico.append(nova_simulacao)

    # Salva o histórico atualizado
    with open('historico_resultados.json', 'w') as file:
        json.dump(historico, file, indent=4)

    # Deleta o arquivo de resultados atual
    if os.path.exists('resultados_partidas_atual.json'):
        os.remove('resultados_partidas_atual.json')
    else:
        print("O arquivo do histórico não foi encontrado.")




def listar_simulacoes():

    if not all(os.path.exists(arquivo) for arquivo in ["campeoes.json", "historico_gols.json", "historico_resultados.json"]):
        print("\nArquivo(s) não encontrado(s).\n")
        return
    try:
        # Carrega o arquivo campeões
        with open("campeoes.json", "r") as file:
            campeoes = json.load(file)
    except FileNotFoundError:
        campeoes = []

    if not campeoes:
        print("\n\nNenhuma simulação encontrada.\n\n")
        return

    # Cria uma lista com os dados formatados para calcular o comprimento máximo
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


    # Determina o comprimento máximo baseado nos dados de simulações
    tamanho_linha = 97

    # Cabeçalho formatado
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

        # Formata a linha com os dados
        linha_formatada = f"│{simulacao}│{vencedor}│{placar}│{vice}│{nivel}              │"
        print(linha_formatada)

    # Rodapé formatado
    print(f"{'└' + '─' * tamanho_linha + '┘'}")


def excluir_simulacao_por_numero(simulacao_numero):
    arquivos = ["campeoes.json", "historico_gols.json", "historico_resultados.json"]

    # Função auxiliar para carregar e remover simulação de um arquivo
    def remover_simulacao_arquivo(nome_arquivo):
        if os.path.exists(nome_arquivo):
            with open(nome_arquivo, 'r') as file:
                dados = json.load(file)

            # Filtra as simulações para remover aquela com o número desejado
            dados_filtrados = [simulacao for simulacao in dados if simulacao.get("simulacao") != simulacao_numero]

            for i, simulacao in enumerate(dados_filtrados, start=1):
                simulacao["simulacao"] = i

            # Escreve os dados filtrados de volta no arquivo
            with open(nome_arquivo, 'w') as file:
                json.dump(dados_filtrados, file, indent=4)

    # Aplica a exclusão nos três arquivos
    for arquivo in arquivos:
        remover_simulacao_arquivo(arquivo)

    print(f"\nSimulação {simulacao_numero} removida dos arquivos!\n")

# Função principal para interação com o usuário
def excluir_simulacao():
    if not all(os.path.exists(arquivo) for arquivo in ["campeoes.json", "historico_gols.json", "historico_resultados.json"]):
        print("\nArquivo(s) não encontrado(s).\n")
        return
    else:
    # Lista todas as simulações
        while True:
            
            listar_simulacoes()

            # Solicita ao usuário o número da simulação a ser excluída
            entrada = input("\n\nDigite o número da simulação que deseja excluir ou 'S' para voltar:\n\n")
            
            # Verifica se o usuário deseja voltar
            if entrada.lower() == 's':
                print("\nVoltando...\n")
                return

            # Tenta converter a entrada em número
            try:
                simulacao_numero = int(entrada)

                # Verifica se o número da simulação é válido
                with open("campeoes.json", "r") as file:
                    campeoes = json.load(file)
                
                if simulacao_numero < 1 or simulacao_numero > len(campeoes):
                    print(f"\n\nSimulação {simulacao_numero} não existe. Tente novamente.\n\n")
                else:
                    # Confirmação antes da exclusão
                    confirmacao = input(f"\n\nTem certeza de que deseja excluir a simulação {simulacao_numero}? Digite 'S' para confirmar a exclusão:\n\n")
                    if confirmacao.lower() == 's':
                        excluir_simulacao_por_numero(simulacao_numero)
                    else:
                        print("\n\nExclusão cancelada.\n\n")

            except ValueError:
                # Entrada inválida (não é um número)
                print("\n\nEntrada inválida! Por favor, insira um número de simulação válido.\n\n")












def exibir_classificacao(classificacao):
    # Ordena primeiro por pontos, depois por saldo de gols, e depois por gols marcados
    classificacao_ordenada = sorted(classificacao.items(), key=lambda x: (x[1]['pontos'], x[1]['saldo_gols'], x[1]['gols_marcados']), reverse=True)
    
    print("\nTabela de Classificação Final:")
    
    # Define o tamanho da linha baseado nos cabeçalhos
    tamanho_linha = 90
    print("\n")

    print("|" + "─" * tamanho_linha + "|")
    print("┌" + "─" * tamanho_linha + "┐")  # Início da borda superior
    print("│" + "{:<4} | {:<20} | {:<6} | {:<6} | {:<6} | {:<6} | {:<6} | {:<6} | {:<6}".format("Pos", "Time", "Pts", "GM", "GS", "SG", "V", "E", "D") + "│")  # Cabeçalho
    print("├" + "─" * tamanho_linha + "┤")  # Linha horizontal após o cabeçalho
    
    for i, (time, dados) in enumerate(classificacao_ordenada, start=1):
        time = time.upper()
        # Adiciona cor verde nos primeiros 8 colocados (apenas posição e nome)
        if i <= 8:
            posicao_nome = f"\033[32m{i:<4} | {time:<20}\033[0m"
        # Adiciona cor azul do 9º ao 24º colocados (apenas posição e nome)
        elif 9 <= i <= 24:
            posicao_nome = f"\033[34m{i:<4} | {time:<20}\033[0m"
        # Adiciona cor vermelha do 25º colocado em diante (apenas posição e nome)
        else:
            posicao_nome = f"\033[31m{i:<4} | {time:<20}\033[0m"
        
        # Exibe a linha da tabela com as cores aplicadas apenas na posição e no nome do time
        linha = f"{posicao_nome} | {dados['pontos']:<6} | {dados['gols_marcados']:<6} | {dados['gols_sofridos']:<6} | {dados['saldo_gols']:<6} | {dados['vitorias']:<6} | {dados['empates']:<6} | {dados['derrotas']:<6}"
        print("│" + linha + "│")
        print("├" + "─" * tamanho_linha + "┤")  # Linha horizontal entre as linhas da tabela
    
    print("└" + "─" * tamanho_linha + "┘")  # Borda inferior
    print("\n")
    print(f"\033[32m●\033[0m - Classificados para oitavas\n")
    print(f"\033[34m●\033[0m - Classificados para playoffs\n")
    print(f"\033[31m●\033[0m - Eliminados\n")







def simular_confrontos(home_away, resultados, classificacao):
    largura_total = 64  # Largura total para as caixas do nome e das partidas
    resultados_partidas = []

    for time in sorted(home_away.keys()):
        # Caixa para o nome do time (mesma largura da caixa de partidas)
        espacos_antes_time = (largura_total - len(time.upper()) - 4) // 2  # Centralizar o nome do time na caixa
        linha_superior_time = "┌" + "─" * (largura_total - 2) + "┐"  # Linha superior da caixa do nome
        resultado_time = f"|{' ' * espacos_antes_time}\033[32m{time.upper()}\033[0m{' ' * (largura_total - 2 - len(time.upper()) - espacos_antes_time)}|"
        linha_inferior_time = "└" + "─" * (largura_total - 2) + "┘"  # Linha inferior da caixa do nome

        # Adiciona a borda superior, nome do time centralizado, e borda inferior para a caixa do nome
        resultados_partidas.append(f"\n\n\n{linha_superior_time}\n{resultado_time}\n{linha_inferior_time}")

        # Caixa maior para as partidas
        linha_superior_partidas = "┌" + "─" * (largura_total - 2) + "┐"  # Linha superior da caixa de partidas
        linha_inferior_partidas = "└" + "─" * (largura_total - 2) + "┘"  # Linha inferior da caixa de partidas
        resultados_partidas.append(linha_superior_partidas)

        # Resultados das partidas (tanto "home" quanto "away")
        for adversario in home_away[time]["home"]:
            resultado = simular_partida(time, adversario, resultados, classificacao)
            resultado = resultado.replace(time, time.upper())  
            espacos_antes_resultado = (largura_total - len(resultado) - 4) // 2  # Centralizar resultado na caixa
            resultado_formatado = f"|{' ' * espacos_antes_resultado}{resultado}{' ' * (largura_total - 2 - len(resultado) - espacos_antes_resultado)}|"
            resultados_partidas.append(resultado_formatado)
        
        for adversario in home_away[time]["away"]:
            resultado = simular_partida(adversario, time, resultados, classificacao)
            resultado = resultado.replace(time, time.upper())  
            espacos_antes_resultado = (largura_total - len(resultado) - 4) // 2  # Centralizar resultado na caixa
            resultado_formatado = f"|{' ' * espacos_antes_resultado}{resultado}{' ' * (largura_total - 2 - len(resultado) - espacos_antes_resultado)}|"
            resultados_partidas.append(resultado_formatado)

        # Adiciona a borda inferior da caixa de partidas
        resultados_partidas.append(linha_inferior_partidas)
    
    return resultados_partidas












def print_trophy(vencedorFinal):
    # Códigos de escape para cores
    amarelo = "\033[33m"  # Cor amarela
    laranja = "\033[38;5;214m"  # Cor laranja (usando 256 colors)
    reset = "\033[0m"  # Reset para a cor padrão

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
        
        # Se o arquivo já existir, carregue o conteúdo
        if os.path.exists(nome_arquivo):
            with open(nome_arquivo, 'r') as file:
                historico_finais = json.load(file)
        else:
            historico_finais = []

        # Define o número da nova simulação com base na última
        numero_simulacao = len(historico_finais) + 1

        configuracao_atual = carregar_configuracao()
        nivel_gols_simulacao = configuracao_atual["nivel_gols"]

        # Adiciona os dados da final atual, incluindo o número da simulação
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

        # Escreve o conteúdo atualizado no arquivo
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

            # Dicionário para contar os títulos de cada time
            contador_titulos = {}

            # Contabiliza os títulos de cada time
            for final in historico_finais:
                campeao = final['campeao']['time']

                # Se o time já estiver no dicionário, incrementa o número de títulos
                if campeao in contador_titulos:
                    contador_titulos[campeao] += 1
                else:
                    # Se for a primeira vez, inicializa com 1 título
                    contador_titulos[campeao] = 1

            return contador_titulos
    else:
        return {}

def listar_campeoes_ordenados():
    # Conta os campeões e seus títulos
    campeoes = contar_campeoes()

    if campeoes:
        # Soma o total de títulos (simulações realizadas)
        total_simulacoes = sum(campeoes.values())

        # Ordena os campeões pelo número de títulos em ordem decrescente
        campeoes_ordenados = sorted(campeoes.items(), key=lambda item: item[1], reverse=True)

        # Exibe a frase com o número total de simulações
        print(f"\nLista de campeões após {total_simulacoes} simulação(ões):")
        print("\n")
        print(f"{'Nº'.ljust(4)}│ {'Time'.ljust(30)}│ {'Títulos'.ljust(10)}")
        print("─" * 50)

        # Exibe os campeões em formato numerado
        for i, (time, titulos) in enumerate(campeoes_ordenados, start=1):
            print(f"{str(i).ljust(4)}│ {time.ljust(30)}│ {str(titulos).ljust(10)}")
    else:
        print("\nNenhum campeão registrado ainda.")




def contar_vices():
    nome_arquivo = "campeoes.json"
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r') as file:
            historico_finais = json.load(file)

            # Dicionário para contar os vice-campeonatos de cada time
            contador_vices = {}

            # Contabiliza os vice-campeonatos de cada time
            for final in historico_finais:
                vice = final['vice']['time']

                # Se o time já estiver no dicionário, incrementa o número de vice-campeonatos
                if vice in contador_vices:
                    contador_vices[vice] += 1
                else:
                    # Se for a primeira vez, inicializa com 1 vice-campeonato
                    contador_vices[vice] = 1

            return contador_vices
    else:
        return {}

def listar_vices_ordenados():
    # Conta os vice-campeões e seus vice-campeonatos
    vices = contar_vices()

    if vices:
        # Soma o total de simulações realizadas (vices)
        total_simulacoes = sum(vices.values())

        # Ordena os vices pelo número de vice-campeonatos em ordem decrescente
        vices_ordenados = sorted(vices.items(), key=lambda item: item[1], reverse=True)

        # Exibe a frase com o número total de simulações
        print(f"\nLista de vice-campeões após {total_simulacoes} simulação(ões):")
        print("\n")
        print(f"{'Nº'.ljust(4)}│ {'Time'.ljust(30)}│ {'Vice-Campeonatos'.ljust(18)}")
        print("─" * 50)

        # Exibe os vice-campeões em formato numerado
        for i, (time, vices_count) in enumerate(vices_ordenados, start=1):
            print(f"{str(i).ljust(4)}│ {time.ljust(30)}│ {str(vices_count).ljust(18)}")
    else:
        print("\nNenhum vice-campeão registrado ainda.")





def verificar_time_no_historico(nome_time):
    """Verifica se o time existe no histórico de resultados."""
    # Transforma o nome_time em minúsculas para uma comparação consistente
    nome_time = nome_time.lower()

    # Carrega o histórico de resultados
    try:
        with open('historico_resultados.json', 'r') as file:
            historico = json.load(file)
    except FileNotFoundError:
        print("Arquivo de histórico não encontrado.")
        return False

    # Verifica cada simulação no histórico
    for simulacao in historico:
        resultados = simulacao['resultados']
        for time in resultados:
            # Compara os nomes convertidos para minúsculas para garantir consistência
            if nome_time == time.lower():
                return True
                
    return False



nome_arquivo_campeoes = "campeoes.json"
nome_arquivo_historico_gols = "historico_gols.json"


def pesquisar_campeao_por_time(nome_time):
    contador_campeao = 0
    contador_vice = 0

    # Verifica se o time está nos potes
    if not verificar_time_no_historico(nome_time):
        print(f"\nO time {nome_time.upper()} não existe nos registros.")
        return 0

    # Carregar campeões e vices do arquivo campeoes.json
    if os.path.exists(nome_arquivo_campeoes):
        with open(nome_arquivo_campeoes, 'r') as file:
            historico_finais = json.load(file)

            # Verifica se o time foi campeão ou vice-campeão
            for final in historico_finais:
                campeao_time = final['campeao']['time'].lower()  # Converte o nome do campeão para minúsculas
                vice_time = final['vice']['time'].lower()  # Converte o nome do vice-campeão para minúsculas

                # Compara ambos os nomes em minúsculas para campeões
                if campeao_time == nome_time.lower():
                    contador_campeao += 1  # Incrementa o contador de títulos de campeão

                # Compara ambos os nomes em minúsculas para vice-campe
                # Compara ambos os nomes em minúsculas para vice-campeões
                if vice_time == nome_time.lower():
                    contador_vice += 1  # Incrementa o contador de vice-campeonatos

    # Carregar estatísticas de gols do arquivo historico_gols.json
    historico_gols = carregar_historico_gols()
    gols_feitos = 0
    gols_sofridos = 0
    partidas_jogadas = 0
    participacoes = 0  # Contador de participações para o time
    vitorias = 0
    empates = 0
    derrotas = 0

    # Contadores de eliminações por fase
    eliminacoes_por_fase = {
        "grupos": 0,
        "playoffs": 0,
        "oitavas": 0,
        "quartas": 0,
        "semis": 0,
        "final": 0
    }

    # Percorrer o histórico de gols para encontrar as estatísticas do time
    nome_time_min = nome_time.lower()
    for simulacao in historico_gols:
        for time in simulacao['gols']:
            if time.lower() == nome_time_min:  # Compara minúsculas
                gols_feitos += simulacao['gols'][time]
                gols_sofridos += simulacao['gols_sofridos'][time]
                partidas_jogadas += simulacao['partidas_jogadas'][time]
                participacoes += 1
                vitorias += simulacao.get('vitorias', {}).get(time, 0)
                empates += simulacao.get('empates', {}).get(time, 0)
                derrotas += simulacao.get('derrotas', {}).get(time, 0)
                break  # Para evitar múltiplas adições, sair do loop após encontrar o time

    # Inicializar o contador de eliminações por fase
    eliminacoes_por_fase = {
        "grupos": 0,
        "playoffs": 0,
        "oitavas": 0,
        "quartas": 0,
        "semis": 0,
        "final": 0
    }

    nome_time_min = nome_time.lower()  # Converte a entrada do usuário para minúsculas

    # Lê o arquivo historico_resultados.json
    if not os.path.exists('historico_resultados.json'):
        print("\n")
        print("Sem informações salvas. O histórico pode estar com informações faltantes.")
        print("\n")
    else:
        try:
            with open('historico_resultados.json', 'r') as file:
                historico_resultados = json.load(file)
                
                # Verifica se o arquivo está vazio
                if not historico_resultados:
                    print("Histórico vazio")
                else:
                    for simulacao in historico_resultados:
                        # Converte os nomes dos times para minúsculas para comparação
                        resultados = {time.lower(): jogos for time, jogos in simulacao['resultados'].items()}

                        # Verifica se o time participou da simulação
                        if nome_time_min in resultados:
                            jogos = resultados[nome_time_min]['jogos']
                            ultima_fase = None

                            for jogo in jogos:
                                ultima_fase = jogo['fase']  # Atualiza a última fase jogada

                            # Verifica a última fase jogada e se a próxima fase foi jogada
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
                            elif ultima_fase == "final":
                                for jogo in jogos:
                                    if jogo['fase'] == "final":
                                        if jogo['gols_marcados'] < jogo['gols_sofridos']:
                                            eliminacoes_por_fase["final"] += 1
                                        break
        except json.JSONDecodeError:
            print("Erro ao ler o histórico. O arquivo pode estar corrompido.")


    # Cálculo das médias
    media_gols_feitos = gols_feitos / partidas_jogadas if partidas_jogadas > 0 else 0
    media_gols_sofridos = gols_sofridos / partidas_jogadas if partidas_jogadas > 0 else 0

    # Exibição das estatísticas


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
        print(f"{'Participações:'.ljust(30)}{participacoes}\n")  # Exibe a quantidade de participações
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

    # Exibindo as médias
    print("┌" + "─" * 44 + "┐")
    print(f"│ {'Média de Gols Feitos:'.ljust(30)}{media_gols_feitos:.2f}         │")
    print(f"│ {'Média de Gols Sofridos:'.ljust(30)}{media_gols_sofridos:.2f}         │")
    print("└" + "─" * 44 + "┘\n")

    # Exibir as eliminações por fase
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




# Carregar a configuração de gols do arquivo JSON
def carregar_configuracao():
    with open("configuracao_gols.json", "r") as file:
        configuracao = json.load(file)
    return configuracao

# Função para salvar a configuração alterada pelo usuário
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
        print("\n--- Configurações de Níveis de Gols ---\n".upper())
        print("\n")
        print(f"Nível de gols atual: {config_atual['nivel_gols'].replace('_', ' ').upper()}")
        print("\n")
        print("Escolha o nível da média de gols para as simulações:")
        print("\n")
        escolha = input("\n1 - Média de gols baixa\n2 - Média de gols média (recomendado)\n3 - Média de gols alta\n4 - Média de gols muito alta\n5 - Exibir detalhes\n\n")
        print("\n")
        print("\n")
        if escolha == "1":
            nivel_gols = "baixa"
        elif escolha == "2":
            nivel_gols = "media"
        elif escolha == "3":
            nivel_gols = "alta"
        elif escolha == "4":
            nivel_gols = "muito_alta"
        elif escolha == '5':
            # Exibe os detalhes da configuração atual
            print("\n")
            print("Configurações disponíveis:")
            print("\n")
            for nivel, config in config_atual["configuracoes"].items():
                print("\n")
                print(f"\nNível: {nivel.capitalize()}")
                print("\n")
                print(f"  Média Base: {config['media_base']}")
                print(f"  Divisor da Média: {config['media_divisor']}")
                print(f"  Desvio Base: {config['desvio_base']}")
                print(f"  Divisor do Desvio: {config['desvio_divisor']}")
                print(f"  Soma: {config['soma']}")
            print("\n")
            
        
        
        
            # Após exibir os detalhes, retorna ao menu de configuração
            return configurar_nivel_gols()
        else:
            print("\n")
            print(f"Opção inválida. Usando configuração atual ({config_atual['nivel_gols']}).")
            print("\n")
            return configurar_nivel_gols()

        # Salvar a nova configuração
        salvar_configuracao(nivel_gols)
        print("\n\n")
        print(f"Configuração do nível de gols ajustada para {nivel_gols.replace('_', ' ').upper()} com sucesso!")
        print("\n\n")



# Função para criar o arquivo JSON com configurações padrão
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
    # Carrega os dados do arquivo resultados_partidas.json
    try:
        with open('resultados_partidas_atual.json', 'r') as file:
            resultados = json.load(file)
    except FileNotFoundError:
        print("Arquivo de resultados não encontrado.")
        return
    
    # Solicita o nome do time e converte para minúsculas
    nome_time = input("Digite o nome do time: ").strip().lower()

    # Normaliza as chaves do dicionário (nomes dos times) para minúsculas
    resultados_normalizados = {time.lower(): partidas for time, partidas in resultados.items()}

    # Verifica se o time existe no arquivo (considerando letras maiúsculas e minúsculas)
    if nome_time not in resultados_normalizados:
        print(f"Time '{nome_time}' não encontrado.")
        return

    # Organiza as partidas por fase
    partidas_por_fase = {
        "grupos": [],
        "playoffs": [],
        "oitavas": [],
        "quartas": [],
        "semis": [],
        "final": []
    }

    # Filtra as partidas e as agrupa por fase
    for partida in resultados_normalizados[nome_time]["jogos"]:  # Acesso à chave "jogos"
        fase = partida["fase"]
        adversario = partida["adversario"]
        gols_marcados = partida["gols_marcados"]
        gols_sofridos = partida["gols_sofridos"]

        # Formatação do resultado
        resultado = "{:>20} {:<1} x {:<1} {:<20}".format(nome_time.capitalize(), gols_marcados, gols_sofridos, adversario)

        # Adiciona a partida na fase correspondente
        if fase in partidas_por_fase:
            partidas_por_fase[fase].append(resultado)
        else:
            print(f"Fase desconhecida: {fase}")
    
    # Exibe as partidas agrupadas por fase
    print(f"\nPartidas jogadas pelo {nome_time.capitalize()}:\n")

    for fase, partidas in partidas_por_fase.items():
        if partidas:  # Exibe somente se houver partidas na fase
            # Calcula o comprimento máximo das partidas para a formatação
            max_len_time = max(len(nome_time), max(len(partida) for partida in partidas))
            if max_len_time % 2 == 0:
                max_len_time += 1
            tamanho_linha = max_len_time + 28  # Adiciona uma margem de 28 caracteres
            metade = (tamanho_linha - 5) // 2

            print(f"Fase {fase.capitalize()}:\n")
            print("┌" + "─" * tamanho_linha + "┐")
            print("├" + "─" * tamanho_linha + "┤")

            for partida in partidas:
                print("| {:^{}} |".format(partida, tamanho_linha - 2))  # Alinha a partida no centro

            print("└" + "─" * tamanho_linha + "┘\n")  # Finaliza a fase com um box











def buscar_partidas_historico():
    while True:
        # Carrega os dados do arquivo historico_resultados.json
        try:
            with open('historico_resultados.json', 'r') as file:
                historico = json.load(file)
        except FileNotFoundError:
            print("Arquivo de histórico não encontrado.")
            return
        
        quantidade_simulacoes = len(historico)
        # Solicita o número da simulação ou a letra 'A' para todas as simulações
        escolha = input(f"\nENTER - VOLTAR\nDigite o número da simulação ou 'A' para todas (total de {quantidade_simulacoes}): \n\n").strip().lower()
        print("\n")
        if escolha == '':
            return  # Isso faz com que a função termine e retorne à função que a chamou

        # Solicita o nome do time
        print("\n")
        nome_time = input("Digite o nome do time: \n\n").strip().lower()
        print("\n")

        # Organiza as partidas por fase
        partidas_por_fase = {
            "grupos": [],
            "playoffs": [],
            "oitavas": [],
            "quartas": [],
            "semis": [],
            "final": []
        }

        # Se a escolha for 'A', percorre todas as simulações
        if escolha == 'a':
            time_encontrado = False
            for num_simulacao, simulacao in enumerate(historico, 1):
                resultados = simulacao["resultados"]

                # Normaliza os nomes dos times no dicionário para minúsculas
                resultados_normalizados = {time.lower(): dados for time, dados in resultados.items()}

                # Verifica se o time existe na simulação
                if nome_time in resultados_normalizados:
                    time_encontrado = True  
                    print(f"\nPartidas jogadas pelo {nome_time.capitalize()} na simulação {num_simulacao}:\n")

                    # Filtra as partidas e as agrupa por fase
                    for partida in resultados_normalizados[nome_time]["jogos"]:
                        fase = partida["fase"]
                        adversario = partida["adversario"]
                        gols_marcados = partida["gols_marcados"]
                        gols_sofridos = partida["gols_sofridos"]

                        # Formatação do resultado
                        resultado = "{:>20} {:<1} x {:<1} {:<20}".format(nome_time.capitalize(), gols_marcados, gols_sofridos, adversario)

                        # Adiciona a partida na fase correspondente
                        if fase in partidas_por_fase:
                            partidas_por_fase[fase].append(resultado)
                        else:
                            print(f"Fase desconhecida: {fase}")

                    # Exibe as partidas agrupadas por fase com a nova formatação
                    for fase, partidas in partidas_por_fase.items():
                        if partidas:
                            # Calcula o comprimento máximo para a formatação
                            max_len_time = max(len(nome_time), max(len(partida) for partida in partidas))
                            if max_len_time % 2 == 0:
                                max_len_time += 1
                            tamanho_linha = max_len_time + 28  # Adiciona uma margem de 28 caracteres
                            metade = (tamanho_linha - 5) // 2

                            print(f"Fase {fase.capitalize()}:\n")
                            print("┌" + "─" * tamanho_linha + "┐")
                            print("├" + "─" * tamanho_linha + "┤")

                            for partida in partidas:
                                print("| {:^{}} |".format(partida, tamanho_linha - 2))  # Alinha a partida no centro

                            print("└" + "─" * tamanho_linha + "┘\n")  # Finaliza a fase com um box
                    partidas_por_fase = {k: [] for k in partidas_por_fase}  # Limpa as partidas para a próxima simulação
            if not time_encontrado:
                print(f"\nO time {nome_time} não existe nos registros.\n")
        else:
            # Tenta converter a escolha para número de simulação
            try:
                num_simulacao = int(escolha)
            except ValueError:
                print("Entrada inválida. Digite um número ou 'A' para todas as simulações.")
                continue

            # Verifica se o número da simulação existe
            if num_simulacao > len(historico) or num_simulacao <= 0:
                print(f"Simulação {num_simulacao} não encontrada.")
                continue

            # Busca a simulação correspondente
            simulacao = historico[num_simulacao - 1]  # Ajusta o índice (começando em 0)
            resultados = simulacao["resultados"]

            # Normaliza os nomes dos times no dicionário para minúsculas
            resultados_normalizados = {time.lower(): dados for time, dados in resultados.items()}

            # Verifica se o time existe na simulação
            if nome_time not in resultados_normalizados:
                print(f"Time '{nome_time}' não encontrado na simulação {num_simulacao}.")
                continue

            # Filtra as partidas e as agrupa por fase
            for partida in resultados_normalizados[nome_time]["jogos"]:
                fase = partida["fase"]
                adversario = partida["adversario"]
                gols_marcados = partida["gols_marcados"]
                gols_sofridos = partida["gols_sofridos"]

                # Formatação do resultado
                resultado = "{:>20} {:<1} x {:<1} {:<20}".format(nome_time.capitalize(), gols_marcados, gols_sofridos, adversario)

                # Adiciona a partida na fase correspondente
                if fase in partidas_por_fase:
                    partidas_por_fase[fase].append(resultado)
                else:
                    print(f"Fase desconhecida: {fase}")

            # Exibe as partidas agrupadas por fase com a nova formatação
            print(f"\nPartidas jogadas pelo {nome_time.capitalize()} na simulação {num_simulacao}:\n")

            for fase, partidas in partidas_por_fase.items():
                if partidas:  # Exibe somente se houver partidas na fase
                    # Calcula o comprimento máximo para a formatação
                    max_len_time = max(len(nome_time), max(len(partida) for partida in partidas))
                    if max_len_time % 2 == 0:
                        max_len_time += 1
                    tamanho_linha = max_len_time + 28  # Adiciona uma margem de 28 caracteres
                    metade = (tamanho_linha - 5) // 2

                    print(f"Fase {fase.capitalize()}:\n")
                    print("┌" + "─" * tamanho_linha + "┐")
                    print("├" + "─" * tamanho_linha + "┤")

                    for partida in partidas:
                        print("| {:^{}} |".format(partida, tamanho_linha - 2))  # Alinha a partida no centro

                    print("└" + "─" * tamanho_linha + "┘\n")  # Finaliza a fase com um box

















def analisar_estatisticas():
    """Analisa o arquivo de gols acumulados e imprime estatísticas de ataque, defesa e maior goleada."""
    gols_acumulados = carregar_gols_acumulados()
    
    gols = gols_acumulados["gols"]
    gols_sofridos = gols_acumulados["gols_sofridos"]
    partidas_jogadas = gols_acumulados["partidas_jogadas"]

    # Inicializa as listas
    melhores_ataques = []
    piores_ataques = []
    melhores_defesas = []
    piores_defesas = []
    
    # Inicializa variáveis para médias
    melhor_media_gols = float('-inf')
    pior_media_gols = float('inf')
    melhor_media_defensiva = float('inf')
    pior_media_defensiva = float('-inf')

    # Armazena os times correspondentes às melhores e piores médias
    time_melhor_media_gols = None
    time_pior_media_gols = None
    time_melhor_media_defensiva = None
    time_pior_media_defensiva = None

    # Análise das estatísticas
    for time in gols:
        # Melhor ataque
        if gols[time] > (melhores_ataques[0]['gols'] if melhores_ataques else -1):
            melhores_ataques = [{"time": time, "gols": gols[time], "partidas": partidas_jogadas.get(time, 0)}]
        elif gols[time] == (melhores_ataques[0]['gols'] if melhores_ataques else -1):
            melhores_ataques.append({"time": time, "gols": gols[time], "partidas": partidas_jogadas.get(time, 0)})

        # Pior ataque
        if gols[time] < (piores_ataques[0]['gols'] if piores_ataques else float('inf')):
            piores_ataques = [{"time": time, "gols": gols[time], "partidas": partidas_jogadas.get(time, 0)}]
        elif gols[time] == (piores_ataques[0]['gols'] if piores_ataques else float('inf')):
            piores_ataques.append({"time": time, "gols": gols[time], "partidas": partidas_jogadas.get(time, 0)})

        # Melhor defesa
        if gols_sofridos[time] < (melhores_defesas[0]['gols_sofridos'] if melhores_defesas else float('inf')):
            melhores_defesas = [{"time": time, "gols_sofridos": gols_sofridos[time], "partidas": partidas_jogadas.get(time, 0)}]
        elif gols_sofridos[time] == (melhores_defesas[0]['gols_sofridos'] if melhores_defesas else float('inf')):
            melhores_defesas.append({"time": time, "gols_sofridos": gols_sofridos[time], "partidas": partidas_jogadas.get(time, 0)})

        # Pior defesa
        if gols_sofridos[time] > (piores_defesas[0]['gols_sofridos'] if piores_defesas else -1):
            piores_defesas = [{"time": time, "gols_sofridos": gols_sofridos[time], "partidas": partidas_jogadas.get(time, 0)}]
        elif gols_sofridos[time] == (piores_defesas[0]['gols_sofridos'] if piores_defesas else -1):
            piores_defesas.append({"time": time, "gols_sofridos": gols_sofridos[time], "partidas": partidas_jogadas.get(time, 0)})

        # Cálculo das médias
        if partidas_jogadas.get(time, 0) > 0:  # Evita divisão por zero
            media_gols = gols[time] / partidas_jogadas[time]
            media_defensiva = gols_sofridos[time] / partidas_jogadas[time]

            # Melhor média de gols
            if media_gols > melhor_media_gols:
                melhor_media_gols = media_gols
                time_melhor_media_gols = time
            
            # Pior média de gols
            if media_gols < pior_media_gols:
                pior_media_gols = media_gols
                time_pior_media_gols = time

            # Melhor média defensiva
            if media_defensiva < melhor_media_defensiva:
                melhor_media_defensiva = media_defensiva
                time_melhor_media_defensiva = time
            
            # Pior média defensiva
            if media_defensiva > pior_media_defensiva:
                pior_media_defensiva = media_defensiva
                time_pior_media_defensiva = time

    # Impressão das estatísticas
    print(f"{'_' * 64}\n")
    print("Melhor(es) Ataque(s):")
    for ataque in melhores_ataques:
        print(f"{ataque['time']}: {' ' * (20 - len(ataque['time']))} {ataque['gols']} gols em {ataque['partidas']} partidas")
    print(f"{'_' * 64}\n")

    print("\nMelhor(es) Defesa(s):")
    for defesa in melhores_defesas:
        print(f"{defesa['time']}: {' ' * (20 - len(defesa['time']))} {defesa['gols_sofridos']} gols sofridos em {defesa['partidas']} partidas")
    print(f"{'_' * 64}\n")

    print("\nPior(es) Ataque(s):")
    for ataque in piores_ataques:
        print(f"{ataque['time']}: {' ' * (20 - len(ataque['time']))} {ataque['gols']} gols em {ataque['partidas']} partidas")
    print(f"{'_' * 64}\n")

    print("\nPior(es) Defesa(s):")
    for defesa in piores_defesas:
        print(f"{defesa['time']}: {' ' * (20 - len(defesa['time']))} {defesa['gols_sofridos']} gols sofridos em {defesa['partidas']} partidas")
    print(f"{'_' * 64}\n")
    # Impressão das maiores goleadas
    print("\nMaior(es) Goleada(s) da fase de liga:")
    print("\n")
    for goleada in maiores_goleadas:
        print("{:>20} {:<1} x {:<1} {:<20}".format(goleada['time1'], goleada['gols_time1'], goleada['gols_time2'], goleada['time2']))
    print("\n")
    print(f"{'_' * 64}\n")
    print("\nMaior(s) goleada(s) da fase de mata-mata:")
    print("\n")
    for goleada in maiores_goleadas_mata_mata:
        print("{:>20} {:<1} x {:<1} {:<20}".format(goleada['time1'], goleada['gols_time1'], goleada['gols_time2'], goleada['time2']))


    print("\n")
    print(f"{'_' * 64}\n")
    # Impressão das novas estatísticas de médias
    # Exibindo as médias com espaçamento formatado
    print("\nMelhor média de gols:")
    print(f"{time_melhor_media_gols}: {' ' * (20 - len(time_melhor_media_gols))} {melhor_media_gols:.2f} gols por partida")

    print("\nMelhor média defensiva:")
    print(f"{time_melhor_media_defensiva}: {' ' * (20 - len(time_melhor_media_defensiva))} {melhor_media_defensiva:.2f} gols sofridos por partida")

    print("\nPior média de gols:")
    print(f"{time_pior_media_gols}: {' ' * (20 - len(time_pior_media_gols))} {pior_media_gols:.2f} gols por partida")

    print("\nPior média defensiva:")
    print(f"{time_pior_media_defensiva}: {' ' * (20 - len(time_pior_media_defensiva))} {pior_media_defensiva:.2f} gols sofridos por partida")
    print(f"{'_' * 64}\n")




class ExitLoops(Exception):
    pass

def main():
    global potes, stats
    try:
        if not os.path.exists("configuracao_gols.json"):
            criar_configuracao_padrao()
        carregar_stats_inicial()

    
        voltar_menu_principal = False  # Inicializa fora de todos os loops

        while True:
            menu_principal()        
            escolha_menu = input("\nENTER - Entrar no simulador\n1 - Configurações\n2 - Sair\n\n".upper()).strip().upper()

            if escolha_menu == '1':
                while True:  # Adiciona um loop para o menu de configurações
                    print("\n")
                    configs = input("\n1 - Editar média de gols do jogo\n2 - Editar times\n3 - Trocar para configuração padrão ou personalizada\n4 - Excluir times personalizados\n5 - Excluir simulação\n6 - Voltar\n99 - RESETAR DADOS\n\n".upper())
                    print("\n")
                    print("\n")

                    if configs == '99':
                        resetar_aplicacao()

                    elif configs == '1':
                        configurar_nivel_gols()
                    elif configs == '2':
                        substituir_time(potes, stats)
                        continue
                    elif configs == '4':
                        if os.path.exists("stats_personalizados.json"):
                            confirma = input("Tem certeza que deseja excluir os times personalizados e voltar para a configuração padrão?\n\n1 - SIM\n2 - NÃO\n\n")

                        
                            if confirma == '1':
                                excluir_stats_personalizados()
                                potes, stats = carregar_times_stats2()
                                continue
                            elif confirma == '2':
                                print("\n")
                                print("Operação cancelada.")
                                continue
                            else:
                                print("\n")
                                print("Opção inválida. Tente novamente.")
                        else:
                            print("\n\nArquivo não encontrado.\n\n")
                    elif configs == '3':
                        alternar_stats()
                        continue
                    elif configs == '5':
                        excluir_simulacao()
                        continue

                    elif configs == '6':
                        break  # Sai do loop de configurações e volta para o menu principal
                    else:
                        print("Opção inválida. Tente novamente.")

            if escolha_menu == '2':
                print("\n")
                print("\nSaindo do programa...")
                break  # Encerra o programa

            elif escolha_menu == '':  # Inicia o simulador
                try:
                    while True:
                            # Inicializa e sorteia confrontos
                            confrontos = inicializa_confrontos(potes)
                            assign_all_internal_rivals(potes, confrontos)
                            success = assign_all_external_rivals(potes, confrontos)

                            if not success:
                                print("Falha ao sortear os confrontos.")
                                continue

                            home_away = assign_home_away(confrontos)
                            classificacao = inicializar_classificacao(potes)

                            # Exibe os confrontos sorteados na ordem dos potes
                            print("\n")
                            print("\nConfrontos sorteados:")
                            print("\n")
                            for time in sorted(confrontos.keys()):
                                rivais_ordenados = agrupar_rivais_por_pote_intercalados(confrontos, time)
                                print("{:<20}| {}".format(time.upper(), ', '.join(f"{rival:<2}" for rival in rivais_ordenados)))

                            # Pergunta ao usuário se ele quer simular as partidas, pesquisar dados ou voltar ao menu principal
                            print("\n")
                            print("\n")
                            escolha = input("\nENTER - Simular partidas\n1 - Sortear novamente\n2 - Pesquisar dados\n3 - Menu Principal\n\n".upper()).strip().upper()

                            if escolha == '':
                                resultados = {}
                                print("\n")
                                print("\nSimulando partidas...")
                                print("\n")
                                print_stats_com_momento()
                                resultados_partidas = simular_confrontos(home_away, resultados, classificacao)
                                inicializar_gols_acumulados(classificacao)
                                print("\n")
                                print("\nResultados das partidas:")
                                print("\n")
                                print("\n".join(resultados_partidas))
                                print("\n")

                                # Nova condição para exibir a tabela de classificação ou playoffs
                                while True:
                                    escolha_tabela = input("\n1 - Exibir tabela de classificação\n2 - Voltar para o Menu Sorteio\nENTER - Exibir confrontos dos play-offs\n\n".upper()).strip().upper()
                                    print("\n")

                                    if escolha_tabela == '1':
                                        print("\n")
                                        exibir_classificacao(classificacao)
                                        print("\n")

                                    elif escolha_tabela == '':
                                        print("\n")
                                        exibir_playoffs(classificacao)
                                        print("\n")
                                        while True:
                                            continuar = input("\n1 - Exibir tabela de classificação\nENTER - Simular play-offs\n\n".upper()).strip().upper()
                                            print("\n")

                                            if continuar == '1':        
                                                print("\n")
                                                exibir_classificacao(classificacao)
                                                print("\n")


                                            elif continuar == '':
                                                print("\n")
                                                vencedores = placar_final_playoffs(classificacao)
                                                print("\n")

                                                # Após a simulação dos playoffs, continua o fluxo
                                                while True:
                                                    escolha_finais = input("\n1 - Exibir tabela de classificação\nENTER - Exibir confrontos das oitavas\n\n".upper()).strip().upper()
                                                    print("\n")

                                                    if escolha_finais == '1':
                                                        print("\n")
                                                        exibir_classificacao(classificacao)
                                                        print("\n")

                                                    elif escolha_finais == '':
                                                        exibir_oitavas(classificacao, vencedores)
                                                        print("\n")
                                                        print("\n")
                                                        while True:
                                                            oitavas = input("\n1 - Exibir tabela de classificação\nENTER - Simular oitavas de final\n\n".upper()).strip().upper()
                                                            print("\n")

                                                            if oitavas == '1':
                                                                print("\n")
                                                                exibir_classificacao(classificacao)
                                                                print("\n")

                                                            elif oitavas == '':
                                                                vencedores_oitavas = placar_final_oitavas(classificacao, vencedores)
                                                                print("\n")
                                                                print("\n")
                                                                while True:
                                                                    quartas = input("\n1 - Exibir tabela de classificação\nENTER - Sortear confrontos das quartas\n\n".upper()).strip().upper()
                                                                    print("\n")

                                                                    if quartas == '1':
                                                                        print("\n")
                                                                        exibir_classificacao(classificacao)
                                                                        print("\n")


                                                                    elif quartas == '':
                                                                        quartas_de_final = sortear_quartas(vencedores_oitavas)
                                                                        exibir_confrontos_quartas(quartas_de_final)
                                                                        print("\n")
                                                                        print("\n")
                                                                        while True:
                                                                            simular_quartas = input("\n1 - Exibir tabela de classificação\nENTER - Simular quartas de final\n\n".upper()).strip().upper()
                                                                            print("\n")

                                                                            if simular_quartas == '1':
                                                                                print("\n")
                                                                                exibir_classificacao(classificacao)
                                                                                print("\n")


                                                                            elif simular_quartas == '':
                                                                                vencedores_quartas = placar_final_quartas(quartas_de_final)
                                                                                print("\n")
                                                                                print("\n")
                                                                                while True:
                                                                                    semis = input("\n1 - Exibir tabela de classificação\nENTER - Exibir confrontos das semifinais\n\n".upper()).strip().upper()
                                                                                    print("\n")
                                                                                    if semis == '1':
                                                                                        print("\n")
                                                                                        exibir_classificacao(classificacao)
                                                                                        print("\n")


                                                                                    elif semis == '':
                                                                                        exibir_semi_final(vencedores_quartas)
                                                                                        print("\n")
                                                                                        print("\n")
                                                                                        while True:
                                                                                            simular_semis = input("\n1 - Exibir tabela de classificação\nENTER - Simular semifinais\n\n".upper()).strip().upper()
                                                                                            print("\n")
                                                                                            if simular_semis == '1':
                                                                                                print("\n")
                                                                                                exibir_classificacao(classificacao)
                                                                                                print("\n")


                                                                                            elif simular_semis == '':
                                                                                                vencedores_semis = placar_final_semis(vencedores_quartas)
                                                                                                print("\n")
                                                                                                print("\n")
                                                                                                while True:
                                                                                                    final = input("\n1 - Exibir tabela de classificação\nENTER - Exibir final\n\n".upper()).strip().upper()
                                                                                                    print("\n")
                                                                                                    if final == '1':
                                                                                                        print("\n")
                                                                                                        exibir_classificacao(classificacao)
                                                                                                        print("\n")


                                                                                                    elif final == '':
                                                                                                        exibir_final(vencedores_semis)
                                                                                                        print("\n")
                                                                                                        print("\n")
                                                                                                        while True:
                                                                                                            simular_Final = input("\nENTER - Simular final\n\n".upper()).strip().upper()
                                                                                                            print("\n")

                                                                                                            if simular_Final == '':
                                                                                                                vencedor_final, gols_vencedor, vice_final, gols_vice = placar_final_final(vencedores_semis)
                                                                                                                print("\n{:>16}\nCampeão: {}".format('', vencedor_final))
                                                                                                                print_trophy(vencedor_final)
                                                                                                                print("\n")
                                                                                                                print("\n")
                                                                                                                

                                                                                                                # Alterações nesta parte
                                                                                                                while True:
                                                                                                                    escolha_finais2 = input("\n1 - Exibir tabela de classificação\n2 - Finalizar\nENTER - Estatísticas\n\n".upper()).strip().upper()
                                                                                                                    print("\n")

                                                                                                        

                                                                                                                    if escolha_finais2 == '1':
                                                                                                                        print("\n")
                                                                                                                        exibir_classificacao(classificacao)
                                                                                                                        print("\n")
                                                                                                                        while True:
                                                                                                                            voltar_ao_sorteio = input("\n1 - Voltar\nENTER - Finalizar\n\n").strip().upper()
                                    
                                                                                                                            print("\n")

                                                                                                                            if voltar_ao_sorteio == '':
                                                                                                                                print("\n")
                                                                                                                                
                                                                                                                                finalizar_simulacao(vencedor_final, gols_vencedor, vice_final, gols_vice)
                                                                                                                                transferir_para_historico()
                                                                                                                               
                                                                                                                                raise ExitLoops
                                                                                                                            elif voltar_ao_sorteio == '1':
                                                                                                                                break

                                                                                                                            else:
                                                                                                                                print("\n")
                                                                                                                                print("\nOpção inválida. Por favor, tente novamente.\n\n")
                                                                                                                            

                                                                                                                            
                                                                                                                            
                                                                                                    

                                                                                                                    elif escolha_finais2 == '2':
                                                                                                                        while True:  # Novo loop para Outras Opções
                                                                                                                            print("\n")
                                                                                                                            
                                                                                                                            finalizar_simulacao(vencedor_final, gols_vencedor, vice_final, gols_vice)
                                                                                                                            transferir_para_historico()
                                                                                                                            outras_opcoes = input("\nENTER - Voltar para o menu\n\n").strip().upper()
                                                                                                                            print("\n")
                                                                                                                            if outras_opcoes == '':
                                                                                                                                raise ExitLoops
                                                                                
                                                                                                                            else:
                                                                                                                                print("\n")
                                                                                                                                print("\nOpção inválida. Por favor, tente novamente.\n\n")
                                                                                                                            

                                                                                                                    elif escolha_finais2 == '':
                                                                                                                            print("\n")
                                                                                                                            analisar_estatisticas()
                                                                                                                            print("\n")
                                                                                                                            while True:

                                                                                                                                voltar_ao_sorteio = input("\n1 - Voltar\n2 - Pesquisar trajeto do time\nENTER - Finalizar\n\n").strip().upper()
                                    
                                                                                                                                print("\n")


                                                                                                                                if voltar_ao_sorteio == '':
                                                                                                                                    print("\n")
                                                                                                                                    finalizar_simulacao(vencedor_final, gols_vencedor, vice_final, gols_vice)
                                                                                                                                    transferir_para_historico()
                                                                                                                                    raise ExitLoops
                                                                                                                                elif voltar_ao_sorteio == '2':
                                                                                                                                    print("\n")
                                                                                                                                    buscar_partidas_por_time()
                                                                                                                                    
                                                                                                                                elif voltar_ao_sorteio == '1':
                                                                                                                                    break

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

                                    elif escolha_tabela == '2':
                                        resetar_arquivo_gols()
                                        resetar_arquivo_resultados()
                                        break  # Volta ao menu principal

                                    else:
                                        print("\n")
                                        print("\nOpção inválida. Por favor, tente novamente.\n\n")

                            elif escolha == '2':
                                while True:  # Loop secundário para voltar à pesquisa
                                    print("\n")
                                    procurar_dados = input("\n1 - Exibir todas as finais\n2 - Listar campeões\n3 - Listar vice-campeões\n4 - Melhores Ataques Histórico\n5 - Melhores Defesas histórico\n6 - Exibir médias de ataque e defesa\n7 - Ordem por vitórias\n8 - Pesquisar por time\n9 - Todas as partidas registradas\n10 - Voltar para o sorteio\n\n".upper())
                                    print("\n")

                                    if procurar_dados == '1':
                                        print("\n")
                                        exibir_finais()
                                        print("\n")
                                        voltar = input("ENTER - Voltar para pesquisa de dados\n1 - Voltar para sorteio\n\n".upper())
                                        print("\n")

                                        if voltar == '':
                                            continue  # Volta para o loop de pesquisa
                                        elif voltar == '1':
                                            break  # Sai do loop de pesquisa e volta para o início

                                    elif procurar_dados == '2':
                                        print("\n")
                                        listar_campeoes_ordenados()
                                        print("\n")
                                        voltar = input("ENTER - Voltar para pesquisa de dados\n2 - Voltar para sorteio\n\n".upper())
                                        print("\n")

                                        if voltar == '':
                                            continue  # Volta para o loop de pesquisa
                                        elif voltar == '2':
                                            break  # Sai do loop de pesquisa e volta para o início


                                    elif procurar_dados == '3':
                                        print("\n")
                                        listar_vices_ordenados()
                                        print("\n")
                                        voltar = input("ENTER - Voltar para pesquisa de dados\n2 - Voltar para sorteio\n\n".upper())
                                        print("\n")

                                        if voltar == '':
                                            continue  # Volta para o loop de pesquisa
                                        elif voltar == '2':
                                            break  # Sai do loop de pesquisa e volta para o início
                                    elif procurar_dados == '4':
                                        print("\n")
                                        historico_melhores_ataques()
                                        print("\n")
                                        voltar = input("ENTER - Voltar para pesquisa de dados\n2 - Voltar para sorteio\n\n".upper())
                                        print("\n")

                                        if voltar == '':
                                            continue  # Volta para o loop de pesquisa
                                        elif voltar == '2':
                                            break  # Sai do loop de pesquisa e volta para o início

                                    elif procurar_dados == '5':
                                        print("\n")
                                        historico_melhores_defesas()
                                        print("\n")
                                        voltar = input("ENTER - Voltar para pesquisa de dados\n2 - Voltar para sorteio\n\n".upper())
                                        print("\n")

                                        if voltar == '1':
                                            continue  # Volta para o loop de pesquisa
                                        elif voltar == '2':
                                            break  # Sai do loop de pesquisa e volta para o início

                                    elif procurar_dados == '6':
                                        print("\n")
                                        media_gols_feitos()
                                        print("\n")
                                        media_gols_sofridos()
                                        print("\n")
                                        voltar = input("ENTER - Voltar para pesquisa de dados\n2 - Voltar para sorteio\n\n".upper())
                                        print("\n")

                                        if voltar == '1':
                                            continue  # Volta para o loop de pesquisa
                                        elif voltar == '2':
                                            break  # Sai do loop de pesquisa e volta para o início

                                    elif procurar_dados == '9':
                                        print("\n")
                                        
                                        while True:  # Novo loop para pesquisar por time até o usuário escolher sair
                                            print("\n")
                                            buscar_partidas_historico()
                                            print("\n")
                                            break

                                    elif procurar_dados == '8':
                                        while True:  # Novo loop para pesquisar por time até o usuário escolher sair
                                            print("\n")
                                            nome_time = input("Digite o nome do time que deseja pesquisar: \n\n")
                                            print("\n")
                                            print("\n")
                                            pesquisar_campeao_por_time(nome_time)

                                            print("\n")
                                            voltar = input("\n1 - Voltar\nENTER - Pesquisar novamente\n\n".upper())
                                            print("\n")

                                            if voltar == '':
                                                continue  # Volta para pesquisar outro time
                                            elif voltar == '1':
                                                break  # Volta para o menu de pesquisa de dados


                                        if voltar == '3':
                                            break
                                    elif procurar_dados == '7':
                                        while True:  # Novo loop para pesquisar por time até o usuário escolher sair
                                            print("\n")
                                            historico_mais_vitorias()
                                            print("\n")
                                            break
                                        

                                    elif procurar_dados == '10':
                                        break
                                    else:
                                        print("\n")
                                        print("\nInsira uma opção válida\n\n")
                                        continue

                            elif escolha == '3':
                                break  # Volta ao menu principal

                            elif escolha == '1':
                                continue # Sorteia novamente

                            else:
                                continue  # Sorteia novamente

                except ExitLoops:
                    print("Voltando para o menu principal...")
                    print("\n")
    except KeyboardInterrupt:
        print("\n")
        resetar_arquivo_gols()
        resetar_arquivo_resultados()
        print("\nPrograma interrompido pelo usuário.")
        print("\n")

# Executa o programa
if __name__ == "__main__":
    main()