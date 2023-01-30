
# VM provisiona com Vagrant e Python

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
## Referência

 - [Vagrant by HashiCorp](https://www.vagrantup.com/)
 - [Oracle JDK](https://www.oracle.com/in/java/technologies/downloads/)
 - [Apache Zeppelin](https://zeppelin.apache.org/)

