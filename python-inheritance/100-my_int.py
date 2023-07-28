#!/usr/bin/python3
'''Defines new class MyInt
'''


class MyInt(int):
    '''int's rebel sibling. Inverts == and !=
    '''
    def __ne__(self, other_int):
        '''handled equality operations btw to integers
        '''
        return float(self) == float(other_int)

    def __eq__(self, other_int):
        '''handles non-equality operations btw integers
        '''
        return float(self) != float(other_int)
