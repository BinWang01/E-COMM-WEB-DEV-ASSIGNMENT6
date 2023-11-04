from django.contrib import admin
from data.models import College, Department, Degree, Course, DegreeCourse

# Register your models here.
admin.site.register(College)
admin.site.register(Department)
admin.site.register(Degree)
admin.site.register(Course)
admin.site.register(DegreeCourse)
