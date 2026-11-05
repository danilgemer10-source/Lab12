import sphere

R = float(input("Введіть радіус: "))

if R <= 0:
    print("Радіус повинен бути додатним.")
    exit()
    
print("Об'єм сфери:", sphere.volume_of_a_sphere(R))
print("Площа поверхні сфери:", sphere.surface_area_of_a_sphere(R))