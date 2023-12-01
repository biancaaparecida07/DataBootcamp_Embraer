# Banco de Dados MySQL - Resumo
Resumo baseado nas aulas do Data Bootcamp - Embraer Social Tech Careers - Gama Academy

## Comandos mais utilizados
- **status;**
Exibe todas as informações da conexão bem como o database em uso no momento e o usuário logado.

- **\\! cls;**
Limpa a tela do MySQL Command Line Client

- **show databases;**
Exibe os databases existentes.

- **create database nomeDoDatabase**
Cria uma base de dados. 

- **use nomeDoDatabase;**
Permite o acesso e uso da base de dados mencionada no comando.

- **show tables**
Exibe as tabelas existentes na base de dados em uso.

- **desc nomeDaTabela**
Exibe a estrutura da tabela mencionada. Nota: para conseguir acessar a tabela é preciso estar com o banco a qual ela pertence em uso. Também pode ser usado describe ao invés de desc. 

## Criação da Base de Dados
```
create database ecommerce
```
## Acesso à Base de Dados
```
use ecommerce
```
## Criação de Tabelas
``` sql
create table cliente(
    id integer not null auto_increment primary key,
    nome varchar(100) not null,
    email varchar(70) unique,
    senha varchar(20) not null,
    cpf varchar(20) not null unique
);

create table departamento(
    numero integer not null auto_increment primary key,
    nome varchar(30) not null,
    descricao text,
);

create table endereco(
    num_seq integer not null auto_increment primary key,
    tipo varchar(5) not null,
    logradouro varchar(50) unique,
    numero integer,
    complemento varchar(20),
    bairro varchar(30),
    cidade varchar(50),
    estado varchar(2),
    cep varchar(10),
    id_cliente integer not null,
    constraint endereco_cliente foreign key (id_cliente) references cliente(id)
);

create table pedido(
    numero integer not null auto_increment primary key,
    status varchar(1) not null,
    data_pedido date,
    valor_bruto double,
    desconto double,
    valor_liq double,
    id_cliente integer not null,
    constraint cliente_pedido foreign key (id_cliente) references cliente(id)
);

create table produto(
    codigo integer not null auto_increment primary key,
    nome varchar(50) not null, 
    descricao text,
    preco double,
    estoque integer,
    link_foto varchar(255),
    numero_dpto integer not null,
    constraint produto_dpto foreign key (numero_dpto) references departamento(numero)
);

create table item_pedido(
    seq integer not null auto_increment primary key,
    quantidade integer,
    preco_unit double,
    preco_final double,
    codigo_produto integer not null,
    constraint item_produto foreign key (codigo_produto) references produto(codigo),
    numero_pedido integer not null,
    constraint item_pedido foreign key (numero_pedido) references pedido(numero)
);
```

**not null** - Campo não pode ser vazio  
**auto_increment** - Campo que será incrementado automaticamente.
**primary key** - Campo classificado como chave primária. O valor deste campo não se repete nos registros da tabela e, então, serve de identificador único para cada registro.   
**unique** - Campo deve ser único diante de todos os registros. Funciona como chave alternativa podendo buscar um registro por este campo também.   
**text** - tipo de dado que aceita até 16k caracteres  
**constraint** - Cria uma restrição que precisa ser nomeada, por exemplo: endereco_cliente.   
**foreign key** - Indica que a restrição é para uma chave estrangeira, ou seja, referenciará campo de uma outra tabela.   
**references** - Neste caso, o (id_cliente) vai referenciar o campo (id) da tabela cliente.   
**default 0** - Para campos numéricos onde, quando não indicado seu valor, o valor padrão é zero. 

## Alterações de Estruturas do Banco de Dados
Estes comandos precisam ser planejados cuidadosamente. Alterar ou apagar tabelas podem influenciar no modelo construído. Uma outra tabela pode referenciar a que seria apagada. Inclusive, se a tabela que seria apagada tiver algum relacionamento, o comando não será executado pela primeira vez como alerta. 
``` sql
alter table cliente add column rg varchar(10) not null after senha;

drop table cliente;

drop database ecommercev2;

alter table cliente modify column rg varchar(15);

alter table cliente change column rg registro_geral varchar(10) not null;

```
**alter table** - Comando inicial para alterar uma tabela.   
**add column** - Em conjunto com o alter table, adiciona uma nova coluna na tabela.   
**modify column** - Em conjunto com o alter table, modifica o tipo de dado da coluna já existente da tabela.   
**change column** - Em conjunto com o alter table, altera o nome de uma coluna já existente da tabela bem como seu tipo de dado.  
**drop column** - Em conjunto com o alter table, apaga columa da tabela.   
**drop table** - Apaga determinada tabela.  
**drop database** - Apaga uma base de dados. 

### Estudo de Caso
Situação: Criada a tabela de Produto com o campo de código apenas como chave primária e not null. Deveria também ter sido criada como auto_increment. 
Criou-se em seguida a tabela item_pedido já com o relacionamento com produto. Então, código da tabela de PRODUTO seria chave estrangeira na tabela de ITEM_PEDIDO. 

Percebido o erro, não foi possível alterar o campo código da tabela produto pois ele mantinha um relacionamento com a tabela de item_pedido. O que fazer: 

``` sql
ALTER TABLE item_pedido DROP FOREIGN KEY fk_pedido_has_produto_produto1;
ALTER TABLE produto MODIFY codigo INT AUTO_INCREMENT;
ALTER TABLE item_pedido ADD CONSTRAINT fk_pedido_has_produto_produto1 FOREIGN KEY (produto_codigo) REFERENCES produto(codigo);
```

## INSERT - Inserção de dados nas tabelas
CRUD - C - Create
Inserindo dados com a definição dos campos, não importando a ordem. Atentar-se ao nome dos campos que devem ser idênticos aos declarados na tabela. 
``` sql
insert into departamento(codigo, nome, descricao) values (1, 'Tecnologia', 'Produtos para computadores');

```
Atenção à ordem da estrutura nas tabelas. A ordem para inserir os dados na tabela deve ser a mesma ordem de definição dos campos da tabela se os campos não foram definidos no comando. 

O campo de código foi definido como auto-increment, portanto, neste caso ele pode ser declarado como vazio e entende-se que o valor não se aplica  e p banco de dados decidirá. 

``` sql
insert into departamento values (null, 'Eletrônicos', 'Tudo o que não é computador e liga na tomada');
```
Também há a possibilidade de inserir mais de um registro em apenas um comando de insert da seguinte forma:

``` sql
insert into departamento values 
    (null, 'Games', 'Para jogadores Hard Level'),
    (null, 'Acessorios', 'Cabos e conectores que a gente sempre perde'),
    (null, 'Alimentação', 'Porque dev não vive só de dogão');
```

Ao inserir um registro na tabela produto, o último campo é o campo de departamento_id. Então, neste caso, teríamos um vínculo entre tabelas. Portanto, é preciso conferir que o valor inserido como departamento_id na tabela produto seja um id existente na tabela de departamentos. Se não houver um departamento com id = 10 cadastrado, a inserção não terá sucesso. 

``` sql
insert into produto values
	(null, 'Computador','Computador cheio de led top de linha', 500.0, 3, './imagens/computador.png', 10);
```
## SELECT - Busca e exibe resultados
CRUD - R - Read

Seleciona todos os dados da tabela departamento.
``` sql
select * from departamento;
```

## UPDATE - Atualiza registro
CRUD - U - Update
Atualiza determinado campo da tabela que cumpra o critério de identificação do campo. 

``` sql
update departamento set nome = 'Informática e Tecnologia' where codigo = 1;
```

## DELETE - Deleta registro
CRUD - D - Delete
Deleta um determinado arquivo da tabela especificada que cumpra o critério de identificação. 
``` sql
delete from departamento where codigo = 1;
```

Tanto no UPDATE quanto no DELETE, é importantíssimo o critério para que não haja maiores intercorrências como atualizar campos indevidos ou até mesmo deletar campos. 

## Consultas Simples
É possível selecionar apenas as tabelas que se deseja exibir. 
``` sql
select id, nome, email, senha, cpf from cliente;
select * from cliente;
```
Recuperando todos os produtos:
``` sql
select * from produto;
```

Buscando produtos por alguma palavra-chave:
``` sql
select * from produto where nome like "%USB%";
```

Recuperando todos os pedidos:
``` sql
select * from pedido;
```

Recuperando o total faturado geral (sem critério algum):
``` sql
select sum(valor_final) from pedido;
```

Buscando quantos clientes ao total:
``` sql
select count(id) from cliente;
```

A mesma consulta acima, mudando o titulo da coluna:
``` sql
select count(id) as 'total de clientes' from cliente;
```

Buscando através de um critério:
``` sql
select * from cliente where id = 1;
```

Ordenando clientes pelo nome:
``` sql
select * from cliente order by nome asc;
```

## Agrupamentos - Group by
Recuperando dados da tabela produtos agrupados de forma que o retorno seja quantos produtos tem de cada departamento. 
``` sql
select  departamento_codigo, count(codigo) as quantidade from produto group by departamento_codigo;
```
Recuperando dados da tabela produtos agrupados de forma que o retorno seja qual o valor total de produtos de cada departamento. 
``` sql
select departamento_codigo, sum(preco*estoque) as 'Valor Total' from produto group by departamento_codigo;
```

## Junções
### Junções com 2 tabelas
Junção simples como produto cartesiano: Traz a combinação entre as duas tabelas, como se uma linha de uma tabela se multiplicasse por todas as linhas da outra. 
``` sql
select * from produto inner join departamento;
```

Agora trazemos a restrição como condição para trazer o que realmente foi modelado. Trazendo a linha do produto somente com o departamento no qual faz parte. 
``` sql
select * from produto inner join departamento on produto.departamento_codigo=departamento.codigo;
```

Junção de uma mesma tabela fazendo uma cópia da mesma para cruzamento dos produtos sem que um produto se cruze com ele mesmo. **Nota**: é possível criar alias para tabelas, não apenas para o que vai ser selecionado. 
``` sql
SELECT 
    produtoA.nome as produtoA, 
    produtoB.nome as produtoB 
FROM 
    produto AS produtoA
INNER JOIN 
    produto AS produtoB
    ON produtoA.nome <> produtoB.nome;
```

Recuperando todos os clientes e seus respectivos endereços
``` sql
select * from cliente inner join endereco on cliente.id=endereco.cliente_id;
```

### Junções com 3 ou mais tabelas
1. Passo 1: encontrando os itens de cada pedido
1. Passo 2: fazer junção com produto
1. Passo 3: fazer a junção com cliente.
``` sql
select * from 
pedido inner join item_pedido 
	on pedido.numero=item_pedido.num_sequencial
    inner join produto on item_pedido.produto_codigo=produto.codigo
    inner join cliente on cliente.id=cliente_id;
```
Mesma consulta anterior, porém buscando todos os dados do pedido + nome do cliente + nome do produto
``` sql
select pedido.*, cliente.nome, produto.nome from 
pedido inner join item_pedido 
	on pedido.numero=item_pedido.num_sequencial
    inner join produto on item_pedido.produto_codigo=produto.codigo
    inner join cliente on cliente.id=cliente_id;
```


### Junções Externas
**Nota**: Fixar e preservar a tabela que deve ser exibidos todos os registros. 

Buscando todos os produtos a partir dos departamentos
``` sql
select * from departamento inner join produto on departamento.codigo=produto.departamento_codigo;
``` 
Inserindo um novo departamento
``` sql
insert into departamento values (null, 'Móveis', 'Móveis para escritório e gamers de todas as idades');
```
``` sql
select * from departamento;
```
Utilizar uma junção externa (outer join): retorna os registros que contemplam o filtro ON e também os que ficam de fora. No nosso caso, se buscassemos, não traria o departamento de Móveis por nao ter nenhum produto vinculado a ele. Mas agora, ele vai trazer e dizer que não há nada. 
Tabela dominante: departamento. À esquerda. Por isso colocar o left
``` sql
select * from departamento left outer join produto on departamento.codigo=produto.departamento_codigo;
```
Agora usando right outer 
```sql
select * from produto right outer join departamento on departamento.codigo=produto.departamento_codigo;
```


### Subconsultas - Subqueries
Critério de seleção (where) depende da resolução de outra consulta. 

Buscar todos os pedidos que possuem o produto mais caro do ecommerce
* Como saber qual o produto mais caro? Opções.
```sql
select * from produto order by preco desc limit 1;
select * from produto having max(preco);
select * from produto where preco = (select max(preco) from produto);
```
* Mas na verdade, preciso dos pedidos que contem este produto.
``` sql
select * from pedido inner join item_pedido 
	on item_pedido.pedido_numero = pedido.numero 
    where item_pedido.produto_codigo=(select codigo from produto having max(preco));
```

* Caso eu queira os clientes que compraram este produto mais caro basta fazer na consulta externa uma junção com cliente e recuperar seu nome.
```sql
select * from cliente inner join pedido on cliente.id=pedido.cliente_id
inner join item_pedido on item_pedido.pedido_numero=pedido_numero
where item_pedido.produto_codigo=(select codigo from produto having max(preco));
```