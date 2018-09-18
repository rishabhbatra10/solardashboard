# @coding: utf-8              #
# @auther: Rishabh Batra      #
# Indian Institute of Science #

""" THIS FILE GENERATES THE GRAPHS/ VIEW FOR MAIN HTML PAGE"""

#  TODO:
#  Remove cache from backend and put it on front-end.
#  Reduce the code size with one function one work.
#  Change number of days in month and year depending upon the month and year i.e. leap years has 366 days and feb has 28
#  Add logging
#  Fix the problem in the database

import decimal
import pandas as pd

# Importing the django attributes required
from django.shortcuts import render_to_response, redirect # rendering and redirecting
from django.http import HttpResponse # for returning Http response 
from django.views.decorators.csrf import csrf_exempt # decorater for excepmting the security
from django.core.cache import cache # for caheing the data temporarily
from django_pandas.io import read_frame

from .models import * # importing models from dashboard app

# Importing the bokeh plots attributes required for plotting
from bokeh.plotting import figure, output_file, show 
from bokeh.embed import components 
from bokeh.resources import CDN
from bokeh.models import HoverTool

# declaring Variables
# dictionary containing mapping for parameters
PARAM_MAP = {
    'time': 'Time',
    'eac_t': 'Eac_Today',
    'vpv': 'Vpv',
    'ipv': 'Ipv',
    'ppv': 'Ppv',
    'vac': 'Vac',
    'iac': 'Iac',
    'fac': 'Fac',
    'day': 'Date',
    'month': 'Month',
    'year': 'Year',
    'cuf': 'Capacity Utilisation Factor',
    'fy': 'Final Yield'
}

# dictionary containing units for parameters
UNITS = {
    'time': 'DATE',
    'eac_t': 'ENERGY',
    'vpv': 'PV POTENTIAL',
    'ipv': 'PV CURRENT',
    'ppv': 'PV POWER',
    'vac': 'AC POTENTIAL',
    'iac': 'AC CURRENT',
    'fac': 'AC FREQUENCY',
    'cuf': 'C. U. F.',
    'fy': 'FINAL YIELD',
    'day': 'DAYS',
    'month': 'MONTHS',
    'year': 'YEARS'
}

# dictionary containing values for datatables in models
DB_TABLES = {
    'SN05_D': SN05_D, 'SN05_M': SN05_M, 'SN05_Y': SN05_Y,
    'SN7B_D': SN7B_D, 'SN7B_M': SN7B_M, 'SN7B_Y': SN7B_Y,
    'SN13_D': SN13_D, 'SN13_M': SN13_M, 'SN13_Y': SN13_Y,
    'SN15_D': SN13_D, 'SN15_M': SN13_M, 'SN15_Y': SN13_Y,
    'SN28_D': SN13_D, 'SN28_M': SN13_M, 'SN28_Y': SN13_Y,
    'SN33_D': SN13_D, 'SN33_M': SN13_M, 'SN33_Y': SN13_Y,
    'SN34_D': SN13_D, 'SN34_M': SN13_M, 'SN34_Y': SN13_Y,
    'SN44_D': SN13_D, 'SN44_M': SN13_M, 'SN44_Y': SN13_Y,
    'SN48_D': SN13_D, 'SN48_M': SN13_M, 'SN48_Y': SN13_Y,
    'SN66_D': SN13_D, 'SN66_M': SN13_M, 'SN66_Y': SN13_Y,
    'SN83_D': SN13_D, 'SN83_M': SN13_M, 'SN83_Y': SN13_Y,
    'SN89_D': SN13_D, 'SN89_M': SN13_M, 'SN89_Y': SN13_Y,
}

# no of days in I day, month or year to be used in CUF
DAYS = {
    'day': '1',
    'month': '30',
    'year': '365',
}

def compile_by(compile):
    """
    Renames the table names according what is mentioned in the database
    :param compile: compile by day, month or year by giving 'D', 'M' or 'Y' respectively
    :return: renamed values containing alphabet
    """
    if compile not in ['D', 'M', 'Y']:
        raise ValueError('%s is not a valid compilation for the data')
    return 'SN05_%s' % compile, 'SN7B_%s' % compile, 'SN13_%s' % compile, 'SN15_%s' % compile, 'SN28_%s' % compile, \
           'SN33_%s' % compile, 'SN34_%s' % compile, 'SN44_%s' % compile, 'SN48_%s' % compile, 'SN66_%s' % compile, \
           'SN83_%s' % compile, 'SN89_%s' % compile


def load_db_tables(compiled='day'):
    """
    loads tables from database as dataframes
    :param compiled: combination of data quarterly, monthly and yearly
    :return:
    """
    compiling_param= ['day', 'month', 'year']
    if compiled not in compiling_param:
        raise ValueError('%s is not a valid compilation for the data' % compiled)

    # getting DB names
    db_sn05, db_sn7b, db_sn13, db_sn15, db_sn28, db_sn33, db_sn34, db_sn44, db_sn48, db_sn66, db_sn83, db_sn89 = \
        compile_by(compiled[0].upper())
    df_sn05 = DB_TABLES[db_sn05].objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
    df_sn7b = DB_TABLES[db_sn7b].objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
    df_sn13 = DB_TABLES[db_sn13].objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
    df_sn15 = DB_TABLES[db_sn15].objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
    df_sn28 = DB_TABLES[db_sn28].objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
    df_sn33 = DB_TABLES[db_sn33].objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
    df_sn34 = DB_TABLES[db_sn34].objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
    df_sn44 = DB_TABLES[db_sn44].objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
    df_sn48 = DB_TABLES[db_sn48].objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
    df_sn66 = DB_TABLES[db_sn66].objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
    df_sn83 = DB_TABLES[db_sn83].objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
    df_sn89 = DB_TABLES[db_sn89].objects.all().to_dataframe(fieldnames=['Time', 'Eac_Today', 'Vpv', 'Ipv', 'Ppv', 'Vac', 'Iac', 'Pac', 'Fac'])
    print('100% data loaded')
    return df_sn05, df_sn7b, df_sn13, df_sn15, df_sn28, df_sn33, df_sn34, df_sn44, df_sn48, df_sn66, df_sn83, df_sn89


def calc_param(param, df_list):
    """
    Add the given parameter accross the tables of different panels
    :param param: parameter which is to be added
    :param df_list: data tables for all the panels
    :return: added values for each day
    """
    return df_list[0][param]+ df_list[1][param] + df_list[2][param] + df_list[3][param] + df_list[4][param] \
           + df_list[5][param] + df_list[6][param] + df_list[7][param] + df_list[8][param] + df_list[9][param] \
           + df_list[10][param]


def plot_first_graph(X, Y):
    """
    Plots the graph being displayed first
    :param X: Values for parameters of sensors
    :param Y: Values for parameters of sensors except time
    :return: plot
    """
    df = pd.DataFrame()

    # loading data tables from DB as dataframes
    df_sn05, df_sn7b, df_sn13, df_sn15, df_sn28, df_sn33, df_sn34, df_sn44, df_sn48, df_sn66, df_sn83, df_sn89 \
        = load_db_tables(X)

    # defining x_axis value
    if X == 'year':
        # df['year'] = df_sn89['Time'].dt.year
        df['year'] = ['2016', '2017', '2018']
        x_val = df['year']
    else:
        x_val = df_sn89['Time']

    # calculating values for Y_axis
    df['Eac_Today'] = df_sn05['Eac_Today'] + df_sn7b['Eac_Today'] + df_sn13['Eac_Today'] + df_sn28['Eac_Today'] + \
        df_sn33['Eac_Today'] + df_sn34['Eac_Today'] + df_sn44['Eac_Today'] \
        + df_sn48['Eac_Today'] + df_sn66['Eac_Today'] + df_sn83['Eac_Today'] + df_sn89['Eac_Today']

    df['fy'] = df['Eac_Today'] / (decimal.Decimal('2920'))
    df['cuf'] = df['Eac_Today'] / \
        (decimal.Decimal('2920') * decimal.Decimal('24.0000') * decimal.Decimal(DAYS[X]))

    y_val = df[Y]

    print(len(x_val))
    print(len(y_val))

    # plotting the graphs
    title = '%s vs %s' % (PARAM_MAP[X], PARAM_MAP[Y])
    plot = figure(title=title,
                  x_axis_type="datetime",
                  x_axis_label=UNITS[X],
                  y_axis_label=UNITS[Y],
                  plot_width=700, plot_height=350)

    plot.title.align = 'center'
    plot.title.text_font = 'century gothic'

    plot.vbar(x=x_val, top=y_val, width=0.2, color='navy')

    return plot


def plot_second_graph(X, Y):
    """
    Plots the graph being displayed second
    :param X: Values either day, month or year
    :param Y: capacity utilasation factor or final yeild
    :return: plot
    """
    # loading data tables
    df_sn05, df_sn7b, df_sn13, df_sn15, df_sn28, df_sn33, df_sn34, df_sn44, df_sn48, df_sn66, df_sn83, df_sn89 \
        = load_db_tables('day')

    # list of dataframes to calculate parameters
    df_list = [df_sn05, df_sn7b, df_sn13, df_sn28, df_sn33, df_sn34, df_sn44, df_sn48, df_sn66, df_sn83, df_sn89]

    # x_axis value for graph 2
    x_val = df_sn89[PARAM_MAP[X]]

    # y_axis value for graph_2
    y_val = calc_param(PARAM_MAP[Y], df_list)

    title = '%s vs %s' % (PARAM_MAP[Y], PARAM_MAP[X])

    # Plotting figures
    if PARAM_MAP[X] == 'Time':
        plot = figure(title=title,
                      x_axis_type="datetime",
                      x_axis_label=UNITS[X],
                      y_axis_label=UNITS[Y],
                      plot_width=700, plot_height=350)
    else:
        plot = figure(title=title,
                      x_axis_label=UNITS[X],
                      y_axis_label=UNITS[Y],
                      plot_width=700, plot_height=350)

    plot.title.align = 'center'
    plot.title.text_font = 'century gothic'

    plot.line(x_val, y_val, color='navy')
    print(len(x_val))
    print(len(y_val))
    return plot


@csrf_exempt
def index(request):
    """
    Main API plots the graphs and feeds to the html using bokeh
    :param request:
    :return:
    """
    print("Let's start")

    # Fetching values from user
    g1_x_axis = "year"
    g1_y_axis = "cuf"
    g2_x_axis = "time"
    g2_y_axis = "eac_t"

    # On posting to fetch the data
    if request.method == 'POST':
        g1_x_axis = request.POST.get('X_axis_1')
        g1_y_axis = request.POST.get('Y_axis_1')
        g2_x_axis = request.POST.get('X_axis_2')
        g2_y_axis = request.POST.get('Y_axis_2')
    print(g1_x_axis)
    print(g1_y_axis)
    print(g2_x_axis)
    print(g2_y_axis)

    ## Making First Graph
    # cache.get('abcd') == None
    if True:
        plot_1 = plot_first_graph(g1_x_axis, g1_y_axis)
        print("I am here 2")
        cache.set('graph_1_data', components(plot_1, CDN))

    ## Making Second Graph
    # cache.get('graph_2_data') == None
    if True:
        plot_2 = plot_second_graph(g2_x_axis, g2_y_axis)
        # Store components
        print("I am here 2")
        cache.set('graph_2_data', components(plot_2, CDN))
        # getting graph from cache

    # Store components
    print("I am here 3")
    script_2, div_2 = cache.get('graph_2_data')
    script_1, div_1 = cache.get('graph_1_data')
        

    # Feed them to the Django template.
    return render_to_response( 'dashboard/bokeh.html',
            {'script_1' : script_1 , 'div_1' : div_1, 'script_2': script_2, 'div_2': div_2} )


def test(request):
    return 'Hello, This is the test function'
