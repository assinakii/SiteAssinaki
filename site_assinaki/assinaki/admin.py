from pyexpat import model

from django.contrib import admin

# Register your models here.
from .models import Cliente

class AdminCliente(admin.ModelAdmin):
    list_display = ["nome", "sobrenome", "data_nascimento", "cpf", "cnpj", "telefone_fixo", "telefone_celular", "e_mail", "timestamp"]
    class Meta:
        model = Cliente

admin.site.register(Cliente, AdminCliente)
