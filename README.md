Este é um modelo básico de um sistema físico que desenvolvi como parte de um trabalho acadêmico. Uma colega de um grupo de Networking no qual participo compartilhou um modelo conceitual mais complexo, enquanto o meu representa apenas uma implementação física, ou seja, um código que precisa de ajustes, correções e melhorias. O enunciado do trabalho dela era o seguinte:

**Criação de um modelo conceitual, lógico e físico com base nas regras de negócios abaixo:**

No contexto de um supermercado chamado Super3S, considere as seguintes regras:

1. O processo de venda é realizado diretamente pelo cliente, que escolhe os produtos e os coloca no carrinho de compras.
2. Ao finalizar a escolha dos produtos, o cliente dirige-se ao caixa, onde o funcionário registra todos os itens. Ao fim do processo, será solicitada a forma de pagamento, que pode ser: dinheiro, PIX, cartão de crédito ou débito. Não é permitido o parcelamento da compra, nem o uso de mais de um tipo de pagamento.
3. A cada venda realizada, as quantidades dos produtos vendidos são automaticamente descontadas do estoque, sem segmentação por lote ou fornecedor.
4. Após várias vendas, é necessário registrar o valor mínimo de cada produto no estoque, para que seja possível filtrar aqueles que precisarão ser reabastecidos.
5. As compras de novas mercadorias serão feitas diretamente com um fornecedor. É possível ter múltiplos fornecedores para o mesmo produto, mas cada compra será feita apenas com um fornecedor por vez.
   5.1. Cada compra gerará uma conta a pagar, que poderá ser quitada em parcelas, utilizando os meios de pagamento: cartão de crédito, cheque ou boleto.
6. Os produtos devem ter suas principais características armazenadas, como: nome, tipo, unidade, descrição, código de barras e quantidade em estoque.
   6.1. Em novembro, ocorre a Black Friday, assim como em outras datas festivas, e as variações de preço (preço atual e anterior) devem ser armazenadas junto ao valor atual do produto.
7. As vendas podem ocorrer presencialmente ou por delivery, registrando informações do cliente (nome, CPF, endereço, e-mail e telefone), os impostos por produto (ICMS, alíquota), o valor total da compra e os impostos pagos.
8. Durante a venda, o cliente pode optar por emitir ou não a nota fiscal eletrônica.
9. Quando uma venda é cancelada, ela não é removida do banco de dados, mas marcada como "cancelada" e a quantidade dos produtos envolvidos é restituída ao estoque.
10. Cada caixa deve ter uma meta mensal; ao atingi-la, recebe uma bonificação de 10% do seu salário.
11. Os salários dos funcionários serão armazenados conforme a categoria, permitindo o gerenciamento da folha de pagamento e a geração das contas a pagar do mês.

Esse modelo busca atender de forma clara e objetiva as necessidades descritas no cenário de negócios do supermercado Super3S.
