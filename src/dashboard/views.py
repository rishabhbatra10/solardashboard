# @auther: Rishabh Batra #
# Indian Institute of Science #
#============== Solar_Dashboard ================#

""" Importing the django attributes required """
from django.shortcuts import render, render_to_response, redirect # rendering and redirecting
from django.http import HttpResponse # for returning Http response 
from django.views.decorators.csrf import csrf_exempt # decorater for excepmting the security
from django.core.cache import cache # for caheing the data temporarily

from .models import * # importing models 
from dashboard.models import * # importing models from dashboard app

""" Importing the bokeh plots attributes required for plotting"""
from bokeh.plotting import figure, output_file, show 
from bokeh.embed import components 
from bokeh.resources import CDN
from bokeh.models import HoverTool

import sqlite3
from sqlite3 import Error
import numpy as np # Numpy for calculations
import pandas as pd

import decimal

@csrf_exempt
def index(request):
    print("Let's start")
    query1 = "year"
    query2 = "cuf"
    query3 = "time"
    query4 = "eac_t"
    if request.method == 'POST':
        query1 = request.POST.get('X_axis_1')       
        query2 = request.POST.get('Y_axis_1')
        query3 = request.POST.get('X_axis_2')
        query4 = request.POST.get('Y_axis_2')
        print(query1)
        print(query2)
        print(query3)
        print(query4)
    #cache.get('graph_2_data') == None
    if 0==0:
        df_g2 = pd.DataFrame()
        df_sn05 = SN05_D.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
        print("8% Data Loaded")
        df_sn7b = SN7B_D.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
        print("16% Data Loaded")
        df_sn13 = SN13_D.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
        print("25% Data Loaded")
        df_sn15 = SN15_D.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
        print("33% Data Loaded")
        df_sn28 = SN28_D.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
        print("41% Data Loaded")
        df_sn33 = SN33_D.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
        print("50% Data Loaded")
        df_sn34 = SN34_D.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
        print("58% Data Loaded")
        df_sn44 = SN44_D.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
        print("66% Data Loaded")
        df_sn48 = SN48_D.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
        print("74% Data Loaded")
        df_sn66 = SN66_D.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
        print("82% Data Loaded")
        df_sn83 = SN83_D.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
        print("91% Data Loaded")
        df_sn89 = SN89_D.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
        print("100% Data Loaded")
        print("I am here")
        if query3 == 'time':
            x_dec = df_sn89['Time']
            if query4 == 'eac_t':
                df_g2['Eac_Today'] = df_sn05['Eac_Today'] + df_sn7b['Eac_Today'] + df_sn13['Eac_Today'] + df_sn28['Eac_Today'] + df_sn33['Eac_Today'] + df_sn34['Eac_Today'] + df_sn44['Eac_Today'] \
                + df_sn48['Eac_Today'] + df_sn66['Eac_Today'] + df_sn83['Eac_Today'] + df_sn89['Eac_Today']
                
                Y = df_g2['Eac_Today']
                
                plot = figure(title= 'Time Vs Eac_Today', x_axis_type="datetime", x_axis_label= 'DATE', y_axis_label= 'ENERGY', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.line(x_dec, Y, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'vpv':
                df_g2['Vpv'] = df_sn05['Vpv'] + df_sn7b['Vpv'] + df_sn13['Vpv'] + df_sn28['Vpv'] + df_sn33['Vpv'] + df_sn34['Vpv'] + df_sn44['Vpv'] \
                + df_sn48['Vpv'] + df_sn66['Vpv'] + df_sn83['Vpv'] + df_sn89['Vpv']
                
                Y = df_g2['Vpv']
                
                plot = figure(title= 'Time Vs V pv', x_axis_type="datetime", x_axis_label= 'DATE', y_axis_label= 'PV POTENTIAL', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.line(x_dec, Y, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'ipv':
                df_g2['Ipv'] = df_sn05['Ipv'] + df_sn7b['Ipv'] + df_sn13['Ipv'] + df_sn28['Ipv'] + df_sn33['Ipv'] + df_sn34['Ipv'] + df_sn44['Ipv'] \
                + df_sn48['Ipv'] + df_sn66['Ipv'] + df_sn83['Ipv'] + df_sn89['Ipv']
                
                Y = df_g2['Ipv']
                
                plot = figure(title= 'Time Vs I pv', x_axis_type="datetime", x_axis_label= 'DATE', y_axis_label= 'PV CURRENT', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.line(x_dec, Y, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'ppv':
                df_g2['Ppv'] = df_sn05['Ppv'] + df_sn7b['Ppv'] + df_sn13['Ppv'] + df_sn28['Ppv'] + df_sn33['Ppv'] + df_sn34['Ppv'] + df_sn44['Ppv'] \
                + df_sn48['Ppv'] + df_sn66['Ppv'] + df_sn83['Ppv'] + df_sn89['Ppv']
                
                Y = df_g2['Ppv']
                
                plot = figure(title= 'Time Vs P pv', x_axis_type="datetime", x_axis_label= 'DATE', y_axis_label= 'PV POWER', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.line(x_dec, Y, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'vac':
                df_g2['Vac'] = df_sn05['Vac'] + df_sn7b['Vac'] + df_sn13['Vac'] + df_sn28['Vac'] + df_sn33['Vac'] + df_sn34['Vac'] + df_sn44['Vac'] \
                + df_sn48['Vac'] + df_sn66['Vac'] + df_sn83['Vac'] + df_sn89['Vac']
                
                Y = df_g2['Vac']
                
                plot = figure(title= 'Time Vs V ac', x_axis_type="datetime", x_axis_label= 'DATE', y_axis_label= 'AC POTENTIAL', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.line(x_dec, Y, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'iac':
                df_g2['Iac'] = df_sn05['Iac'] + df_sn7b['Iac'] + df_sn13['Iac'] + df_sn28['Iac'] + df_sn33['Iac'] + df_sn34['Iac'] + df_sn44['Iac'] \
                + df_sn48['Iac'] + df_sn66['Iac'] + df_sn83['Iac'] + df_sn89['Iac']
                
                Y = df_g2['Iac']
                
                plot = figure(title= 'Time Vs I ac', x_axis_type="datetime", x_axis_label= 'DATE', y_axis_label= 'AC CURRENT', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.line(x_dec, Y, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'pac':
                df_g2['Pac'] = df_sn05['Pac'] + df_sn7b['Pac'] + df_sn13['Pac'] + df_sn28['Pac'] + df_sn33['Pac'] + df_sn34['Pac'] + df_sn44['Pac'] \
                + df_sn48['Pac'] + df_sn66['Pac'] + df_sn83['Pac'] + df_sn89['Pac']
                
                Y = df_g2['Pac']
                
                plot = figure(title= 'Time Vs I ac', x_axis_type="datetime", x_axis_label= 'DATE', y_axis_label= 'AC POWER', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.line(x_dec, Y, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'fac':
                df_g2['Fac'] = df_sn05['Fac'] + df_sn7b['Fac'] + df_sn13['Fac'] + df_sn28['Fac'] + df_sn33['Fac'] + df_sn34['Fac'] + df_sn44['Fac'] \
                + df_sn48['Fac'] + df_sn66['Fac'] + df_sn83['Fac'] + df_sn89['Fac']
                
                Y = df_g2['Fac']
                
                plot = figure(title= 'Time Vs F ac', x_axis_type="datetime", x_axis_label= 'DATE', y_axis_label= 'AC FREQUENCY', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.line(x_dec, Y, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
        
        if query3 == 'eac_t':
            df_g2['Eac_Today'] = df_sn05['Eac_Today'] + df_sn7b['Eac_Today'] + df_sn13['Eac_Today'] + df_sn28['Eac_Today'] + df_sn33['Eac_Today'] + df_sn34['Eac_Today'] + df_sn44['Eac_Today'] \
            + df_sn48['Eac_Today'] + df_sn66['Eac_Today'] + df_sn83['Eac_Today'] + df_sn89['Eac_Today']
            x_dec = df_g2['Eac_Today']
            if query4 == 'eac_t':
                Y = df_g2['Eac_Today']
                
                plot = figure(title= 'Eac_Today Vs Eac_Today', x_axis_label= 'ENERGY', y_axis_label= 'ENERGY', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'vpv':
                df_g2['Vpv'] = df_sn05['Vpv'] + df_sn7b['Vpv'] + df_sn13['Vpv'] + df_sn28['Vpv'] + df_sn33['Vpv'] + df_sn34['Vpv'] + df_sn44['Vpv'] \
                + df_sn48['Vpv'] + df_sn66['Vpv'] + df_sn83['Vpv'] + df_sn89['Vpv']
                
                Y = df_g2['Vpv']
                
                plot = figure(title= 'Eac_Today Vs V pv', x_axis_label= 'ENERGY', y_axis_label= 'PV POTENTIAL', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'ipv':
                df_g2['Ipv'] = df_sn05['Ipv'] + df_sn7b['Ipv'] + df_sn13['Ipv'] + df_sn28['Ipv'] + df_sn33['Ipv'] + df_sn34['Ipv'] + df_sn44['Ipv'] \
                + df_sn48['Ipv'] + df_sn66['Ipv'] + df_sn83['Ipv'] + df_sn89['Ipv']
                
                Y = df_g2['Ipv']
                
                plot = figure(title= 'Eac_Today Vs I pv', x_axis_label= 'ENERGY', y_axis_label= 'PV CURRENT', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'ppv':
                df_g2['Ppv'] = df_sn05['Ppv'] + df_sn7b['Ppv'] + df_sn13['Ppv'] + df_sn28['Ppv'] + df_sn33['Ppv'] + df_sn34['Ppv'] + df_sn44['Ppv'] \
                + df_sn48['Ppv'] + df_sn66['Ppv'] + df_sn83['Ppv'] + df_sn89['Ppv']
                
                Y = df_g2['Ppv']
                
                plot = figure(title= 'Eac_Today Vs P pv', x_axis_label= 'ENERGY', y_axis_label= 'PV POWER', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'vac':
                df_g2['Vac'] = df_sn05['Vac'] + df_sn7b['Vac'] + df_sn13['Vac'] + df_sn28['Vac'] + df_sn33['Vac'] + df_sn34['Vac'] + df_sn44['Vac'] \
                + df_sn48['Vac'] + df_sn66['Vac'] + df_sn83['Vac'] + df_sn89['Vac']
                
                Y = df_g2['Vac']
                
                plot = figure(title= 'Eac_Today Vs V ac', x_axis_label= 'ENERGY', y_axis_label= 'AC POTENTIAL', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'iac':
                df_g2['Iac'] = df_sn05['Iac'] + df_sn7b['Iac'] + df_sn13['Iac'] + df_sn28['Iac'] + df_sn33['Iac'] + df_sn34['Iac'] + df_sn44['Iac'] \
                + df_sn48['Iac'] + df_sn66['Iac'] + df_sn83['Iac'] + df_sn89['Iac']
                
                Y = df_g2['Iac']
                
                plot = figure(title= 'Eac_Today Vs I ac', x_axis_label= 'ENERGY', y_axis_label= 'AC CURRENT', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'pac':
                df_g2['Pac'] = df_sn05['Pac'] + df_sn7b['Pac'] + df_sn13['Pac'] + df_sn28['Pac'] + df_sn33['Pac'] + df_sn34['Pac'] + df_sn44['Pac'] \
                + df_sn48['Pac'] + df_sn66['Pac'] + df_sn83['Pac'] + df_sn89['Pac']
                
                Y = df_g2['Pac']
                
                plot = figure(title= 'Eac_Today Vs I ac', x_axis_label= 'ENERGY', y_axis_label= 'AC POWER', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'fac':
                df_g2['Fac'] = df_sn05['Fac'] + df_sn7b['Fac'] + df_sn13['Fac'] + df_sn28['Fac'] + df_sn33['Fac'] + df_sn34['Fac'] + df_sn44['Fac'] \
                + df_sn48['Fac'] + df_sn66['Fac'] + df_sn83['Fac'] + df_sn89['Fac']
                
                Y = df_g2['Fac']
                
                plot = figure(title= 'Eac_Today Vs F ac', x_axis_label= 'ENERGY', y_axis_label= 'AC FREQUENCY', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
        
        if query3 == 'vpv':
            df_g2['Vpv'] = df_sn05['Vpv'] + df_sn7b['Vpv'] + df_sn13['Vpv'] + df_sn28['Vpv'] + df_sn33['Vpv'] + df_sn34['Vpv'] + df_sn44['Vpv'] \
            + df_sn48['Vpv'] + df_sn66['Vpv'] + df_sn83['Vpv'] + df_sn89['Vpv']
            
            x_dec = df_g2['Vpv']
            
            if query4 == 'eac_t':
                df_g2['Eac_Today'] = df_sn05['Eac_Today'] + df_sn7b['Eac_Today'] + df_sn13['Eac_Today'] + df_sn28['Eac_Today'] + df_sn33['Eac_Today'] + df_sn34['Eac_Today'] + df_sn44['Eac_Today'] \
                + df_sn48['Eac_Today'] + df_sn66['Eac_Today'] + df_sn83['Eac_Today'] + df_sn89['Eac_Today']
                
                Y = df_g2['Eac_Today']
                
                plot = figure(title= 'V pv Vs Eac_Today', x_axis_label= 'PV POTENTIAL', y_axis_label= 'ENERGY', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'vpv':
                Y = df_g2['Vpv']
                
                plot = figure(title= 'V pv Vs V pv', x_axis_label= 'PV POTENTIAL', y_axis_label= 'PV POTENTIAL', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'ipv':
                df_g2['Ipv'] = df_sn05['Ipv'] + df_sn7b['Ipv'] + df_sn13['Ipv'] + df_sn28['Ipv'] + df_sn33['Ipv'] + df_sn34['Ipv'] + df_sn44['Ipv'] \
                + df_sn48['Ipv'] + df_sn66['Ipv'] + df_sn83['Ipv'] + df_sn89['Ipv']
                
                Y = df_g2['Ipv']
                
                plot = figure(title= 'V pv Vs I pv', x_axis_label= 'PV POTENTIAL', y_axis_label= 'PV CURRENT', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'ppv':
                df_g2['Ppv'] = df_sn05['Ppv'] + df_sn7b['Ppv'] + df_sn13['Ppv'] + df_sn28['Ppv'] + df_sn33['Ppv'] + df_sn34['Ppv'] + df_sn44['Ppv'] \
                + df_sn48['Ppv'] + df_sn66['Ppv'] + df_sn83['Ppv'] + df_sn89['Ppv']
                
                Y = df_g2['Ppv']
                
                plot = figure(title= 'V pv Vs P pv', x_axis_label= 'PV POTENTIAL', y_axis_label= 'PV POWER', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'vac':
                df_g2['Vac'] = df_sn05['Vac'] + df_sn7b['Vac'] + df_sn13['Vac'] + df_sn28['Vac'] + df_sn33['Vac'] + df_sn34['Vac'] + df_sn44['Vac'] \
                + df_sn48['Vac'] + df_sn66['Vac'] + df_sn83['Vac'] + df_sn89['Vac']
                
                Y = df_g2['Vac']
                
                plot = figure(title= 'V pv Vs V ac', x_axis_label= 'PV POTENTIAL', y_axis_label= 'AC POTENTIAL', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'iac':
                df_g2['Iac'] = df_sn05['Iac'] + df_sn7b['Iac'] + df_sn13['Iac'] + df_sn28['Iac'] + df_sn33['Iac'] + df_sn34['Iac'] + df_sn44['Iac'] \
                + df_sn48['Iac'] + df_sn66['Iac'] + df_sn83['Iac'] + df_sn89['Iac']
                
                Y = df_g2['Iac']
                
                plot = figure(title= 'V pv Vs I ac', x_axis_label= 'PV POTENTIAL', y_axis_label= 'AC CURRENT', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'pac':
                df_g2['Pac'] = df_sn05['Pac'] + df_sn7b['Pac'] + df_sn13['Pac'] + df_sn28['Pac'] + df_sn33['Pac'] + df_sn34['Pac'] + df_sn44['Pac'] \
                + df_sn48['Pac'] + df_sn66['Pac'] + df_sn83['Pac'] + df_sn89['Pac']
                
                Y = df_g2['Pac']
                
                plot = figure(title= 'V pv Vs I ac', x_axis_label= 'PV POTENTIAL', y_axis_label= 'AC POWER', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'fac':
                df_g2['Fac'] = df_sn05['Fac'] + df_sn7b['Fac'] + df_sn13['Fac'] + df_sn28['Fac'] + df_sn33['Fac'] + df_sn34['Fac'] + df_sn44['Fac'] \
                + df_sn48['Fac'] + df_sn66['Fac'] + df_sn83['Fac'] + df_sn89['Fac']
                
                Y = df_g2['Fac']
                
                plot = figure(title= 'V pv Vs F ac', x_axis_label= 'PV POTENTIAL', y_axis_label= 'AC FREQUENCY', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
        
        if query3 == 'ipv':
            
            df_g2['Ipv'] = df_sn05['Ipv'] + df_sn7b['Ipv'] + df_sn13['Ipv'] + df_sn28['Ipv'] + df_sn33['Ipv'] + df_sn34['Ipv'] + df_sn44['Ipv'] \
                + df_sn48['Ipv'] + df_sn66['Ipv'] + df_sn83['Ipv'] + df_sn89['Ipv']
            
            x_dec = df_g2['Ipv']
            
            if query4 == 'eac_t':
                df_g2['Eac_Today'] = df_sn05['Eac_Today'] + df_sn7b['Eac_Today'] + df_sn13['Eac_Today'] + df_sn28['Eac_Today'] + df_sn33['Eac_Today'] + df_sn34['Eac_Today'] + df_sn44['Eac_Today'] \
                + df_sn48['Eac_Today'] + df_sn66['Eac_Today'] + df_sn83['Eac_Today'] + df_sn89['Eac_Today']
                
                Y = df_g2['Eac_Today']
                
                plot = figure(title= 'I pv Vs Eac_Today', x_axis_label= 'PV CURRENT', y_axis_label= 'ENERGY', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'vpv':
                df_g2['Vpv'] = df_sn05['Vpv'] + df_sn7b['Vpv'] + df_sn13['Vpv'] + df_sn28['Vpv'] + df_sn33['Vpv'] + df_sn34['Vpv'] + df_sn44['Vpv'] \
                + df_sn48['Vpv'] + df_sn66['Vpv'] + df_sn83['Vpv'] + df_sn89['Vpv']
                
                Y = df_g2['Vpv']
                
                plot = figure(title= 'I pv Vs V pv', x_axis_label= 'PV CURRENT', y_axis_label= 'PV POTENTIAL', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'ipv':
                              
                Y = df_g2['Ipv']
                
                plot = figure(title= 'I pv Vs I pv', x_axis_label= 'PV CURRENT', y_axis_label= 'PV CURRENT', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'ppv':
                df_g2['Ppv'] = df_sn05['Ppv'] + df_sn7b['Ppv'] + df_sn13['Ppv'] + df_sn28['Ppv'] + df_sn33['Ppv'] + df_sn34['Ppv'] + df_sn44['Ppv'] \
                + df_sn48['Ppv'] + df_sn66['Ppv'] + df_sn83['Ppv'] + df_sn89['Ppv']
                
                Y = df_g2['Ppv']
                
                plot = figure(title= 'I pv Vs P pv', x_axis_label= 'PV CURRENT', y_axis_label= 'PV POWER', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'vac':
                df_g2['Vac'] = df_sn05['Vac'] + df_sn7b['Vac'] + df_sn13['Vac'] + df_sn28['Vac'] + df_sn33['Vac'] + df_sn34['Vac'] + df_sn44['Vac'] \
                + df_sn48['Vac'] + df_sn66['Vac'] + df_sn83['Vac'] + df_sn89['Vac']
                
                Y = df_g2['Vac']
                
                plot = figure(title= 'I pv Vs V ac', x_axis_label= 'PV CURRENT', y_axis_label= 'AC POTENTIAL', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'iac':
                df_g2['Iac'] = df_sn05['Iac'] + df_sn7b['Iac'] + df_sn13['Iac'] + df_sn28['Iac'] + df_sn33['Iac'] + df_sn34['Iac'] + df_sn44['Iac'] \
                + df_sn48['Iac'] + df_sn66['Iac'] + df_sn83['Iac'] + df_sn89['Iac']
                
                Y = df_g2['Iac']
                
                plot = figure(title= 'I pv Vs I ac', x_axis_label= 'PV CURRENT', y_axis_label= 'AC CURRENT', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'pac':
                df_g2['Pac'] = df_sn05['Pac'] + df_sn7b['Pac'] + df_sn13['Pac'] + df_sn28['Pac'] + df_sn33['Pac'] + df_sn34['Pac'] + df_sn44['Pac'] \
                + df_sn48['Pac'] + df_sn66['Pac'] + df_sn83['Pac'] + df_sn89['Pac']
                
                Y = df_g2['Pac']
                
                plot = figure(title= 'I pv Vs I ac', x_axis_label= 'PV CURRENT', y_axis_label= 'AC POWER', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'fac':
                df_g2['Fac'] = df_sn05['Fac'] + df_sn7b['Fac'] + df_sn13['Fac'] + df_sn28['Fac'] + df_sn33['Fac'] + df_sn34['Fac'] + df_sn44['Fac'] \
                + df_sn48['Fac'] + df_sn66['Fac'] + df_sn83['Fac'] + df_sn89['Fac']
                
                Y = df_g2['Fac']
                
                plot = figure(title= 'I pv Vs F ac', x_axis_label= 'PV CURRENT', y_axis_label= 'AC FREQUENCY', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
        
        if query3 == 'ppv':
            df_g2['Ppv'] = df_sn05['Ppv'] + df_sn7b['Ppv'] + df_sn13['Ppv'] + df_sn28['Ppv'] + df_sn33['Ppv'] + df_sn34['Ppv'] + df_sn44['Ppv'] \
            + df_sn48['Ppv'] + df_sn66['Ppv'] + df_sn83['Ppv'] + df_sn89['Ppv']
            
            x_dec = df_g2['Ppv']
            
            if query4 == 'eac_t':
                df_g2['Eac_Today'] = df_sn05['Eac_Today'] + df_sn7b['Eac_Today'] + df_sn13['Eac_Today'] + df_sn28['Eac_Today'] + df_sn33['Eac_Today'] + df_sn34['Eac_Today'] + df_sn44['Eac_Today'] \
                + df_sn48['Eac_Today'] + df_sn66['Eac_Today'] + df_sn83['Eac_Today'] + df_sn89['Eac_Today']
                
                Y = df_g2['Eac_Today']
                
                plot = figure(title= 'P pv Vs Eac_Today', x_axis_label= 'PV POWER', y_axis_label= 'ENERGY', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'vpv':
                df_g2['Vpv'] = df_sn05['Vpv'] + df_sn7b['Vpv'] + df_sn13['Vpv'] + df_sn28['Vpv'] + df_sn33['Vpv'] + df_sn34['Vpv'] + df_sn44['Vpv'] \
                + df_sn48['Vpv'] + df_sn66['Vpv'] + df_sn83['Vpv'] + df_sn89['Vpv']
                
                Y = df_g2['Vpv']
                
                plot = figure(title= 'P pv Vs V pv', x_axis_label= 'PV POWER', y_axis_label= 'PV POTENTIAL', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'ipv':
                df_g2['Ipv'] = df_sn05['Ipv'] + df_sn7b['Ipv'] + df_sn13['Ipv'] + df_sn28['Ipv'] + df_sn33['Ipv'] + df_sn34['Ipv'] + df_sn44['Ipv'] \
                + df_sn48['Ipv'] + df_sn66['Ipv'] + df_sn83['Ipv'] + df_sn89['Ipv']
                
                Y = df_g2['Ipv']
                
                plot = figure(title= 'P pv Vs I pv', x_axis_label= 'PV POWER', y_axis_label= 'PV CURRENT', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'ppv':
                                
                Y = df_g2['Ppv']
                
                plot = figure(title= 'P pv Vs P pv', x_axis_label= 'PV POWER', y_axis_label= 'PV POWER', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
            
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'vac':
                df_g2['Vac'] = df_sn05['Vac'] + df_sn7b['Vac'] + df_sn13['Vac'] + df_sn28['Vac'] + df_sn33['Vac'] + df_sn34['Vac'] + df_sn44['Vac'] \
                + df_sn48['Vac'] + df_sn66['Vac'] + df_sn83['Vac'] + df_sn89['Vac']
                
                Y = df_g2['Vac']
                
                plot = figure(title= 'P pv Vs V ac', x_axis_label= 'PV POWER', y_axis_label= 'AC POTENTIAL', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'iac':
                df_g2['Iac'] = df_sn05['Iac'] + df_sn7b['Iac'] + df_sn13['Iac'] + df_sn28['Iac'] + df_sn33['Iac'] + df_sn34['Iac'] + df_sn44['Iac'] \
                + df_sn48['Iac'] + df_sn66['Iac'] + df_sn83['Iac'] + df_sn89['Iac']
                
                Y = df_g2['Iac']
                
                plot = figure(title= 'P pv Vs I ac', x_axis_label= 'PV POWER', y_axis_label= 'AC CURRENT', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'pac':
                df_g2['Pac'] = df_sn05['Pac'] + df_sn7b['Pac'] + df_sn13['Pac'] + df_sn28['Pac'] + df_sn33['Pac'] + df_sn34['Pac'] + df_sn44['Pac'] \
                + df_sn48['Pac'] + df_sn66['Pac'] + df_sn83['Pac'] + df_sn89['Pac']
                
                Y = df_g2['Pac']
                
                plot = figure(title= 'P pv Vs I ac', x_axis_label= 'PV POWER', y_axis_label= 'AC POWER', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'fac':
                df_g2['Fac'] = df_sn05['Fac'] + df_sn7b['Fac'] + df_sn13['Fac'] + df_sn28['Fac'] + df_sn33['Fac'] + df_sn34['Fac'] + df_sn44['Fac'] \
                + df_sn48['Fac'] + df_sn66['Fac'] + df_sn83['Fac'] + df_sn89['Fac']
                
                Y = df_g2['Fac']
                
                plot = figure(title= 'P pv Vs F ac', x_axis_label= 'PV POWER', y_axis_label= 'AC FREQUENCY', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
        
        if query3 == 'vac':
            df_g2['Vac'] = df_sn05['Vac'] + df_sn7b['Vac'] + df_sn13['Vac'] + df_sn28['Vac'] + df_sn33['Vac'] + df_sn34['Vac'] + df_sn44['Vac'] \
            + df_sn48['Vac'] + df_sn66['Vac'] + df_sn83['Vac'] + df_sn89['Vac']
            
            x_dec = df_g2['Vac']
            
            if query4 == 'eac_t':
                df_g2['Eac_Today'] = df_sn05['Eac_Today'] + df_sn7b['Eac_Today'] + df_sn13['Eac_Today'] + df_sn28['Eac_Today'] + df_sn33['Eac_Today'] + df_sn34['Eac_Today'] + df_sn44['Eac_Today'] \
                + df_sn48['Eac_Today'] + df_sn66['Eac_Today'] + df_sn83['Eac_Today'] + df_sn89['Eac_Today']
                
                Y = df_g2['Eac_Today']
                
                plot = figure(title= 'V ac Vs Eac_Today', x_axis_label= 'AC POTENTIAL', y_axis_label= 'ENERGY', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'vpv':
                df_g2['Vpv'] = df_sn05['Vpv'] + df_sn7b['Vpv'] + df_sn13['Vpv'] + df_sn28['Vpv'] + df_sn33['Vpv'] + df_sn34['Vpv'] + df_sn44['Vpv'] \
                + df_sn48['Vpv'] + df_sn66['Vpv'] + df_sn83['Vpv'] + df_sn89['Vpv']
                
                Y = df_g2['Vpv']
                
                plot = figure(title= 'V ac Vs V pv', x_axis_label= 'AC POTENTIAL', y_axis_label= 'PV POTENTIAL', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'ipv':
                df_g2['Ipv'] = df_sn05['Ipv'] + df_sn7b['Ipv'] + df_sn13['Ipv'] + df_sn28['Ipv'] + df_sn33['Ipv'] + df_sn34['Ipv'] + df_sn44['Ipv'] \
                + df_sn48['Ipv'] + df_sn66['Ipv'] + df_sn83['Ipv'] + df_sn89['Ipv']
                
                Y = df_g2['Ipv']
                
                plot = figure(title= 'V ac Vs I pv', x_axis_label= 'AC POTENTIAL', y_axis_label= 'PV CURRENT', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'ppv':
                df_g2['Ppv'] = df_sn05['Ppv'] + df_sn7b['Ppv'] + df_sn13['Ppv'] + df_sn28['Ppv'] + df_sn33['Ppv'] + df_sn34['Ppv'] + df_sn44['Ppv'] \
                + df_sn48['Ppv'] + df_sn66['Ppv'] + df_sn83['Ppv'] + df_sn89['Ppv']
                                
                Y = df_g2['Ppv']
                
                plot = figure(title= 'V ac Vs P pv', x_axis_label= 'AC POTENTIAL', y_axis_label= 'PV POWER', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'vac':
                               
                Y = df_g2['Vac']
                
                plot = figure(title= 'V ac Vs V ac', x_axis_label= 'AC POTENTIAL', y_axis_label= 'AC POTENTIAL', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'iac':
                df_g2['Iac'] = df_sn05['Iac'] + df_sn7b['Iac'] + df_sn13['Iac'] + df_sn28['Iac'] + df_sn33['Iac'] + df_sn34['Iac'] + df_sn44['Iac'] \
                + df_sn48['Iac'] + df_sn66['Iac'] + df_sn83['Iac'] + df_sn89['Iac']
                
                Y = df_g2['Iac']
                
                plot = figure(title= 'V ac Vs I ac', x_axis_label= 'AC POTENTIAL', y_axis_label= 'AC CURRENT', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'pac':
                df_g2['Pac'] = df_sn05['Pac'] + df_sn7b['Pac'] + df_sn13['Pac'] + df_sn28['Pac'] + df_sn33['Pac'] + df_sn34['Pac'] + df_sn44['Pac'] \
                + df_sn48['Pac'] + df_sn66['Pac'] + df_sn83['Pac'] + df_sn89['Pac']
                
                Y = df_g2['Pac']
                
                plot = figure(title= 'V ac Vs I ac', x_axis_label= 'AC POTENTIAL', y_axis_label= 'AC POWER', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'fac':
                df_g2['Fac'] = df_sn05['Fac'] + df_sn7b['Fac'] + df_sn13['Fac'] + df_sn28['Fac'] + df_sn33['Fac'] + df_sn34['Fac'] + df_sn44['Fac'] \
                + df_sn48['Fac'] + df_sn66['Fac'] + df_sn83['Fac'] + df_sn89['Fac']
                
                Y = df_g2['Fac']
                
                plot = figure(title= 'V ac Vs F ac', x_axis_label= 'AC POTENTIAL', y_axis_label= 'AC FREQUENCY', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))


        if query3 == 'iac':
            df_g2['Iac'] = df_sn05['Iac'] + df_sn7b['Iac'] + df_sn13['Iac'] + df_sn28['Iac'] + df_sn33['Iac'] + df_sn34['Iac'] + df_sn44['Iac'] \
            + df_sn48['Iac'] + df_sn66['Iac'] + df_sn83['Iac'] + df_sn89['Iac']            
            x_dec = df_g2['Iac']
            
            if query4 == 'eac_t':
                df_g2['Eac_Today'] = df_sn05['Eac_Today'] + df_sn7b['Eac_Today'] + df_sn13['Eac_Today'] + df_sn28['Eac_Today'] + df_sn33['Eac_Today'] + df_sn34['Eac_Today'] + df_sn44['Eac_Today'] \
                + df_sn48['Eac_Today'] + df_sn66['Eac_Today'] + df_sn83['Eac_Today'] + df_sn89['Eac_Today']
                
                Y = df_g2['Eac_Today']
                
                plot = figure(title= 'I ac Vs Eac_Today', x_axis_label= 'AC CURRENT', y_axis_label= 'ENERGY', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'vpv':
                df_g2['Vpv'] = df_sn05['Vpv'] + df_sn7b['Vpv'] + df_sn13['Vpv'] + df_sn28['Vpv'] + df_sn33['Vpv'] + df_sn34['Vpv'] + df_sn44['Vpv'] \
                + df_sn48['Vpv'] + df_sn66['Vpv'] + df_sn83['Vpv'] + df_sn89['Vpv']
                
                Y = df_g2['Vpv']
                
                plot = figure(title= 'I ac Vs V pv', x_axis_label= 'AC CURRENT', y_axis_label= 'PV POTENTIAL', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'ipv':
                df_g2['Ipv'] = df_sn05['Ipv'] + df_sn7b['Ipv'] + df_sn13['Ipv'] + df_sn28['Ipv'] + df_sn33['Ipv'] + df_sn34['Ipv'] + df_sn44['Ipv'] \
                + df_sn48['Ipv'] + df_sn66['Ipv'] + df_sn83['Ipv'] + df_sn89['Ipv']
                
                Y = df_g2['Ipv']
                
                plot = figure(title= 'I ac Vs I pv', x_axis_label= 'AC CURRENT', y_axis_label= 'PV CURRENT', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'ppv':
                df_g2['Ppv'] = df_sn05['Ppv'] + df_sn7b['Ppv'] + df_sn13['Ppv'] + df_sn28['Ppv'] + df_sn33['Ppv'] + df_sn34['Ppv'] + df_sn44['Ppv'] \
                + df_sn48['Ppv'] + df_sn66['Ppv'] + df_sn83['Ppv'] + df_sn89['Ppv']
                                
                Y = df_g2['Ppv']
                
                plot = figure(title= 'I ac Vs P pv', x_axis_label= 'AC CURRENT', y_axis_label= 'PV POWER', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'vac':
                df_g2['Vac'] = df_sn05['Vac'] + df_sn7b['Vac'] + df_sn13['Vac'] + df_sn28['Vac'] + df_sn33['Vac'] + df_sn34['Vac'] + df_sn44['Vac'] \
                + df_sn48['Vac'] + df_sn66['Vac'] + df_sn83['Vac'] + df_sn89['Vac']
                
                Y = df_g2['Vac']
                
                plot = figure(title= 'I ac Vs V ac', x_axis_label= 'AC CURRENT', y_axis_label= 'AC POTENTIAL', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'iac':
                                
                Y = df_g2['Iac']
                
                plot = figure(title= 'I ac Vs I ac', x_axis_label= 'AC CURRENT', y_axis_label= 'AC CURRENT', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'pac':
                df_g2['Pac'] = df_sn05['Pac'] + df_sn7b['Pac'] + df_sn13['Pac'] + df_sn28['Pac'] + df_sn33['Pac'] + df_sn34['Pac'] + df_sn44['Pac'] \
                + df_sn48['Pac'] + df_sn66['Pac'] + df_sn83['Pac'] + df_sn89['Pac']
                
                Y = df_g2['Pac']
                
                plot = figure(title= 'I ac Vs I ac', x_axis_label= 'AC CURRENT', y_axis_label= 'AC POWER', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'fac':
                df_g2['Fac'] = df_sn05['Fac'] + df_sn7b['Fac'] + df_sn13['Fac'] + df_sn28['Fac'] + df_sn33['Fac'] + df_sn34['Fac'] + df_sn44['Fac'] \
                + df_sn48['Fac'] + df_sn66['Fac'] + df_sn83['Fac'] + df_sn89['Fac']
                
                Y = df_g2['Fac']
                
                plot = figure(title= 'I ac Vs F ac', x_axis_label= 'AC CURRENT', y_axis_label= 'AC FREQUENCY', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
        
        if query3 == 'pac':
            df_g2['Pac'] = df_sn05['Pac'] + df_sn7b['Pac'] + df_sn13['Pac'] + df_sn28['Pac'] + df_sn33['Pac'] + df_sn34['Pac'] + df_sn44['Pac'] \
            + df_sn48['Pac'] + df_sn66['Pac'] + df_sn83['Pac'] + df_sn89['Pac']
                        
            x_dec = df_g2['Pac']
            
            if query4 == 'eac_t':
                df_g2['Eac_Today'] = df_sn05['Eac_Today'] + df_sn7b['Eac_Today'] + df_sn13['Eac_Today'] + df_sn28['Eac_Today'] + df_sn33['Eac_Today'] + df_sn34['Eac_Today'] + df_sn44['Eac_Today'] \
                + df_sn48['Eac_Today'] + df_sn66['Eac_Today'] + df_sn83['Eac_Today'] + df_sn89['Eac_Today']
                
                Y = df_g2['Eac_Today']
                
                plot = figure(title= 'P ac Vs Eac_Today', x_axis_label= 'AC POWER', y_axis_label= 'ENERGY', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'vpv':
                df_g2['Vpv'] = df_sn05['Vpv'] + df_sn7b['Vpv'] + df_sn13['Vpv'] + df_sn28['Vpv'] + df_sn33['Vpv'] + df_sn34['Vpv'] + df_sn44['Vpv'] \
                + df_sn48['Vpv'] + df_sn66['Vpv'] + df_sn83['Vpv'] + df_sn89['Vpv']
                
                Y = df_g2['Vpv']
                
                plot = figure(title= 'P ac Vs V pv', x_axis_label= 'AC POWER', y_axis_label= 'PV POTENTIAL', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'ipv':
                df_g2['Ipv'] = df_sn05['Ipv'] + df_sn7b['Ipv'] + df_sn13['Ipv'] + df_sn28['Ipv'] + df_sn33['Ipv'] + df_sn34['Ipv'] + df_sn44['Ipv'] \
                + df_sn48['Ipv'] + df_sn66['Ipv'] + df_sn83['Ipv'] + df_sn89['Ipv']
                
                Y = df_g2['Ipv']
                
                plot = figure(title= 'P ac Vs I pv', x_axis_label= 'AC POWER', y_axis_label= 'PV CURRENT', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'ppv':
                df_g2['Ppv'] = df_sn05['Ppv'] + df_sn7b['Ppv'] + df_sn13['Ppv'] + df_sn28['Ppv'] + df_sn33['Ppv'] + df_sn34['Ppv'] + df_sn44['Ppv'] \
                + df_sn48['Ppv'] + df_sn66['Ppv'] + df_sn83['Ppv'] + df_sn89['Ppv']
                                
                Y = df_g2['Ppv']
                
                plot = figure(title= 'P ac Vs P pv', x_axis_label= 'AC POWER', y_axis_label= 'PV POWER', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'vac':
                df_g2['Vac'] = df_sn05['Vac'] + df_sn7b['Vac'] + df_sn13['Vac'] + df_sn28['Vac'] + df_sn33['Vac'] + df_sn34['Vac'] + df_sn44['Vac'] \
                + df_sn48['Vac'] + df_sn66['Vac'] + df_sn83['Vac'] + df_sn89['Vac']
                
                Y = df_g2['Vac']
                
                plot = figure(title= 'P ac Vs V ac', x_axis_label= 'AC POWER', y_axis_label= 'AC POTENTIAL', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'iac':
                df_g2['Iac'] = df_sn05['Iac'] + df_sn7b['Iac'] + df_sn13['Iac'] + df_sn28['Iac'] + df_sn33['Iac'] + df_sn34['Iac'] + df_sn44['Iac'] \
                + df_sn48['Iac'] + df_sn66['Iac'] + df_sn83['Iac'] + df_sn89['Iac']
                                
                Y = df_g2['Iac']
                
                plot = figure(title= 'P ac Vs I ac', x_axis_label= 'AC POWER', y_axis_label= 'AC CURRENT', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'pac':
                                
                Y = df_g2['Pac']
                
                plot = figure(title= 'P ac Vs I ac', x_axis_label= 'AC POWER', y_axis_label= 'AC POWER', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'fac':
                df_g2['Fac'] = df_sn05['Fac'] + df_sn7b['Fac'] + df_sn13['Fac'] + df_sn28['Fac'] + df_sn33['Fac'] + df_sn34['Fac'] + df_sn44['Fac'] \
                + df_sn48['Fac'] + df_sn66['Fac'] + df_sn83['Fac'] + df_sn89['Fac']
                
                Y = df_g2['Fac']
                
                plot = figure(title= 'P ac Vs F ac', x_axis_label= 'AC POWER', y_axis_label= 'AC FREQUENCY', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
    
        if query3 == 'fac':
            df_g2['Fac'] = df_sn05['Fac'] + df_sn7b['Fac'] + df_sn13['Fac'] + df_sn28['Fac'] + df_sn33['Fac'] + df_sn34['Fac'] + df_sn44['Fac'] \
            + df_sn48['Fac'] + df_sn66['Fac'] + df_sn83['Fac'] + df_sn89['Fac']
                        
            x_dec = df_g2['Fac']
            
            if query4 == 'eac_t':
                df_g2['Eac_Today'] = df_sn05['Eac_Today'] + df_sn7b['Eac_Today'] + df_sn13['Eac_Today'] + df_sn28['Eac_Today'] + df_sn33['Eac_Today'] + df_sn34['Eac_Today'] + df_sn44['Eac_Today'] \
                + df_sn48['Eac_Today'] + df_sn66['Eac_Today'] + df_sn83['Eac_Today'] + df_sn89['Eac_Today']
                
                Y = df_g2['Eac_Today']
                
                plot = figure(title= 'F ac Vs Eac_Today', x_axis_label= 'AC FREQUENCY', y_axis_label= 'ENERGY', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'vpv':
                df_g2['Vpv'] = df_sn05['Vpv'] + df_sn7b['Vpv'] + df_sn13['Vpv'] + df_sn28['Vpv'] + df_sn33['Vpv'] + df_sn34['Vpv'] + df_sn44['Vpv'] \
                + df_sn48['Vpv'] + df_sn66['Vpv'] + df_sn83['Vpv'] + df_sn89['Vpv']
                
                Y = df_g2['Vpv']
                
                plot = figure(title= 'F ac Vs V pv', x_axis_label= 'AC FREQUENCY', y_axis_label= 'PV POTENTIAL', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'ipv':
                df_g2['Ipv'] = df_sn05['Ipv'] + df_sn7b['Ipv'] + df_sn13['Ipv'] + df_sn28['Ipv'] + df_sn33['Ipv'] + df_sn34['Ipv'] + df_sn44['Ipv'] \
                + df_sn48['Ipv'] + df_sn66['Ipv'] + df_sn83['Ipv'] + df_sn89['Ipv']
                
                Y = df_g2['Ipv']
                
                plot = figure(title= 'F ac Vs I pv', x_axis_label= 'AC FREQUENCY', y_axis_label= 'PV CURRENT', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'ppv':
                df_g2['Ppv'] = df_sn05['Ppv'] + df_sn7b['Ppv'] + df_sn13['Ppv'] + df_sn28['Ppv'] + df_sn33['Ppv'] + df_sn34['Ppv'] + df_sn44['Ppv'] \
                + df_sn48['Ppv'] + df_sn66['Ppv'] + df_sn83['Ppv'] + df_sn89['Ppv']
                                
                Y = df_g2['Ppv']
                
                plot = figure(title= 'F ac Vs P pv', x_axis_label= 'AC FREQUENCY', y_axis_label= 'PV POWER', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'vac':
                df_g2['Vac'] = df_sn05['Vac'] + df_sn7b['Vac'] + df_sn13['Vac'] + df_sn28['Vac'] + df_sn33['Vac'] + df_sn34['Vac'] + df_sn44['Vac'] \
                + df_sn48['Vac'] + df_sn66['Vac'] + df_sn83['Vac'] + df_sn89['Vac']
                
                Y = df_g2['Vac']
                
                plot = figure(title= 'F ac Vs V ac', x_axis_label= 'AC FREQUENCY', y_axis_label= 'AC POTENTIAL', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'iac':
                df_g2['Iac'] = df_sn05['Iac'] + df_sn7b['Iac'] + df_sn13['Iac'] + df_sn28['Iac'] + df_sn33['Iac'] + df_sn34['Iac'] + df_sn44['Iac'] \
                + df_sn48['Iac'] + df_sn66['Iac'] + df_sn83['Iac'] + df_sn89['Iac']
                                
                Y = df_g2['Iac']
                
                plot = figure(title= 'F ac Vs I ac', x_axis_label= 'AC FREQUENCY', y_axis_label= 'AC CURRENT', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'pac':
                df_g2['Pac'] = df_sn05['Pac'] + df_sn7b['Pac'] + df_sn13['Pac'] + df_sn28['Pac'] + df_sn33['Pac'] + df_sn34['Pac'] + df_sn44['Pac'] \
                + df_sn48['Pac'] + df_sn66['Pac'] + df_sn83['Pac'] + df_sn89['Pac']
                                
                Y = df_g2['Pac']
                
                plot = figure(title= 'F ac Vs I ac', x_axis_label= 'AC FREQUENCY', y_axis_label= 'AC POWER', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))
            
            elif query4 == 'fac':
                                
                Y = df_g2['Fac']
                
                plot = figure(title= 'F ac Vs F ac', x_axis_label= 'AC FREQUENCY', y_axis_label= 'AC FREQUENCY', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.circle(x_dec, Y, size=3, color='navy')
                
                #Store components 
                print("I am here 2")
                cache.set('graph_2_data', components(plot, CDN))            
    print("I am here 3")
    script_2, div_2 = cache.get('graph_2_data')
    #cache.get('abcd') == None
    if 0==0:
        if query1 == "day":
            df = pd.DataFrame()
            df_sn05 = SN05_D.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
            print("8% Data Loaded")
            df_sn7b = SN7B_D.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
            print("16% Data Loaded")
            df_sn13 = SN13_D.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
            print("25% Data Loaded")
            df_sn15 = SN15_D.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
            print("33% Data Loaded")
            df_sn28 = SN28_D.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
            print("41% Data Loaded")
            df_sn33 = SN33_D.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
            print("50% Data Loaded")
            df_sn34 = SN34_D.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
            print("58% Data Loaded")
            df_sn44 = SN44_D.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
            print("66% Data Loaded")
            df_sn48 = SN48_D.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
            print("74% Data Loaded")
            df_sn66 = SN66_D.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
            print("82% Data Loaded")
            df_sn83 = SN83_D.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
            print("91% Data Loaded")
            df_sn89 = SN89_D.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
            print("100% Data Loaded")
            print("I am here")
            
            x_dec = df_sn89['Time']
            
            df['Eac_Today'] = df_sn05['Eac_Today'] + df_sn7b['Eac_Today'] + df_sn13['Eac_Today'] + df_sn28['Eac_Today'] + df_sn33['Eac_Today'] + df_sn34['Eac_Today'] + df_sn44['Eac_Today'] \
            + df_sn48['Eac_Today'] + df_sn66['Eac_Today'] + df_sn83['Eac_Today'] + df_sn89['Eac_Today']
            #df['Eac_Today'] = df.fillna(0).add(df_sn15['Eac_Today'], axis = 'index')
            if query2 == 'cuf':
                df['Eac_Today'] = df['Eac_Today'] / (decimal.Decimal('2920') * decimal.Decimal('24.0000'))
                #df.Eac_Today = df.Eac_Today.divide(decimal.Decimal(24.0000))
                Y = df['Eac_Today']
                print(x_dec)
                print(Y)
                plot = figure(title= 'Capacity Utilsation Factor', x_axis_type="datetime", x_axis_label= 'DATE', y_axis_label= 'C. U. F.', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.vbar(x=x_dec, top=Y, width=0.2, color='navy')
                
                #hover = plot.select(dict(type=HoverTool))
                #hover.tooltips = [('x', '@x'),('y', '@y')]
                
                #Store components 
                print("I am here 2")
                cache.set('graph_1_data', components(plot, CDN))
            elif query2 == 'fy':
                df['Eac_Today'] = df['Eac_Today'] / (decimal.Decimal('2920'))
                Y = df['Eac_Today']           
                
                plot = figure(title= 'DATE vs FINAL YEILD', x_axis_type="datetime", x_axis_label= 'DATE', y_axis_label= 'FINAL YEILD.', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.vbar(x=x_dec, top=Y, width=0.2, color='navy')
                
                
                print('Final Yeild')
                cache.set('graph_1_data', components(plot, CDN))
        elif query1 == 'month':
            df = pd.DataFrame()
            df_sn05 = SN05_M.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
            print("8% Data Loaded")
            df_sn7b = SN7B_M.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
            print("16% Data Loaded")
            df_sn13 = SN13_M.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
            print("25% Data Loaded")
            df_sn15 = SN15_M.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
            print("33% Data Loaded")
            df_sn28 = SN28_M.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
            print("41% Data Loaded")
            df_sn33 = SN33_M.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
            print("50% Data Loaded")
            df_sn34 = SN34_M.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
            print("58% Data Loaded")
            df_sn44 = SN44_M.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
            print("66% Data Loaded")
            df_sn48 = SN48_M.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
            print("74% Data Loaded")
            df_sn66 = SN66_M.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
            print("82% Data Loaded")
            df_sn83 = SN83_M.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
            print("91% Data Loaded")
            df_sn89 = SN89_M.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
            print("100% Data Loaded")
            print("I am here")
            
            x_dec = df_sn89['Time']
            df['days'] = df_sn89['Time'].dt.date
            
            df['Eac_Today'] = df_sn05['Eac_Today'] + df_sn7b['Eac_Today'] + df_sn13['Eac_Today'] + df_sn15['Eac_Today']+ df_sn28['Eac_Today'] + df_sn33['Eac_Today'] + df_sn34['Eac_Today'] + df_sn44['Eac_Today'] \
            + df_sn48['Eac_Today'] + df_sn66['Eac_Today'] + df_sn83['Eac_Today'] + df_sn89['Eac_Today']

            if query2 == 'cuf':
                df['Eac_Today'] = df['Eac_Today'] / (decimal.Decimal('2920') * decimal.Decimal('24.0000') * decimal.Decimal('30'))
                
                Y = df['Eac_Today']
                print(x_dec)
                print(Y)
                plot = figure(title= 'Capacity Utilsation Factor', x_axis_type="datetime", x_axis_label= 'MONTH', y_axis_label= 'C. U. F.', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.vbar(x=x_dec, top=Y, width=0.4, line_width=1, color='navy')
                
                #hover = plot.select(dict(type=HoverTool))
                #hover.tooltips = [('x', '@x'),('y', '@y')]
                
                #Store components 
                print("I am here 2")
                cache.set('graph_1_data', components(plot, CDN))
            elif query2 == 'fy':
                df['Eac_Today'] = df['Eac_Today'] / (decimal.Decimal('2920'))
                
                Y = df['Eac_Today']
                plot = figure(title= 'MONTH vs FINAL YIELD', x_axis_type="datetime", x_axis_label= 'MONTH', y_axis_label= 'FINAL YIELD', plot_width =700, plot_height =350)
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.vbar(x=x_dec, top=Y, width=0.4, line_width=1, color='navy')
                
                #hover = plot.select(dict(type=HoverTool))
                #hover.tooltips = [('x', '@x'),('y', '@y')]
                
                #Store components 
                print("I am here 2")
                cache.set('graph_1_data', components(plot, CDN))
        elif query1 == 'year':
            df = pd.DataFrame()
            df_sn05 = SN05_Y.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
            print("8% Data Loaded")
            df_sn7b = SN7B_Y.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
            print("16% Data Loaded")
            df_sn13 = SN13_Y.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
            print("25% Data Loaded")
            df_sn15 = SN15_Y.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
            print("33% Data Loaded")
            df_sn28 = SN28_Y.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
            print("41% Data Loaded")
            df_sn33 = SN33_Y.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
            print("50% Data Loaded")
            df_sn34 = SN34_Y.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
            print("58% Data Loaded")
            df_sn44 = SN44_Y.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
            print("66% Data Loaded")
            df_sn48 = SN48_Y.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
            print("74% Data Loaded")
            df_sn66 = SN66_Y.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
            print("82% Data Loaded")
            df_sn83 = SN83_Y.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
            print("91% Data Loaded")
            df_sn89 = SN89_Y.objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
            print("100% Data Loaded")
            print("I am here")
            
            df['year'] = df_sn89['Time'].dt.year
            x_dec = df['year']
            df['Eac_Today'] = df_sn05['Eac_Today'] + df_sn7b['Eac_Today'] + df_sn13['Eac_Today'] + df_sn13['Eac_Today'] + df_sn28['Eac_Today'] + df_sn33['Eac_Today'] + df_sn34['Eac_Today'] + df_sn44['Eac_Today'] \
            + df_sn48['Eac_Today'] + df_sn66['Eac_Today'] + df_sn83['Eac_Today'] + df_sn89['Eac_Today']
            
            if query2 == 'cuf':
                df['Eac_Today'] = df['Eac_Today'] / (decimal.Decimal('2.92') * decimal.Decimal('24.0000') * decimal.Decimal('365'))
                
                Y = df['Eac_Today']
                print(x_dec)
                print(Y)
                plot = figure(title= 'Capacity Utilsation Factor', x_axis_label= 'YEAR', y_axis_label= 'C. U. F.', plot_width =700, plot_height =350)
                
                plot.xaxis.ticker = [2015, 2016, 2017]
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.vbar(x=x_dec, top=Y, width=0.5, bottom=0, line_color = 'navy', color='navy')
                
                #hover = plot.select(dict(type=HoverTool))
                #hover.tooltips = [('x', '@x'),('y', '@y')]
                
                #Store components 
                print("I am here 2")
                cache.set('graph_1_data', components(plot, CDN))
            elif query2 == 'fy':
                df['Eac_Today'] = df['Eac_Today'] / (decimal.Decimal('2.92'))
                
                Y = df['Eac_Today']
                plot = figure(title= 'YEAR vs FINAL YIELD', x_axis_label= 'YEAR', y_axis_label= 'FINAL YIELD', plot_width =700, plot_height =350)
                
                plot.xaxis.ticker = [2015, 2016, 2017]
                
                plot.title.align = 'center'
                plot.title.text_font = 'century gothic'
                
                plot.vbar(x=x_dec, top=Y, width=0.5, bottom=0, line_color = 'navy', color='navy')
                
                #hover = plot.select(dict(type=HoverTool))
                #hover.tooltips = [('x', '@x'),('y', '@y')]
                
                #Store components 
                print("I am here 2")
                cache.set('graph_1_data', components(plot, CDN))
            
    #Store components
    print("I am here 3")
    script_1, div_1 = cache.get('graph_1_data')
        

    #Feed them to the Django template.
    return render_to_response( 'dashboard/bokeh.html',
            {'script_1' : script_1 , 'div_1' : div_1, 'script_2': script_2, 'div_2': div_2} )


@csrf_exempt
def test(request):
     if request.method == 'POST':
         query2 = request.POST.get('Y_axis')
         query1 = request.POST.get('X_axis')
         #
         return reverse(index)
     

         
     
     

