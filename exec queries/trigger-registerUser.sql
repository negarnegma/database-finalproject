----------------------------------------trigers

create or replace function register_user_func()
    returns trigger as
$func$
begin
    insert into akshaye_tabriz(pass, salt)
    VALUES (new.pass, new.salt);
    -- returning id as @passId;

--     declare @passId int;

    insert into "user"(nasional_number, fullname, address, role, password_id, register_date)
    values (new.nasional_number, new.fullname, new.address, 1,
            (select id from akshaye_tabriz a where a.pass = new.pass and a.salt = new.salt), current_timestamp);

    insert into wallet (balance, owner_id) values
    (10, (select id from "user" where nasional_number = new.nasional_number));

    return new;

end
$func$ LANGUAGE plpgsql;


create trigger register_user
    instead of insert
    on registering_users_view
    for each row
execute procedure register_user_func();