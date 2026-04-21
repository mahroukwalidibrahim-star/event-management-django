from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from events.models import Event
from participations.models import Participation


@login_required
def join_event(request, id):
    event = Event.objects.get(id=id)

    count = Participation.objects.filter(event=event).count()

    if count < event.capacite_max:
        Participation.objects.get_or_create(
            user=request.user,
            event=event
        )

    return redirect('event_detail', id=id)

@login_required
def cancel_event(request, id):
    event = Event.objects.get(id=id)

    Participation.objects.filter(
        user=request.user,
        event=event
    ).delete()

    return redirect('event_detail', id=id)

@login_required
def participants_list(request, id):
    event = Event.objects.get(id=id)
    participants = Participation.objects.filter(event=event)

    return render(request, 'events/participants.html', {
        'event': event,
        'participants': participants
    })
