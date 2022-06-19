w = float(input("Masukan berat badan (kg): "))
h = float(input("Masukan tinggi badan (cm): "))
h *= 0.01

def bmi(w, h):
    calc = w/(h*h)
    print(f"BMI anda adalah {calc}!")

bmi(w,h)