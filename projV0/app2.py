from user import user_crud

user_crud.print_users()

user_crud.register_user("12345678", "python user", "python1", "123")

print(user_crud.login_user("12345678", "123"))
print(user_crud.login_user("12345678", "12"))
print(user_crud.login_user("123468", "12"))
