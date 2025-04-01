from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome da Marca')
    ativo = models.BooleanField(default=True, verbose_name='Ativo')
    descricao = models.TextField(verbose_name='Descrição da Marca')
    dt_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    dt_atualizacao = models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')
    
    class Meta:
        ordering = ['nome']
        verbose_name = 'Marca'

    def __str__(self):
        return self.nome
    
class Categoria(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome da Categoria')
    ativo = models.BooleanField(default=True, verbose_name='Ativo')
    descricao = models.TextField(verbose_name='Descrição da Categoria')
    dt_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    dt_atualizacao = models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')

    class Meta:
        ordering = ['nome']
        verbose_name = 'Categoria'
        
    def __str__(self):
        return self.nome
    

class Produto(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome do Produto')
    ativo = models.BooleanField(default=True, verbose_name='Ativo')
    descricao = models.TextField(verbose_name='Descrição do Produto')
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    dt_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    dt_atualizacao = models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='produtos', verbose_name='Categoria')
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name='produtos', verbose_name='Marca')

    class Meta:
        ordering = ['nome']
        verbose_name = 'Produto'
        
    def __str__(self):
        return self.nome
    
