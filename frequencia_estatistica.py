'''
Tabela de Distribuição de Frequências
Atividade de Ciência de Dados proposta por Profº Fred Jorge Tavares de Lucena - FICR

Desenvolver um algoritmo que receba `n` valores e o número de classes (`k`),
organize os dados e exiba uma tabela estatística.

# Restrições
- Não utilizar bibliotecas de análise de dados (Pandas, Numpy, etc).
- A lógica de ordenação e cálculo deve ser manual.

# Passos do Algoritmo
1. Entrada: Receber lista de valores (desordenados) e o número de classes (k).
2. Ordenação: Ordenar os valores crescentemente.
3. Cálculos Base:
   - Amplitude Total (At) = V_max - V_min
   - Tamanho da Classe (Tk) = At / k (Arredondando pra cima se necessário)
4. Iteração: Percorrer os dados para preencher as classes.
5. Cálculo de Frequências:
   - Absoluta (fk): Contagem na classe.
   - Relativa (frel): fk / total_elementos (%).
   - Absoluta Acumulada (Fk): Soma entre a frequência atual com a frequências anterior.
   - Relativa Acumulada (Frel): Soma das % anteriores.
6. Saída: Exibir a tabela formatada com todos os dados e frequências.

# Autores deste código
- Israel Brito
- Higor Gomes

'''

import math

def ordenar_valores(valores):
    # Passo 2: Ordenando os valores
    valores.sort()
    n = len(valores)
    v_min = valores[0]
    v_max = valores[-1]
    return valores, n, v_min, v_max

def calcular_amplitude_e_tamanho_classe(v_min, v_max, k):
    # Passo 3: Cálculos Base
    amplitude_total = v_max - v_min
    tam_k = math.ceil(amplitude_total / k)
    return amplitude_total, tam_k

def frequencias(valores, k, tam_k, v_min, n):
    
    # Inicializar classes e frequências
    classes = []
    frequencias_absolutas = [0] * k
    
    # Definir as classes
    for i in range(k):
        classe_inferior = v_min + i * tam_k
        classe_superior = classe_inferior + tam_k
        classes.append((classe_inferior, classe_superior))
        
    # Calcular frequências absolutas
    for valor in valores:
        for i, (inferior, superior) in enumerate(classes):
            if i == k - 1:
                if inferior <= valor <= superior:
                    frequencias_absolutas[i] += 1
                    break
            else:
                if inferior <= valor < superior:
                    frequencias_absolutas[i] += 1
                    break
                
    # Calcular frequências relativas e acumuladas e colocando dentro de listas
    frequencias_relativas = [fk / n * 100 for fk in frequencias_absolutas]
    frequencias_acumuladas = []
    frequencias_acumuladas_relativas = []
    
    acumulada = 0
    acumulada_relativa = 0.0
    
    for fk, frel in zip(frequencias_absolutas, frequencias_relativas):
        acumulada += fk
        acumulada_relativa += frel
        frequencias_acumuladas.append(acumulada)
        frequencias_acumuladas_relativas.append(acumulada_relativa)

    return classes, frequencias_absolutas, frequencias_relativas, frequencias_acumuladas, frequencias_acumuladas_relativas

def tabela_frequencia(valores, k):
    # Ordenar os valores e obter valor mínimo, valor máximo e n (qtd. elementos)
    valores, n, v_min, v_max = ordenar_valores(valores)
    
    # Calcular amplitude total e tamanho da classe
    amplitude_total, tam_k = calcular_amplitude_e_tamanho_classe(v_min, v_max, k)
    
    # Calcular as frequências
    classes, frequencias_absolutas, frequencias_relativas, frequencias_acumuladas, frequencias_acumuladas_relativas = frequencias(valores, k, tam_k, v_min, n)
    
    # Imprimir a tabela de frequências
    print("\n" + "="*170)
    print(f"{'(K) Classe':<10} | {'Intervalos':<25} | {'(fk) Freq.Absoluta':<20} | {'(frel) Freq. Relativa':<25} | {'(Fk) Freq. Abs. Acumulada':<30} | {'(Frel) Freq. Rel. Acumulada':<30}")
    print("-" * 170)

    # Linhas de dados
    for i in range(k):
        inferior = classes[i][0]
        superior = classes[i][1]
        # Formatação da classe
        if i == k - 1:
            # Se o valor máximo dos valores atingir o teto dos intervalos
            if v_max == superior:
                classe_str = f"{inferior} |--| {superior}"
            else:
                # Caso contrário, usa o símbolo |- indicando o intervalo aberto
                classe_str = f"{inferior} |-   {superior}"
        else:
            classe_str = f"{inferior} |-   {superior}"
            
        # Formatação dos valores: frel e Frel com '%' e arredondados para 2 casas decimais
        frel_str = f"{frequencias_relativas[i]:.2f}%"
        frel_acum_str = f"{frequencias_acumuladas_relativas[i]:.2f}%"
        
        print(f"{i+1:<10} {classe_str:<20} {frequencias_absolutas[i]:<20} {frel_str:<25} {frequencias_acumuladas[i]:<30} {frel_acum_str:<30}")
    
    print("-" * 170)
    
    # Linha Total
    total_fk = sum(frequencias_absolutas)
    total_frel = sum(frequencias_relativas)
    
    # Garantindo que o total de frel seja 100% 
    if abs(total_frel - 100.0) < 0.01:
        total_frel = 100.0

    print(f"{'Total':<10} {'':<25} {total_fk:<20} {total_frel:.2f}%{'':<25} {'':<30} {'':<30}")

    print("\n")

        
# Input do usuário
valores = input("Digite os valores separados por espaço: ").split()
valores = [float(v) for v in valores]  # Convertendo para float
k = int(input("Digite o número de classes (k): "))

tabela_frequencia(valores, k)