import streamlit as st

st.write("# Давай проверим, правильный ли у тебя вес!")
st.write("### Привет, бабушка Люда! Надеюсь, тебе понравится этот сайт.")
st.write("### Введите ниже параметры человека, которого хотите проверить.")

st.divider()

# Funzione per determinare i valori di BMI normali in base al sesso, età e anzianità
def get_bmi_range(sesso, eta):
    if eta < 18:
        # Valori per bambini e adolescenti (esempio di percentili)
        if sesso == "Мужчина":
            if eta <= 5:
                return 14.0, 18.0  # Bambini piccoli
            elif 6 <= eta <= 12:
                return 14.5, 20.0  # Bambini più grandi
            else:
                return 17.5, 24.0  # Adolescenti maschi
        else:
            if eta <= 5:
                return 13.5, 17.5  # Bambine piccole
            elif 6 <= eta <= 12:
                return 14.0, 19.0  # Bambine più grandi
            else:
                return 16.5, 23.5  # Adolescenti femmine
    elif eta >= 65:
        # Valori per anziani
        return 22.0, 29.0  # Intervallo per anziani (maschi e femmine)
    else:
        # Valori normali per adulti
        if sesso == "Женщина":
            return 20.0, 25.0  # Intervallo per maschi adulti
        else:
            return 18.5, 24.9  # Intervallo per femmine adulte

# Selezione del sesso
sesso = st.radio("Пол: ", ("Мужчина", "Женщина"))

# Input per peso
peso = st.number_input('Масса', value=50.0, step=0.5)

if peso > 0:
    # Input per età
    eta = st.number_input('возраст', value=10, step=1)

if eta > 0:
    # Input per altezza
    altezza = st.number_input('Высота', value=1.6, step=0.05)

# Calcolo del BMI
bmi_ora = peso / (altezza ** 2)

# Ottieni l'intervallo di BMI normale in base al sesso, età e anzianità
bmi_min, bmi_max = get_bmi_range(sesso, eta)

# Calcola i pesi minimi e massimi in base all'intervallo di BMI
peso_min = bmi_min * altezza * altezza
peso_max = bmi_max * altezza * altezza

st.write('### Ваш BMI :', round(bmi_ora,2))

st.divider()

if(bmi_ora > bmi_max):
  st.write('# У тебя лишний вес!!!')
 # st.write('# Минимальный вес:',PesoMin)
 # st.write('# Тяжёлый вес:',PesoMax)
  
  # Calcolo di quanto peso perdere per rientrare nel normopeso
  peso_da_perdere = peso - peso_max
  st.write(f'### Вам нужно сбросить около {round(peso_da_perdere, 2)}кг, чтобы вернуться к нормальному весу.')

elif (bmi_ora < bmi_min):
  st.write('# У тебя недостаточный вес!!!')
 # st.write('### Минимальный вес:',PesoMin)
 # st.write('### Тяжёлый вес',PesoMax)
  
  # Calcolo di quanto peso mettere su per rientrare nel normopeso
  peso_da_guadagnare = peso_min - peso
  st.write(f'### Вам нужно набрать около {round(peso_da_guadagnare, 2)}кг, чтобы вернуться к нормальному весу.')
    

else:
  st.write('# Вы в идеальной форме!')
  st.write('### Рекомендуемый минимальный вес:', round(peso_min, 2), 'kg')
  st.write('### Рекомендуемый максимальный вес:', round(peso_max, 2), 'kg')
