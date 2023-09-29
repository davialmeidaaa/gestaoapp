# Navegar até o diretório do projeto
cd 'D:\0 - Repositories\personal\juliana\GestaoApp'

# Iniciar o container do Docker
docker-compose up -d db

# Aguardar alguns segundos para garantir que o banco de dados está pronto
Start-Sleep -Seconds 5

# Iniciar o servidor Django em background
Start-Process -NoNewWindow -FilePath "python" -ArgumentList "manage.py runserver"

# Aguardar alguns segundos para garantir que o servidor Django está pronto
Start-Sleep -Seconds 5

# Abrir o navegador padrão no endereço do projeto
Start-Process "http://127.0.0.1:8000/"
