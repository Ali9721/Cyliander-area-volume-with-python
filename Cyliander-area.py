# At first I use math module
import math

# Get input for radius and height 
radius = float(input("Enter the radius of the cylinder: "))
 
height = float(input("Enter the height of the cylinder: "))

#Let's calculate the volume and surface 
# Obviously I use this equal "π" = "math.pi" in formula
volume = math.pi*radius**2* height
surface_area = 2*math.pi*radius**2 + 2*math.pi*radius*height

# display the result
print("Volume of the cylinder is: " ,round(volume,2))
print("Surface area of the cylinder is: " ,round(surface_area,2))
