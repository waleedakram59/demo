class Car:
    """Car that turns drives and tells you direction 
    
    Attributes: 
        x(int): the x coordinate 
        y(int): the y coordinate
        

    
    
    
    """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.heading = "n"

    def turn(self, direction):
        "INSERT DOCSTRING"
        if self.heading == "n" and direction == "r":
            self.heading = "e"
        elif self.heading == "n" and direction == "l":
            self.heading = "w"
        elif self.heading == "s" and direction == "r":
            self.heading = "w"
        elif self.heading == "s" and direction == "l":
            self.heading = "e" 
        elif self.heading == "e" and direction == "r":
            self.heading = "s"
        elif self.heading == "e" and direction == "l":
            self.heading = "n"    
        elif self.heading == "w" and direction == "r":
            self.heading = "n"
        elif self.heading == "w" and direction == "l":
            self.heading = "s"      
    
    def drive(self, distance = 1):
        "INSERT DOCSTRING"
        print(self.heading)
        if self.heading == "n":
            self.y += distance
        if self.heading == "e":
            self.x += distance
        if self.heading == "w":
            self.x -= distance
        if self.heading == "s":
            self.y -= distance
        
    def status(self):
        print(f"Coordinates: ({self.x}, {self.y})" )
        print(f"Heading: {self.heading}")
        

