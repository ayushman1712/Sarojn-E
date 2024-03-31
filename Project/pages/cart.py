from time import sleep
import mysql.connector
import streamlit as st
#from streamlit.state.session_state import SessionState

db = mysql.connector.connect(
    
    host = "localhost",
    user = "root",
    password = "Duppu0903)()#",
    database = "mydb"
    
    
)

st.set_page_config(initial_sidebar_state="collapsed")
st.markdown("""
    <style>
    [data-testid="collapsedControl"] { display: none }
    </style>
""", unsafe_allow_html=True)




global cr
cr = db.cursor()
cr.execute("use mydb")


def view_cart():
  if len(st.session_state.cart) > 0:
    
    st.subheader("Your Cart")
    for product_id, quantity in st.session_state.cart.items():
      st.write(product_id)
      # Fetch product details based on product_id
      cr.execute(f"select Name, Cost from product where ProductID = {product_id}")
      product_data = cr.fetchone()
      # Display product details and quantity
      st.write(f"{product_data[0]} - ${product_data[1]:.2f} (x{quantity})")
      # Add buttons for update quantity or remove from cart (optional)

# Call view_cart() after the product listing section
view_cart()