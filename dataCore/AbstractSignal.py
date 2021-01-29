import h5py
from dataCore.CreateDataset import DataSet
from dataCore.CreateGroup import GroupAttributes



class AbstractSignal:

    #passing data in csv and groupName
    def __init__(self, data, groupName):
        self.data = data
        self.groupName = groupName

#function to create h5 file
    def createh5File(self):

        #creating a h5 file
        file = h5py.File('OutputFile.h5', 'w')

        #creating group in h5 file
        create_Group = GroupAttributes(self.groupName, file)
        create_Group.createGroup()

        #creating dataset and attributes to h5 file
        create_Dataset = DataSet(self.data, file, self.groupName)
        create_Dataset.createDataset()






    