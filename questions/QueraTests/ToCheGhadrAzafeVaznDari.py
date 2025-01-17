# تو جه قدر اضافه وزن داری ؟
# https://quera.org/problemset/3404
n = int(input())
m = float(input())
bmi = (n/(m**2))
print(f"{bmi:.2f}")
if bmi<18.5:
    print("Underweight")
elif 18.5<=bmi and bmi<25:
    print("Normal")
elif 25<=bmi and bmi<30:
    print("Overweight")
elif 30<=bmi:
    print("Obese")