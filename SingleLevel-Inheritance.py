# INHERITANCE
#1.	Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.
#2.	Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to
#   calculate the area of the rectangle.
#3.	Create a method display() that display the length, width, perimeter and area of an object created using
#   an instantiation on rectangle class.
#4.	Create a Parallelepipede child class inheriting from the Rectangle class and with a
#   height attribute and another Volume()method to calculate the volume of the Parallelepiped.

class rectangle:  # PARENT CLASS WITH AREA, VOLUME,DISPLAY METHOD
    length = 20
    breadth=  30

    def perimeter(self):
        self.peri=2*(self.length + self.breadth)
        return(self.peri)

    def area(self):
        self.area_var= self.length*self.breadth
        return(self.area_var)

    def display(self):
        print("The length",self.length)
        print("The breadth", self.breadth)
        print("The area", self.area())
        print("The perimeter", self.perimeter())

class para_pip(rectangle): # CHILD CLASS INHERITING FROM RECTANGLE CLASS WITH A NEW VOLUME METHOD
        height = 70
        def volume(self):
            self.volume_pip= rectangle.area(self)*self.height
            return(self.volume_pip)

        def display1(self):
            print("The volume of parallelopipped: ",self.volume())

r_obj = rectangle()
r_obj.display()
p_obj = para_pip()
p_obj.display1()
