# ⚖️ Weight Detector - BMI Calculator

A **multilingual web-based BMI calculator** built with **Streamlit** and **Python**, created with love for my Ukrainian grandmother to help her check if family members are in healthy shape.  
Now she'll never ask me again if someone needs to gain or lose weight! 💙💛

## 🌐 Live Demo

**Try it now:** [Weight Detector Web App](https://weightdetector.streamlit.app/)  
No installation required — start checking your BMI immediately in your browser!

---

## 🎯 Why This Project Exists

This app was made for my grandmother Luda, who always worries about whether her family members are eating enough or too much. Instead of answering the same questions repeatedly, I built her this simple tool so she can check for herself!

I hope it makes her happy! ❤️

---

## 🧩 Features

### 📊 Comprehensive BMI Analysis
- **Accurate BMI calculation** based on weight, height, age, and sex
- **Age-specific BMI ranges** following WHO and CDC guidelines:
  - Children (2-17 years): Age and sex-adjusted percentiles
  - Adults (18-64 years): Standard WHO categories
  - Elderly (65+ years): Adjusted ranges for better health outcomes
- **Detailed BMI categories** with 8 different classifications
- **Weight recommendations**: Shows exactly how much to gain/lose
- **Visual BMI range** with color-coded progress bar

### 🌍 Multi-Language Support
Full interface available in:
- 🇷🇺 **Русский** (Russian) - For Grandma Luda!
- 🇮🇹 **Italiano** (Italian)
- 🇬🇧 **English**

### 📱 User-Friendly Interface
- **Simple input fields** for weight, age, and height
- **Instant results** with clear visual feedback
- **Emoji indicators** for quick understanding (⚠️ for warnings, 🏃🏻 for healthy)
- **Responsive design** works on desktop, tablet, and mobile
- **Medical-grade accuracy** using validated BMI formulas

---

## 📦 Local Installation

If you want to run it locally or modify the code:

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/YourUsername/weight-detector.git
cd weight-detector
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
streamlit run WebApplication.py
```

4. **Open your browser**  
The app will automatically open at `http://localhost:8501`

---

## 🚀 Usage

### Quick Start Guide

1. **Select your language** from the sidebar (🌍 Language selector)
2. **Choose sex** (Male/Female) - affects BMI calculations for children
3. **Enter weight** in kilograms (0.5 - 500 kg)
4. **Enter age** in years (1 - 120 years)
5. **Enter height** in meters (0.30 - 2.50 m)
6. **View results instantly**:
   - Your current BMI score
   - BMI category classification
   - Weight recommendations (if needed)
   - Recommended healthy weight range
   - Visual BMI range indicator

### Understanding Your Results

**BMI Categories (Adults 18-64):**
- **< 16.0**: Severely underweight ⚠️
- **16.0 - 17.0**: Moderately underweight ⚠️
- **17.0 - 18.5**: Mildly underweight ⚠️
- **18.5 - 24.9**: Normal weight ✅
- **25.0 - 29.9**: Overweight ⚠️
- **30.0 - 34.9**: Obese Class I ⚠️
- **35.0 - 39.9**: Obese Class II ⚠️
- **≥ 40.0**: Obese Class III ⚠️

**Special Considerations:**
- Children (2-17): Uses age and sex-adjusted percentiles
- Elderly (65+): Healthy range is 23-30 BMI (slightly higher)
- Very young children (<2): BMI is less reliable, consult pediatrician

---

## 📁 Project Structure

```
weight-detector/
├── WebApplication.py      # Main Streamlit application
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

---

## 🔧 Technical Details

**Built with:**
- **Streamlit**: Modern web framework for data apps
- **Python**: Core programming language
- **WHO/CDC Guidelines**: Medical-grade BMI calculations

**Key Features:**
- Age-specific BMI ranges for accuracy across all age groups
- Sex-adjusted calculations for children and adolescents
- Special considerations for elderly population (65+)
- Multilingual support with complete translations
- Input validation to prevent errors
- Real-time calculations with instant feedback

**BMI Formula:**
```
BMI = weight (kg) / height² (m²)
```

**Age-Adjusted Ranges:**
- The app uses different BMI ranges based on extensive medical research
- Children's ranges follow CDC growth chart percentiles
- Elderly ranges account for protective effects of slightly higher BMI
- Adult ranges follow WHO international standards

---

## ⚠️ Medical Disclaimer

**IMPORTANT**: This tool is for informational and educational purposes only.

**Key Considerations:**
1. **BMI is a screening tool**, not a diagnostic tool
2. **Consult a healthcare professional** for personalized medical advice
3. **BMI limitations**: Does not distinguish between muscle and fat mass
4. **Athletes and bodybuilders** may have high BMI due to muscle mass
5. **Pregnant women** should consult their doctor for appropriate weight ranges
6. **Medical conditions** may require different healthy weight ranges
7. **Children under 2** require specialized pediatric assessment

**Before making health decisions:**
- Always consult with a qualified healthcare provider
- Consider other health indicators beyond BMI
- Account for individual body composition and medical history
- Never start extreme diets without medical supervision

---

## 💡 Why BMI Matters

BMI (Body Mass Index) is widely used by healthcare professionals worldwide because:
- **Simple and fast** screening tool for weight categories
- **Correlates with health risks** at population level
- **Standardized across countries** for consistency
- **No special equipment needed** - just weight and height
- **Validated by decades of research** linking BMI to health outcomes

**However, remember**: BMI is just one piece of the health puzzle. Body composition, fitness level, diet quality, and overall lifestyle are equally important!

---

## 🎯 Use Cases

This tool is perfect for:
- **Concerned grandmothers** checking on their grandchildren 👵
- **Families** tracking healthy weight ranges for all members
- **Individuals** monitoring their weight status over time
- **Parents** checking if their children are growing healthily
- **Health-conscious people** wanting quick BMI reference
- **Anyone** curious about their weight category

---

## 🌟 Special Thanks

This project exists because of:
- **Grandma Luda** - for always caring about our health (even when we're fine!)
- **Our family** - for being the guinea pigs for this app
- **Streamlit community** - for making web apps so easy to build
- **WHO and CDC** - for providing scientifically validated BMI guidelines

---

## 📊 Example Scenarios

**Scenario 1: Adult Male**
- Weight: 80 kg, Height: 1.80 m, Age: 30
- BMI: 24.7 (Normal weight)
- Result: "🏃🏻 You are in perfect shape!"

**Scenario 2: Teenager**
- Weight: 55 kg, Height: 1.65 m, Age: 15, Sex: Female
- BMI: 20.2
- Uses age-adjusted percentiles for accurate assessment

**Scenario 3: Senior**
- Weight: 75 kg, Height: 1.70 m, Age: 70
- BMI: 25.9
- Healthy range: 23-30 (protective for elderly)

---

## 🛠️ Future Enhancements

Planned features:
- [ ] BMI history tracking over time
- [ ] Ideal weight calculator with different formulas
- [ ] Waist-to-height ratio calculator
- [ ] Body fat percentage estimator
- [ ] Calorie needs calculator
- [ ] Printable health reports
- [ ] More language options
- [ ] Dark mode theme

---

## 📜 License

Made with ❤️ for family use. Feel free to use, modify, and share!

---

## 👤 About

Created by a loving grandson/granddaughter who got tired of answering the same health questions!

If you also have a worried grandmother, feel free to share this app with her. 😊

---

## 💬 Feedback

If you find this tool useful or have suggestions:
- Open an **Issue** for bugs or feature requests
- Share it with your worried relatives!
- Tell me if your grandmother likes it 😊

---

## 🙏 A Note to Grandma Luda

Я люблю тебя, бабушка, спасибо за идею! 😄

Ti voglio bene! ❤️

---

## ❓ FAQ

**Q: Is this medically accurate?**  
A: Yes! The app uses WHO and CDC validated BMI guidelines. However, always consult a doctor for medical decisions.

**Q: Why does my grandmother need this?**  
A: Because she worries about everyone's health and now she can check herself! 😊

**Q: Can I use this for my kids?**  
A: Yes! The app has special age-adjusted BMI ranges for children from 2-17 years.

**Q: What about muscle mass vs fat?**  
A: BMI doesn't distinguish between muscle and fat. Bodybuilders and athletes may appear "overweight" despite being very fit.

**Q: Why is the elderly range different?**  
A: Recent studies show that slightly higher BMI (23-30) is protective for people over 65, reducing mortality risk.

**Q: Can I add more languages?**  
A: Yes! The code is structured to easily add new translations. Feel free to contribute!

**Q: Is it free?**  
A: Completely free! Made with love, not for profit.

---

⭐ **If this helps your family stay healthy, please give it a star!** ⭐

---

**Made with love for Grandma Luda 💙💛**  
*Because family health matters, even when they're perfectly fine!*

