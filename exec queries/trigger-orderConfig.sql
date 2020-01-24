----------------------------------------triggers

create or replace function config_cost_date_func()
    returns trigger as
$func$
begin
    --set new.create_date = current_timestamp; todo if just insert. do itforall inserts

    --check resources:
    perform offered_config.id
    from offered_config
    where offered_config.id = new.offered_config_id
      and cpu_freq <= new.cpu_freq
      and cores <= new.cores
      and ram <= new.ram
      and bound_rate <= new.bound_rate;
    if not FOUND then
        raise exception 'invalid config';
    end if;

    --set cost:
    new.daily_cost =
                (new.cores * new.cpu_freq * 5000) + (new.ram * 4000) + (new.disk * 2000) + (new.bound_rate * 1000);

    --check wallet:
    if (new.daily_cost > (select balance from wallet where new.owner_id = wallet.owner_id)) then
        -- todo  - cost of other configs
        -- todo users with nowallet!
        raise exception ' not enough money';
    end if;

    return new;

end
$func$ LANGUAGE plpgsql;


create trigger config_cost_date_trigger
    before insert or update
    on user_config
    for each row
execute procedure config_cost_date_func();