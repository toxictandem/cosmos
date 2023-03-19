from django.shortcuts import render

from .forms import *
from .models import *
from random import randint
def index(request):

    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['forma']
            data = list(map(str, data[1:-1].split(';')))
            check = []
            for i in range(len(data)):
                temp = list(map(str, data[i][1:-1].split(',')))
                import math
                oxi = 60
                s = int(temp[0])
                c = int(temp[1])
                e = 220
                best = -1
                ans = -1
                g0 = 8

                for t in range(31):
                    temp = 0
                    for i in range(t + 1):
                        temp += i
                    if best == -1 or (temp > best and temp <= e):
                        best = temp
                        ans = t

                k = math.sin(-3.14 / 2 + (3.14 * (ans + 0.5 * oxi)) / 40)
                m1 = g0 + 192 + g0 * k
                count = 0
                while g0 <= c - 8:
                    g0 += g0 * k
                    count += 1
                count = max(1, count)

                m2 = 400 * s // count
                const = 80
                days = count
                resourses = (oxi // m2 // m1) * 7 + const * 10

                population = c - 8
                check.append([days, resourses,population, const,oxi // (m2 - m1)])
            return render(request, 's1.html', {'data': data, 'check': check})
    else:
        form = InputForm()

    return render(request, 'q1.html', {'form': form})

def new(request):
    return render(request, 'q1.css')

def kk(request):
    import math
    oxi = 60
    s = int(input())
    c = int(input())
    e = 220
    best = -1
    ans = -1
    g0 = 8

    for t in range(31):
        temp = 0
        for i in range(t + 1):
            temp += i
        if best == -1 or (temp > best and temp <= e):
            best = temp
            ans = t

    k = math.sin(-3.14 / 2 + (3.14 * (ans + 0.5 * oxi)) / 40)
    m1 = g0 + 192 + g0 * k
    count = 0
    while g0 <= c - 8:
        g0 += g0 * k
        count += 1

    m2 = 400 * s // count
    const = 80
    days = count
    resourses = (oxi // m2 // m1) * 7 + const * 10
    population = c - 8
    print(days)
    print('idk')
    print(resourses)
    print(const)
    print(population)
    return render(request, )