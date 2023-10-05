from django.contrib import admin


from reserva.models import Reserva, PetShop


# Register your models here.
@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email','nome_pet', 'data_reserva', 'turno']
    search_fields= ['nome', 'email', 'nome_pet']
    list_filter = ['data_reserva','turno', 'porte' ]


@admin.register(PetShop)
class PetshopAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email','telefone']
    search_fields= ['nome', 'email', 'telefone']
