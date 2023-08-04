from django.db import models


UF_CHOICES = (
    ('MG', 'Minas Gerais'),
    ('SP', 'São Paulo'),
    ('RJ', 'Rio de Janeiro'),
    ('BA', 'Bahia'),
    ('RO', 'Rondônia'),
    ('AC', 'Acre'),
    ('AM', 'Amazonas'),
    ('RR', 'Roraima'),
    ('PA', 'Pará'),
    ('AP', 'Amapá'),
    ('TO', 'Tocantins'),
    ('MA', 'Maranhão'),
    ('PA', 'Pará'),
    ('PI', 'Piauí'),
    ('CE', 'Ceará'),
    ('RN', 'Rio Grande do Norte'),
    ('PB', 'Paraíba'),
    ('PE', 'Pernambuco'),
    ('AL', 'Alagoas'),
    ('SE', 'Sergipe'),
    ('ES', 'Espírito Santo'),
    ('PR', 'Paraná'),
    ('SC', 'Santa Catarina'),
    ('RS', 'Rio Grande do Sul'),
    ('MS', 'Mato Grosso do Sul'),
    ('MT', 'Mato Grosso'),
    ('GO', 'Goiás'),
    ('DF', 'Distrito Federal'),
)

class Cliente(models.Model):
    nome = models.CharField(max_length=250, blank=True)
    nome_fantasia = models.CharField(max_length=250, blank=True, null=True)
    cnpj = models.CharField(max_length=18, unique=True, blank=True)
    endereco = models.CharField(max_length=250, blank=True)
    numero = models.IntegerField(blank=True, null=True)
    complemento = models.CharField(max_length=250, blank=True, null=True)
    cep = models.CharField(max_length=9, blank=True)
    bairro = models.CharField(max_length=250, blank=True)
    cidade = models.CharField(max_length=250, blank=True)
    uf = models.CharField(max_length=2, choices=UF_CHOICES, blank=True)
    email = models.EmailField(max_length=250, blank=True, null=True)
    telefone = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.nome
    