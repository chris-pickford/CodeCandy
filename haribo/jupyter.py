"""the HAribo module is part of the dbutility package


Naming Conventions:

Package:            thispackage (short name)
Module:             this_module (short name)
Class:              ThisIsAClass
Function:           this_is_a_function
Public Method:      this_is_a_public_method
Non-Public Method:  _this_is_a_non_public_method
Variables:          thisIsAVariable
Constant:           THIS_IS_A_CONSTANT

"""

__status__ = "development"
__version__ = 'mdl 1.0.0'
__date__ = "12 Jun 2019"
__author__ = 'Chris Pickford <drchrispickford@gmail.com>'


from IPython.core.display import display, HTML
import pandas as pd
import os
import sys
import _pickle as pickle


def set_screen_width():
    '''

    Resizes the cells in the Jupyter notebook to fit the screen

    :return: None
    '''


    display(HTML("<style>.container { width:90% !important; }</style>"))



def show_df(df, allRows=False):
    if allRows:
        with pd.option_context('display.max_rows', df.shape[0], 'display.max_columns', df.shape[1]):
            display(df)
    else:
        with pd.option_context('display.max_columns', df.shape[1]):
            display(df)
    print(df.shape)


def pickle_it(obj, filepath):
    '''

    This is a defensive way to write pickle.write, allowing for very large files on all platforms

    :param obj: The data to pickle
    :param filepath: The string path of where to save the data
    :return:
    '''

    max_bytes = 2**31 - 1
    bytes_out = pickle.dumps(obj)
    n_bytes = sys.getsizeof(bytes_out)
    with open(filepath, 'wb') as f_out:
        for idx in range(0, n_bytes, max_bytes):
            f_out.write(bytes_out[idx:idx+max_bytes])

def from_pickle_jar(filepath):
    '''

    This is a defensive way to write pickle.load, allowing for very large files on all platforms

    :param filepath: The string path of where to load data from
    :return:
    '''


    max_bytes = 2**31 - 1
    try:
        input_size = os.path.getsize(filepath)
        bytes_in = bytearray(0)
        with open(filepath, 'rb') as f_in:
            for _ in range(0, input_size, max_bytes):
                bytes_in += f_in.read(max_bytes)
        obj = pickle.loads(bytes_in)
    except:
        return None
    return obj


def help(funcName = None):

    if funcName is None:
        print('The haribo package provides the following functions to use in Jupyter:\n')
        print('set_screen_width() - sets cells to be 90% of screen width\n')
        print('show_df(dataFrame, allRows = False) - shows all columns of a dataFrame when displayed\n')
        print('pickle_it(data, path) - safely pickles a file\n')
        print('from_pickle_jar(path) - safely loads a pickled file\n')

    if funcName == 'set_screen_width':
        pass

    if funcName == 'show_df':
        pass

    if funcName == 'set_screen_width':
        pass

    if funcName == 'pickle_it':
        pass

    if funcName == 'from_pickle_jar':
        pass