----------------------------------------triggers

create or replace function ssh_func()
    returns trigger as
$func$
begin

    insert into ssh(name, content)
    values (new.name, new.content);

    insert into user_ssh(user_id, ssh_id)
    values (1, 1);
        return new;

end
$func$ LANGUAGE plpgsql;


create trigger config_cost_date_trigger
    before insert or update
    on user_config
    for each row
execute procedure config_cost_date_func();