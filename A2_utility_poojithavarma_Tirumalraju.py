"""
<Project Title>


Copyright (c) 2022 -- This is the 2022 Summer version of the Template
Licensed
Written by <> <---- PLEASE, WRITE YOUR NAME HERE

# you can also rely on the docstring documentation from pandas on how to format dosctrings:
# https://pandas.pydata.org/pandas-docs/stable/development/contributing_docstring.html

"""

import pandas as pd
from bs4 import BeautifulSoup as bs
import sqlite3

def add_nums(a, b):
    """
    Add two numbers together
    :param a: first number
    :param b: second number
    :return: the sum of two inputs
    """
    
    return a + b

def txtfile(a):
    """
    takes text file location/name as input
    :param a: location of the text file
    :return: variable with pandas dataframe structure
    """
    f = pd.read_csv(a, sep="|")
    return f

def csvfile(a):
    """
    takes csv file location/name as input
    :param a: Location of the csv file
    :return: variable with pandas dataframe structure
    """
    f = pd.read_csv(a)
    return f

def excelfile(a):
    """
    basic operation on excel file
    :param a: location of excel file
    :return: variable with pandas dataframe structure
    """
    f = pd.read_excel(a, 'Sheet000', header=[3]).dropna(axis=1, how='all')
    return f

def htmlfile(a):
    """
    basic operation on HTML file
    :param a: location of html file
    :return: variable with html file data as a string
    """

    file = open('grativational_wave.html' , encoding="UTF-8")
    f = file.read()
    return f


def jsonfile(a):
    """
    basic operation on json file
    :param a: file location
    :return: variable with pandas dataframe structure
    """
    f = pd.read_json(a ,encoding = "UTF-8")
    return f

def sqlitefile(a):
    """
    basic operation on sqlite file
    :param a: file location
    :return: variable with sqlite3.connection
    """
    connection = sqlite3.connect(a)
    return connection



if __name__ == '__main__':
    (add_nums(3,5))
