from django.contrib import admin
from .models import WellnessRecord

@admin.register(WellnessRecord)
class WellnessRecordAdmin(admin.ModelAdmin):
    list_display = (
        "student_name", "course", "score", "mood", "created_at"
    )
    list_filter = ("mood", "course")
    search_fields = ("student_name", "course")
