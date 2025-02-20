import streamlit as st

# دالة التوصية الغذائية
def recommend_food(age, weight, health_status, activity, preference):
    if health_status == "Diabetes":
        return ("Low-carb, High-protein food", "Your cat has diabetes, so a low-carb, high-protein food is recommended.")
    elif health_status == "Kidney Problems":
        return ("Low-protein, Renal diet food", "Cats with kidney problems need a special renal diet with reduced protein.")
    elif age < 1:
        return ("High-calorie kitten food", "Kittens need high-calorie food to support their growth.")
    elif weight > 5 and activity == "Low":
        return ("Weight-control food", "Your cat is overweight and needs weight-control food.")
    elif activity == "High":
        return ("High-energy food", "Since your cat is very active, it needs high-energy food.")
    elif preference == "Natural":
        return ("Natural food", "You can try organic or natural food options.")
    else:
        return ("Balanced adult food", "A balanced food is suitable for most adult cats.")

# واجهة المستخدم باستخدام Streamlit
st.title("Cat Nutrition Advisor")
st.write("Hello! Let's help you find the best food for your cat. 🐱")

# مدخلات المستخدم
age = st.number_input("Cat's Age (in years)", min_value=0.0, step=0.1)
weight = st.number_input("Cat's Weight (kg)", min_value=0.0, step=0.1)
activity = st.selectbox("Activity Level", ["Low", "Medium", "High"])
health = st.selectbox("Health Status", ["Healthy", "Diabetes", "Kidney Problems"])
preference = st.selectbox("Food Preference", ["Any", "Natural"])

# التوصية بعد الضغط على الزر
if st.button("Get Recommendation"):
    recommendation, explanation = recommend_food(age, weight, health, activity, preference)
    st.success(f"Recommended Food: {recommendation}")
    st.info(f"Explanation: {explanation}")
    st.write("""
    **Additional Tips:**
    - Ensure fresh water is always available.
    - Consult a vet for any health concerns.
    - Consider regular check-ups to keep your cat healthy.
    """)
