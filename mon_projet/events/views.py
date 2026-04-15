from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import EventForm
from .models import Event
from participations.models import Participation
from django.db.models import Count


@login_required
def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html',  {
    'events': events,
    'user': request.user
})

@login_required
def add_event(request):
    form = EventForm()

    if request.method == 'POST':
        form = EventForm(request.POST)

        if form.is_valid():
            event = form.save(commit=False)
            event.organisateur = request.user   
            event.save()
            return redirect('event_list')

    return render(request, 'events/add_event.html', {'form': form})

@login_required
def event_detail(request, id):
    event = Event.objects.get(id=id)
    return render(request, 'events/event_detail.html', {'event': event})

@login_required
def edit_event(request, id):
    event = Event.objects.get(id=id)

    if request.user != event.organisateur:
        return redirect('event_list')

    form = EventForm(request.POST or None, instance=event)

    if form.is_valid():
        form.save()
        return redirect('event_list')

    return render(request, 'events/edit_event.html', {'form': form})

@login_required
def delete_event(request, id):
    event = Event.objects.get(id=id)

    if request.user != event.organisateur:
        return redirect('event_list')

    if request.method == "POST":
        event.delete()
        return redirect('event_list')

    return render(request, 'events/delete_event.html', {'event': event})



@login_required
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request, 'register.html', {'form': form})
@login_required
def stats(request):
    total_events = Event.objects.count()
    total_participations = Participation.objects.count()

    top_event = Event.objects.annotate(
        num_participants=Count('participation')
    ).order_by('-num_participants').first()

    return render(request, 'events/stats.html', {
        'total_events': total_events,
        'total_participations': total_participations,
        'top_event': top_event
    })

@login_required
def cancel_event(request, id):
    event = Event.objects.get(id=id)

    Participation.objects.filter(
        user=request.user,
        event=event
    ).delete()

    return redirect('event_detail', id=id)

