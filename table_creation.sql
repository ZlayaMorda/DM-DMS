create table if not exists users 
(
    id_user serial primary key,
    name varchar(128),
    last_name varchar (128),
    email varchar (256),
    password varchar (64),
    image_s3_path varchar (256),
    role varchar (10),
    is_blocked bool default false,
    unique(id_user, email, password)
);

create table if not exists logs
(
    date_time timestamp,
    action varchar(128),
	id_user integer,
    foreign key (id_user) references users (id_user) on delete restrict,
    primary key(date_time, action, id_user)
);

create table if not exists chats
(
    id_chat serial primary key,
    name varchar(128),
    admin integer,
    unique(id_chat)
);

create table if not exists chats_users
(
    id_chat int,
    id_user int,
    foreign key (id_user) references users (id_user) on delete restrict,
    foreign key (id_chat) references chats (id_chat) on delete restrict,
    primary key(id_chat, id_user)
);

create table if not exists messages
(
    id_chat int,
    id_user int,
    content varchar(512),
    date_time timestamp,
    foreign key (id_user) references users (id_user) on delete restrict,
    foreign key (id_chat) references chats (id_chat) on delete restrict,
    primary key(id_chat, id_user, content, date_time)
);

create table if not exists pages
(
    id_page serial primary key,
    name varchar(128),
    description varchar(512),
    id_owner int,
    unblock_date timestamp,
    foreign key (id_owner) references users (id_user) on delete cascade,
    unique(id_page)
);

create table if not exists followers
(
    id_page int,
    id_user int,
    primary key (id_page, id_user),
    foreign key (id_user) references users (id_user) on delete cascade,
    foreign key (id_page) references pages (id_page) on delete cascade    
);

create table if not exists tags
(
    name varchar(128) primary key,
    unique(name)
);

create table if not exists pages_tags
(
    id_page int,
    name varchar(128),
    foreign key (id_page) references pages (id_page) on delete cascade,
    foreign key (name) references tags (name) on delete cascade,
    primary key(id_page, name)    
);

create table if not exists posts
(
    id_post serial primary key,
    id_page int,
    id_user int,
    content varchar(1024),
    reply_post_id int,
    created_at timestamp,
    updated_at timestamp,
    unique(id_post),
    foreign key (id_page) references pages (id_page) on delete cascade,
    foreign key (id_user) references users (id_user) on delete restrict,
    foreign key (reply_post_id) references posts (id_post) on delete cascade 
);

create table if not exists reactions
(
    id_post int,
    id_user int,
    likes bool default false,
    dislikes bool default false,
    foreign key (id_user) references users (id_user) on delete restrict,
    foreign key (id_post) references posts (id_post) on delete cascade,
    primary key(id_post, id_user)    
);
