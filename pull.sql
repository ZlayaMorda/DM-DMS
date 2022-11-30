-- crud, order by, limit, in, like, and, or, case
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

select content from messages
where id_user in
(
    select id_user from messages, chats
	    where messages.id_user = chats.admin
);

select name from chats
where id_chat in
(
	select id_chat from messages
	where date_time <= current_timestamp - interval '1 day'
	and 
	(length(content) < 6 or length(content) > 12)
);

select count(likes), id_post
from (
	select id_post, likes from reactions
	where id_post in (
		select id_post from posts
		group by id_post
		having count(reply_post_id) >= 1
	)
) as foo
group by id_post;

select likes,
	case when likes = true then 'liked'
		 when likes = false then 'unliked'
		 else 'something strange'
	end
from reactions;

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

create view myview as select p1.id_post as reply_id, p1.content as reply_content, p2.id_post, p2.content
from posts p1 join posts p2 on p1.reply_post_id = p2.id_post;




