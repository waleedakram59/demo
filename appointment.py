#Programmer
class Appointment:  
    "Intialize the onject"

    "set the attrivute of name, start, and end"
    def _init_(self, name, start, end ):
        self.name = name
        self.start = start
        self.end = end
    
    def overlaps(self, other):

        " this function determines the start or end of one class overlaps with another"

        if other.start<= self.start < other.end:
            return True
        elif other.start < self.end <= other.end:
            return True
        elif self.start <= other.start < self.end:
            return True
        elif self.start < other.end <= self.end:
            return True
        else:
            return False 