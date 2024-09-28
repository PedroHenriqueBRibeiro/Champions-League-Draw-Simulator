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
    # Fórmula para a média
    media = max(0.5, (ataque_time - defesa_adversario) / 10 + 1.5)  # Fórmula ajustável
    # Definimos o desvio padrão como uma fração da média (20% da média, por exemplo)

    desvio = max(0.7, (50 - abs(ataque_time - defesa_adversario)) / 30)  # Exemplo de escala ajustável
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
    # Número inicial de cobranças
    num_cobrancas = 5
    gols_time1 = 0
    gols_time2 = 0

    while True:
        for i in range(num_cobrancas):
            # Time 1 cobra
            if random.random() < 0.75:  # 80% de chance de gol
                gols_time1 += 1

            # Time 2 cobra (somente se ainda houver cobranças restantes)
            if i < num_cobrancas - 1:
                if random.random() < 0.75:  # 80% de chance de gol
                    gols_time2 += 1
        
        # Verifica se os gols são diferentes
        if gols_time1 != gols_time2:
            break  # Sai do loop se houver um vencedor

        # Se os gols forem iguais, resetamos para uma nova rodada
        gols_time1 = 0
        gols_time2 = 0

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
        
        print("{:>20} {:<1} x {:<1} {:<20}".format(time1, gols_time1, gols_time2, time2))

    resultados_volta = {}
    print("\n")
    print("Jogo de volta - Playoffs:\n")
    for time2, time1 in confrontos_playoffs:
        gols_time1, gols_time2 = gerar_gols(time1, time2)
        resultados_volta[(time1, time2)] = (gols_time1, gols_time2)
        
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
    primeiros_colocados = sorted(classificacao.items(), key=lambda x: x[1]['pontos'], reverse=True)[:8]
    
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
    primeiros_colocados = sorted(classificacao.items(), key=lambda x: x[1]['pontos'], reverse=True)

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
        
        print("{:>20} {:<1} x {:<1} {:<20}".format(time1, gols_time1, gols_time2, time2))

    resultados_volta = {}
    print("\n")
    print("Jogos de volta - Oitavas de final:\n")
    for time2, time1 in confrontos_oitavas:
        gols_time1, gols_time2 = gerar_gols(time1, time2)
        resultados_volta[(time1, time2)] = (gols_time1, gols_time2)
        
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
        print("{:>20} {:<1} x {:<1} {:<20}".format(time1, gols_time1, gols_time2, time2))

    resultados_volta = {}
    print("\n")
    print("Jogos de volta - Quartas de Final:\n")
    
    # Simula jogos de volta
    for time2, time1 in quartas_de_final:
        gols_time1, gols_time2 = gerar_gols(time1, time2)
        resultados_volta[(time1, time2)] = (gols_time1, gols_time2)
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
    
    # Confronto 1: [0] vs [1]
    print("{:>20} x {:<20}".format(vencedores_quartas[0], vencedores_quartas[1]))
    
    # Confronto 2: [2] vs [3]
    print("{:>20} x {:<20}".format(vencedores_quartas[2], vencedores_quartas[3]))


def simular_semifinais(vencedores_quartas):
    resultados_ida = {}
    resultados_volta = {}

    print("\nJogos de ida - Semifinais:\n")
    
    # Simula os jogos de ida para os dois confrontos
    for i in range(0, len(vencedores_quartas), 2):  # Percorre a lista de 2 em 2
        time1 = vencedores_quartas[i]
        time2 = vencedores_quartas[i + 1]
        gols_time1, gols_time2 = gerar_gols(time1, time2)
        resultados_ida[(time1, time2)] = (gols_time1, gols_time2)
        print("{:>20} {:<1} x {:<1} {:<20}".format(time1, gols_time1, gols_time2, time2))

    print("\nJogos de volta - Semifinais:\n")
    
    # Simula os jogos de volta para os dois confrontos
    for i in range(0, len(vencedores_quartas), 2):  # Percorre a lista de 2 em 2
        time1 = vencedores_quartas[i]
        time2 = vencedores_quartas[i + 1]
        gols_time2, gols_time1 = gerar_gols(time2, time1)  # Inverte os times para o jogo de volta
        resultados_volta[(time2, time1)] = (gols_time2, gols_time1)
        print("{:>20} {:<1} x {:<1} {:<20}".format(time2, gols_time2, gols_time1, time1))

    return resultados_ida, resultados_volta


def placar_final_semis(vencedores_quartas):
    resultados_ida, resultados_volta = simular_semifinais(vencedores_quartas)
    vencedores_semis = []
    print("\n")
    print("\nPlacar Agregado - Semifinais:")
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
    print("\nVencedores das semifinais:\n")
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

    # Calcula o placar final e determina o vencedor
    for (time1, time2), (gols_time1, gols_time2) in resultado.items():
        print("{:>20} {:<1} x {:<1} {:<20}".format(time1, gols_time1, gols_time2, time2))

        # Caso de empate no tempo normal, simula pênaltis
        if gols_time1 == gols_time2:
            gols_penaltis1, gols_penaltis2 = simular_penaltis(time1, time2)
            print(f"{'':>16}Pen ({gols_penaltis1} - {gols_penaltis2})")
            vencedor = time1 if gols_penaltis1 > gols_penaltis2 else time2
            vencedor_final.append(vencedor)
            vice = time1 if gols_penaltis1 < gols_penaltis2 else time2
            vice_final.append(vice)
            gols_vencedor = (f"{gols_time1} ({gols_penaltis1} PEN)")
            gols_vice = (f"{gols_time2} ({gols_penaltis2} PEN)")
        else:
            vencedor = time1 if gols_time1 > gols_time2 else time2
            vencedor_final.append(vencedor)
            vice = time1 if gols_time1 < gols_time2 else time2
            vice_final.append(vice)
            gols_vencedor = gols_time1 if vencedor == time1 else gols_time2
            gols_vice = gols_time2 if vencedor == time1 else gols_time1

    # Salva os resultados da final (campeão, vice, e os gols)
    #salvar_resultado_final(vencedor_final[0], gols_vencedor, vice_final[0], gols_vice)

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

    # Adiciona os dados da final atual (incluindo os gols do vencedor e do vice)
    final = {
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

def exibir_campeoes():
    nome_arquivo = "campeoes.json"
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r') as file:
            historico_finais = json.load(file)
            print("\nHistórico de Finais:\n")
            for i, final in enumerate(historico_finais, start=1):
                print(f"{i}. {final['campeao']['time'].upper()} {final['campeao']['gols']}, {final['vice']['time']} {final['vice']['gols']}")
    else:
        print("Nenhum campeão registrado ainda.")

def verificar_time_nos_potes(nome_time):
    """Verifica se o time existe nos potes"""
    nome_time = nome_time.capitalize()
    for pote in potes:
        if nome_time in pote:  # Verifica se o time está na lista de potes
            return True
    return False

def pesquisar_campeao_por_time(nome_time):
    nome_arquivo = "campeoes.json"
    contador = 0

    # Verifica se o time está nos potes
    if not verificar_time_nos_potes(nome_time):
        print(f"\nO time {nome_time.upper()} não existe nos potes.")
        return 0

    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r') as file:
            historico_finais = json.load(file)

            # Verifica se o time foi campeão
            for final in historico_finais:
                if final['campeao']['time'].capitalize() == nome_time.capitalize():
                    contador += 1  # Incrementa o contador se o time for campeão


    if contador == 0:
        print(f"\nO time {nome_time.upper()} não foi campeão até agora.")
    else: 
        print("\n")        
        print(f"O time {nome_time.upper()} foi campeão {contador} vez(es).")
        print("\n")
    
    return contador










def main():
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
        print("\nConfrontos sorteados:")
        print("\n")
        for time in sorted(confrontos.keys()):
            rivais_ordenados = agrupar_rivais_por_pote_intercalados(confrontos, time)
            # Imprime apenas uma linha formatada para cada time
            print("{:<20}¦ {}".format(time, ', '.join(f"{rival:<2}" for rival in rivais_ordenados)))

        # Pergunta ao usuário se ele quer simular as partidas ou sortear novamente
        escolha = input("\n1 - Simular partidas\n2 - Pesquisar dados\nENTER - Sortear novamente\n").strip().upper()
        if escolha == '2':
            while True:  # Loop secundário para voltar à pesquisa
                procurar_dados = input("\n1 - Exibir todas as finais\n2 - Pesquisar por time\n3 - Voltar para o sorteio\n")
                
                if procurar_dados == '1':
                    exibir_campeoes()
                    print("\n")
                    voltar = input("1 - Voltar para pesquisa de dados\n2 - Voltar para sorteio\n")
                    
                    if voltar == '1':
                        print("Voltando para pesquisa dados...\n")
                        continue  # Volta para o loop de pesquisa
                    
                    elif voltar == '2':
                        print("Voltando para o sorteio...\n")
                        break  # Sai do loop de pesquisa e volta para o início
                
                elif procurar_dados == '2':
                    while True:  # Novo loop para pesquisar por time até o usuário escolher sair
                        print("\n")
                        nome_time = input("Digite o nome do time que deseja pesquisar: \n")
                        print("\n")
                        nome_time = nome_time.capitalize()
                        pesquisar_campeao_por_time(nome_time)
        
                        print("\n")
                        voltar = input("1 - Pesquisar novamente\n2 - Voltar para pesquisa de dados\n3 - Voltar para sorteio\n")
                        
                        if voltar == '1':
                            # Se o usuário escolher 1, o loop continua e volta para pesquisar outro time
                            continue
                        
                        elif voltar == '2':
                            print("Voltando para pesquisa de dados...\n")
                            break  # Sai desse loop e volta para o menu de pesquisa de dados
                        
                        elif voltar == '3':
                            print("Voltando para o sorteio...\n")
                            break  # Sai desse loop e volta para o início da simulação
                    
                    if voltar == '3':  # Se o usuário escolheu voltar para sorteio, sai do loop de pesquisa de dados também
                        break

                elif procurar_dados == '3':
                    break
                elif procurar_dados == '':
                    print("\nInsira uma opção válida\n")
                    continue


        elif escolha == '1':
            resultados = {}
            print("\nSimulando partidas...")
            resultados_partidas = simular_confrontos(home_away, resultados, classificacao)
            print("\nResultados das partidas:")
            print("\n".join(resultados_partidas))

            # Nova condição para exibir a tabela de classificação ou playoffs
            while True:
                escolha_tabela = input("\n1 - Exibir tabela de classificação\n2 - Sair\nENTER - Exibir confrontos dos play-offs\n").strip().upper()
                
                if escolha_tabela == '1':
                    exibir_classificacao(classificacao)
                
                elif escolha_tabela == '':
                    print("\n")
                    exibir_playoffs(classificacao)
                    continuar = input("\n1 - Sair\nENTER - Simular play-offs\n").strip().upper()
                    
                    if continuar == '':
                        vencedores = placar_final_playoffs(classificacao)
                        print("\n")
                    
                        
                        # Após a simulação dos playoffs, pergunta se deseja simular a volta
                        simular_volta_opcao = input("\n1 - Sair\nENTER - Continuar\n").strip().upper()
                        
                        if simular_volta_opcao == '':

                            # Exibe opções após resultados finais dos playoffs
                            while True:
                                escolha_finais = input("\n1 - Exibir tabela de classificação\n2 - Sair\nENTER - Exibir confrontos das oitavas\n").strip().upper()

                                if escolha_finais == '1':
                                    exibir_classificacao(classificacao)

                                elif escolha_finais == '':
                                    exibir_oitavas(classificacao, vencedores)
                                    print("\n")
                                    oitavas = input("ENTER - Simular oitavas de final\n")
                                    print("\n")
                                    
                                    if oitavas == '':
                                        vencedores_oitavas = placar_final_oitavas(classificacao, vencedores)
                                        print("\n")
                                        quartas = input("ENTER - Exibir confrontos das quartas").strip().upper()
                                        print("\n")                                       
                                        if quartas == '':
                                            # Sorteia e exibe os confrontos das quartas sem repetir a simulação
                                            quartas_de_final = sortear_quartas(vencedores_oitavas)
                                            
                                            exibir_confrontos_quartas(quartas_de_final)
                                            print("\n")
                                            simular_quartas = input("ENTER - Simular quartas de final\n")
                                            print("\n")
                                            if simular_quartas == '':
                                                vencedores_quartas = placar_final_quartas(quartas_de_final)
                                                print("\n")
                                                semis = input("ENTER - Exibir confrontos das semifinais\n").strip().upper()
                                                print("\n")
                                                if semis == '':
                                                    exibir_semi_final(vencedores_quartas)
                                                    print("\n")
                                                    simular_semis = input("ENTER - Simular semifinais\n").strip().upper()
                                                    print("\n")
                                                    if simular_semis == '':
                                                        vencedores_semis = placar_final_semis(vencedores_quartas)
                                                        final = input("\nENTER - Exibir final\n").strip().upper()
                                                        print("\n")
                                                        if final == '':
                                                            exibir_final(vencedores_semis)
                                                            print("\n")
                                                            
                                                            # Simula a final
                                                            simular_Final = input("ENTER - Simular final\n").strip().upper()
                                                            print("\n")
                                                            print("\n")
                                                            print("\n")
                                                            if simular_Final == '':
                                                                # Define e exibe o vencedor final
                                                                vencedorFinal, gols_vencedor, viceFinal, gols_vice = placar_final_final(vencedores_semis)

                                                                print("\n")
                                                                print("{:>16}\nCampeão: {}".format('', vencedorFinal))
                                                                print("\n")
                                                                print_trophy(vencedorFinal)
                                                                salvar_resultado_final(vencedorFinal, gols_vencedor, viceFinal, gols_vice)
                                                                print("\n")
                                                                escolha_finais2 = input("\n1 - Exibir tabela de classificação\n2 - Simular novamente a partir das oitavas\nENTER - Encerrar simulação\n").strip().upper()
                                                                if escolha_finais2 == '1':
                                                                    exibir_classificacao(classificacao)
                                                                    replay = input("\n1 - Simular novamente a partir das oitavas\nENTER - Encerrar simulação\n").strip().upper()
                                                                    if replay == '1':
                                                                        escolha_finais
                                                                    elif replay == '':
                                                                        print("\nSaindo do programa.")
                                                                        return
                                                                
                                                                elif escolha_finais2 == '2':
                                                                    escolha_finais

                                                                elif escolha_finais2 == '':
                                                                    print("\nSaindo do programa.")
                                                                    return
                                                                
                                
                                                                

                                        

                                
                                elif escolha_finais == '2':
                                    print("\nSaindo do programa.")
                                    return
                                
                                else:
                                    print("\nOpção inválida. Por favor, tente novamente.")
                        
                        elif simular_volta_opcao == '1':
                            print("\nSaindo do programa.")
                            return
                    
                    elif continuar == '1':
                        print("\nSaindo do programa.")
                        return
                    
                    else:
                        print("\nOpção inválida. Por favor, tente novamente.")
                
                elif escolha_tabela == '2':
                    print("\nSaindo do programa.")
                    return
                
                else:
                    print("\nOpção inválida. Por favor, tente novamente.")



# Executa o programa
if __name__ == "__main__":
    main()



