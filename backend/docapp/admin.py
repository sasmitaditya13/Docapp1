from django.contrib import admin
from .models import User
from .models import Project
from .models import Project_role
from .models import Document
from .models import Document_role


admin.site.register(User)
admin.site.register(Project)
admin.site.register(Project_role)
admin.site.register(Document)
admin.site.register(Document_role)
# Register your models here.
