from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic

from .forms import DayCreateForm, SearchForm
from .models import Day

import json


def index(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        # year = form.cleaned_data['year']
        # month = form.cleaned_data['month']
        # day = form.cleaned_data['day']
        query = form.cleaned_data['search']
        # diaries = Day.search(year, month, day, query).order_by('-date')
        diaries = Day.search(query).order_by('-date')
    else:
        print("!!!error:",form.errors)
        diaries = Day.objects.order_by('-date')
    paginator = Paginator(diaries, 3) 
    page_number = request.GET.get('page', 1)
    try:
        page_number = max(1, int(page_number))
    except ValueError:
        page_number = 1
    page_obj = paginator.get_page(page_number)

    dlist = [d.date.strftime("%Y%m%d") for d in Day.objects.all()]
    context = {
        "page_obj": page_obj, "dlist": json.dumps(dlist),
        'form': form, 'query': query
    }

    return render(request, 'diary/day_list.html', context)


def add(request):
    form = DayCreateForm(request.POST or None, request.FILES or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('diary:index')

    context = {
        'form': form
    }
    return render(request, 'diary/day_form.html', context)


def update(request, pk):
    day = get_object_or_404(Day, pk=pk)
    form = DayCreateForm(request.POST or None, request.FILES or None, instance=day)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('diary:index')

    context = {
        'form': form
    }
    return render(request, 'diary/day_form.html', context)


def delete(request, pk):
    # urlのpkを基に、Dayを取得
    day = get_object_or_404(Day, pk=pk)

    # method=POST、つまり送信ボタン押下時、入力内容が問題なければ
    if request.method == 'POST':
        day.delete()
        return redirect('diary:index')

    # 通常時のページアクセスや、入力内容に誤りがあればまたページを表示
    context = {
        'day': day,
    }
    return render(request, 'diary/day_confirm_delete.html', context)


def detail(request, pk):
    # urlのpkを基に、Dayを取得
    day = get_object_or_404(Day, pk=pk)

    # 通常時のページアクセスや、入力内容に誤りがあればまたページを表示
    context = {
        'day': day,
    }
    return render(request, 'diary/day_detail.html', context)
