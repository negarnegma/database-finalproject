create table offered_config
(
    id         serial primary key,
    os         varchar(50),
    ram        float,
    cores      float,
    disk       float,
    cpu_freq   float,
    bound_rate float
);

create table ssh
(
    id      serial primary key,
    name    varchar(50),
    content varchar(3000),
    owner_id int references "user" (id)

);
create table akshaye_tabriz
(
    id   serial primary key,
    pass varchar(128),
    salt varchar(128)
);
create table "user"
(
    id              serial primary key,
    nasional_number varchar(20) unique ,
    fullname        varchar(50),
    address         varchar(200),
    role            int,
    password_id     int references akshaye_tabriz (id),
    register_date   timestamp
);
create table wallet
(
    id       serial primary key,
    balance  float,
    owner_id int references "user" (id)
);
-- create table user_ssh
-- (
--     user_id int references "user" (id),
--     ssh_id  int references ssh (id)
-- );
create table ticket
(
    id          serial primary key,
    owner_id int references "user" (id),
    content    varchar(200),
    -- responder_id int references "user" (id),
    -- answer      varchar(200),
    c_date timestamp,
    status      int,
    first_ticket_id int references ticket(id),
    "order" int
);
create table user_config
(
    id         serial primary key,
    os         varchar(50),
    ram        float,
    cores      float,
    disk       float,
    cpu_freq   float,
    bound_rate float,
    create_date timestamp,
    offered_config_id int references offered_config(id),
    ssh_id     int references ssh (id),
    owner_id   int references "user" (id),
    daily_cost float
);

create table "snapshot"
(
    id          serial primary key,
    create_date timestamp,
    size        float,
    user_config_id int references user_config (id)
);
-- create table user_config_snapshot
-- (
--     user_config_id int references user_config (id),
--     snapshot_id    int references "snapshot" (id)

-- );
