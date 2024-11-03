-- Tabela para armazenar informações dos clientes
CREATE TABLE Cliente (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT, -- Identificador único para cada cliente
    nome VARCHAR(255) NOT NULL, -- Nome completo do cliente
    cpf VARCHAR(11) UNIQUE NOT NULL, -- CPF único do cliente
    endereco VARCHAR(255), -- Endereço do cliente
    email VARCHAR(255), -- E-mail para contato
    telefone VARCHAR(15) -- Telefone do cliente
);

-- Tabela para armazenar informações dos produtos no supermercado
CREATE TABLE Produto (
    id_produto INT PRIMARY KEY AUTO_INCREMENT, -- Identificador único do produto
    nome VARCHAR(255) NOT NULL, -- Nome do produto
    tipo VARCHAR(100), -- Categoria do produto (ex: alimento, bebida)
    unidade VARCHAR(50), -- Unidade de medida (ex: kg, unidade)
    descricao TEXT, -- Descrição detalhada do produto
    codigo_barra VARCHAR(13) UNIQUE, -- Código de barras do produto
    quantidade_estoque INT DEFAULT 0, -- Quantidade no estoque
    preco_atual DECIMAL(10, 2), -- Preço atual do produto
    preco_anterior DECIMAL(10, 2) -- Preço anterior, caso haja desconto
);

-- Tabela para registrar as vendas
CREATE TABLE Venda (
    id_venda INT PRIMARY KEY AUTO_INCREMENT, -- Identificador único da venda
    id_cliente INT, -- Cliente que realizou a compra
    data_venda DATETIME DEFAULT CURRENT_TIMESTAMP, -- Data e hora da venda
    valor_total DECIMAL(10, 2), -- Valor total da venda
    imposto_total DECIMAL(10, 2), -- Total dos impostos
    nota_fiscal BOOLEAN, -- Indica se a nota fiscal foi emitida
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente) -- Ligação com Cliente
);

-- Tabela para registrar pagamentos das vendas
CREATE TABLE Pagamento (
    id_pagamento INT PRIMARY KEY AUTO_INCREMENT, -- Identificador do pagamento
    id_venda INT, -- Venda relacionada ao pagamento
    forma_pagamento ENUM('dinheiro', 'pix', 'cartão_credito', 'cartão_débito'), -- Forma de pagamento
    FOREIGN KEY (id_venda) REFERENCES Venda(id_venda) -- Ligação com a Venda
);

-- Tabela para gerenciar o estoque de produtos
CREATE TABLE Estoque (
    id_estoque INT PRIMARY KEY AUTO_INCREMENT, -- Identificador do estoque
    id_produto INT, -- Produto no estoque
    quantidade INT, -- Quantidade do produto disponível
    FOREIGN KEY (id_produto) REFERENCES Produto(id_produto) -- Ligação com Produto
);

-- Tabela para fornecedores
CREATE TABLE Fornecedor (
    id_fornecedor INT PRIMARY KEY AUTO_INCREMENT, -- Identificador do fornecedor
    nome VARCHAR(255) NOT NULL, -- Nome do fornecedor
    contato VARCHAR(255) -- Contato do fornecedor
);

-- Tabela para registrar compras de fornecedores
CREATE TABLE Compra (
    id_compra INT PRIMARY KEY AUTO_INCREMENT, -- Identificador da compra
    id_fornecedor INT, -- Fornecedor relacionado à compra
    data_compra DATETIME DEFAULT CURRENT_TIMESTAMP, -- Data da compra
    valor_total DECIMAL(10, 2), -- Valor total da compra
    FOREIGN KEY (id_fornecedor) REFERENCES Fornecedor(id_fornecedor) -- Ligação com Fornecedor
);

-- Tabela para informações dos funcionários e salários
CREATE TABLE Funcionario (
    id_funcionario INT PRIMARY KEY AUTO_INCREMENT, -- Identificador do funcionário
    nome VARCHAR(255) NOT NULL, -- Nome do funcionário
    categoria VARCHAR(100), -- Cargo ou categoria
    salario DECIMAL(10, 2) -- Salário do funcionário
);