import pandas as pd
import h5py
import numpy as numpy
from dataCore.AbstractSignal import AbstractSignal


# main 
if __name__ == '__main__':

    #data read from csv file
    data = pd.read_csv('test.csv')
    data.columns = data.columns.str.replace('/',' ')

    #group name , later will take from input file
    groupName = 'Hyundai'

    #coversion of csv to h5 file
    createH5 = AbstractSignal(data, groupName )
    createH5.createh5File()
    print('Converted CSV File to H5 file successfully')