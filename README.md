# RelSys – Sistema de Emissão de Relatórios e Documentos
## Visão Geral

O RelSys é uma aplicação voltada à automação da emissão de relatórios e documentos corporativos.
Seu objetivo é eliminar tarefas manuais repetitivas, reduzir erros e padronizar a geração de documentos internos, como comunicados, relatórios e materiais de boas-vindas para novos colaboradores.

Desenvolvido em Python, o RelSys integra manipulação de arquivos .docx, leitura de dados externos (planilhas ou sistemas internos) e geração automatizada de documentos formatados de acordo com modelos pré-definidos.

Funcionalidades Principais

- Preenchimento automático de modelos .docx com placeholders.
- Interface gráfica simples e funcional desenvolvida em Tkinter.
- Suporte a configuração via arquivo .env (senhas padrão, diretórios, variáveis de ambiente).
- Validação e substituição de dados de forma consistente, mesmo em modelos complexos.
- Geração de arquivos de saída em diretórios definidos pelo usuário.

## Estrutura do Projeto
```
relsys/
│
├── main.py                 # Aplicação principal (interface Tkinter)
├── core/
│   ├── document.py         # Funções de leitura e preenchimento de modelos
│   ├── config.py           # Leitura de variáveis de ambiente (.env)
│   └── utils.py            # Funções auxiliares
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
Requisitos

Python 3.10+

Bibliotecas listadas em requirements.txt:

python-docx
python-dotenv
tkinter (incluso no Python)

Configuração do Ambiente

Clone o repositório:

git clone https://github.com/empresa/relsys.git
cd relsys


Crie um ambiente virtual e instale as dependências:
```
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate   # Linux/Mac
```
```
pip install -r requirements.txt
```

Crie um arquivo .env com as configurações básicas:
```
DEFAULT_PASSWORD_WINDOWS=NoS@work2025
DEFAULT_PASSWORD_EMAIL=Mudar@2025
TEMPLATE_PATH=templates/welcome-model.docx
OUTPUT_DIR=output
```
Execução

Para iniciar o sistema:
```
python main.py
```

A interface gráfica será exibida, permitindo selecionar o modelo, inserir dados e gerar o documento final.

Boas Práticas

Utilize placeholders padronizados no formato {{CAMPO}} dentro dos modelos .docx.

Evite armazenar dados sensíveis no código; use o .env.

Mantenha modelos e saídas organizados por pasta e tipo de documento.

Versione apenas o código-fonte e modelos genéricos.

Licença

Este projeto é de uso interno e restrito à empresa.
A redistribuição ou modificação sem autorização é proibida.