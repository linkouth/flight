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
