until nc -z -v -w30 db 5432
do
  echo "Waiting for database connection"
  sleep 5
done

python manage.py runserver 127.0.0.1:8080
