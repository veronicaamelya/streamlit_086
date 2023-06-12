import streamlit as st
import pandas as pd
import math
import scipy.stats as stats
from streamlit_option_menu import option_menu

with st.sidebar :
    selected = option_menu ('Statistika Deskriptif',
    ['Distribusi Binomial',
     'Distribusi Normal',
     'Distribusi Poisson'],
    default_index=0)

if (selected == 'Distribusi Binomial') :
    st.title("Aplikasi Distribusi Binomial")

    def kombinasi(n, k):
        return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

    def distribusi_binomial(n, k, p):
        kombinasi_nk = kombinasi(n, k)
        q = 1 - p
        hasil = kombinasi_nk * (p ** k) * (q ** (n - k))
        return hasil

    n = st.number_input("Masukkan jumlah percobaan (n)", value=10, min_value=1, step=1)
    k = st.number_input("Masukkan jumlah kejadian sukses (k)", value=5, min_value=0, step=1)
    p = st.number_input("Masukkan probabilitas sukses (p)", value=0.5, min_value=0.0, max_value=1.0, step=0.01)
    Hitung = st.button('Hitung')

    if Hitung :
        hasil_distribusi = distribusi_binomial(n, k, p)
        st.write("Hasil distribusi binomial adalah:", hasil_distribusi)

if (selected == 'Distribusi Normal') :
    st.title("Aplikasi Distribusi Normal")

    mean = st.number_input("Masukkan nilai rata-rata (mean)", value=0.0, step=0.1)
    std_dev = st.number_input("Masukkan simpangan baku (standard deviation)", value=1.0, step=0.1)
    x = st.number_input("Masukkan nilai x:", value=0.0, step=0.1)
    Hitung = st.button('Hitung')

    if Hitung :
        probabilitas = stats.norm.cdf(x, mean, std_dev)
        z_score = (x - mean) / std_dev
        st.write("Probabilitas:", probabilitas)
        st.write("Z-Score:", z_score)

if (selected == 'Distribusi Poisson') :
    st.title("Aplikasi Distribusi Poisson")

    l = st.number_input("Masukkan nilai lambda", value=1.0, step=0.1)
    k = st.number_input("Masukkan nilai k", value=0, step=1)
    Hitung = st.button('Hitung')

    if Hitung :
        probabilitas = stats.poisson.pmf(k, l)
        nilai_harapan = stats.poisson.mean(l)
        st.write("Probabilitas:", probabilitas)
        st.write("Nilai Harapan:", nilai_harapan)
