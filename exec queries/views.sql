create or replace view registering_users_view AS
select "user".id, nasional_number, fullname, address, pass, salt
from "user"
         left join akshaye_tabriz a on "user".password_id = a.id;
