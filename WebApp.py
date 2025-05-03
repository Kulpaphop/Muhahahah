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

    if bmi < 18.5:
        category = "Underweight"
        if gender == "Female":
            image_url = ""
        else:
            image_url = ""
        st.warning(f"Category: {category}")
    elif bmi < 24.9:
        category = "Normal weight"
        if gender == "Female":
            image_url = ""
        else:
            image_url = ""
        st.success(f"Category: {category}")
    elif bmi < 29.9:
        category = "Overweight"
        if gender == "Female":
            image_url = ""
        else:
            image_url = ""
        st.info(f"Category: {category}")
    elif bmi < 34.9:
        category = "Obesity"
        if gender == "Female":
            image_url = "https://img.freepik.com/premium-vector/red-hair-woman-overweight-icon-cartoon-of-red-hair-woman-overweight-vector-icon-for-web-design-isolated-on-white-background_98402-34733.jpg"
        else:
            image_url = ""
        st.error(f"Category: {category}")
    else:
        category = "Extreme Obesity"
        if gender == "Female":
            image_url = "https://tse3.mm.bing.net/th/id/OIP.3pUGtxzJZ-4pYmlo-VhFmQAAAA?w=358&h=626&rs=1&pid=ImgDetMain"
        else:
            image_url = "https://png.pngtree.com/png-clipart/20240314/original/pngtree-sad-fat-cute-man-png-image_14589849.png"
        st.error(f"Category: {category}")

    st.image(image_url, caption=f"{bmi:.2f}", width=300)

    if gender == "Female":
        st.info("Stay healthy and keep shining!")
    else:
        st.info("Stay strong and maintain a healthy lifestyle!")
