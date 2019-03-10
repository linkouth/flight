from django.shortcuts import render
from django.db import connection


def procedure_list(request):
    return render(request, 'flight/index.html', {})


def proc1(request):
    param = request.POST['param']
    with connection.cursor() as cursor:
        cursor.execute("exec proc1 %s;", [param])
        rows = cursor.fetchall()
    return render(request, 'flight/proc1.html', {
        'param': param,
        'rows': rows
    })


def proc2(request):
    param = request.POST['param']
    with connection.cursor() as cursor:
        cursor.execute("declare @seats_count int; exec proc2 %s, @seats_count output; select @seats_count;", [param])
        rows = cursor.fetchall()
    return render(request, 'flight/proc2.html', {
        'param': param,
        'rows': rows,
    })


def proc4(request):
    param = request.POST['param']
    with connection.cursor() as cursor:
        cursor.execute("exec proc3 1, %s", [param])
        rows = cursor.fetchall()
    return render(request, 'flight/proc4.html', {
        'param': param,
        'rows': rows,
    })


def proc5(request):
    param = request.POST['param']
    with connection.cursor() as cursor:
        cursor.execute("declare @a int; exec @a = proc4 %s; select @a;", [param])
        rows = cursor.fetchall()
    return render(request, 'flight/proc5.html', {
        'param': param,
        'rows': rows,
    })