insert into offered_config(os, ram, cores, disk, cpu_freq, bound_rate)
values ('freeBSD', 2, 3, 20, 3, 4);
insert into offered_config(os, ram, cores, disk, cpu_freq, bound_rate)
values ('win7', 4, 2, 10, 2, 6);
insert into offered_config(os, ram, cores, disk, cpu_freq, bound_rate)
values ('win7', 16, 2, 30, 5, 5);

insert into ssh(name, content)
values ('my-ssh1', 'begin-private-key-ararar-end');

insert into akshaye_tabriz(pass, salt)
values ('myhashedpass', 'paprica');

insert into "user"(nasional_number, fullname, address, role, password_id, register_date)
values ('123456789', 'Negar n Zamiri', 'st.23 Mashhad', 0, 1, current_timestamp);

insert into wallet(balance, owner_id)
values (100000, 1);

insert into user_ssh(user_id, ssh_id)
values (1, 1);

insert into ticket(question, answer, answer_date, status)
values ('how can i setup network for my vms?', 'dude! we"re in test mode!!', current_timestamp, 1);

insert into user_config(os, ram, cores, disk, cpu_freq, bound_rate, ssh_id, owner_id, daily_cost)
values ('freeBSD', 2, 3, 20, 3, 4, 1, 1, 500);

insert into snapshot(create_date, size)
values (current_timestamp, 128);

insert into user_config_snapshot(user_config_id, snapshot_id)
values (1, 1);
---------------------------------
insert into registering_users_view (nasional_number, fullname, address, pass, salt)
values ('0000', 'negi neg', 'aven1', 'hashedwith2', 'salt2');
insert into registering_users_view (nasional_number, fullname, address, pass, salt)
values ('001200', 'Sahar Babaii', 'aven1', 'hashedwith3', 'salt4');
-------------------------------------
insert into user_config (os, ram, cores, disk, cpu_freq, bound_rate, ssh_id, owner_id, daily_cost, offered_config_id)
VALUES ('freeBSD', 2, 3, 20, 3, 4, 1, 1, 0, 1);

