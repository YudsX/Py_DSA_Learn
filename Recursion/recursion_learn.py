# Metode Recursion Seperti kotak di dalam kotak, akan berhenti ketika kotak itu sudah mendapatkan reward nya
# Atau mungkin seperti konsep faktorial

# 5! = 5 * 4 * 3 * 2 * 1 = 120
# contoh
def faktorial(n):
    if n == 1:
        return 1

    return n * faktorial(n - 1)

print(faktorial(10))