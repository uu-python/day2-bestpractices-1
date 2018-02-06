class Fish:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Nemo', 'Salmon']
 
    def printMembers(self):
        print('Printing members of the harmless Fish class')
        for member in self.members:
            print('\t%s ' % member)
