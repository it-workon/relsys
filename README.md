# RelSys – Sistema de Emissão de Relatórios e Documentos
## Visão Geral

O RelSys é uma aplicação voltada à automação da emissão de relatórios e documentos corporativos.
Seu objetivo é eliminar tarefas manuais repetitivas, reduzir erros e padronizar a geração de documentos internos, como comunicados, relatórios e materiais de boas-vindas para novos colaboradores.

Desenvolvido em Python, o RelSys integra manipulação de arquivos .docx, leitura de dados externos (planilhas ou sistemas internos) e geração automatizada de documentos formatados de acordo com modelos pré-definidos.

Funcionalidades Principais

- Preenchimento automático de modelos .docx com placeholders.
- Interface gráfica simples e funcional desenvolvida em Tkinter.
- Validação e substituição de dados de forma consistente, mesmo em modelos complexos.
- Geração de arquivos de saída em diretórios definidos pelo usuário.

## Estrutura do Projeto
```
relsys/
│
├── core/
│   ├── document.py         # Funções de leitura e preenchimento de modelos
│   ├── config.py           # Placeholders e configurações de documento
│   ├── utils.py            # Funções auxiliares
│   ├── generator.py        # Gerador de senhas
│   ├── state.py            # Variáveis de estado
│   └── ui.py               # Arquivo Principal
│
├── templates/
│   └── welcome-model.docx  # Exemplo de modelo base
│
├── output/
│   └── ...                 # Documentos gerados
│
├── .env                    # Configurações (senhas padrão, caminhos)
├── requirements.txt        # Dependências do projeto
└── README.md
```
## Requisitos
```
Python 3.10+
```
### Bibliotecas: 
- python-docx
- tkinter (incluso no Python)

Caso não possuir as bibliotecas, instale com:
```
pip install python-docx
pip install tk
```
## Configuração do Ambiente

Clone o repositório:
```
git clone https://github.com/it-workon/relsys.git
cd relsys
```
## Execução

Para iniciar o sistema:
```
python ui.py
```
- A interface gráfica será exibida, permitindo selecionar o modelo, inserir dados e gerar o documento final.

## Boas Práticas

- Mantenha modelos e saídas organizados por pasta e tipo de documento.
- Versione apenas o código-fonte e modelos genéricos.

## Licença

Este projeto é de uso interno e restrito à empresa.
A redistribuição ou modificação sem autorização é proibida.