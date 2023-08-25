from django.contrib import admin, messages

# Register your models here.

from base.models import Contato

#decoretor pega o que vem em segui e faz algo com ela, nesse caso vai fazer alguma acção 
@admin.action(description= "Marcar como lido")
def marcar_como_lido(modeladmin,request, queryset):
    #queryset mexe no sql
    queryset.update(lido = True)
    modeladmin.message_user(request, 'Formulário(s) marcado(s) como lido', messages.SUCCESS)


#aqui ele registra no django admin
#classe de contato para Django
@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'data', 'lido']
    search_fields = ['nome', 'email']
    list_filter = ['data', 'lido']
    actions = [marcar_como_lido]
