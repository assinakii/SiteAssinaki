from pyexpat import model

from django.contrib import admin

# Register your models here.
from .models import Cliente

class AdminCliente(admin.ModelAdmin):
    list_display = ["e_mail", "nome", "sobrenome", "data_nascimento", "cpf", "cnpj", "telefone_fixo", "telefone_celular", "timestamp"]
    list_display_links = ["nome", "sobrenome"]
    list_filter = ["cpf", "cnpj", "timestamp"]
    list_editable = ["e_mail", "telefone_fixo", "telefone_celular"]
    search_fields = ["e_mail", "nome", "sobrenome"]

    class Meta:
        model = Cliente

admin.site.register(Cliente, AdminCliente)
