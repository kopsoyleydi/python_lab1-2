def cube_volume(edge_length):
    volume1 = edge_length ** 3
    return volume1


def cube_surface_area(edge_length):
    surface_area1 = 6 * (edge_length ** 2)
    return surface_area1


c = float(input())

volume = cube_volume(c)
surface_area = cube_surface_area(c)

print(f"Volume = {volume}")
print(f"Total surface area = {surface_area}")

N = int(input())
K = int(input())

tangerines_per_student = K // N
remaining_tangerines = K % N

print(tangerines_per_student)
print(remaining_tangerines)

number = int(input("Enter a number: "))

thousands_digit = number // 1000
hundreds_digit = (number // 100) % 10
tens_digit = (number // 10) % 10
units_digit = number % 10

print(f"The digit in the thousands position is {thousands_digit}")
print(f"The digit in the hundreds position is {hundreds_digit}")
print(f"The digit in the tens position is {tens_digit}")
print(f"The digit in the position of units is {units_digit}")

people = int(input())

if people % 2 == 0:
    people = people
else:
    people = people + 1

print(people / 2)

num = int(input("Введите целое число: "))

num1 = num << 1

print(f"Результат побитового сдвига влево на один бит: {num1}")

if num1 == 0:
    print("Результат равен нулю.")

num1 = float(input("Пожалуйста, введите первое число: "))
num2 = float(input("Пожалуйста, введите второе число: "))

operation = input("Пожалуйста, выберите операцию (+, -, *, /): ")

result = None
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        print("Ошибка: деление на ноль.")
    else:
        result = num1 / num2
else:
    print("Ошибка: неверная операция.")

if result is not None:
    print(f"{num1} {operation} {num2} = {result:.3f}")


