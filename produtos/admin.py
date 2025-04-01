import csv
from django.contrib import admin
from django.http import HttpResponse
from .models import Categoria, Marca, Produto

# Register your models here.
@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo', 'descricao', 'dt_criacao', 'dt_atualizacao')
    search_fields = ('nome',)
    list_filter = ('ativo',)
    ordering = ('nome',)
    
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo', 'descricao', 'dt_criacao', 'dt_atualizacao')
    search_fields = ('nome',)
    list_filter = ('ativo',)
    ordering = ('nome',)
    

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'marca', 'categoria', 'preco', 'ativo', 'dt_criacao', 'dt_atualizacao')
    search_fields = ('nome','marca__nome', 'categoria__nome')
    list_filter = ('ativo', 'marca', 'categoria')
    ordering = ('nome',)

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="produtos.csv"'
        writer = csv.writer(response)
        writer.writerow(['título', 'marca', 'categoria', 'preço',
                         'ativo', 'descrição', 'criado_em', 'atualizado_em'])
        for produto in queryset:
            writer.writerow([produto.nome, produto.marca.nome, produto.categoria.nome,
                             produto.preco, produto.ativo, produto.descricao,
                             produto.dt_criacao, produto.dt_atualizacao])
        return response

    export_to_csv.short_description = 'Exportar para CSV'
    actions = [export_to_csv]
