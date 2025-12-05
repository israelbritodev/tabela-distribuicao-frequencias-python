# 📊 Gerador de Tabela de Distribuição de Frequências

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Estatística](https://img.shields.io/badge/Statistics-Fundamental-orange?style=for-the-badge)
![Estrutura de Dados](https://img.shields.io/badge/Data%20Structure-Algorithms-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)

> Um algoritmo robusto desenvolvido em **Python Puro**  para organizar dados brutos em tabelas estatísticas detalhadas, sem a dependência de bibliotecas externas como Pandas ou NumPy.

---

## 🧐 O Porquê deste Código

Em um mundo dominado por bibliotecas prontas, **entender o que acontece "por baixo do capô"** é uma habilidade essencial. O objetivo deste projeto foi desafiar a lógica de programação ao implementar manualmente os conceitos estatísticos de distribuição de frequências.

O código resolve problemas de **arredondamento de classes**, **intervalos abertos/fechados** e **formatação visual** dinâmica no terminal.


## 🚀 Funcionalidades e Estrutura

O código foi estruturado de forma modular para facilitar a leitura e manutenção. Abaixo, a explicação de cada etapa lógica:

### 1. Ordenação e Dados Brutos (`ordenar_valores`)
Recebe uma lista desordenada de números.
- **Lógica:** Utiliza o método `.sort()` para garantir a sequenciação.
- **Resultado:** Identificação imediata de $V_{min}$ (Mínimo) e $V_{max}$ (Máximo).

### 2. Matemática da Classe (`calcular_amplitude`)
Calcula matematicamente o tamanho de cada "gaveta" (classe) da tabela.
- **Fórmula:** $T_k = \lceil \frac{V_{max} - V_{min}}{k} \rceil$
- **Detalhe:** Uso de `math.ceil` para arredondar para cima, garantindo que todos os elementos caibam nas classes estipuladas.

### 3. Iteração e Contagem (`frequencias`)
O coração do algoritmo. Percorre os dados e os aloca em suas respectivas classes.
- **Destaque:** Lógica condicional para tratar a última classe, que deve incluir o limite superior (intervalo fechado `<=`) diferentemente das anteriores (intervalo aberto `<`).

### 4. Visualização Dinâmica (`tabela_frequencia`)
Aqui brilha a **formatação condicional** implementada.
- **Seta Dinâmica:** O código verifica se o valor máximo real dos dados atingiu o teto da classe.
    - `|--|` : Indica que o intervalo fechou exatamente no limite (ex: $Max=100$, Limite=100).
    - `|-  ` : Indica que o intervalo permaneceu aberto visualmente pois o valor máximo não tocou o limite (ex: $Max=97$, Limite=100).


## 🛠️ Tecnologias e Habilidades Desenvolvidas

Durante a construção deste algoritmo, foram aprimoradas as seguintes competências:

* 🐍 **Python Fluency:** Manipulação de listas, loops aninhados (`for`), f-strings e input de dados.
* 🧮 **Lógica Algorítmica:** Tradução de fórmulas matemáticas para código funcional.
* 📉 **Estatística Descritiva:** Compreensão profunda de Frequência Absoluta ($f_k$), Relativa ($fr\%$) e Acumulada ($F_k$).
* 🎨 **UX no Terminal:** Formatação de strings para criar tabelas visualmente alinhadas e legíveis.
* 🚫 **Constraint Programming:** Resolver o problema sem usar `import pandas`.


## 💻 Como Executar

Certifique-se de ter o **Python 3** instalado.

1. Clone o repositório:
```bash
git clone https://github.com/israelbritodev/tabela-distribuicao-frequencias-python.git
```

2. Execute o arquivo:
```bash
python frequencia_estatistica.py
``` 
3. Insira os dados quando solicitado:
```bash
Digite os valores: 50 51 52 59 60 70 80 97
Digite o k (classes): 5
```

## 📈 Resultados Obtidos

O script gera uma tabela alinhada no console, calculando automaticamente as porcentagens, frequências e acumulados.

Exemplo de Saída (Output):

```bash 
=====================================================================================================================================
K Classe   Toneladas de Lixo         fk Freq.Absoluta     frel Freq. Relativa       Fk Freq. Abs. Acumulada        Frel Freq. Rel. Acumulada     
-------------------------------------------------------------------------------------------------------------------------------------
1          50.0 |-   60.0            14                   28.00%                    14                             28.00%                        
2          60.0 |-   70.0            13                   26.00%                    27                             54.00%                        
3          70.0 |-   80.0            7                    14.00%                    34                             68.00%                        
4          80.0 |-   90.0            8                    16.00%                    42                             84.00%                        
5          90.0 |-   100.0           8                    16.00%                    50                             100.00%                       
-------------------------------------------------------------------------------------------------------------------------------------
Total                                50                   100.00%                                                                                
=====================================================================================================================================
``` 


🤝 Autores
Israel Brito e Higor Gomes

<p align="center"> Feito com 💙 e muito ☕ em Python </p>