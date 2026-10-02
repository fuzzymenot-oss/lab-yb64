# Проверка принадлежности точки прямоугольнику.
x_coord = float(input("Координата X: "))
y_coord = float(input("Координата Y: "))

# Условие попадания внутрь (включая границы)
is_inside = (0 <= x_coord <= 5) and (0 <= y_coord <= 3)

if is_inside:
    print("Внутри или на границе")
else:
    print("Снаружи")