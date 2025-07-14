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