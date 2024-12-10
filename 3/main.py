import numpy as np
import matplotlib.pyplot as plt

# ============
#  Завдання 1
# ============

I = 4
N = 64
delta_t = I / N

t = np.linspace(0, I, N)

def f(t):
    return np.where((t >= 0) & (t <= 2), 1.5, 0)

x = f(t)  # Масив x[N]
f_s = 1 / delta_t  # Частота дискретизації

print(f"Крок дискретизації = {delta_t}")
print(f"Частота дискретизації = {f_s}")

# ============
#  Завдання 2
# ============

t_continuous = np.linspace(0, I, 1000)
t_discrete = np.linspace(0, I, N)

f_continuous = f(t_continuous)
f_discrete = f(t_discrete)

plt.figure(figsize=(12, 6))
plt.plot(t_continuous, f_continuous, label="Неперервний сигнал")
plt.plot(t_discrete, f_discrete, label="Дискретний сигнал", marker="o", ls=" ")
plt.xlabel("Час, t")
plt.ylabel("Амплітуда")
plt.title("Неперервний та дискретний сигнал")
plt.legend()
plt.grid()
plt.show()

# ===============
#  Завдання 3, 5
# ===============

# Швидке Перетворення Фур'є FFT
X_continuous = np.fft.fft(f_discrete)
amplitude_spectrum_continuous = np.abs(X_continuous)

# Зсув частоти для симетрії
frequencies_continuous = np.fft.fftfreq(N, delta_t)
frequencies_continuous_shifted = np.fft.fftshift(frequencies_continuous)
amplitude_spectrum_continuous_shifted = np.fft.fftshift(amplitude_spectrum_continuous)

plt.figure(figsize=(12, 6))
plt.plot(frequencies_continuous_shifted, amplitude_spectrum_continuous_shifted, label="Амплітудний спектр")
plt.xlabel("Частота (Гц)")
plt.ylabel("Амплітуда")
plt.title("Амплітудний спектр неперервного сигналу (через np.fft)")
plt.grid()
plt.legend()
plt.show()

# ============
#  Завдання 4
# ============

# Дискретне Перетворення Фур'є
def DFT(x, N):
    X_k = np.zeros(N, dtype=complex)

    for k in range(N):  # Для кожної частоти
        for n in range(N):  # Сума по всіх n
            X_k[k] += x[n] * np.exp(-2j * np.pi * k * n / N)

    return X_k


# Розрахунок ДПФ
frequencies_dft = np.fft.fftfreq(N, delta_t)  # Масив частот
X_dft = DFT(x, N)
amplitude_spectrum_dft = np.abs(X_dft)

# Зсув для симетрії
frequencies_dft_shifted = np.fft.fftshift(frequencies_dft)
amplitude_spectrum_dft_shifted = np.fft.fftshift(amplitude_spectrum_dft)

plt.figure(figsize=(12, 6))
plt.plot(frequencies_dft_shifted, amplitude_spectrum_dft_shifted, label="Амплітудний спектр дискретного сигналу (DTFT)")
plt.xlabel("Частота (Гц)")
plt.ylabel("Амплітуда")
plt.title("Амплітудний спектр дискретного сигналу")
plt.grid()
plt.legend()
plt.show()

# ============
#  Завдання 7
# ============

# Обернене перетворення Фур'є із перетворенням уявних чисел
x_inverse = np.fft.ifft(X_continuous).real

# Порівняння дискретного та оберненого сигналів
plt.figure(figsize=(12, 6))
plt.plot(t_discrete, x_inverse, label="Обернене перетворення дискретних сигналів, $x'[N]$")
plt.plot(t_discrete, f_discrete, label="Дискретні сигнали, $x[N]$", marker="o", ls=" ")
plt.xlabel("Час, t")
plt.ylabel("Амплітуда")
plt.title("Порівняння оригінального та відновленого сигналів")
plt.legend()
plt.grid()
plt.show()

# Висновок
max_diff = np.max(np.abs(f_discrete - x_inverse))
print(f"Максимальна різниця між x[N] та x'[N]: {max_diff:.2e}")

# Відновлений сигнал x'[N] є майже ідентичним з x[N]
# Така мала похибка (4.44 * 10^{-16}) може бути зумовленою
# використанням експоненційних функцій під час обчислення Фур'є,
# та обмежену точність арифметичних операцій
