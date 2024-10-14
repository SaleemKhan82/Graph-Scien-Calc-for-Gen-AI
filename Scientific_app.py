import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt

# Set up the title and sidebar
st.title("Graphical and Scientific Calculator")

# Function to calculate and display scientific operations
def scientific_calculator():
    st.header("Scientific Calculator")
    
    num = st.number_input("Enter a number:", value=0.0, step=0.1)
    
    operation = st.selectbox("Choose an operation:", 
                             ["None", "Square", "Square Root", "Sine", "Cosine", "Tangent", "Logarithm", "Exponential"])
    
    result = None
    
    if operation == "Square":
        result = num ** 2
    elif operation == "Square Root":
        result = math.sqrt(num)
    elif operation == "Sine":
        result = math.sin(math.radians(num))
    elif operation == "Cosine":
        result = math.cos(math.radians(num))
    elif operation == "Tangent":
        result = math.tan(math.radians(num))
    elif operation == "Logarithm":
        if num > 0:
            result = math.log(num)
        else:
            st.error("Logarithm is undefined for numbers <= 0")
    elif operation == "Exponential":
        result = math.exp(num)
    
    if result is not None:
        st.write(f"The result of {operation.lower()} of {num} is {result}")

# Function to plot a graph of some functions
def plot_graph():
    st.header("Graph Plotter")
    
    func = st.selectbox("Choose a function to plot:", 
                        ["None", "Sine", "Cosine", "Tangent", "Exponential"])
    
    x = np.linspace(-10, 10, 400)
    y = None
    
    if func == "Sine":
        y = np.sin(x)
    elif func == "Cosine":
        y = np.cos(x)
    elif func == "Tangent":
        y = np.tan(x)
    elif func == "Exponential":
        y = np.exp(x)
    
    if y is not None:
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_title(f"{func} Function")
        st.pyplot(fig)

# Function for basic arithmetic calculator
def basic_calculator():
    st.header("Basic Calculator")
    
    num1 = st.number_input("Enter first number:", value=0.0, step=0.1)
    num2 = st.number_input("Enter second number:", value=0.0, step=0.1)
    
    operation = st.selectbox("Choose an operation:", ["Add", "Subtract", "Multiply", "Divide"])
    
    result = None
    
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Cannot divide by zero!")
    
    if result is not None:
        st.write(f"The result of {operation.lower()} is: {result}")

# Sidebar navigation
option = st.sidebar.selectbox("Choose Calculator Type", ["Basic", "Scientific", "Graphical"])

if option == "Basic":
    basic_calculator()
elif option == "Scientific":
    scientific_calculator()
elif option == "Graphical":
    plot_graph()
