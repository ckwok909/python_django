from django.contrib import admin
from first_django_web.models import AccessRecord,Topic,Webpage,PeopleRecord
# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(PeopleRecord)

