from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from controllers.login import autenticar_usuario

class LoginScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Login")
        layout = QVBoxLayout()
        self.label = QLabel("Usuário:")
        self.input_user = QLineEdit()
        self.label2 = QLabel("Senha:")
        self.input_pass = QLineEdit()
        self.input_pass.setEchoMode(QLineEdit.Password)
        self.button = QPushButton("Entrar")
        self.button.clicked.connect(self.login)
        layout.addWidget(self.label)
        layout.addWidget(self.input_user)
        layout.addWidget(self.label2)
        layout.addWidget(self.input_pass)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def login(self):
        user = self.input_user.text()
        pwd = self.input_pass.text()
        if autenticar_usuario(user, pwd):
            QMessageBox.information(self, "Sucesso", "Login bem-sucedido!")
            # Troca de tela pode ser implementada aqui
        else:
            QMessageBox.warning(self, "Erro", "Usuário ou senha inválidos.")