class Vector:
    
    def __init__(self, a):
        self.values = a
        self.len = len(a)

    def __add__(self, other):
        if self.len == other.len:
            new = Vector(self.values)
            for x in range (other.len):
                new.values[x] = self.values[x] + other.values[x]
            return new
        else:
            print ('error: vector dimensions do not match')
            Vector.values='error'
            return Vector
            
        
    def __sub__(self, other):
        if self.len == other.len:
            new = Vector(self.values)
            for x in range (other.len):
                new.values[x] = self.values[x] - other.values[x]
            return new
        else:
            print ('error: vector dimensions do not match')
            Vector.values='error'
            return Vector
        

    def __mul__(self, other):
        if self.len == other.len:
            multi = 0
            for x in range (other.len):
                multi = multi + self.values[x]+other.values[x]
            return multi
        else:
            print ('error: vector dimensions do not match')
            multi = 'error'
            return multi


