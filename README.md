<h1> Projeto 2 - Protocolo de Interconexão de Redes de Computadores</h1>
<h2> Descrição </h2>

> * Projeto desenvolvido como atividade referente a matéria Protocolo de Interconexão de Redes de Computadores do curso Tecnologia em Sistemas para internet - IFPB Guarabira.
>  O projeto consiste na estruturação de uma página Web usando a biblioteca Flask do python, na qual coleta informações do usuário e as retorna em sua página principal.
> * As informações cadastradas são arquivadas em formato JSON administrado pelo flask.

<h3> Pré - Requisitos </h3>

> * Ter conexão com a internet.

<h3>  Aplicação </h3>

> Método de captação de dados para o banco de dados:
> 
> * O arquivo json é aberto no método de leitura, carregado e salvo à uma variavel 
> * usando ".json" da biblioteca json.

> Funcionalidades da página:

> * Mostrar a lista de contatos.
> * Cadrastar novos contatos de e-mail.
>
> Bibliotecas usadas no servidor:
>
> * Flask
> * Json

<h3> Execucão </h3>

> A execução da página inicializa com o servidor python, onde é disponibilizado um link de acesso à página.
> Imaginando que a página estivesse no ar, o cliente teria apenas que colocar a URL de acesso, a partir daí ele teria acesso as funcionalidades da página como cadastro e lista de contatos.

<h2> Estruturação do código </h2>

<h3> Arquivo Python </h3>

> * Ele começa importando as bibliotecas Flask e Json no python.
> * Logo em seguida é criada a função que ler o banco de dados e retorna a página principal com os dados dos contatos cadastrados.
> * Caso a rota de cadastro for solicitada, é executada uma função que ler o banco de dados, salva seu " .load " em uma variável, processa os dados que forem colocados no campo " nome " e " email ", em seguida todos são salvos em uma variável do tipo json, e adicionado onde o carregamento do banco de dados foi salvo.

<h3> Arquivos HTML </h3>
<h4> HTML contato <h4>

> * No geral é um código bem simples, ele começa criando conexões entre os arquivos css
> * a página tem um título com o nome " contatos " e um botão em seguida para adicionar novos contatos, nesse botão tem o redirecionamento para a página de cadastro.
> * em seguida é criado um container com os dados dos clientes que são captados da variável " contatos " do arquivos python onde estão os dados no formato json.

<h4> HTML cadastrar </h4>

> * Ela começa linkando aos arquivos do css
> * a página tem um botão nomeado de " home ", em que redireciona para a página principal
> * em seguida é estruturado o formulário de cadastro, que solicita o nome e o email do cliente e exibe um botão que envia os dados para o banco de dados. 
