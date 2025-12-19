# RelSyS – Sistema de Automação de Rotinas de TI

## Visão Geral

O **RelSyS** é uma aplicação desktop desenvolvida em Python para automatizar e padronizar rotinas internas do setor de TI, reduzindo tarefas manuais, erros operacionais e retrabalho.

O sistema centraliza funcionalidades como:

- Geração de relatórios e documentos
- Checklists operacionais
- Planilhamento de máquinas
- Registro de desligamento de colaboradores

O projeto evoluiu para uma **arquitetura em camadas (UI, Service e Infra)**, aliada a um **Design System próprio**, garantindo consistência visual, manutenibilidade e facilidade de evolução.

---

## Funcionalidades Principais

- Geração automatizada de relatórios
- Checklist de preparação de máquinas
- Registro de máquinas em planilhas corporativas
- Checklist e registro de desligamento de colaboradores
- Interface gráfica desktop com navegação por abas
- Integração com planilhas Excel (.xlsx)
- Padronização visual via Design System

---

## Arquitetura do Projeto

O projeto segue uma separação clara de responsabilidades:

- **UI**: Camada de interface gráfica (Tkinter / ttkbootstrap)
- **Services**: Regras de negócio e orquestração
- **Infra**: Acesso a arquivos, planilhas e recursos externos
- **Design**: Design System (cores, tipografia, espaçamentos e componentes)

```
relsys/
│
├── core/
│ ├── main.py # Ponto de entrada da aplicação
│
├── ui/
│ ├── document_ui.py
│ ├── checklist_ui.py
│ ├── plan_ui.py
│ └── termination_ui.py
│
├── services/
│ ├── document_service.py
│ ├── plan_service.py
│ └── termination_service.py
│
├── infra/
│ ├── document_repository.py
│ ├── plan_repository.py
│ └── termination_repository.py
│
├── design/
│ ├── design.py # Tokens de design
│ ├── apply.py # Aplicação global do tema
│ ├── components.py # Estilos e componentes reutilizáveis
│ ├── colors.py
│ ├── typography.py
│ └── padding.py
│
├── requirements.txt
└── README.md
```

---

## Design System

O Design System centraliza toda a identidade visual do projeto:

- **Cores** (`Design.Colors`)
- **Tipografia** (`Design.Typography`)
- **Espaçamentos** (`Design.Padding`)
- **Componentes reutilizáveis** (`components.py`)

Isso permite alterações globais de estilo sem impactar a lógica das telas.

---

## Requisitos

- Python **3.10+**
- Sistema operacional com suporte a interface gráfica

### Bibliotecas principais

- `tkinter` (incluso no Python)
- `ttkbootstrap`
- `openpyxl`

Instalação das dependências:

```bash
pip install -r requirements.txt
```

## Execução

Para iniciar o sistema:

```
python core/main.py
```

A aplicação será aberta com interface gráfica e navegação por abas.

## Boas Práticas do Projeto

- UI sem lógica de negócio

- Services sem dependência de interface

- Infra responsável apenas por I/O

- Estilo visual nunca definido diretamente na UI

- Componentes reutilizáveis centralizados no Design System

## Licença

**Projeto de uso interno e restrito.**
**Redistribuição ou modificação sem autorização não é permitida.**