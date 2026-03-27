from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import VolleyPlayer
from .forms import VolleyPlayerForm


# READ - List all players
def player_list(request):
    query = request.GET.get('q', '')
    players = VolleyPlayer.objects.all()
    if query:
        players = players.filter(name__icontains=query)
    return render(request, 'volley_app/player_list.html', {
        'players': players,
        'query': query
    })


# READ - View single player
def player_detail(request, pk):
    player = get_object_or_404(VolleyPlayer, pk=pk)
    return render(request, 'volley_app/player_detail.html', {'player': player})


# CREATE - Add new player
def player_create(request):
    if request.method == 'POST':
        form = VolleyPlayerForm(request.POST)
        if form.is_valid():
            player = form.save()
            messages.success(request, f'Player "{player.name}" added successfully!')
            return redirect('player_list')
    else:
        form = VolleyPlayerForm()
    return render(request, 'volley_app/player_form.html', {'form': form, 'action': 'Add'})


# UPDATE - Edit existing player
def player_update(request, pk):
    player = get_object_or_404(VolleyPlayer, pk=pk)
    if request.method == 'POST':
        form = VolleyPlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            messages.success(request, f'Player "{player.name}" updated successfully!')
            return redirect('player_list')
    else:
        form = VolleyPlayerForm(instance=player)
    return render(request, 'volley_app/player_form.html', {'form': form, 'action': 'Edit', 'player': player})


# DELETE - Remove player
def player_delete(request, pk):
    player = get_object_or_404(VolleyPlayer, pk=pk)
    if request.method == 'POST':
        name = player.name
        player.delete()
        messages.success(request, f'Player "{name}" deleted successfully!')
        return redirect('player_list')
    return render(request, 'volley_app/player_confirm_delete.html', {'player': player})
