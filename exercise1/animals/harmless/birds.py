class Birds:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Penguin', 'Crow', 'Chicken']
        
    def printMembers(self):
        print('Printing members of the harmless.Birds class')
        for member in self.members:
            print('\t%s ' % member)