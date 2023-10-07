class Vector(object):
    def __init__(self, coordinates):
        """
        This function is used to initialize a vector
        Args:
            (self)
            (coordinates): The values of the vector
        """
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
        
        except ValueError:
            raise ValueError('Empty Coordinates')
        except TypeError:
            raise TypeError('Must be iterable')
        
    def __str__(self):
        """
           This function is Used when printing the object
           Return:
                A string that contains the coordonates
        """
        return 'Vector: {}'.format(self.coordinates)
    
    def __eq__(self, v):
        """
            This function is used to perform equality 
            Return:
                If the coordinates are equal returns true
        """
        return self.coordinates == v.coordinates