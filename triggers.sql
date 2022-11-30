create function log_user() returns trigger as $log_user$
	begin
		IF (TG_OP = 'DELETE') THEN
            INSERT INTO logs(id_user, date_time, action) values (old.id_user, current_timestamp, 'delete');
        ELSIF (TG_OP = 'UPDATE') THEN
            INSERT INTO logs(id_user, date_time, action) values (new.id_user, current_timestamp, 'update');
        ELSIF (TG_OP = 'INSERT') THEN
            INSERT INTO logs(id_user, date_time, action) values (new.id_user, current_timestamp, 'insert');
        END IF;
        RETURN NULL;
    END;
$log_user$ LANGUAGE plpgsql;
CREATE TRIGGER log_user AFTER INSERT OR UPDATE OR DELETE ON users
    FOR EACH ROW EXECUTE FUNCTION log_user();
    
create function log_message() returns trigger as $log_message$
	begin
		IF (TG_OP = 'DELETE') THEN
            INSERT INTO logs(id_user, date_time, action) values 
            (old.id_user, current_timestamp, 'delete' || '_on chat_' || old.id_chat::text);
        ELSIF (TG_OP = 'UPDATE') THEN
            INSERT INTO logs(id_user, date_time, action) values
            (new.id_user, current_timestamp, 'update' || '_on chat_' || new.id_chat::text);
        ELSIF (TG_OP = 'INSERT') THEN
            INSERT INTO logs(id_user, date_time, action) values
            (new.id_user, current_timestamp, 'insert' || '_on chat_' || new.id_chat::text);
        END IF;
        RETURN NULL;
    END;
$log_message$ LANGUAGE plpgsql;
CREATE TRIGGER log_message AFTER INSERT OR UPDATE OR DELETE ON messages
    FOR EACH ROW EXECUTE FUNCTION log_message();
    
    
drop trigger log_message on messages;

select * from information_schema.triggers;


create or replace procedure create_user(
    name varchar(128),
    last_name varchar (128),
    email varchar (256),
    password varchar (64),
    image_s3_path varchar (256),
    role varchar (10)
)
language plpgsql    
as $$
begin
	insert into users(name, last_name, email, password, image_s3_path, role)
	values(
		name,
		last_name,
		email,
		password,
		image_s3_path,
		role
	);

    commit;
end;$$;
	
	
call create_user('TP','RP','trP@m.ru','12345678','linkP','user');


create or replace procedure create_message(
    id_chat int,
    id_user int,
    content varchar(512)
)
language plpgsql    
as $$
begin
	insert into messages(id_chat, id_user, content, date_time)
	values(id_chat, id_user, content, current_timestamp);

    commit;
end;$$;


