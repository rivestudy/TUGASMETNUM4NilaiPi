import numpy as np
import time

# Fungsi yang akan diintegrasikan
def f(x):
    return 4 / (1 + x**2)

# Implementasi metode trapezoid
def trapezoid_integration(a, b, N):
    x = np.linspace(a, b, N+1)
    y = f(x)
    h = (b - a) / N
    integral = (h / 2) * (y[0] + 2 * sum(y[1:-1]) + y[-1])
    return integral

# Nilai referensi pi
pi_reference = 3.14159265358979323846

# Variasi nilai N
N_values = [10, 100, 1000, 10000]

# Menyimpan hasil
results = []

for N in N_values:
    start_time = time.time()
    integral_value = trapezoid_integration(0, 1, N)
    end_time = time.time()
    
    error = np.abs(pi_reference - integral_value)
    rms_error = np.sqrt(error**2)
    execution_time = end_time - start_time
    
    results.append((N, integral_value, rms_error, execution_time))

# Menampilkan hasil
for result in results:
    N, integral_value, rms_error, execution_time = result
    print(f'N: {N}')
    print(f'Integral Value: {integral_value}')
    print(f'RMS Error: {rms_error}')
    print(f'Execution Time: {execution_time} seconds')
    print('------------------------------')

N_values = [result[0] for result in results]
rms_errors = [result[2] for result in results]
execution_times = [result[3] for result in results]

