class Mammals:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Lion', 'Wolf', 'Panther']
        
    def printMembers(self):
        print('Printing members of the dangerous.Mammals class')
        for member in self.members:
            print('\t%s ' % member)