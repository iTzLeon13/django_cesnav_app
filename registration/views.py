from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ParticipantForm
from .models import Participant
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
import random

def register(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Formulario enviado correctamente")
        else:
            print(form.errors)
    else:
        form = ParticipantForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def view_participants(request):
    participants = Participant.objects.all()
    return render(request, 'registration/view_participants.html', {'participants': participants})

@login_required
def create_teams(request):
    if request.method == 'POST':
        participants = list(Participant.objects.filter(will_attend=True))
        random.shuffle(participants)
        teams = [participants[i:i + 10] for i in range(0, len(participants), 10)]
        
        # Send emails to participants
        for idx, team in enumerate(teams):
            team_members = ", ".join([p.name for p in team])
            for participant in team:
                send_mail(
                    'Tu equipo para el rally',
                    f'Hola {participant.name},\n\nTu equipo es:\n{team_members}',
                    settings.DEFAULT_FROM_EMAIL,
                    [participant.email],
                    fail_silently=False,
                )
        return redirect('teams_confirmed')
    return render(request, 'registration/create_teams.html')