# granGestor-desktop-python

Sistema desktop de gestão para animais, fornecedores, clientes, vendas e estoque, com login, balanço automático e emissão de DANFE, inspirado no UX/UI do granGestor.

## Tecnologias
- Python 3.9+
- PySide6 (Qt for Python)
- SQLAlchemy
- SQLite
- Jinja2, ReportLab (emissão de DANFE)

## Como rodar
```sh
pip install -r requirements.txt
python main.py
```

## Funcionalidades iniciais
- Tela de login segura
- Cadastro e administração de animais, fornecedores, clientes, vendas, entradas de estoque (vivo/morto, com possibilidade de associar a encomendas)
- Administração de animais por espécie
- Relatórios de vendas e estoque
- Emissão de DANFE (PDF)
- Interface fácil de personalizar para seguir o design do granGestor

## Estrutura básica de diretórios
```
granGestor-desktop-python/
├─ main.py
├─ db/
│   └─ models.py
│   └─ database.py
├─ ui/
│   └─ main_window.py
│   └─ login.py
├─ controllers/
│   └─ login.py
├─ requirements.txt
└─ README.md
```