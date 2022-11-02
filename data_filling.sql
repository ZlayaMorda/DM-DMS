insert into users(name, last_name, email, password, image_s3_path, role)
values(
    'Taras',
    'Rusakovich',
    't@m.ru',
    '12345678',
    'link',
    'admin'
);

insert into users(name, last_name, email, password, image_s3_path, role)
values(
    'Torres',
    'rus',
    'tar@m.ru',
    '12345678',
    'link',
    'moderatore'
);

insert into users(name, last_name, email, password, image_s3_path, role)
values(
    'T',
    'R',
    'tr@m.ru',
    '12345678',
    'link',
    'user'
);

insert into users(name, last_name, email, password, image_s3_path, role)
values(
    'Tara',
    'Rusa',
    'tara@m.ru',
    '12345678',
    'link',
    'user'
);

insert into users(name, last_name, email, password, image_s3_path, role)
values(
    'Trassa',
    'vich',
    'tv@m.ru',
    '12345678',
    'link',
    'user'
);

insert into chats(name, admin)
values
('management', 1),
('users', 3),
('punks', 4),
('kdjafkjkadjfklajdkjka', 3);


insert into chats_users(id_chat, id_user)
values
(1, 1), (1, 2), (2, 3), (3, 2), (3, 5), (4, 4), (4, 5);

insert into messages(id_chat, id_user, content, date_time)
values
(1, 1, 'hello', current_timestamp),
(1, 1, 'You are probably wondering why I have gathered you here', current_timestamp + '10 second'),
(1, 2, 'no.', current_timestamp + '15 second'),
(4, 4, 'sdjffsd', current_timestamp),
(4, 5, 'asdas', current_timestamp),
(2, 3, 'hello', current_timestamp),
(2, 3, 'You are probably wondering why I have gathered you here', current_timestamp + '10 second'),
(3, 5, 'no.', current_timestamp + '15 second'),
(3, 5, 'sdjffsd', current_timestamp),
(3, 5, 'asdas', current_timestamp);

insert into pages(name, description, id_owner)
values
('stones', 'page for stones lovers', 3),
('memes', 'Я в своем познании настолько преисполнился, что я как будто бы уже сто триллионов миллиардов лет проживаю на триллионах и триллионах таких же планет, как эта Земля, мне этот мир абсолютно понятен', 4),
('laptops', 'love laptop to use laptop ', 5),
('street food', 'want shawarma', 3);

insert into followers(id_page, id_user)
values
(1, 1), (1, 2), (3, 3), (3, 4), (4, 4), (5, 4), (5, 5), (5, 3);

insert into tags(name)
values ('stone'), ('mem'), ('funny'), ('love'), ('food'), ('yammy');

insert into pages_tags(id_page, name)
values (1, 'stone'), (1, 'love'), (3, 'funny'), (3, 'mem'), (4, 'love'), (5, 'food'), (5, 'love'), (3, 'yammy');

insert into posts(id_page, id_user, content, reply_post_id, created_at, updated_at)
values 
(1, 3, 'huge stone - good stone', null, current_timestamp, current_timestamp),
(3, 4, '░░░░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▄▄▄░░░░░░░░░░
░░░░░░░░░░░░▄█▀▀░░░░░░░░░░░▄█▀█▄▄░░░░░░
░░░░░░░░░░▄█▀░░░░░░░░░░░░░░█░█▄░▀█▄░░░░
░░░░░░░░░░█░░░░░░░░░░░▄░▄░░▄░▄▀░░░░█▄░░
░░░░░░░░░█░░░░░░░░░░▄▄▄▀██▄░█▄░▄▄░░░▀▄░
░░░░░░░░█▀░░░░░░░░░░░▀█▄░▄██░███▀█▄░░█▄
░░░░░░░░█░░░░░░░░░░░▀▀▀▀▀░░░░▀████▀░░░█
░░░░░░░░█░░░░░░░░░░░░░▀▀▀░▄▄▄░░█░░░░░░█
░░░░░░░░█░░░░░░░░░░░░░░░░░██▀▀▀▀█░░░░░█
░░░░░░░░█░░░░░░░░░░░░░░░░█░▄▀▄▄▄▀░░░░░█
░░░░░░░░█░░░░░░░░░░░░░░░░██▀████░░░░░▄█
░░░░░░░░█▄░░░░░░░░░░░░░░░█▄█████░░░░░█░
░░░░░░░░░█▄░░░░░░░░░░░░░▀▀█████▀░░░░▄▀░
░░░░░░░░░▄██▄░░░░░░░░░░▄▄▄▄▄░░▄░░░▄█▀░░
░░░░░░░▄█▀▄░░▀▀▄▄░░▄▄▀░▀░░░░▀▀▀▄▄▀▀░░░░
░░░░░▄█▀░░░▀▄░░░░▀▀▀██▄▄▄▄▄▄█▀▀░░░░░░░░
░░░▄▀░░░░░░░░█▄░░░░░░░▄█▀▄░▄▄▄░░░░▀███░
░░█▀░░░░░░░░░░▀█▄░░░░▄█▄▄▄█████▄▄▄▀░░░░
▄▀░░░░░░░░░░░░░░░▀▀▀█▀▀▀░░░░▀██▀▀░░░░░░', null, current_timestamp, current_timestamp),
(3, 4, '░░░░░░░░░░░░░░░▄▄▄▄▄▄▄▄░░░░░░░░░░░░░░░░░
░░░░░░░░░▄▄█████████████▄░░░░░░░░░░░░░░░
░░░░░░░▄██████████████████░░░░░░░░░░░░░░
░░░░░▄██████████████▀▀▀░▀██░░░░░░░░░░░░░
░░░░▄██████▀▀▀▀▀▀░░░░░░░░▀██░░░░░░░░░░░░
░░░░████████░░░░░░░░░░░░░░▀█░░░░░░░░░░░░
░░░░████████░░░░░░░░░░░░░░▄█▄░░░░░░░░░░░
░░░░████████░░░░░░░░░░▄░░███▀░░░░░░░░░░░
░░░░░██████░░░░░█▀███▀▀░░░░░░░░░░░░░░░░░
░░░░░███████░░░░░▀▀▀░░░░░░░░░░░░░░░░░░░░
░░░░░▀█░░▀██░░░░░░░░░░▄░░░░▀░░░░░░░░░░░░
░░░░░░▀▄░░▄▀░░░░░░░░░░░▄████▀░░░░░░░░░░░
░░░░░░░░░░░░▄░░░░░░░░██▀█▄██░░░░░░░░░░░░
░░░░░░░░░░░▀░░░░░░░░░░░▀▀▀▀▀░▀░░░░░░░░░░
░░░░░░▄▄▄███░░░░░░░░░░░░░░░░░█▄░░░░░░░░░
▄▄▄█████████▀░░░░░░░░▄▄░░░░▄▄█████▄▄▄░░░
████████████░░░░░░░░░░██████████████████
█████████████░░░▀░░░░░▄█████████████████
██████████████░░░▄█▀▀█▀▀████████████████', null, current_timestamp, current_timestamp),
(4, 5, 'nice sjdkjflsd', null, current_timestamp, current_timestamp),
(5, 3, 'shawarma top!', null, current_timestamp, current_timestamp);

insert into posts(id_page, id_user, content, reply_post_id, created_at, updated_at)
values
(5, 4, 'such an accurate statement!', 5, current_timestamp, current_timestamp),
(1, 2, 'such an accurate statement!', 1, current_timestamp, current_timestamp);

insert into reactions(id_post, id_user, likes, dislikes)
values
(1, 1, true, true),
(1, 2, true, false),
(2, 3, true, false),
(2, 4, false, true),
(5, 5, true, true),
(5, 4, true, true),
(5, 3, true, true);
