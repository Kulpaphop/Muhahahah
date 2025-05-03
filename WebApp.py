import streamlit as st

page_bg_img = """
<style>
.st-emotion-cache-1yiq2ps {
    background-image: url('https://images.hdqwalls.com/download/purple-curves-8k-tf-3840x2400.jpg');
    background-size: cover;
    background-position: center
    background-repeat: no-repeat;
    background-attachment: fixed;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("BMI Calculator")
gender = st.selectbox("Select Gender", ["Male", "Female"])
weight = st.slider("Select your weight (kg):", min_value=0.0, max_value=200.0, value=70.0, step=0.1)
height_cm = st.slider("Select your height (cm):", min_value=50.0, max_value=250.0, value=170.0, step=0.1)

if weight > 0 and height_cm > 0:
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)

    st.write(f"Your BMI is: {bmi:.2f}")
    
    # Display BMI result with a smaller image
    st.image(
        "https://png.pngtree.com/png-clipart/20240314/original/pngtree-sad-fat-cute-man-png-image_14589849.png",
        caption=f"{bmi:.2f}",
        width=300
    )
    if bmi < 18.5:
        st.warning("Category: Underweight")
    elif 18.5 <= bmi < 24.9:
        st.success("Category: Normal weight")
    elif 25.0 <= bmi < 29.9:
        st.info("Category: Overweight")
    elif 30.0 <= bmi < 34.9:
        st.error("Category: Obesity")
    else:
        st.error("Category: Extreme Obesity")

    if gender == "Male":
        st.info("Stay strong and maintain a healthy lifestyle!")
    elif gender == "Female":
        st.info("Stay healthy and keep shining!")
        
    
        
