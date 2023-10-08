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
    
    def __eq__(self, vector):
        """
            This function is used to perform equality 
            Return:
                If the coordinates are equal returns true
        """
        return self.coordinates == vector.coordinates
    
    def sum(self, vector):
        """
            This function is used to perform the sum of two vectors:
            Args:
            (vector): the intend to sum vector
            Return:
            (sum): return the sum answer
        """
    
    def minus(self, vector):
        """
            This function is used to perform the minus of two vectors:
            Args:
            (vector): the intend to minus vector
            Return:
            (minus): return the minus answer
        """
    
    def scaler_multiplication(self, scaler):
        """
            This function is used to perform the scaler multiplication of a vector:
            Args:
            (scaler): the intend to multiply with a scaler
            Return:
            (scaler_multiplication): return the answer of scaler multiplication
        """

    def magnitude(self):
        """
            This function is used to get the magnitude of a vector
            Return:
            (magnitude): returns a value of the vector's magnitude
        """


    def normalize(self, magnitude):
        """
            This function is used to get the normalized vector of this
            Args:
            (magnitude): the calculated magnitude of the vector using magnitude() function
            Return:
            (normalized_vector): returns the normalized vector
        """

    def dot(self, v):
        """
            This function is used to find the dot product of two vectors
            Args:
            (v): the target vecor
            Return:
            the answer of the dot product.
        """

    def angle(self, v):
        """
            This function is used to find the angle between two vectors
            Args:
            (v): the second vector
            Returns:
            The angle between two vectors.
        """

    def is_orthogonal_to(self, v):
        """
        
        """
    
    def is_parallel_to(self, v):
        """
        
        """

    def component_parallel_to(self, basis):
        """
        
        """
        
    def component_orthogonal_to(self, basis):
        """
        
        """