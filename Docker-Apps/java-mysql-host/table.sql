create table users (id bigint not null, first_name varchar(255), last_name varchar(255), user_name varchar(255), primary key (id)) engine=MyISAM;


create table hibernate_sequence (next_val bigint) engine=MyISAM;
insert into hibernate_sequence values ( 1 );

Insert into users values(1,'Mohan','Bhragav','Swadeshi');

Insert into users values(2,'Bhola','Raja','Protector');