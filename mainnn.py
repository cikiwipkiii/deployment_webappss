import streamlit as st
from streamlit_option_menu import option_menu

st.title('Aplikasi Konsep Mol')

with st.sidebar :
    Pilihan = option_menu(menu_title=None,
              options=['Pengertian Mol','Massa ke Mol','Mol ke Massa','Volume Gas ke Mol','Mol ke Volume Gas','Jumlah Partikel ke Mol','Mol ke Jumlah Partikel','Molaritas ke Mol','Mol ke Molaritas','Tentang Kita'])
 

 #Pengertian Mol
if Pilihan == "Pengertian Mol" :
    
    st.header ('WELCOME TO :blue[OUR WEB] :sunglasses:')
    st.subheader('Pengertian Mol')
    st.markdown(':red[Mol] adalah jumlah suatu zat yang mengandung jumlah satuan dasar (atom, molekul dan ion) yang sama dalam atom-atom dalam 12 g isotop carbon (c-12). Banyak rumus untuk mengetahui jumlah :red[Mol] sesuai dari data yang diketahui')
    st.subheader('Tujuan Pembuatan Website')
    st.markdown('Untuk menghindari kesalahan dalam perhitungan mol serta memudahkan para staff laboratorium ataupun analis dalam menghitung :red[Mol] dengan cepat dan akurat')
    

#Diketahui Massa
if Pilihan =="Massa ke Mol" :
    Massa = st.number_input('masukkan nilai Massa')
    Mr = st.number_input('masukkan nilai Mr')

    tombol = st.button('hitung nilai Mol')

    if tombol:
        nilai_Mol = Massa/Mr
        st.success(f'Nilai Mol sebesar {nilai_Mol}')
        st.balloons()
        
    
#Diketahui Mol
elif Pilihan =="Mol ke Massa" :
    Mol = st.number_input('masukkan nilai Mol')
    Mr = st.number_input('masukkan nilai Mr')
    
    tombol = st.button('hitung nilai Massa')
    
    if tombol:
        nilai_Massa = Mol*Mr
        st.success(f'Nilai Massa sebesar {nilai_Massa}')
        st.balloons()
    

#Diketahui Volume
elif Pilihan == "Volume Gas ke Mol" :
    Volume = st.number_input('masukkan nilai Volume')
    stp = st.number_input('masukkan nilai stp')

    tombol = st.button('hitung nilai Mol')

    if tombol:
        nilai_Mol = Volume/stp
        st.success(f'Nilai Mol sebesar {nilai_Mol}')
        st.snow()
        
        
#Diketahui Mol
elif Pilihan == "Mol ke Volume Gas" :
    Mol = st.number_input('masukkan nilai Mol')
    stp = st.number_input('masukkan nilai stp')
    
    tombol = st.button('hitung nilai Volume')
    
    if tombol:
        nilai_Volume = Mol*stp
        st.success(f'Nilai Volume sebesar {nilai_Volume}')
        st.snow()
        
#Diketahui Jumlah Partikel
elif Pilihan == "Jumlah Partikel ke Mol" :
    JumlahPartikel = st.number_input('masukkan nilai JumlahPartikel')
    BilAvogrado = st.number_input('masukkan nilai BilAvogrado')
    
    tombol = st.button('hitung nilai Mol')
    
    if tombol:
        nilai_Mol = JumlahPartikel/BilAvogrado
        st.success(f'nilai Mol sebesar {nilai_Mol}')
        st.balloons()
        
        
#Diketahui Mol
elif Pilihan == "Mol ke Jumlah Partikel" :
    Mol = st.number_input('masukkan nilai Mol')
    BilAvogrado = st.number_input('masukkan nilai BilAvogrado')
    
    tombol = st.button('hitung nilai Jumlah Partikel')
    
    if tombol:
        nilai_JumlahPartikel = Mol*BilAvogrado
        st.success(f'nilai Jumlah Partikel sebesar {nilai_JumlahPartikel}')
        st.balloons()
        
#Diketahui Molaritas
elif Pilihan == "Molaritas ke Mol" :
    Molaritas = st.number_input('masukkan nilai Molaritas')
    Volume = st.number_input('masukkan nilai volume')
    
    tombol = st.button('hitung nilai mol')
    
    if tombol:
        nilai_Mol = Molaritas*Volume
        st.success(f'nilai Mol sebesar {nilai_Mol}')
        st.snow()
        
        
#Diketahui Mol
elif Pilihan == "Mol ke Molaritas" :
    Mol = st.number_input('masukkan nilai Mol')
    Volume = st.number_input('masukkan nilai volume')
    
    tombol = st.button('hitung nilai Molaritas')
    
    if tombol:
        nilai_Molaritas = Mol/Volume
        st.success(f'nilai Molaritas sebesar {nilai_Molaritas}')
        st.snow()
        
#Tentang Kita
elif Pilihan == "Tentang Kita" :
    
    st.header('YUK KENALAN SAMA KAMI :star2:')
    st.markdown('Assalamualaikum Wr. Wb. Perkenalkan kami dari Mahasiswa Politeknik AKA Bogor memperkenalkan web perhitungan konsep :red[Mol] yang telah berhasil kami buat. Terlebih untuk memenuhi kewajiban mata kuliah :green[Logika Pemrograman Komputer] dan memiliki tujuan mempermudah pekerjaan staff laboratorium serta para analis dalam menghitung jumlah :red[Mol] suatu zat')
    st.markdown('''Tim Penyusun :
1. Adyatma Fikry Fachrezi (NIM 2260002)
2. Faika Ahda Rosyadi (NIM 2260013)
3. Kalyca Agatha Zahra (NIM 2260024)
4. Nisa Widia Wulandari (NIM 2260035)
5. Rifqi Farihan Azis (NIM 2260046)
6. Zahda Aulia Bahrudin (NIM 2260057)''')
    st.markdown('Kami berharap web perhitungan :red[Mol] ini bermanfaat bagi para penggunanya. Wassalammualaikum Wr.Wb.')

else :
    st.write()


       

   