from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.db.models import Model

from relacionamentos.models import Pessoa
from relacionamentos.models import Passaporte
from relacionamentos.models import Reporter
from relacionamentos.models import Artigo
from relacionamentos.models import ArtigoAdmin
from relacionamentos.models import Revista
from relacionamentos.models import Reportagem
from relacionamentos.models import Aluno
from relacionamentos.models import Disciplina
from relacionamentos.models import Matricula

# Register your models here.
admin.site.register(Pessoa)
admin.site.register(Passaporte)
admin.site.register(Reporter)
admin.site.register(Artigo, ArtigoAdmin)
admin.site.register(Revista)
admin.site.register(Reportagem)
admin.site.register(Aluno)
admin.site.register(Disciplina)
admin.site.register(Matricula)
