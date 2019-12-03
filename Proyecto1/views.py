from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
from Proyecto1.serialtest import mySerial
from myPlot import myPlot
from math import pi
from time import sleep

class views ():
    def saludo(request): # Vista
        return HttpResponse("<html><body><h1>Hola esta es mi primera pagina con Django</h1></body></html>")

    def sensores(request):
        #global launchxl
        pulsos = 0.0
        setpoint = 0.0
        error = 0.0
        varControl = 0
        if request.method == 'POST' and 'run_script' in request.POST:
            # import function to run
            # call function
            global launchxl
            #global pulsos
            launchxl =mySerial()
            launchxl.setName('launch1')
            launchxl.start()
            sleep(0.05)
            pulsos, setpoint = launchxl.data()
            pulsos = round(pulsos,2)
            error = round(setpoint - pulsos, 2)
            varControl = 1

        elif request.method == 'POST' and 'close_script' in request.POST:
            launchxl.stop()
            pulsos, setpoint = launchxl.data()
            pulsos = round(pulsos,2)
            error = round(setpoint - pulsos, 2)

        elif request.method == 'POST' and 'update_data' in request.POST:
            pulsos, setpoint = launchxl.data()
            pulsos = round(pulsos,2)
            error = round(setpoint - pulsos, 2)
            varControl = 1
        
        elif request.method == 'POST' and 'plot_pos' in request.POST:
            posPlot = myPlot()
            posPlot.graph_pos()

        elif request.method == 'POST' and 'plot_err' in request.POST:
            posPlot = myPlot()
            posPlot.graph_err()          

        elif request.method == 'GET' and 'tSetpoint' in request.GET:
            #print("Todo ok con" + str(request.GET.get))
            newSetpoint = int(request.GET.get('tSetpoint', ''))
            print(newSetpoint)
            launchxl.sendData(newSetpoint);
            varControl = 1
            sleep(0.05)
            pulsos, setpoint = launchxl.data()
            pulsos = round(pulsos,2)
            error = round(setpoint - pulsos, 2)

        #print(pulsos, setpoint)
        return render(request, "sensors.html", {"lpulsos": pulsos, "lsetpoint": setpoint, "lerror":error, "lcontrol": varControl})

    def principal(request):
        fecha_actual = datetime.datetime.now()
        return render(request, "intro.html", {"damefecha": fecha_actual})

