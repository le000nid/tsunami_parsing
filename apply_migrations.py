from yoyo import read_migrations, get_backend

backend = get_backend('postgres://postgres:password@localhost/postgres')
migrations = read_migrations('./migrations')
backend.apply_migrations(backend.to_apply(migrations))