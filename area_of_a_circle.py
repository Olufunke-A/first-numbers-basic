#find the area of a circle using formular
def compute_area(radius,pi):

    Area= pi*radius*radius
    
    return Area

radius=float(input())
pi=3.14
total=compute_area(radius,pi)
print("Area is ",total )
