from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Bb, Rubric
from .forms import BbForm


def get_rubrics():
    return Rubric.objects.all()


def index(request):
    bbs = Bb.objects.filter(is_active=True).select_related('rubric', 'author')

    paginator = Paginator(bbs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'bbs': page_obj,
        'rubrics': get_rubrics(),
    }
    return render(request, 'bboard/index.html', context)


def by_rubric(request, rubric_id):
    rubric = get_object_or_404(Rubric, pk=rubric_id)
    bbs = Bb.objects.filter(rubric=rubric, is_active=True).select_related('author')

    paginator = Paginator(bbs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'rubric': rubric,
        'bbs': page_obj,
        'rubrics': get_rubrics(),
        'current_rubric_id': rubric_id,
    }
    return render(request, 'bboard/by_rubric.html', context)


def detail(request, pk):
    bb = get_object_or_404(Bb, pk=pk)
    context = {
        'bb': bb,
        'rubrics': get_rubrics(),
    }
    return render(request, 'bboard/detail.html', context)


@login_required
def add_bb(request):
    if request.method == 'POST':
        form = BbForm(request.POST)
        if form.is_valid():
            bb = form.save(commit=False)
            bb.author = request.user
            bb.save()
            messages.success(request, 'Объявление успешно добавлено!')
            return redirect('bboard:index')
    else:
        form = BbForm()

    context = {
        'form': form,
        'rubrics': get_rubrics(),
    }
    return render(request, 'bboard/add_bb.html', context)


@login_required
def my_ads(request):
    bbs = Bb.objects.filter(author=request.user)
    context = {
        'bbs': bbs,
        'rubrics': get_rubrics(),
    }
    return render(request, 'bboard/my_ads.html', context)