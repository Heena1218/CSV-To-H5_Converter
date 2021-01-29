import h5py
import pandas as pd

class DataSet:
    def __init__(self, data, file, groupName):
        self.data = data
        self.file = file
        self.groupName = groupName

#function to create dataset in h5 file
    def createDataset(self):
        #print(self.groupName)

#data set creation for each column in h5 file
        for col in self.data:
            if self.data[col].dtypes == object:
                dt = h5py.string_dtype(encoding='utf-8')
                dataset = self.file[self.groupName].create_dataset(col, self.data[col].shape, dtype = dt)
            else:
                dataset = self.file[self.groupName].create_dataset(col, self.data[col].shape, dtype = self.data[col].dtypes)
            
            name_of_Column = col.split('[')
            unit = name_of_Column[1].replace(']','')

#attribute creation for each col in h5 file
            dataset.attrs.create("Name", name_of_Column[0])   # Name attribute
            dataset.attrs.create("Unit", unit)                # Unit attribute
# more attributes can be added here later using above code


#defining data for each dataset created 
            dataset_data = self.data[col]
            dataset = dataset_data
            

            

        
