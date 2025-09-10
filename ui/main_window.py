from PySide6.QtWidgets import QMainWindow, QStackedWidget, QWidget, QHBoxLayout, QFrame, QListWidget, QVBoxLayout
from PySide6.QtCore import Qt
from ui.login import LoginScreen
from ui.dashboard import DashboardScreen
from ui.animais import AnimaisScreen
from ui.fornecedores import FornecedoresScreen
from ui.clientes import ClientesScreen
from ui.vendas import VendasScreen
from ui.estoque import EstoqueScreen
from ui.danfe import DanfeScreen
from ui.styles import MATERIAL_STYLE

MENU_ITEMS = [
    "Dashboard",
    "Animais",
    "Fornecedores",
    "Clientes",
    "Vendas",
    "Estoque",
    "DANFE",
    "Sair"
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("granGestor Desktop")
        self.resize(1000, 600)
        self.setStyleSheet(MATERIAL_STYLE)

        # Widgets de navegação
        self.stacked = QStackedWidget()

        # Telas principais
        self.dashboard = DashboardScreen()
        self.animais = AnimaisScreen()
        self.fornecedores = FornecedoresScreen()
        self.clientes = ClientesScreen()
        self.vendas = VendasScreen()
        self.estoque = EstoqueScreen()
        self.danfe = DanfeScreen()
        self.login = LoginScreen(main_window=self)

        self.stacked.addWidget(self.dashboard)      # 0
        self.stacked.addWidget(self.animais)        # 1
        self.stacked.addWidget(self.fornecedores)   # 2
        self.stacked.addWidget(self.clientes)       # 3
        self.stacked.addWidget(self.vendas)         # 4
        self.stacked.addWidget(self.estoque)        # 5
        self.stacked.addWidget(self.danfe)          # 6

        # Menu lateral (Drawer)
        self.menu = QFrame()
        self.menu.setObjectName("SideMenu")
        self.menu.setFixedWidth(180)
        menu_layout = QVBoxLayout()
        self.menu_list = QListWidget()
        self.menu_list.setObjectName("MenuList")
        self.menu_list.addItems(MENU_ITEMS)
        self.menu_list.setCurrentRow(0)
        menu_layout.addWidget(self.menu_list)
        menu_layout.addStretch()
        self.menu.setLayout(menu_layout)

        # Layout Horizontal: Menu + Conteúdo
        layout = QHBoxLayout()
        layout.addWidget(self.menu)
        layout.addWidget(self.stacked, stretch=1)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.menu_list.currentRowChanged.connect(self.on_menu_changed)

    def on_menu_changed(self, idx):
        if idx == 7:  # Sair
            self.ir_para_login()
        else:
            self.stacked.setCurrentIndex(idx)

    def ir_para_home(self):
        self.stacked.setCurrentIndex(0)
        self.menu_list.setCurrentRow(0)

    def ir_para_login(self):
        # Fecha tudo e volta para tela de login
        self.login.input_user.clear()
        self.login.input_pass.clear()
        self.setCentralWidget(self.login)
