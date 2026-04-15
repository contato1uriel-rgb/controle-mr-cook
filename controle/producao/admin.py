from django.contrib import admin

from .models import FiltroPedido, Relacao


@admin.register(Relacao)
class RelacaoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "litros_divisor_m3", "finalizada", "criada_em")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_filter = ("finalizada",)
    ordering = ("-criada_em",)


@admin.register(FiltroPedido)
class FiltroPedidoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "cod_interno",
        "volume_m3",
        "descricao",
        "numero_pedido",
        "setor",
    )
    list_display_links = ("id",)
    list_editable = ("volume_m3",)
    search_fields = ("cod_interno", "descricao", "descricao_produto", "codigo_produto")
    list_filter = ("setor", "fonte")
    ordering = ("cod_interno", "id")
