# Generated by Django 4.2.4 on 2023-08-04 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=250)),
                ('nome_fantasia', models.CharField(blank=True, max_length=250, null=True)),
                ('cnpj', models.CharField(blank=True, max_length=18, unique=True)),
                ('endereco', models.CharField(blank=True, max_length=250)),
                ('numero', models.IntegerField(blank=True, null=True)),
                ('complemento', models.CharField(blank=True, max_length=250, null=True)),
                ('cep', models.CharField(blank=True, max_length=9)),
                ('bairro', models.CharField(blank=True, max_length=250)),
                ('cidade', models.CharField(blank=True, max_length=250)),
                ('uf', models.CharField(blank=True, max_length=250)),
                ('email', models.EmailField(blank=True, max_length=250, null=True)),
                ('telefone', models.CharField(blank=True, max_length=250)),
            ],
        ),
    ]