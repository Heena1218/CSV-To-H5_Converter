import h5py


class GroupAttributes:

    def __init__(self, groupName, file):
        self.groupName = groupName
        self.file = file

#function to create group in h5 file
    def createGroup(self):
        self.file.create_group(self.groupName)
        #print('group created')
        
