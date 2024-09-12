create database if not exists OP_Database;

create table if not exists
    Song (
        ID varchar (50) not null primary key,
        Name varchar (255) not null,
        NumberStream int not null,
        NbOccurence int
    );
create table
    Session (
        ID varchar(50) not null primary key,
        Date date not null,
        NbShooters int,
        ThemeBlindTest varchar (255),
        NbDropCoupe int
    );
create table
    Song_Session (
        ID_Song varchar (50) not null,
        ID_Session varchar (50) not null,
        Found bit not null,
        IsOral bit not null,
        primary key (ID_Song, ID_Session)
    );
create table
    Equipe (
        ID varchar (50) not null primary key,
        Name varchar (50) not null
    );
create table
    Participant (
        ID varchar (50) not null primary key,
        LastName varchar (50) not null,
        FirstName varchar (50) not null,
        Description varchar (255)
    );
create table
    Artist (
        ID varchar (50) not null primary key,
        Name varchar (50) not null
    );
create table
    Session_Participant (
        ID_Session varchar (255) not null,
        ID_Participant varchar (255) not null,
        primary key (ID_Session, ID_Participant)
    );
create table
    Session_Equipe (
        ID_Session varchar (50) not null,
        ID_Equipe varchar (50) not null,
        Position int not null,
        Score int not null,
        primary key (ID_Session, ID_Equipe)
    );
create table
    Song_Artist (
        ID_Song varchar (50) not null,
        ID_Artist varchar (50) not null,
        primary key (ID_Song, ID_Artist)
    )