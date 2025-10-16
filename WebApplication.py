import streamlit as st

# Translation dictionary
TRANSLATIONS = {
    'ru': {
        'title': 'Давай проверим, правильный ли у тебя вес!',
        'subtitle': 'Привет, бабушка Люда! Надеюсь, тебе понравится этот сайт.',
        'instructions': 'Введите ниже параметры человека, которого хотите проверить.',
        'language': 'Язык',
        'sex': 'Пол:',
        'male': 'Мужчина',
        'female': 'Женщина',
        'weight': 'Масса (кг)',
        'age': 'Возраст (лет)',
        'height': 'Высота (м)',
        'your_bmi': 'Ваш BMI:',
        'overweight': '⚠️ У тебя лишний вес!!!',
        'underweight': '⚠️ У тебя недостаточный вес!!!',
        'ideal': '🏃🏻 Вы в идеальной форме!',
        'lose_weight': 'Вам нужно сбросить около {:.2f} кг, чтобы вернуться к нормальному весу.',
        'gain_weight': 'Вам нужно набрать около {:.2f} кг, чтобы вернуться к нормальному весу.',
        'min_weight': 'Рекомендуемый минимальный вес:',
        'max_weight': 'Рекомендуемый максимальный вес:',
        'bmi_category': 'Категория BMI:',
        'severely_underweight': 'Сильный недостаточный вес',
        'moderately_underweight': 'Умеренный недостаточный вес',
        'mildly_underweight': 'Легкий недостаточный вес',
        'normal': 'Нормальный вес',
        'overweight_cat': 'Избыточный вес',
        'obese_class1': 'Ожирение I степени',
        'obese_class2': 'Ожирение II степени',
        'obese_class3': 'Ожирение III степени'
    },
    'it': {
        'title': 'Controlliamo se hai il peso giusto!',
        'subtitle': 'Ciao, nonna Luda! Spero che questo sito ti piaccia.',
        'instructions': 'Inserisci i parametri della persona che vuoi controllare.',
        'language': 'Lingua',
        'sex': 'Sesso:',
        'male': 'Maschio',
        'female': 'Femmina',
        'weight': 'Peso (kg)',
        'age': 'Età (anni)',
        'height': 'Altezza (m)',
        'your_bmi': 'Il tuo BMI:',
        'overweight': '⚠️ Sei in sovrappeso!!!',
        'underweight': '⚠️ Sei sottopeso!!!',
        'ideal': '🏃🏻 Sei in forma ideale!',
        'lose_weight': 'Devi perdere circa {:.2f} kg per tornare al peso normale.',
        'gain_weight': 'Devi guadagnare circa {:.2f} kg per tornare al peso normale.',
        'min_weight': 'Peso minimo raccomandato:',
        'max_weight': 'Peso massimo raccomandato:',
        'bmi_category': 'Categoria BMI:',
        'severely_underweight': 'Grave sottopeso',
        'moderately_underweight': 'Moderato sottopeso',
        'mildly_underweight': 'Lieve sottopeso',
        'normal': 'Peso normale',
        'overweight_cat': 'Sovrappeso',
        'obese_class1': 'Obesità di classe I',
        'obese_class2': 'Obesità di classe II',
        'obese_class3': 'Obesità di classe III'
    },
    'en': {
        'title': "Let's check if you have the right weight!",
        'subtitle': 'Hello, Grandma Luda! I hope you like this website.',
        'instructions': 'Enter the parameters of the person you want to check below.',
        'language': 'Language',
        'sex': 'Sex:',
        'male': 'Male',
        'female': 'Female',
        'weight': 'Weight (kg)',
        'age': 'Age (years)',
        'height': 'Height (m)',
        'your_bmi': 'Your BMI:',
        'overweight': '⚠️ You are overweight!!!',
        'underweight': '⚠️ You are underweight!!!',
        'ideal': '🏃🏻 You are in perfect shape!',
        'lose_weight': 'You need to lose about {:.2f} kg to return to normal weight.',
        'gain_weight': 'You need to gain about {:.2f} kg to return to normal weight.',
        'min_weight': 'Recommended minimum weight:',
        'max_weight': 'Recommended maximum weight:',
        'bmi_category': 'BMI Category:',
        'severely_underweight': 'Severely underweight',
        'moderately_underweight': 'Moderately underweight',
        'mildly_underweight': 'Mildly underweight',
        'normal': 'Normal weight',
        'overweight_cat': 'Overweight',
        'obese_class1': 'Obese Class I',
        'obese_class2': 'Obese Class II',
        'obese_class3': 'Obese Class III'
    }
}

def get_bmi_range(sex, age):
    """
    Returns normal BMI values based on updated medical guidelines.
    Uses WHO and CDC criteria for different age groups.
    """
    if age < 2:
        # For very young children, BMI is not the best tool
        return 14.0, 18.0
    elif age < 18:
        # For children and adolescents, specific percentiles are used by age and sex
        # These are approximate values based on 5th and 85th percentiles
        if sex == "male":
            if 2 <= age <= 5:
                return 14.0, 17.5
            elif 6 <= age <= 9:
                return 14.0, 19.0
            elif 10 <= age <= 13:
                return 15.0, 22.0
            else:  # 14-17
                return 17.0, 24.5
        else:  # female
            if 2 <= age <= 5:
                return 13.5, 17.0
            elif 6 <= age <= 9:
                return 13.5, 18.5
            elif 10 <= age <= 13:
                return 15.0, 22.5
            else:  # 14-17
                return 17.5, 24.5
    elif age >= 65:
        # For elderly, a slightly higher BMI is protective
        # Based on recent studies showing benefits with BMI 23-30
        return 23.0, 30.0
    else:
        # Adults (18-64 years) - WHO Standard
        return 18.5, 24.9

def get_bmi_category(bmi, age):
    """
    Determines BMI category based on WHO standards for adults
    and adapted criteria for other age groups.
    """
    if age >= 18:
        if bmi < 16.0:
            return 'severely_underweight'
        elif bmi < 17.0:
            return 'moderately_underweight'
        elif bmi < 18.5:
            return 'mildly_underweight'
        elif bmi < 25.0:
            return 'normal'
        elif bmi < 30.0:
            return 'overweight_cat'
        elif bmi < 35.0:
            return 'obese_class1'
        elif bmi < 40.0:
            return 'obese_class2'
        else:
            return 'obese_class3'
    else:
        # For children/adolescents, simplified categories
        bmi_min, bmi_max = get_bmi_range("male", age)
        if bmi < bmi_min:
            return 'underweight'
        elif bmi <= bmi_max:
            return 'normal'
        else:
            return 'overweight_cat'

# Language initialization
if 'language' not in st.session_state:
    st.session_state.language = 'ru'

# Language selection in sidebar
with st.sidebar:
    lang_options = {'Русский': 'ru', 'Italiano': 'it', 'English': 'en'}
    selected_lang = st.selectbox(
        '🌍 ' + TRANSLATIONS[st.session_state.language]['language'],
        options=list(lang_options.keys()),
        index=list(lang_options.values()).index(st.session_state.language)
    )
    st.session_state.language = lang_options[selected_lang]

# Get translations for selected language
t = TRANSLATIONS[st.session_state.language]

# Header
st.write(f"# {t['title']}")
st.write(f"### {t['subtitle']}")
st.write(f"### {t['instructions']}")
st.divider()

# Sex selection
sex_options = {t['male']: 'male', t['female']: 'female'}
selected_sex = st.radio(t['sex'], options=list(sex_options.keys()))
sex = sex_options[selected_sex]

# Input for weight, age and height with validation
col1, col2, col3 = st.columns(3)

with col1:
    weight = st.number_input(t['weight'], min_value=0.5, max_value=500.0, value=50.0, step=0.5)

with col2:
    age = st.number_input(t['age'], min_value=1, max_value=120, value=25, step=1)

with col3:
    height = st.number_input(t['height'], min_value=0.30, max_value=2.50, value=1.70, step=0.01)

# BMI calculation
if weight > 0 and height > 0 and age > 0:
    bmi = weight / (height ** 2)
    
    # Get normal BMI range
    bmi_min, bmi_max = get_bmi_range(sex, age)
    
    # Calculate minimum and maximum weights
    weight_min = bmi_min * height * height
    weight_max = bmi_max * height * height
    
    # Display BMI
    st.write(f'### {t["your_bmi"]} {round(bmi, 2)}')
    
    # Show BMI category for adults
    if age >= 18:
        category = get_bmi_category(bmi, age)
        st.write(f'**{t["bmi_category"]}** {t[category]}')
    
    st.divider()
    
    # Display results with recommendations
    if bmi > bmi_max:
        st.write(f'# {t["overweight"]}')
        weight_to_lose = weight - weight_max
        st.write(f'### {t["lose_weight"].format(weight_to_lose)}')
        st.info(f'{t["max_weight"]} {round(weight_max, 2)} kg')
        
    elif bmi < bmi_min:
        st.write(f'# {t["underweight"]}')
        weight_to_gain = weight_min - weight
        st.write(f'### {t["gain_weight"].format(weight_to_gain)}')
        st.info(f'{t["min_weight"]} {round(weight_min, 2)} kg')
        
    else:
        st.write(f'# {t["ideal"]}')
        st.success(f'{t["min_weight"]} {round(weight_min, 2)} kg')
        st.success(f'{t["max_weight"]} {round(weight_max, 2)} kg')
    
    # Visual BMI display
    st.divider()
    
    # Colored progress bar to visualize BMI
    if age >= 18:
        # Scale from 15 to 40 for adults
        min_scale, max_scale = 15, 40
        normalized_bmi = (bmi - min_scale) / (max_scale - min_scale)
        normalized_bmi = max(0, min(1, normalized_bmi))  # Clamp between 0 and 1
        
        st.write("#### BMI Range Visualization")
        st.progress(normalized_bmi)
        
        # Legend
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.caption("< 18.5\nUnderweight")
        with col2:
            st.caption("18.5-24.9\nNormal")
        with col3:
            st.caption("25-29.9\nOverweight")
        with col4:
            st.caption("≥ 30\nObese")
