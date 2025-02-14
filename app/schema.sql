drop table if exists user;
drop table if exists post;

create table user (
    id integer primary key AUTOINCREMENT,
    username text unique not NULL,
    password text not NULL
);

create table post (
    id integer primary key AUTOINCREMENT,
    author_id integer not NULL,
    created timestamp not NULL default CURRENT_TIMESTAMP,
    title text not NULL,
    body text not NULL,
    FOREIGN KEY (author_id) references user (id)
);
