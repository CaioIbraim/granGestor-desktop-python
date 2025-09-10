from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum
from sqlalchemy.orm import declarative_base, relationship
import enum
import datetime

Base = declarative_base()

class TipoEntrada(enum.Enum):
    vivo = "vivo"
    morto = "morto"

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    senha = Column(String)

class Especie(Base):
    __tablename__ = "especies"
    id = Column(Integer, primary_key=True)
    nome = Column(String, unique=True)

class Fornecedor(Base):
    __tablename__ = "fornecedores"
    id = Column(Integer, primary_key=True)
    nome = Column(String)

class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True)
    nome = Column(String)

class Animal(Base):
    __tablename__ = "animais"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    especie_id = Column(Integer, ForeignKey("especies.id"))
    especie = relationship("Especie")
    estoque = Column(Integer, default=0)
    fornecedor_id = Column(Integer, ForeignKey("fornecedores.id"))
    fornecedor = relationship("Fornecedor")

class Encomenda(Base):
    __tablename__ = "encomendas"
    id = Column(Integer, primary_key=True)
    descricao = Column(String)
    status = Column(String, default="pendente")

class EntradaEstoque(Base):
    __tablename__ = "entradas_estoque"
    id = Column(Integer, primary_key=True)
    animal_id = Column(Integer, ForeignKey("animais.id"))
    quantidade = Column(Integer)
    tipo = Column(Enum(TipoEntrada))
    data = Column(DateTime, default=datetime.datetime.utcnow)
    encomenda_id = Column(Integer, ForeignKey("encomendas.id"), nullable=True)

class Venda(Base):
    __tablename__ = "vendas"
    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    data = Column(DateTime, default=datetime.datetime.utcnow)
    valor_total = Column(Float)

class ItemVenda(Base):
    __tablename__ = "itens_venda"
    id = Column(Integer, primary_key=True)
    venda_id = Column(Integer, ForeignKey("vendas.id"))
    animal_id = Column(Integer, ForeignKey("animais.id"))
    quantidade = Column(Integer)
    preco_unitario = Column(Float)