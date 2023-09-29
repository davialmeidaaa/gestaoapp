# Navegar até o diretório do projeto
cd 'D:\0 - Repositories\personal\juliana\GestaoApp'

# Iniciar o container do Docker
docker-compose up -d db

# Aguardar alguns segundos para garantir que o banco de dados está pronto
Start-Sleep -Seconds 5

# Iniciar o servidor Django
python manage.py runserver
