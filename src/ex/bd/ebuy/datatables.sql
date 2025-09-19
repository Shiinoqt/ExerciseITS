create table categoria (
    nome stringa primary key,
    super stringa 
)

alter table categoria add foreign key (super) references categoria(nome);

