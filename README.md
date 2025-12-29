# RelSyS – Sistema de Automação de Rotinas de TI

## Visão Geral

O **RelSyS** é uma aplicação desktop desenvolvida em **Python** para automatizar e padronizar rotinas internas do setor de TI.  
Seu objetivo é reduzir tarefas manuais, minimizar erros operacionais e centralizar processos recorrentes em uma única ferramenta.

O projeto utiliza **arquitetura em camadas** e um **Design System próprio**, garantindo organização, consistência visual e facilidade de manutenção.

---

## Funcionalidades

- Geração automatizada de relatórios e documentos
- Checklist de preparação de máquinas
- Registro de máquinas em planilhas corporativas
- Checklist e registro de desligamento de colaboradores
- Interface gráfica desktop com navegação por abas
- Integração com arquivos Excel (`.xlsx`)
- Design System centralizado para padronização visual

---

## Estrutura de Pastas

A organização do projeto segue uma separação clara de responsabilidades:
```
relsys/
├── core/
│   ├── common/       # Utilitários e helpers compartilhados
│   ├── design/       # Design System (cores, tipografia, padding, componentes)
│   ├── infra/        # Camada de infraestrutura (acesso a arquivos/planilhas)
│   ├── services/     # Regras de negócio
│   ├── ui/           # Interfaces gráficas (Tkinter / ttkbootstrap)
│   └── main.py       # Ponto de entrada da aplicação
├── output/           # Arquivos gerados pelo sistema
├── templates/        # Templates de documentos
├── requirements.txt  # Dependências do projeto
├── LICENSE
└── README.md
```

---

## Arquitetura

O RelSyS utiliza uma **Layered Architecture simples**:

- **UI**  
  Responsável apenas pela interface gráfica e interação com o usuário.

- **Services**  
  Contém a lógica de negócio e orquestração das operações.

- **Infra**  
  Responsável por acesso a arquivos, planilhas e recursos externos.

- **Design**  
  Centraliza todo o estilo visual do sistema (Design System).

Essa separação facilita manutenção, testes e evolução do projeto.

---

## Design System

O Design System garante consistência visual em toda a aplicação e evita estilos espalhados pela UI.

Componentes principais:
- **Colors** – Paleta de cores
- **Typography** – Fontes e pesos
- **Padding** – Espaçamentos padronizados
- **Components** – Estilos reutilizáveis de `ttk` (botões, labels, frames, checkboxes)

Nenhuma tela define estilos diretamente — tudo é reutilizado a partir do Design System.

---

## Requisitos

- Python **3.10 ou superior**
- Sistema operacional com suporte a interface gráfica

### Dependências principais

- `tkinter` (já incluso no Python)
- `ttkbootstrap`
- `openpyxl`

---

## Ambiente Virtual (venv)

Recomenda-se o uso de um ambiente virtual para isolar as dependências do projeto.

### Criar o ambiente virtual

```
python -m venv .venv
```

### Ativar o ambiente virtual

*Linux / macOS:*
```
source .venv/bin/activate
```

*Windows:*
```
.venv\Scripts\activate
```
## Instalar dependências
```
pip install -r requirements.txt
```
## Executando o Projeto

- Com o ambiente virtual ativado:
```
python core/main.py
```

**A aplicação será iniciada com interface gráfica e navegação por abas.**

## Boas Práticas Adotadas

- UI sem lógica de negócio

- Services independentes da interface

- Infra isolada para I/O

- Design System centralizado

- Código organizado e fácil de evoluir

## Licença

**Projeto de uso interno e restrito.**

**Redistribuição ou modificação sem autorização não é permitida.**