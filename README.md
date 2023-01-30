
# VM provisionada com Vagrant e Python

Script Vagrant que cria e provisiona uma VM( CentOS 7), com 1 CPUs, 2 GB de memória RAM e 50gb de HD, com o nome de “teste-zeppelin”. O acesso(ssh) a VM é realizado por meio de chave privada.

## Lab 1 

Programa em python que realiza a instalação do Java(JDK) e do Apache Zeppelin na VM (Centos7) e inicializa o webserver do Zeppelin na porta 8888, bem com a criação dos usuarios e suas permissões de acesso a plataforma.

### Apache Zeppelin

![Logo](https://zeppelin.apache.org/assets/themes/zeppelin/img/zeppelin_classic_logo.png)



O Apache Zeppelin é uma interface web-based que permite análise de dados interativa. 
Em grandes empresas é comum a utilização de diversos softwares que usam diferentes tipos de bancos de dados, sendo um desafio analisar esses dados em uma única ferramenta.

O Apache Zeppelin oferece uma camada que interpreta várias sintaxes como SQL, Scala, Cassandra entre outros, permitindo criar visualização de dados rapidamente através dos resultados obtidos pelos interpretadores, compartilhá-los e estudá-los de forma colaborativa. 
Se você já usou o Kibana para visualização de dados para o ElasticSearch ou bancos NoSQL, o Zeppelin vai muito além disso.


## Lab 2

Programa em python que realiza a instalação do Python 3.6, do Apache Superset e inializa o seu webserver na VM(Centos 7) criada no lab 1.

Adicionar instalação do MySQL (ou banco de dados semelhante) e do Redis e integrar com o Superset.

### Apache Superset

![Logo](https://upload.wikimedia.org/wikipedia/commons/0/0e/Superset_logo.svg)

O Apache Superset é um aplicativo cloud-native software open source para exploração e visualização de dados capaz de lidar com dados em escala de petabyte. O aplicativo começou como um projeto hack-a-thon de Maxime Beauchemin enquanto trabalhava no Airbnb e entrou no programa Apache Incubator em 2017.

## Lab3

Criar uma aplicação que fique exibindo o valor de uma variável de ambiente do sistema operacional de 20 em 20 segundos, o nome da variável deve ser "TWORPTEST" e o valor desta variável deve ser "true100%".
Criar um container usando docker ou outro orquestrador de containers similar.
Opcional: fazer o upload da imagem construída para um container registry de preferência. 
Observação: o valor da variável deve ser exibido no log do container

Opcional: Instanciar um cluster kubernetes local usando Minikube, K3D ou similar para criação e testes dos manifestos.

Criar manifestos kubernetes incluindo os tipos deployment, service, secret. O deployment deve rodar a imagem docker construida nas etapas anteriores e na secret deve ser adicionado a variável esperada pela aplicação e passada para o container como variável de ambiente.

Bônus (opcional): Fazer um script bash que percorre os namespaces e coleta a secret de cada deployment para comparar se o valor da secret do deployment está sendo exibida no log do container que está rodando a aplicação. Se o valor da secret estiver sendo exibida retornar uma mensagem informando que o container tem um problema de segurança.


## Referência

 - [Vagrant by HashiCorp](https://www.vagrantup.com/)
 - [Oracle JDK](https://www.oracle.com/in/java/technologies/downloads/)
 - [Apache Zeppelin](https://zeppelin.apache.org/)

