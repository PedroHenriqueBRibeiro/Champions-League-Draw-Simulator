import json
import os
import random
import numpy as np

# Definindo os potes com nomes de times reais
pote_1 = ["Barcelona", "Real Madrid", "Manchester City", "Bayern Munich", "PSG", "Juventus", "Chelsea", "Liverpool", "Atlético Madrid"]
pote_2 = ["Borussia Dortmund", "Inter de Milão", "Milan", "Tottenham", "Arsenal", "Napoli", "Leipzig", "Sevilla", "Ajax"]
pote_3 = ["Benfica", "Porto", "Shakhtar", "Zenit", "Sporting", "Atalanta", "Lyon", "Monaco", "Leverkusen"]
pote_4 = ["Fenerbahçe", "Galatasaray", "Olympiacos", "Red Bull Salzburg", "Celtic", "Rangers", "Club Brugge", "Dynamo Kiev", "Anderlecht"]

potes = [pote_1, pote_2, pote_3, pote_4]

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
    "Anderlecht": {"ataque": 67, "defesa": 65},
}

# Função para determinar o pote do time
def get_pote(time):
    for idx, pote in enumerate(potes, start=1):
        if time in pote:
            return idx
    return None








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

    # Calcular médias e desvios
    media_casa, desvio_casa = calcula_media_desvio(ataque_casa, defesa_fora)
    media_fora, desvio_fora = calcula_media_desvio(ataque_fora, defesa_casa)

    # Gerar gols usando uma distribuição normal e arredondar para garantir que não seja negativo
    gols_casa = max(0, int(np.random.normal(media_casa, desvio_casa)))
    gols_fora = max(0, int(np.random.normal(media_fora, desvio_fora)))

    return gols_casa, gols_fora


import random

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










gols_acumulados = {}

def inicializar_gols_acumulados(classificacao):
    """Inicializa o dicionário que armazena os gols acumulados com base na classificação."""
    for time in classificacao.keys():
        gols_acumulados[time] = classificacao[time]['gols_marcados']

def atualizar_gols_acumulados(time, gols):
    """Atualiza o total de gols de um time."""
    if time in gols_acumulados:
        gols_acumulados[time] += gols
    else:
        gols_acumulados[time] = gols

    

nome_arquivo_gols = "gols_simulacao_atual.json"

def carregar_gols_acumulados():
    """Carrega o arquivo de gols acumulados. Se o arquivo não existir, retorna um dicionário vazio."""
    if os.path.exists(nome_arquivo_gols):
        with open(nome_arquivo_gols, 'r') as file:
            return json.load(file)
    return {}

def salvar_gols_acumulados(gols_acumulados):
    """Salva o dicionário de gols acumulados no arquivo JSON."""
    with open(nome_arquivo_gols, 'w') as file:
        json.dump(gols_acumulados, file, indent=4)

def atualizar_gols_acumulados_json(time, gols):
    """Atualiza o total de gols de um time no arquivo JSON."""
    gols_acumulados = carregar_gols_acumulados()
    if time in gols_acumulados:
        gols_acumulados[time] += gols  # Incrementa os gols existentes
    else:
        gols_acumulados[time] = gols  # Inicializa se o time não está no arquivo ainda

    salvar_gols_acumulados(gols_acumulados)


nome_arquivo_historico = "historico_gols.json" 


def carregar_historico_gols():
    """Carrega o arquivo de histórico de gols. Se o arquivo não existir, retorna uma lista vazia."""
    if os.path.exists(nome_arquivo_historico):
        with open(nome_arquivo_historico, 'r') as file:
            return json.load(file)
    return []

def salvar_historico_gols(historico_gols):
    """Salva o histórico de gols no arquivo JSON."""
    with open(nome_arquivo_historico, 'w') as file:
        json.dump(historico_gols, file, indent=4)

def resetar_arquivo_gols():
    """Remove o arquivo de gols acumulados, iniciando uma nova simulação."""
    if os.path.exists(nome_arquivo_gols):
        os.remove(nome_arquivo_gols)

def finalizar_simulacao():
    """Transfere os gols da simulação atual para o histórico e reseta o arquivo de gols acumulados."""
    print("Finalização da simulação...")
    
    # Carrega os gols acumulados e o histórico
    gols_acumulados = carregar_gols_acumulados()
    
    # Verifica se há pelo menos 25 times
    if len(gols_acumulados) < 25:
        print("Erro: Não foi salvo no histórico!")
        return  # Encerra a função sem salvar
    
    configuracao_atual = carregar_configuracao()
    nivel_gols_simulacao = configuracao_atual["nivel_gols"]

    # Carrega o histórico de gols
    historico_gols = carregar_historico_gols()

    # Adiciona os gols da simulação atual ao histórico
    historico_gols.append({
        "simulacao": len(historico_gols) + 1,  # Número da simulação
        "nivel_simulacao": nivel_gols_simulacao,
        "gols": gols_acumulados  # Gols acumulados na simulação atual
    })

    # Salva o novo histórico de gols
    salvar_historico_gols(historico_gols)

    # Remove o arquivo de gols acumulados (reset)
    resetar_arquivo_gols()

    print(f"Simulação finalizada! Os dados foram movidos para o histórico.")



















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
    
    for time1, time2 in confrontos_playoffs:
        print("{:>20} x {:<20}".format(time1, time2))


def simular_playoff(classificacao):
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

    resultados_ida = {}
    print("\n")
    print("Jogo de ida - Playoffs:\n")
    for time1, time2 in confrontos_playoffs:
        gols_time1, gols_time2 = gerar_gols(time1, time2)
        resultados_ida[(time1, time2)] = (gols_time1, gols_time2)
        atualizar_gols_acumulados_json(time1, gols_time1)
        atualizar_gols_acumulados_json(time2, gols_time2)
        
        print("{:>20} {:<1} x {:<1} {:<20}".format(time1, gols_time1, gols_time2, time2))

    resultados_volta = {}
    print("\n")
    print("Jogo de volta - Playoffs:\n")
    for time2, time1 in confrontos_playoffs:
        gols_time1, gols_time2 = gerar_gols(time1, time2)
        resultados_volta[(time1, time2)] = (gols_time1, gols_time2)
        atualizar_gols_acumulados_json(time1, gols_time1)
        atualizar_gols_acumulados_json(time2, gols_time2)
        
        print("{:>20} {:<1} x {:<1} {:<20}".format(time1, gols_time1, gols_time2, time2))

    return resultados_ida, resultados_volta


    

    



def placar_final_playoffs(classificacao):
    resultados_ida, resultados_volta = simular_playoff(classificacao)
    vencedores = []
    print("\n")
    print("\nPlacar Agregado - Playoffs:")
    print("\n")

    for (time1, time2), (gols_ida1, gols_ida2) in resultados_ida.items():
        gols_volta2, gols_volta1 = resultados_volta[(time2, time1)]  # Usar o par correto
        total_time1 = gols_ida1 + gols_volta1
        total_time2 = gols_ida2 + gols_volta2
        print("{:>20} {:<1} x {:<1} {:<20}".format(time1, total_time1, total_time2, time2))

        if total_time1 == total_time2:
            gols_penaltis1, gols_penaltis2 = simular_penaltis(time1, time2)
            print(f"{'':>16}Pen ({gols_penaltis1} - {gols_penaltis2})")
            vencedor = time1 if gols_penaltis1 > gols_penaltis2 else time2
            vencedores.append(vencedor)
        else:
            vencedor = time1 if total_time1 > total_time2 else time2
            vencedores.append(vencedor)

    print("\nVencedores dos playoffs:\n")
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
    
    for time1, time2 in confrontos_oitavas:
        print("{:>20} x {:<20}".format(time1, time2))

    return confrontos_oitavas

def simular_oitavas(classificacao, vencedores):
    primeiros_colocados = sorted(classificacao.items(), key=lambda x: (x[1]['pontos'], x[1]['saldo_gols'], x[1]['gols_marcados']), reverse=True)

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

    resultados_ida = {}
    print("\n")
    print("Jogos de ida - Oitavas de final:\n")
    for time1, time2 in confrontos_oitavas:
        gols_time1, gols_time2 = gerar_gols(time1, time2)
        resultados_ida[(time1, time2)] = (gols_time1, gols_time2)
        atualizar_gols_acumulados_json(time1, gols_time1)
        atualizar_gols_acumulados_json(time2, gols_time2)
        
        print("{:>20} {:<1} x {:<1} {:<20}".format(time1, gols_time1, gols_time2, time2))

    resultados_volta = {}
    print("\n")
    print("Jogos de volta - Oitavas de final:\n")
    for time2, time1 in confrontos_oitavas:
        gols_time1, gols_time2 = gerar_gols(time1, time2)
        resultados_volta[(time1, time2)] = (gols_time1, gols_time2)
        atualizar_gols_acumulados_json(time1, gols_time1)
        atualizar_gols_acumulados_json(time2, gols_time2)
        
        print("{:>20} {:<1} x {:<1} {:<20}".format(time1, gols_time1, gols_time2, time2))

    return resultados_ida, resultados_volta

def placar_final_oitavas(classificacao, vencedores):
    resultados_ida, resultados_volta = simular_oitavas(classificacao, vencedores)
    vencedores_oitavas = []
    print("\n")
    print("\nPlacar Agregado:")
    print("\n")

    for (time1, time2), (gols_ida1, gols_ida2) in resultados_ida.items():
        gols_volta2, gols_volta1 = resultados_volta[(time2, time1)]  # Usar o par correto
        total_time1 = gols_ida1 + gols_volta1
        total_time2 = gols_ida2 + gols_volta2
        print("{:>20} {:<1} x {:<1} {:<20}".format(time1, total_time1, total_time2, time2))

        if total_time1 == total_time2:
            gols_penaltis1, gols_penaltis2 = simular_penaltis(time1, time2)
            print(f"{'':>16}Pen ({gols_penaltis1} - {gols_penaltis2})")
            vencedor_oitavas = time1 if gols_penaltis1 > gols_penaltis2 else time2
            vencedores_oitavas.append(vencedor_oitavas)
        else:
            vencedor_oitavas = time1 if total_time1 > total_time2 else time2
            vencedores_oitavas.append(vencedor_oitavas)

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
    for time1, time2 in quartas_de_final:
        print("{:>20} x {:<20}".format(time1, time2))

def simular_quartas(quartas_de_final):
    resultados_ida = {}
    print("\n")
    print("Jogos de ida - Quartas de Final:\n")
    
    # Simula jogos de ida
    for time1, time2 in quartas_de_final:
        gols_time1, gols_time2 = gerar_gols(time1, time2)
        resultados_ida[(time1, time2)] = (gols_time1, gols_time2)
        atualizar_gols_acumulados_json(time1, gols_time1)
        atualizar_gols_acumulados_json(time2, gols_time2)
        print("{:>20} {:<1} x {:<1} {:<20}".format(time1, gols_time1, gols_time2, time2))

    resultados_volta = {}
    print("\n")
    print("Jogos de volta - Quartas de Final:\n")
    
    # Simula jogos de volta
    for time2, time1 in quartas_de_final:
        gols_time1, gols_time2 = gerar_gols(time1, time2)
        resultados_volta[(time1, time2)] = (gols_time1, gols_time2)
        atualizar_gols_acumulados_json(time1, gols_time1)
        atualizar_gols_acumulados_json(time2, gols_time2)
        print("{:>20} {:<1} x {:<1} {:<20}".format(time1, gols_time1, gols_time2, time2))

    return resultados_ida, resultados_volta

def placar_final_quartas(quartas_de_final):
    resultados_ida, resultados_volta = simular_quartas(quartas_de_final)
    vencedores_quartas = []
    print("\n")
    print("\nPlacar Agregado - Quartas de Final:")
    print("\n")

    # Calcula o placar agregado e determina os vencedores
    for (time1, time2), (gols_ida1, gols_ida2) in resultados_ida.items():
        gols_volta2, gols_volta1 = resultados_volta[(time2, time1)]  # Usar o par correto
        total_time1 = gols_ida1 + gols_volta1
        total_time2 = gols_ida2 + gols_volta2
        print("{:>20} {:<1} x {:<1} {:<20}".format(time1, total_time1, total_time2, time2))

        # Caso de empate no placar agregado, simula pênaltis
        if total_time1 == total_time2:
            gols_penaltis1, gols_penaltis2 = simular_penaltis(time1, time2)
            print(f"{'':>16}Pen ({gols_penaltis1} - {gols_penaltis2})")
            vencedor_quartas = time1 if gols_penaltis1 > gols_penaltis2 else time2
            vencedores_quartas.append(vencedor_quartas)
        else:
            vencedor_quartas = time1 if total_time1 > total_time2 else time2
            vencedores_quartas.append(vencedor_quartas)

    # Exibe os vencedores das quartas de final
    print("\nVencedores das quartas de final:\n")
    for vencedor_quartas in vencedores_quartas:
        print("{:<16}".format(vencedor_quartas)) 
    return vencedores_quartas


def exibir_semi_final(vencedores_quartas):
    print("\nConfrontos das Semifinais:\n")
    print("\n")
    
    # Confronto 1: [0] vs [1]
    print("{:>20} x {:<20}".format(vencedores_quartas[0], vencedores_quartas[1]))
    
    # Confronto 2: [2] vs [3]
    print("{:>20} x {:<20}".format(vencedores_quartas[2], vencedores_quartas[3]))


def simular_semifinais(vencedores_quartas):
    resultados_ida = {}
    resultados_volta = {}

    print("\nJogos de ida - Semifinais:\n")
    print("\n")
    
    # Simula os jogos de ida para os dois confrontos
    for i in range(0, len(vencedores_quartas), 2):  # Percorre a lista de 2 em 2
        time1 = vencedores_quartas[i]
        time2 = vencedores_quartas[i + 1]
        gols_time1, gols_time2 = gerar_gols(time1, time2)
        resultados_ida[(time1, time2)] = (gols_time1, gols_time2)
        atualizar_gols_acumulados_json(time1, gols_time1)
        atualizar_gols_acumulados_json(time2, gols_time2)
        print("{:>20} {:<1} x {:<1} {:<20}".format(time1, gols_time1, gols_time2, time2))

    print("\nJogos de volta - Semifinais:\n")
    print("\n")
    
    # Simula os jogos de volta para os dois confrontos
    for i in range(0, len(vencedores_quartas), 2):  # Percorre a lista de 2 em 2
        time1 = vencedores_quartas[i]
        time2 = vencedores_quartas[i + 1]
        gols_time2, gols_time1 = gerar_gols(time2, time1)  # Inverte os times para o jogo de volta
        resultados_volta[(time2, time1)] = (gols_time2, gols_time1)
        atualizar_gols_acumulados_json(time1, gols_time1)
        atualizar_gols_acumulados_json(time2, gols_time2)
        print("{:>20} {:<1} x {:<1} {:<20}".format(time2, gols_time2, gols_time1, time1))

    return resultados_ida, resultados_volta


def placar_final_semis(vencedores_quartas):
    resultados_ida, resultados_volta = simular_semifinais(vencedores_quartas)
    vencedores_semis = []
    print("\n")
    print("\nPlacar Agregado - Semifinais:\n")
    print("\n")

    # Calcula o placar agregado e determina os vencedores
    for (time1, time2), (gols_ida1, gols_ida2) in resultados_ida.items():
        gols_volta2, gols_volta1 = resultados_volta[(time2, time1)]  # Usar o par correto
        total_time1 = gols_ida1 + gols_volta1
        total_time2 = gols_ida2 + gols_volta2
        print("{:>20} {:<1} x {:<1} {:<20}".format(time1, total_time1, total_time2, time2))

        # Caso de empate no placar agregado, simula pênaltis
        if total_time1 == total_time2:
            gols_penaltis1, gols_penaltis2 = simular_penaltis(time1, time2)
            print(f"{'':>16}Pen ({gols_penaltis1} - {gols_penaltis2})")
            vencedor_semis = time1 if gols_penaltis1 > gols_penaltis2 else time2
            vencedores_semis.append(vencedor_semis)
        else:
            vencedor_semis = time1 if total_time1 > total_time2 else time2
            vencedores_semis.append(vencedor_semis)

    # Exibe os vencedores das semifinais
    print("\n")
    print("\n")
    print("\nVencedores das semifinais:\n")
    print("\n")
    for vencedor_semis in vencedores_semis:
        print("{:<16}".format(vencedor_semis))
    return vencedores_semis






def exibir_final(vencedores_semis):
    print("\nFinal:\n")
    # Confronto 1: [0] vs [1]
    print("{:>20} x {:<20}".format(vencedores_semis[0], vencedores_semis[1]))

def simular_final(vencedores_semis):
    resultado = {}
    
    time1 = vencedores_semis[0]
    time2 = vencedores_semis[1]
    
    # Simula o único jogo da final
    gols_time1, gols_time2 = gerar_gols(time1, time2)
    resultado[(time1, time2)] = (gols_time1, gols_time2)

    return resultado



def placar_final_final(vencedores_semis):
    resultado = simular_final(vencedores_semis)
    vencedor_final = []
    vice_final = []
    gols_vencedor = ""
    gols_vice = ""

    print("\nResultado Final:\n")
    print("\n")

    # Calcula o placar final e determina o vencedor
    for (time1, time2), (gols_time1, gols_time2) in resultado.items():
        atualizar_gols_acumulados_json(time1, gols_time1)
        atualizar_gols_acumulados_json(time2, gols_time2)
        print("{:>20} {:<1} x {:<1} {:<20}".format(time1, gols_time1, gols_time2, time2))

        # Caso de empate no tempo normal, simula pênaltis
        if gols_time1 == gols_time2:
            gols_penaltis1, gols_penaltis2 = simular_penaltis(time1, time2)
            print(f"{'':>16}Pen ({gols_penaltis1} - {gols_penaltis2})")
            
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
            # Vencedor no tempo normal
            vencedor = time1 if gols_time1 > gols_time2 else time2
            vice = time2 if vencedor == time1 else time1
            gols_vencedor = gols_time1 if vencedor == time1 else gols_time2
            gols_vice = gols_time2 if vencedor == time1 else gols_time1

        # Adiciona o vencedor e o vice às listas
        vencedor_final.append(vencedor)
        vice_final.append(vice)

    # Salva os resultados da final (campeão, vice, e os gols)
    # salvar_resultado_final(vencedor_final[0], gols_vencedor, vice_final[0], gols_vice)

    return vencedor_final[0], gols_vencedor, vice_final[0], gols_vice










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

def simular_partida(time_casa, time_fora, resultados, classificacao):
    if (time_casa, time_fora) in resultados:
        return resultados[(time_casa, time_fora)]
    if (time_fora, time_casa) in resultados:
        return resultados[(time_fora, time_casa)]

    gols_casa, gols_fora = gerar_gols(time_casa, time_fora)

    atualizar_classificacao(time_casa, gols_casa, time_fora, gols_fora, classificacao)
    atualizar_gols_acumulados_json(time_casa, gols_casa)
    atualizar_gols_acumulados_json(time_fora, gols_fora)

    resultado = "{:>20} {:<1} x {:<1} {:<20}".format(time_casa, gols_casa, gols_fora, time_fora)
    resultados[(time_casa, time_fora)] = resultado

    return resultado

def exibir_classificacao(classificacao):
    # Ordena primeiro por pontos e depois por saldo de gols
    classificacao_ordenada = sorted(classificacao.items(), key=lambda x: (x[1]['pontos'], x[1]['saldo_gols'], x[1]['gols_marcados']), reverse=True)
    
    print("\nTabela de Classificação Final:")
    print("\n")
    print("{:<4} {:<20} {:<6} {:<6} {:<6} {:<6} {:<6} {:<6} {:<6}".format("Pos", "Time", "Pts", "GM", "GS", "SG", "V", "E", "D"))
    print("\n")
    
    for i, (time, dados) in enumerate(classificacao_ordenada, start=1):
        print(f"{i:<4} {time:<20} {dados['pontos']:<6} {dados['gols_marcados']:<6} {dados['gols_sofridos']:<6} {dados['saldo_gols']:<6} {dados['vitorias']:<6} {dados['empates']:<6} {dados['derrotas']:<6}")










def simular_confrontos(home_away, resultados, classificacao):
    resultados_partidas = []
    for time in sorted(home_away.keys()):
        resultados_partidas.append(f"\n{time}:\n")
        for adversario in home_away[time]["home"]:
            resultados_partidas.append(simular_partida(time, adversario, resultados, classificacao))
        for adversario in home_away[time]["away"]:
            resultados_partidas.append(simular_partida(adversario, time, resultados, classificacao))
    return resultados_partidas













def print_trophy(vencedorFinal):
    print("\n")
    print("\n")
    print(f"""
             ___________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ){vencedorFinal}´´´´
               _.' '._
          `"""""""`
    """)



def salvar_resultado_final(vencedor_final, gols_vencedor, vice_final, gols_vice):
    nome_arquivo = "campeoes.json"
    
    # Se o arquivo já existir, carregue o conteúdo
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r') as file:
            historico_finais = json.load(file)
    else:
        historico_finais = []

    configuracao_atual = carregar_configuracao()
    nivel_gols_simulacao = configuracao_atual["nivel_gols"]

    # Adiciona os dados da final atual (incluindo os gols do vencedor e do vice)
    final = {
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

def exibir_finais():
    nome_arquivo = "campeoes.json"
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r') as file:
            historico_finais = json.load(file)
            print("\nHistórico de Finais:\n")
            for i, final in enumerate(historico_finais, start=1):
                print(f"{i}. {final['campeao']['time'].upper()} {final['campeao']['gols']}, {final['vice']['time']} {final['vice']['gols']}")
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
        print("Nenhum campeão registrado ainda.")
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
        
        # Exibe os campeões em formato numerado
        for i, (time, titulos) in enumerate(campeoes_ordenados, start=1):
             print(f"{i:<4}{time:<30} {titulos} título(s)")
    else:
        print("\n")
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
        print("Nenhum vice-campeão registrado ainda.")
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
        
        # Exibe os vice-campeões em formato numerado
        for i, (time, vices_count) in enumerate(vices_ordenados, start=1):
            print(f"{i:<4}{time:<30} {vices_count} vice-campeonato(s)")
    else:
        print("\nNenhum vice-campeão registrado ainda.")




def verificar_time_nos_potes(nome_time):
    """Verifica se o time existe nos potes"""
    # Transforma o nome_time em minúsculas para uma comparação consistente
    nome_time = nome_time.lower()
    
    for pote in potes:
        for time in pote:
            # Compara os nomes convertidos para minúsculas para garantir consistência
            if nome_time == time.lower():
                return True
    return False

def pesquisar_campeao_por_time(nome_time):
    nome_arquivo = "campeoes.json"
    contador_campeao = 0
    contador_vice = 0

    # Verifica se o time está nos potes
    if not verificar_time_nos_potes(nome_time):
        print(f"\nO time {nome_time.upper()} não existe nos potes.")
        return 0

    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r') as file:
            historico_finais = json.load(file)

            # Verifica se o time foi campeão ou vice-campeão
            for final in historico_finais:
                campeao_time = final['campeao']['time'].lower()  # Converte o nome do campeão para minúsculas
                vice_time = final['vice']['time'].lower()  # Converte o nome do vice-campeão para minúsculas

                # Compara ambos os nomes em minúsculas para campeões
                if campeao_time == nome_time.lower():
                    contador_campeao += 1  # Incrementa o contador de títulos de campeão

                # Compara ambos os nomes em minúsculas para vice-campeões
                if vice_time == nome_time.lower():
                    contador_vice += 1  # Incrementa o contador de vice-campeonatos

    # Exibe os resultados
    if contador_campeao == 0 and contador_vice == 0:
        print(f"\nO time {nome_time.upper()} não chegou à nenhuma final.")
    else:
        print("\n")
        print(f"Time: {nome_time.upper()}")
        print(f"Campeão: {contador_campeao} vez(es)")
        print(f"Vice-campeão: {contador_vice} vez(es)")
        print("\n")

    return contador_campeao, contador_vice


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
    config_atual = carregar_configuracao()

    print("\n")
    print("\n--- Configurações de Níveis de Gols ---\n".upper())
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
        print("\n--- Detalhes da configuração atual ---".upper())
        print("\n")
        print("\n")
        print(f"Nível de gols atual: {config_atual['nivel_gols'].replace('_', ' ').upper()}")
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
    print("\nVoltando para o Menu...")
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















class ExitLoops(Exception):
    pass

def main():

    try:    
        if not os.path.exists("configuracao_gols.json"):
            criar_configuracao_padrao()
    
        voltar_menu_principal = False  # Inicializa fora de todos os loops

        while True:
            menu_principal()        
            escolha_menu = input("\nENTER - Entrar no simulador\n1 - Configurações\n2 - Sair\n\n".upper()).strip().upper()

            if escolha_menu == '1':
                print("\n")
                configs = input("\n1 - Editar média de gols no jogo\n2 - Voltar\n\n".upper())
                print("\n")
                print("\n")
                if configs == '1':
                    configurar_nivel_gols()
                    continue
                elif configs == '2':
                    continue

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
                                print("{:<20}¦ {}".format(time, ', '.join(f"{rival:<2}" for rival in rivais_ordenados)))

                            # Pergunta ao usuário se ele quer simular as partidas, pesquisar dados ou voltar ao menu principal
                            print("\n")
                            print("\n")
                            escolha = input("\nENTER - Simular partidas\n1 - Sortear novamente\n2 - Pesquisar dados\n3 - Menu Principal\n\n".upper()).strip().upper()

                            if escolha == '':
                                resultados = {}
                                print("\n")
                                print("\nSimulando partidas...")
                                print("\n")
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
                                                                                                                vencedorFinal, gols_vencedor, viceFinal, gols_vice = placar_final_final(vencedores_semis)
                                                                                                                print("\n{:>16}\nCampeão: {}".format('', vencedorFinal))
                                                                                                                print_trophy(vencedorFinal)
                                                                                                                print("\n")
                                                                                                                print("\n")
                                                                                                                salvar_resultado_final(vencedorFinal, gols_vencedor, viceFinal, gols_vice)

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
                                                                                                                                finalizar_simulacao()
                                                                                                                                raise ExitLoops
                                                                                                                            elif voltar_ao_sorteio == '1':
                                                                                                                                break

                                                                                                                            else:
                                                                                                                                print("\n")
                                                                                                                                print("\nOpção inválida. Por favor, tente novamente.\n\n")
                                                                                                                            

                                                                                                                            
                                                                                                                            
                                                                                                    

                                                                                                                    elif escolha_finais2 == '2':
                                                                                                                        while True:  # Novo loop para Outras Opções
                                                                                                                            print("\n")
                                                                                                                            finalizar_simulacao()
                                                                                                                            outras_opcoes = input("\nENTER - Voltar para o menu\n\n").strip().upper()
                                                                                                                            print("\n")
                                                                                                                            if outras_opcoes == '':
                                                                                                                                raise ExitLoops
                                                                                
                                                                                                                            else:
                                                                                                                                print("\n")
                                                                                                                                print("\nOpção inválida. Por favor, tente novamente.\n\n")
                                                                                                                            

                                                                                                                    elif escolha_finais2 == '':
                                                                                                                        print("\nstats")
                                                                                                                        

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
                                        break  # Volta ao menu principal

                                    else:
                                        print("\n")
                                        print("\nOpção inválida. Por favor, tente novamente.\n\n")

                            elif escolha == '2':
                                while True:  # Loop secundário para voltar à pesquisa
                                    print("\n")
                                    procurar_dados = input("\n1 - Exibir todas as finais\n2 - Listar campeões\n3 - Listar vice-campeões\n4 - Pesquisar por time\n5 - Voltar para o sorteio\n\n".upper())
                                    print("\n")

                                    if procurar_dados == '1':
                                        print("\n")
                                        exibir_finais()
                                        print("\n")
                                        voltar = input("1 - Voltar para pesquisa de dados\n2 - Voltar para sorteio\n\n".upper())
                                        print("\n")

                                        if voltar == '1':
                                            continue  # Volta para o loop de pesquisa
                                        elif voltar == '2':
                                            break  # Sai do loop de pesquisa e volta para o início

                                    elif procurar_dados == '2':
                                        print("\n")
                                        listar_campeoes_ordenados()
                                        print("\n")
                                        voltar = input("1 - Voltar para pesquisa de dados\n2 - Voltar para sorteio\n\n".upper())
                                        print("\n")

                                        if voltar == '1':
                                            continue  # Volta para o loop de pesquisa
                                        elif voltar == '2':
                                            break  # Sai do loop de pesquisa e volta para o início

                                    elif procurar_dados == '3':
                                        print("\n")
                                        listar_vices_ordenados()
                                        print("\n")
                                        voltar = input("1 - Voltar para pesquisa de dados\n2 - Voltar para sorteio\n\n".upper())
                                        print("\n")

                                        if voltar == '1':
                                            continue  # Volta para o loop de pesquisa
                                        elif voltar == '2':
                                            break  # Sai do loop de pesquisa e volta para o início

                                    elif procurar_dados == '4':
                                        while True:  # Novo loop para pesquisar por time até o usuário escolher sair
                                            print("\n")
                                            nome_time = input("Digite o nome do time que deseja pesquisar: \n\n")
                                            print("\n")
                                            print("\n")
                                            pesquisar_campeao_por_time(nome_time)

                                            print("\n")
                                            voltar = input("\n1 - Voltar para pesquisa de dados\n2 - Voltar para sorteio\nENTER - Pesquisar novamente\n\n".upper())
                                            print("\n")

                                            if voltar == '':
                                                continue  # Volta para pesquisar outro time
                                            elif voltar == '1':
                                                break  # Volta para o menu de pesquisa de dados
                                            elif voltar == '2':
                                                break  # Volta para o sorteio

                                        if voltar == '3':
                                            break

                                    elif procurar_dados == '5':
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
        print("\nPrograma interrompido pelo usuário.")
        print("\n")

# Executa o programa
if __name__ == "__main__":
    main()