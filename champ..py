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
    classificados = sorted(classificacao.items(), key=lambda x: x[1]['pontos'], reverse=True)
    
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
    classificados = sorted(classificacao.items(), key=lambda x: x[1]['pontos'], reverse=True)
    
    print("\nResultados dos playoffs:")
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

    resultados_ida = {}
    
    for time1, time2 in confrontos_playoffs:
        gols_time1, gols_time2 = gerar_gols(time1, time2)
        resultados_ida[(time1, time2)] = (gols_time1, gols_time2)
        print("{:>20} {:<1} x {:<1} {:<20}".format(time1, gols_time1, gols_time2, time2))

    return resultados_ida

def simular_playoff_volta(classificacao):
    # Obtém os classificados para os playoffs (9º a 24º)
    classificados = sorted(classificacao.items(), key=lambda x: x[1]['pontos'], reverse=True)
    
    print("\nResultados da volta:")
    print("\n")
    confrontos_playoffs = [
        (classificados[23][0], classificados[8][0]),  # 9º x 24º
        (classificados[22][0], classificados[9][0]),  # 10º x 23º
        (classificados[21][0], classificados[10][0]),  # 11º x 22º
        (classificados[20][0], classificados[11][0]),  # 12º x 21º
        (classificados[19][0], classificados[12][0]),  # 13º x 20º
        (classificados[18][0], classificados[13][0]),  # 14º x 19º
        (classificados[17][0], classificados[14][0]),  # 15º x 18º
        (classificados[16][0], classificados[15][0]),  # 16º x 17º
    ]

    resultados_volta = {}
    
    for time1, time2 in confrontos_playoffs:
        gols_time1, gols_time2 = gerar_gols(time1, time2)
        resultados_volta[(time1, time2)] = (gols_time1, gols_time2)
        print("{:>20} {:<1} x {:<1} {:<20}".format(time1, gols_time1, gols_time2, time2))

    return resultados_volta


def placar_final_playoffs(classificacao):
    resultados_ida = simular_playoff(classificacao)
    resultados_volta = simular_playoff_volta(classificacao)

    print("\n")
    print("\nResultados dos Playoffs:")
    print("\n")
    
    for (time1, time2), (gols_ida1, gols_ida2) in resultados_ida.items():
        gols_volta1, gols_volta2 = resultados_volta[(time2, time1)]  # Inverte os times para pegar os resultados da volta
        total_time1 = gols_ida1 + gols_volta2
        total_time2 = gols_ida2 + gols_volta1
        print("{:>20} {:<1} x {:<1} {:<20}".format(time1, total_time1, total_time2, time2))











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
        escolha = input("\nAperte 'S' para simular as partidas ou 'R' para sortear novamente: ").strip().upper()

        if escolha == 'S':
            resultados = {}
            print("\nSimulando partidas...")
            resultados_partidas = simular_confrontos(home_away, resultados, classificacao)
            print("\nResultados das partidas:")
            print("\n".join(resultados_partidas))

            # Nova condição para exibir a tabela de classificação
            while True:
                escolha_tabela = input("\nAperte 'T' para exibir a tabela de classificação, 'P' para ver play-offs ou 'R' para sair: ").strip().upper()
                
                if escolha_tabela == 'T':
                    exibir_classificacao(classificacao)
                elif escolha_tabela == 'P':
                    print("\n")
                    exibir_playoffs(classificacao)
                    continuar = input("\nDeseja continuar a simulação dos playoffs? (S para continuar, R para sair): ").strip().upper()
                    if continuar == 'S':
                        # Aqui você pode adicionar a lógica para simular as partidas dos playoffs
                        
                        print("Continuando a simulação dos playoffs...")
                        print("\n")
                        simular_playoff(classificacao)
                        # Após a simulação dos playoffs, pergunta se deseja simular a volta
                        simular_volta_opcao = input("\nDeseja simular os jogos de volta? (S para continuar, R para sair): ").strip().upper()
                        if simular_volta_opcao == 'S':
                            print("Simulando os jogos de volta...")
                            print("\n")
                            simular_playoff_volta(classificacao)
                            print("\n")
                            placar_final_playoffs(classificacao)
                        elif simular_volta_opcao == 'R':
                            print("\nSaindo do programa.")
                            return


                    elif continuar == 'R':
                        print("\nSaindo do programa.")
                        return
                    else:
                        print("\nOpção inválida. Por favor, tente novamente.")
                elif escolha_tabela == 'R':
                    print("\nSaindo do programa.")
                    return
                else:
                    print("\nOpção inválida. Por favor, tente novamente.")


# Executa o programa
if __name__ == "__main__":
    main()



