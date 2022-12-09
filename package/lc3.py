from graphics import *
b=float(input("Enter width of the rectangle"))
h=float(input("Enter height of the rectangle"))
print("Area of the rectangle=",rect_area(b,h))
print("Perimeter of the rectangle",rect_peri(b,h))


r=float(input("Enter radius of the sphere"))
print("Area of the sphere = ",sphere_area(r))
print("Perimeter of the sphere = ",sphere_peri(r))


r=float(input("Enter radius of the circle"))
print("Area of the circle = ",circle_area(r))
print("Perimeter of the circle =",circle_peri(r))


l=float(input("Enter length of the cuboid"))
h=float(input("Enter height of the cuboid"))
b=float(input("Enter breadth of the cuboid"))
print("Area of the cuboid = ",cuboid_area(l,h,b))
print("Perimeter of the cuboid = ",cuboid_peri(l,b,h))
