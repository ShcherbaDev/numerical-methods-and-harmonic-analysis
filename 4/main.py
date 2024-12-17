import numpy as np
import matplotlib.pyplot as plt
import pywt

# ============
#  Завдання 1
# ============

def f(time):
    return np.where((time >= 0) & (time <= 2), 1.5, 0)

time = np.linspace(0, 4, 1000) # 1000 рівновіддалених точок на [0; 5]
signal = f(time)

# ==============
#  Завдання 2-5
# ==============

def analyze_wavelet(signal, wavelet_name, humanfriendly_wavelet_name):
    # DWT
    cA, cD = pywt.dwt(signal, wavelet_name)

    # Зворотне DWT для різних коефіцієнтів
    coef_appr = pywt.idwt(cA, None, wavelet_name) # Тільки апроксимуючі
    coef_detail = pywt.idwt(None, cD, wavelet_name) # Тільки деталізуючі
    coef_both = pywt.idwt(cA, cD, wavelet_name) # Апроксимуючі та деталізуючі

    # Графіки
    _, [original_signal_plot, reconstructed_signal_plot] = plt.subplots(2, 1, figsize=(12, 6))
    original_signal_plot.plot(time, signal)
    original_signal_plot.set_title("Оригінальний сигнал")
    original_signal_plot.set_xlabel("Час")
    original_signal_plot.set_ylabel("Амплітуда")

    reconstructed_signal_plot.plot(coef_appr, label="Апроксимація")
    reconstructed_signal_plot.plot(coef_detail, label="Деталізація")
    reconstructed_signal_plot.plot(coef_both, label="Повний")
    reconstructed_signal_plot.set_title(f"Відновлений сигнал {humanfriendly_wavelet_name}")
    reconstructed_signal_plot.set_xlabel("Час")
    reconstructed_signal_plot.set_ylabel("Амплітуда")
    reconstructed_signal_plot.legend()

    plt.tight_layout()
    plt.show()

analyze_wavelet(signal, "haar", "Вейвлет Хаара")
analyze_wavelet(signal, "dmey", "Вейвлет Меєра (дискретний аналог Морле)") 

# ============
#  Завдання 6
# ============

time = np.linspace(0, 0.05, 1000)

sine_clean = np.sin(2. * np.pi * 440 * time)
sine_noise = sine_clean + np.random.normal(0, 0.3, time.shape)

# ============
#  Завдання 7-8
# ============

coeffs_thresholded = [
    pywt.threshold(coef, 0.1, mode="soft")
    for coef in pywt.wavedec(sine_noise, "haar")
]

# ============
#  Завдання 9
# ============

sine_denoised = pywt.waverec(coeffs_thresholded, "haar")

# =============
#  Завдання 10
# =============

_, [sine_clean_plt, sine_noise_plt, sine_denoised_plt] = plt.subplots(3, 1, figsize=(12, 7))
sine_clean_plt.plot(time, sine_clean)
sine_clean_plt.set_title("Чиста синусоїда 440 Гц")
sine_clean_plt.set_xlabel("Час")
sine_clean_plt.set_ylabel("Амплітуда")

sine_noise_plt.plot(time, sine_noise, linewidth=0.8)
sine_noise_plt.set_title("Синусоїда 440 Гц з шумом")
sine_noise_plt.set_xlabel("Час")
sine_noise_plt.set_ylabel("Амплітуда")

sine_denoised_plt.plot(time, sine_denoised, linewidth=0.8)
sine_denoised_plt.set_title("Оброблена синусоїда 440 Гц")
sine_denoised_plt.set_xlabel("Час")
sine_denoised_plt.set_ylabel("Амплітуда")

plt.tight_layout()
plt.show()
