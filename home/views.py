from django.shortcuts import render, redirect, get_object_or_404
from .models import Spravka
from .forms import SpravkaForm


def verify_spravka(request):
    context = {}
    if request.method == 'POST':
        parol = request.POST.get('parol')
        if parol and parol.isdigit() and len(parol) == 4:
            try:
                spravka = Spravka.objects.get(parol=parol)
                context['spravka'] = spravka
            except Spravka.DoesNotExist:
                context['error'] = "Parol noto‘g‘ri! Iltimos, qayta urinib ko‘ring."
        else:
            context['error'] = "Parol 4 xonali raqam bo‘lishi kerak."
    return render(request, 'verify_sprafka.html', context)



def spravka_list(request):
    sprafkalar = Spravka.objects.all()
    return render(request, 'spravka_list.html', {'sprafkalar': sprafkalar})

def spravka_create(request):
    if request.method == 'POST':
        form = SpravkaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('spravka_list')
    else:
        form = SpravkaForm()
    return render(request, 'spravka_form.html', {'form': form})

def spravka_update(request, pk):
    sprafka = get_object_or_404(Spravka, pk=pk)
    if request.method == 'POST':
        form = SpravkaForm(request.POST, instance=sprafka)
        if form.is_valid():
            form.save()
            return redirect('spravka_list')
    else:
        form = SpravkaForm(instance=sprafka)
    return render(request, 'spravka_form.html', {'form': form})

def spravka_delete(request, pk):
    sprafka = get_object_or_404(Spravka, pk=pk)
    if request.method == 'POST':
        sprafka.delete()
        return redirect('spravka_list')
    return render(request, 'spravka_confirm_delete.html', {'sprafka': sprafka})