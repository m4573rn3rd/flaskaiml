from werkzeug.security import generate_password_hash
a = generate_password_hash('1234')
print(a)