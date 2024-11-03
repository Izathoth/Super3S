from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Boolean, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# Base para as tabelas
Base = declarative_base()

# Definindo a tabela Cliente
class Cliente(Base):
    __tablename__ = 'cliente'
    id_cliente = Column(Integer, primary_key=True)  # Identificador único do cliente
    nome = Column(String, nullable=False)  # Nome do cliente
    cpf = Column(String, unique=True, nullable=False)  # CPF único do cliente
    endereco = Column(String)  # Endereço do cliente
    email = Column(String)  # E-mail de contato
    telefone = Column(String)  # Telefone para contato

# Definindo a tabela Produto
class Produto(Base):
    __tablename__ = 'produto'
    id_produto = Column(Integer, primary_key=True)  # Identificador único do produto
    nome = Column(String, nullable=False)  # Nome do produto
    tipo = Column(String)  # Tipo ou categoria do produto
    unidade = Column(String)  # Unidade de medida
    descricao = Column(String)  # Descrição detalhada
    codigo_barra = Column(String, unique=True)  # Código de barras único
    quantidade_estoque = Column(Integer, default=0)  # Quantidade disponível
    preco_atual = Column(Float)  # Preço atual
    preco_anterior = Column(Float)  # Preço anterior

# Definindo a tabela Venda
class Venda(Base):
    __tablename__ = 'venda'
    id_venda = Column(Integer, primary_key=True)  # Identificador da venda
    id_cliente = Column(Integer, ForeignKey('cliente.id_cliente'))  # Cliente que comprou
    data_venda = Column(DateTime, default=datetime.datetime.utcnow)  # Data da venda
    valor_total = Column(Float)  # Valor total
    imposto_total = Column(Float)  # Total de impostos
    nota_fiscal = Column(Boolean)  # Nota fiscal emitida ou não

# Definindo a tabela Pagamento
class Pagamento(Base):
    __tablename__ = 'pagamento'
    id_pagamento = Column(Integer, primary_key=True)  # Identificador do pagamento
    id_venda = Column(Integer, ForeignKey('venda.id_venda'))  # Venda associada
    forma_pagamento = Column(Enum('dinheiro', 'pix', 'cartão_credito', 'cartão_débito'))  # Forma de pagamento

# Definindo a tabela Estoque
class Estoque(Base):
    __tablename__ = 'estoque'
    id_estoque = Column(Integer, primary_key=True)  # Identificador do estoque
    id_produto = Column(Integer, ForeignKey('produto.id_produto'))  # Produto no estoque
    quantidade = Column(Integer)  # Quantidade disponível

# Definindo a tabela Fornecedor
class Fornecedor(Base):
    __tablename__ = 'fornecedor'
    id_fornecedor = Column(Integer, primary_key=True)  # Identificador do fornecedor
    nome = Column(String, nullable=False)  # Nome do fornecedor
    contato = Column(String)  # Contato do fornecedor

# Definindo a tabela Compra
class Compra(Base):
    __tablename__ = 'compra'
    id_compra = Column(Integer, primary_key=True)  # Identificador da compra
    id_fornecedor = Column(Integer, ForeignKey('fornecedor.id_fornecedor'))  # Fornecedor associado
    data_compra = Column(DateTime, default=datetime.datetime.utcnow)  # Data da compra
    valor_total = Column(Float)  # Valor total

# Definindo a tabela Funcionario
class Funcionario(Base):
    __tablename__ = 'funcionario'
    id_funcionario = Column(Integer, primary_key=True)  # Identificador do funcionário
    nome = Column(String, nullable=False)  # Nome do funcionário
    categoria = Column(String)  # Cargo ou categoria do funcionário
    salario = Column(Float)  # Salário

# Conectando ao banco de dados
engine = create_engine('sqlite:///supermercado.db')  # Substituir com outro banco se necessário
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Função para adicionar um cliente
def adicionar_cliente(nome, cpf, endereco, email, telefone):
    novo_cliente = Cliente(nome=nome, cpf=cpf, endereco=endereco, email=email, telefone=telefone)
    session.add(novo_cliente)
    session.commit()
    print(f"Cliente {nome} adicionado com sucesso.")