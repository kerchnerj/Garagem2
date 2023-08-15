from django.contrib import admin

from garagem.models import Acessorio, Categoria, Cor, Marca, Veiculo

admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Cor)
admin.site.register(Acessorio)