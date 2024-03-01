from django.contrib import admin

from .models import QuestDescription, QuestLongDescription, Quest, Question

# Register your models here.

admin.site.register(QuestDescription)
admin.site.register(QuestLongDescription)
admin.site.register(Quest)
admin.site.register(Question)
