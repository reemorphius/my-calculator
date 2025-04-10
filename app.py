import streamlit as st
import math

st.set_page_config(page_title="Advanced Calculator", page_icon="🧮", layout="centered")

st.title("Advanced Calculator")
st.markdown("**Status:** designed by natirus")

st.write("This is an advanced calculator that supports basic and scientific operations. Enter your numbers and select an operation.")

col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("Enter first number", value=0.0, step=1.0)
with col2:
    num2 = st.number_input("Enter second number (if needed)", value=0.0, step=1.0)

operation = st.selectbox("Select operation", [
    "Addition (+)", 
    "Subtraction (-)", 
    "Multiplication (×)", 
    "Division (÷)", 
    "Power (x^y)", 
    "Logarithm (log base 10)", 
    "Sine (sin)", 
    "Cosine (cos)"
])

if st.button("Calculate"):
    try:
        if operation == "Addition (+)":
            result = num1 + num2
            st.success(f"Result: {num1} + {num2} = {result}")
        elif operation == "Subtraction (-)":
            result = num1 - num2
            st.success(f"Result: {num1} - {num2} = {result}")
        elif operation == "Multiplication (×)":
            result = num1 * num2
            st.success(f"Result: {num1} × {num2} = {result}")
        elif operation == "Division (÷)":
            if num2 == 0:
                st.error("Error: Division by zero is not allowed!")
            else:
                result = num1 / num2
                st.success(f"Result: {num1} ÷ {num2} = {result}")
        elif operation == "Power (x^y)":
            result = num1 ** num2
            st.success(f"Result: {num1}^{num2} = {result}")
        elif operation == "Logarithm (log base 10)":
            if num1 <= 0:
                st.error("Error: Logarithm is undefined for non-positive numbers!")
            else:
                result = math.log10(num1)
                st.success(f"Result: log10({num1}) = {result}")
        elif operation == "Sine (sin)":
            result = math.sin(math.radians(num1))
            st.success(f"Result: sin({num1}°) = {result}")
        elif operation == "Cosine (cos)":
            result = math.cos(math.radians(num1))
            st.success(f"Result: cos({num1}°) = {result}")
    except Exception as e:
        st.error(f"Error: {str(e)}")

st.markdown("---")
st.write("Built with Streamlit and Python 🐍")
