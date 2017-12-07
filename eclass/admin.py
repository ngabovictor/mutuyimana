from django.contrib import admin
from eclass.models import *
# Register your models here.

admin.site.register(eclass)
admin.site.register(course)
admin.site.register(course_for)
admin.site.register(topic)
admin.site.register(note)
admin.site.register(chapter)
admin.site.register(student)
admin.site.register(assignment)
admin.site.register(assignment_for)
admin.site.register(Completed_assignment)
admin.site.register(qtype)
admin.site.register(question)
admin.site.register(qchoice)
admin.site.register(current)
admin.site.register(invited)