import pandas as pd
import streamlit as st
import datetime
import pickle

pickle_in = open("model.pkl","rb")
tsa1 = pickle.load(pickle_in)

pickle_in2 = open("model2.pkl","rb")
tsa2 = pickle.load(pickle_in2)

pickle_in3 = open("model3.pkl","rb")
tsa3 = pickle.load(pickle_in3)

pickle_in4 = open("model4.pkl","rb")
tsa4 = pickle.load(pickle_in4)

now = datetime.date.today()

def predSuhu(now, suhuIn):
    suhuPred = float(tsa1.predict(now)[0])
    suhuResult = round((suhuPred + suhuIn)/2)
    return suhuResult

def predKelembapan(now, kelembapanIn):
    kelembapanPred = float(tsa2.predict(now)[0])
    kelembapanResult = round((kelembapanPred + kelembapanIn)/2)
    return kelembapanResult

def predHujan(now, hujanIn):
    hujanPred = float(tsa3.predict(now)[0])
    hujanResult = round((hujanPred + hujanIn)/2)
    return hujanResult

def predAngin(now, anginIn):
    anginPred = float(tsa4.predict(now)[0])
    anginResult = round((anginPred + anginIn)/2)
    return anginResult*3.6

def nama_hari(urutan):
        if urutan == 0:
            return 'Senin'
        elif urutan == 1:
            return 'Selasa'
        elif urutan == 2:
            return 'Rabu'
        elif urutan == 3:
            return 'Kamis'
        elif urutan == 4:
            return 'Jumat'
        elif urutan == 5:
            return 'Sabtu'
        elif urutan == 6:
            return 'Minggu'

def jenisCuaca(curah_hujan):
    if curah_hujan >= 0 and curah_hujan <= 0.5:
        return 'Berawan'
    elif curah_hujan >= 0.5 and curah_hujan <= 20:
        return 'Hujan Ringan'
    elif curah_hujan >= 20 and curah_hujan <= 50:
        return 'Hujan Sedang'
    elif curah_hujan >= 50 and curah_hujan <= 100:
        return 'Hujan Lebat'
    elif curah_hujan >= 100 and curah_hujan <= 150:
        return 'Hujan Sangat Lebat'
    elif curah_hujan >= 150:
        return 'Hujan Ekstrem'
    else:
        return 'Cerah'

def jenisSuhu(suhu):
    if suhu >= 37:
        return 'Sangat Panas'
    elif suhu >= 30:
        return 'Terasa Panas'
    elif suhu >= 25:
        return 'Terasa Hangat'
    elif suhu >= 15:
        return 'Terasa Sejuk'
    elif suhu >= 10:
        return 'Terasa Dingin'
    elif suhu >= 5:
        return 'Sangat Dingin'
    else:
        return 'Terasa Beku'

def jenisAngin(kecepatan_angin):
    if kecepatan_angin >= 0 and kecepatan_angin <= 20:
        return 'Angin Lembut'
    elif kecepatan_angin >=20 and kecepatan_angin <=38:
        return 'Angin Menengah'
    elif kecepatan_angin >=62 and kecepatan_angin <=72:
        return 'Angin Kuat'
    elif kecepatan_angin >= 75:
        return 'Angin Badai'

now = datetime.date.today()
hari_ini = datetime.datetime.now().weekday()
get_hari_ini = nama_hari(hari_ini)

cuaca = '-'
cuaca1 = '-'
cuaca2 = '-'
cuaca3 = '-'

suhuButton = 0
kelembapanButton = 0
hujanButton = 0
anginButton = 0
suhu1 = 0
kelembapan1 = 0
hujan1 = 0
angin1 = 0
suhu2 = 0
kelembapan2 = 0
hujan2 = 0
angin2 = 0
suhu3 = 0
kelembapan3 = 0
hujan3 = 0
angin3 = 0

suhu_in = st.number_input(label='Suhu')
kelembapan_in = st.number_input(label='Kelembapan')
hujan_in = st.number_input(label='Curah Hujan')
angin_in = st.number_input(label='Kecepatan Angin')

if st.button("Predict"):
    suhuButton = predSuhu(now, suhu_in)
    kelembapanButton = predKelembapan(now, kelembapan_in)
    hujanButton = predHujan(now, hujan_in)
    anginButton = predAngin(now, angin_in)

# ================================= DAY 0 =================================

st.markdown("<h2 style='text-align: right; color: black;'>Sumber Maron Weather Prediction System</h2>", unsafe_allow_html=True)
st.header(':blue[Karangsuko, Kab.Malang]')
jam_hari_ini = datetime.datetime.now().strftime(str('%H:%M'))
st.write(jam_hari_ini)

cuaca = jenisCuaca(hujanButton)

st.header(f'Hari Ini, **{get_hari_ini} :green[{now}]**', divider='green')
st.write(f'Cuaca :', cuaca)
st.write(f'Suhu :', suhuButton, 'C',  f'seperti {jenisSuhu(suhuButton)}')
st.write(f'Kelembapan :', kelembapanButton, '%')
st.write(f'Kecepatan Angin :', anginButton, 'km/h',  f'seperti {jenisAngin(anginButton)}')
st.text('\n\n')

# ================================= DAY +1 =================================

h_plus_1 = datetime.date.today() + datetime.timedelta(days=1)
urutan_h1 = datetime.datetime.strptime(str(h_plus_1), '%Y-%m-%d').weekday()
get_h_plus_1 = nama_hari(urutan_h1)

suhu1 = predSuhu(h_plus_1, suhu_in)
kelembapan1 = predKelembapan(h_plus_1, kelembapan_in)
hujan1 = predHujan(h_plus_1, hujan_in)
angin1 = predAngin(h_plus_1, angin_in)
cuaca1 = jenisCuaca(hujan1)

st.header(f'**{get_h_plus_1}, :blue[{h_plus_1}]**', divider='blue')
st.write(f'Cuaca :', cuaca1)
st.write(f'Suhu :', suhu1,  f'seperti {jenisSuhu(suhu1)}')
st.write(f'Kelembapan :', kelembapan1)
st.write(f'Kecepatan Angin :', angin1,  f'seperti {jenisAngin(angin1)}')
st.text('\n\n')

# ================================= DAY +2 =================================

h_plus_2 = datetime.date.today() + datetime.timedelta(days=2)
urutan_h2 = datetime.datetime.strptime(str(h_plus_2), '%Y-%m-%d').weekday()
get_h_plus_2 = nama_hari(urutan_h2)

suhu2 = predSuhu(h_plus_2, suhu_in)
kelembapan2 = predKelembapan(h_plus_2, kelembapan_in)
hujan2 = predHujan(h_plus_2, hujan_in)
angin2 = predAngin(h_plus_2, angin_in)
cuaca2 = jenisCuaca(hujan2)

st.header(f'**{get_h_plus_2}, :blue[{h_plus_2}]**', divider='blue')
st.write(f'Cuaca :', cuaca2)
st.write(f'Suhu :', suhu2,  f'seperti {jenisSuhu(suhu2)}')
st.write(f'Kelembapan :', kelembapan2)
st.write(f'Kecepatan Angin :', angin2,  f'seperti {jenisAngin(angin2)}')
st.text('\n\n')

# ================================= DAY +2 =================================

h_plus_3 = datetime.date.today() + datetime.timedelta(days=3)
urutan_h3 = datetime.datetime.strptime(str(h_plus_3), '%Y-%m-%d').weekday()
get_h_plus_3 = nama_hari(urutan_h3)

suhu3 = predSuhu(h_plus_3, suhu_in)
kelembapan3 = predKelembapan(h_plus_3, kelembapan_in)
hujan3 = predHujan(h_plus_3, hujan_in)
angin3 = predAngin(h_plus_3, angin_in)
cuaca3 = jenisCuaca(hujan3)

st.header(f'**{get_h_plus_3}, :blue[{h_plus_3}]**', divider='blue')
st.write(f'Cuaca :', cuaca3)
st.write(f'Suhu :', suhu3,  f'seperti {jenisSuhu(suhu3)}')
st.write(f'Kelembapan :', kelembapan3)
st.write(f'Kecepatan Angin :', angin3,  f'seperti {jenisAngin(angin3)}')
st.text('\n\n')
