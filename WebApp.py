import streamlit as st

st.markdown(
    """
    <style>
    .st-emotion-cache-1yiq2ps {
        background-image: url('https://images.hdqwalls.com/download/purple-curves-8k-tf-3840x2400.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("BMI Calculator")
gender = st.selectbox("Select Gender", ["Male", "Female"])
weight = st.slider("Select your weight (kg):", 0.0, 200.0, 70.0, 0.1)
height_cm = st.slider("Select your height (cm):", 50.0, 250.0, 170.0, 0.1)

if weight > 0 and height_cm > 0:
    bmi = weight / ((height_cm / 100) ** 2)
    st.write(f"Your BMI is: {bmi:.2f}")

    category, image_url = (
        ("Underweight", "underweight.jpg") if bmi < 18.5 else
        ("Normal weight", "normal.jpg") if bmi < 24.9 else
        ("Overweight", "overweight.jpg") if bmi < 29.9 else
        ("Obesity", "obesity.jpg") if bmi < 34.9 else
        ("Extreme Obesity", "extreme_obesity.jpg")
    )

    st.error(f"Category: {category}") if bmi >= 30.0 else (
        st.warning(f"Category: {category}") if bmi < 18.5 else
        st.success(f"Category: {category}") if bmi < 24.9 else
        st.info(f"Category: {category}")
    )

    st.image(image_url, caption=f"{bmi:.2f}", width=300)
    st.info("Stay healthy and keep shining!" if gender == "Female" else "Stay strong and maintain a healthy lifestyle!")
