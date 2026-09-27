from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="WellnessRecord",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("student_name", models.CharField(max_length=100)),
                ("course", models.CharField(max_length=100)),
                ("sleep", models.IntegerField()),
                ("stress", models.IntegerField()),
                ("energy", models.IntegerField()),
                ("happiness", models.IntegerField()),
                ("study_pressure", models.IntegerField()),
                ("score", models.IntegerField()),
                ("mood", models.CharField(max_length=50)),
                ("suggestion", models.TextField()),
                ("feedback", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

