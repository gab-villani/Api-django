from django.contrib import admin
from app.models import Carro

class Carros(admin.ModelAdmin):
    list_display =('id','marca','modelo','bits')
    list_display_links =('id','marca')
    search_field = ('marca',)

admin.site.register(Carro,Carros)




