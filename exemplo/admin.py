# Especificações que passamos para a aplicação django admin
from django.contrib import admin
from exemplo.models import Categoria
from exemplo.models import Aluno
from exemplo.models import Compra
from exemplo.models import Problema
from exemplo.models import Pessoa
from exemplo.models import Time
from exemplo.models import Usuario
from exemplo.models import Cidade
from exemplo.models import Esporte

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Aluno)
admin.site.register(Compra)
admin.site.register(Problema)
admin.site.register(Pessoa)
admin.site.register(Time)
admin.site.register(Usuario)
admin.site.register(Cidade)
admin.site.register(Esporte)
