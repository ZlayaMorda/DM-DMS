-- crud, order by, limit, in, like
select * from users
order by name;

select * from messages
limit 3 offset 5;

select name from users
where role = 'admin';

select * from users
where role in ('admin', 'moderatore');

select * from users
where email like 'tar%';

insert into users(name, last_name)
values ('mem', 'kek');

update users
set email = 'mk@m.ru'
where name = 'mem';

delete from users
where name = 'mem';

-- count/union

create temp table temp_followers as
select count(id_user) as page_followers
from followers
where id_page = 5
union
select count(id_user) as page_followers
from followers
where id_page = 4
union
select count(id_user) as page_followers
from followers
where id_page = 1;

-- avg, sum, min, max, group by, having

select avg(page_followers)
from temp_followers;

select sum(page_followers)
from temp_followers;

select avg(page_followers)
from temp_followers;

select min(page_followers), max(page_followers)
from temp_followers;

select id_chat
from chats_users
group by id_chat
having count(id_user) > 1;


-- joins

select pages.id_page, pages.description, posts.content
from pages
join posts on pages.id_page = posts.id_page;

select users.id_user, users.name, pages.id_page from users
left join pages on users.id_user = pages.id_owner;

select * from tags cross join pages;








