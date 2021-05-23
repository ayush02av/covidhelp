from django.contrib import admin
from . import models

admin.site.register(models.VerifiedLead)
admin.site.register(models.NonVerifiedLead)
admin.site.register(models.Case)
admin.site.register(models.BlogArticle)