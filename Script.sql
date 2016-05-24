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
insert into Aluno(Nome, Dt_Nasc, RG, Endereco) 
values ('João', '1991-11-11', 56674884, 'Rua das Árvores, 20');
insert into Aluno(Nome, Dt_Nasc, RG, Endereco) 
values ('José', '1989-05-14', 99087777, 'Rua Flecha, 160');
insert into Aluno(Nome, Dt_Nasc, RG, Endereco) 
values ('Marina', '1990-08-22', 909887666, 'Rua Canário, 14');
insert into Aluno(Nome, Dt_Nasc, RG, Endereco) 
values ('Rafael', '1991-03-10', 3334433, 'Rua Macaé, 204');
insert into Aluno(Nome, Dt_Nasc, RG, Endereco) 
values ('Amarilda', '1991-07-01', 9899988, 'Rua Rio, 111');
insert into Aluno(Nome, Dt_Nasc, RG, Endereco) 
values ('Clarissa', '1990-06-16', 11222121, 'Rua Vinho, 12');


