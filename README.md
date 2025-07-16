# Projeto Final Aprendizado de Maquinas
Por: Vitor Mello

## Enunciado
### Classificação de Bons e Maus Pagadores

Um cliente do setor financeiro forneceu um conjunto de dados contendo informações de diferentes clientes, com o objetivo de identificar bons e maus pagadores. Cada registro do dataset representa um cliente, descrito por diversas variáveis que indicam características financeiras e comportamentais, além da indicação se o cliente é um bom pagador (classe 0) ou mau pagador (classe 1).

O cliente precisa de uma solução automatizada para classificar novos clientes em bons ou maus pagadores de forma eficaz, para otimizar processos de concessão de crédito e minimizar riscos financeiros.

Por se tratar de decisões que envolvem dinheiro real e impacto direto nas operações da empresa, a solução deve atender aos seguintes requisitos essenciais:

- **Desempenho preditivo confiável:** o modelo deve apresentar bom desempenho para garantir decisões adequadas em dados futuros.
- **Interpretabilidade:** o cliente exige que a solução seja compreensível, de modo que os analistas possam identificar quais características influenciam as decisões e justificar os resultados internamente e para órgãos reguladores.
- **Automação:** o processo deve ser automatizado, abrangendo desde o pré-processamento dos dados até a seleção das variáveis mais relevantes e a construção do modelo final.

Sua tarefa é desenvolver uma solução automatizada que atenda a esses objetivos.

A solução entregue deve conter código completo, organizado e documentado, facilitando sua integração ao fluxo operacional do cliente.

## Resultado
### 1. Análise Exploratória dos Dados (EDA)

Removi variáveis com correlação muito baixa ou muito alta com o target. O resultado pode ser visto na tabela abaixo. Mais detalhes estão disponíveis neste [notebook](notebooks/01_eda.ipynb):

|         |        class |
|:--------|-------------:|
| feat_31 |  1           |
| feat_14 |  0.000856701 |
| feat_24 |  0.000400526 |
| feat_23 |  0.000391264 |
| feat_27 | -0.000502959 |

### 2. PCA
Como todas as variáveis apresentaram baixa correlação com o target, investigamos a hipótese de que a redução de dimensionalidade via PCA não comprometeria a performance — o que se confirmou.

Abaixo, os autovalores resultantes do PCA:
![autovalores](img/autovalores.png)

O gráfico a seguir mostra que a performance do modelo se mantém estável com três ou mais componentes principais:

![pca_impact](img/pca_impact.png)

Além disso, observamos que, após o PCA, o target tornou-se bem separável no novo espaço vetorial, o que motivou o uso do SVM como modelo principal:

![divisao](img/pca_division.png)

### 3. SVM Tuning
Utilizamos o Optuna para realizar o tuning dos hiperparâmetros do SVM. Os melhores parâmetros encontrados foram:

```
"C": 10.251516094582083,
"kernel": "rbf",
```

### 4. Benchmark com LGBM
Para comparação, treinamos um modelo benchmark utilizando o LightGBM. O tuning também foi feito com Optuna, e os melhores parâmetros foram:

```
"learning_rate": 0.05588119464680504,
"num_leaves": 82,
"max_depth": 9,
"min_child_samples": 14,
"subsample": 0.8466398877355169,
"colsample_bytree": 0.9156682910427868,
"reg_alpha": 0.000239851442633549,
"reg_lambda": 0.0033246794209540052
```

### 5. Tuning threshold
Como se trata de um problema de crédito com classes desbalanceadas, utilizamos o F1-score como métrica principal. Para isso, foi necessário ajustar o threshold de decisão. A otimização foi feita com o `TunedThresholdClassifierCV`.

### 6. Treino final
O treinamento final do modelo foi realizado com o pipeline salvo no diretório `src/`, e o binário do modelo foi armazenado como `.pkl` no diretório `models/`.

### 7. Desempenho final
| Model    |   F1 Train |   F1 Test |
|:---------|-----------:|----------:|
| LightGBM |     1.0000 |    0.9475 |
| SVM      |     0.9863 |    0.9691 |

## Setup (linux ou macos)
Este projeto utiliza o UV para gerenciamento eficiente de dependências Python e instalação do projeto. O UV é um instalador e resolutor de pacotes Python rápido, moderno e projetado como alternativa ao pip e pip-tools.

Sistemas operacionais suportados: Linux, macOS

### 1. Instalando o UV (Optional)

Siga a documentação oficial do UV para instruções de instalação:
- [Documentação UV: Instalando o UV](https://docs.astral.sh/uv/getting-started/installation/#installing-uv)

Exemplo (macOS/Linux via Homebrew):
```
brew install uv
```
### 2. Instalação do projeto

Ao contrário de projetos Python tradicionais que costumam usar requirements.txt ou setup.py, este projeto gerencia suas dependências diretamente por meio de um arquivo .toml. Isso significa que não há arquivos requirements.txt, requirements.in ou setup.py.

Para configurar o projeto e instalar suas dependências, acesse o diretório raiz deste repositório e execute o seguinte comando:

```
pip install -e .
```
Explanation:

- `pip install`: comando que instala pacotes Python.

- `-e .` (instalação em modo editável): este comando instala o projeto de forma que qualquer alteração no código fonte seja refletida imediatamente sem precisar reinstalar o pacote, facilitando o desenvolvimento.
