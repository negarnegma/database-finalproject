create view registering_users_view AS
select nasional_number, fullname, address, pass, salt
from "user",
     akshaye_tabriz;
