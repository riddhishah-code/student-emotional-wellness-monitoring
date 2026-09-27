from django.shortcuts import render, redirect, get_object_or_404
from .models import WellnessRecord

def home(request):
    return render(request, "wellness/home.html")

def questionnaire(request):
    if request.method == "POST":
        student_name = request.POST.get("student_name", "").strip()
        course = request.POST.get("course", "").strip()
        tired = int(request.POST.get("tired", 1))
        concentration = int(request.POST.get("concentration", 1))
        overwhelmed = int(request.POST.get("overwhelmed", 1))
        enjoyment = int(request.POST.get("enjoyment", 1))
        study_manage = int(request.POST.get("study_manage", 1))
        focus = int(request.POST.get("focus", 1))
        handling = int(request.POST.get("handling", 1))
        social = int(request.POST.get("social", 1))
        motivation = int(request.POST.get("motivation", 1))
        routine_change = int(request.POST.get("routine_change", 1))

        score = ((6-tired)+(6-concentration)+(6-overwhelmed)+enjoyment+
                 (6-study_manage)+(6-focus)+handling+social+motivation+(6-routine_change))

        if score >= 40:
            mood = "Doing Well"
            suggestion = "Your responses show a generally positive routine. Keep maintaining healthy study habits, proper rest, and time for activities you enjoy."
        elif score >= 30:
            mood = "Mostly Okay"
            suggestion = "You seem to be managing things fairly well. Try taking regular breaks, maintaining a good routine, and staying connected with friends or family."
        elif score >= 20:
            mood = "May Need a Break"
            suggestion = "Your responses suggest that you may be experiencing some academic pressure. Take short breaks, get enough rest, and make time for activities you enjoy."
        else:
            mood = "Needs Support"
            suggestion = "Your responses suggest that things may currently feel difficult to manage. Consider talking to a trusted teacher, counselor, family member, or friend."

        feedback = request.POST.get("feedback", "").strip()
        record = WellnessRecord.objects.create(
            student_name=student_name, course=course, sleep=tired,
            stress=concentration, energy=motivation, happiness=enjoyment,
            study_pressure=study_manage, score=score, mood=mood,
            suggestion=suggestion, feedback=feedback,
        )
        return redirect("result", record_id=record.id)
    return render(request, "wellness/questionnaire.html")

def result(request, record_id):
    record = get_object_or_404(WellnessRecord, id=record_id)
    return render(request, "wellness/result.html", {"record": record})

def dashboard(request):
    records = WellnessRecord.objects.all().order_by("-created_at")
    return render(request, "wellness/dashboard.html", {
        "records": records, "total": records.count(),
        "happy": records.filter(mood="Doing Well").count(),
        "good": records.filter(mood="Mostly Okay").count(),
        "stressed": records.filter(mood="May Need a Break").count(),
        "attention": records.filter(mood="Needs Support").count(),
    })
