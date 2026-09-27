from django.db import models

class WellnessRecord(models.Model):
    student_name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    sleep = models.IntegerField()
    stress = models.IntegerField()
    energy = models.IntegerField()
    happiness = models.IntegerField()
    study_pressure = models.IntegerField()
    score = models.IntegerField()
    mood = models.CharField(max_length=50)
    suggestion = models.TextField()
    feedback = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} - {self.mood}"
