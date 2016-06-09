create database teste;

use teste;

create table Aluno(
ID int primary key auto_increment,
Nome varchar(30) not null,
Dt_Nasc date not null,
RG numeric(10) not null,
Endereco varchar(60) not null,
Obs varchar(60)
);

insert into Aluno(Nome, Dt_Nasc, RG, Endereco, Obs) 
values ('Maria', '1990-10-21', 44777331, 'Rua dos Passaros, 10', 'Aluna precisa marcar consulta com dentista');



