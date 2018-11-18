from django.db import models
from django.core.validators import EmailValidator

# Create your models here.
class Clientes(models.Model):
    nome = models.CharField(max_length=150)
    sobrenome = models.CharField(max_length=150)
    data_nascimento = models.DateTimeField(auto_now=False, auto_now_add=False)
    cpf = models.CharField(max_length=11)
    cnpj = models.CharField(max_length=14)
    telefone_fixo = models.CharField(max_length=15)
    telefone_celular = models.CharField(max_length=15)
    e_mail = models.EmailField(validators=[EmailValidator])

    # tabelas separadas
    # pais =
    # estado =
    # cidade =
    # rua =
    # número =
    # complemento =

    # tabela de login
    # login =
    # senha =
    # confirma_senha =
