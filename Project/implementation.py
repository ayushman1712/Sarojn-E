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

cr = db.cursor()
cr.execute("use mydb")


st.set_page_config(initial_sidebar_state="collapsed")

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)



def page3():
    st.title("Page 3")
    st.write("This is Page 3")
    st.write("Some content on Page 3.")
    
def prods(cr, cate):
    
    st.write("enter prods")
    q = "select * from product where category_category_id = %d;"
    cr.execute(q,(cate))
    
    recs = cr.fetchall()
    
    for r in recs:
        st.write(r)
    
    

def cat(cr):
    cr.execute("select * from category;")
    recs = cr.fetchall()
    
    for r in recs:
        st.write(r[0])
        if(st.button(r[1])):
            prods(cr,r[0])
            

        
def login_page(cr):
    
    st.title("Login Page")

    username = st.text_input("EMail ID")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Check credentials here
        q = ("SELECT * FROM account WHERE emailID = %s AND Password = %s;")
        cr.execute(q,(username,password))

        recs = cr.fetchall()
        if(len(recs)==1):
            st.success("Logged in as {}".format(username))
            sleep(2)
            return True
        else:
            st.error("Invalid username or password")
            return False
        
        

def mai(cr):
    log = login_page(cr)
    #sleep(5)
    
    
    if(log):
        st.write("success")
        #sleep(3)
        
        st.switch_page(r"pages\cat.py")
    
        
        
        

        

def browse(cr):
    
    n = input("Would you like to look at the product categories? (y/n)")
    a = 0
    while(a==0):
        if(n.lower()=="y"):
            cr.execute("Select * from category;")
            for i,d in enumerate(cr):
                print(d)
            m = int(input("Select a category_id: "))
            cr.execute(f"Select * from Product where category_category_id = {m};")
            if(len(cr.fetchall())==0):
                print("invalid category")
                continue
            print("-------------------------")
            for i,d in enumerate(cr):
                print(d)
            m = int(input("Enter a product id: "))
            cr.execute(f"Select * from Product where ProductID = {m};")
            if(len(cr.fetchall())==0):
                print("Incorrect product id")
                continue
            print("--------------------------")
            for i,d in enumerate(cr):
                print(d)
                
            b = int(input("Would you like to:\n1. Buy\n2. Go back"))
            
                

#login_page(cr)
#mai(cr)
#test(cr)
import streamlit as st

# Define functions for each page (unchanged)
def page1():
    st.title("Page 1")
    st.write("This is Page 1")
    st.write("Some content on Page 1.")

def page2():
    st.title("Page 2")
    st.write("This is Page 2")
    st.write("Some content on Page 2.")

def page3():
    st.title("Page 3")
    st.write("This is Page 3")
    st.write("Some content on Page 3.")

def main():
    # Initialize session state
    current_page = st.session_state.get("current_page", "Page 1")

    # Navigation buttons directly in main content area
    if st.button("Page 1"):
        current_page = "Page 1"
    elif st.button("Page 2"):
        current_page = "Page 2"
    elif st.button("Page 3"):
        current_page = "Page 3"
    
    # Render current page based on session state
    if current_page == "Page 1":
        page1()
    elif current_page == "Page 2":
        page2()
    elif current_page == "Page 3":
        page3()

#mai(cr)

import streamlit as st

# Improved function for displaying products
def prods(cr, cate):
    q = "select * from product where category_category_id = %d;"
    cr.execute(q, (cate,))
    recs = cr.fetchall()
    for r in recs:
        st.write(r)

# Function for displaying categories and handling navigation
def content_page(cr):
    cr.execute("select * from category;")
    recs = cr.fetchall()
    for r in recs:
        if st.button(r[1]):
            st.session_state["current_page"] = "Products"  # Set session state for products page

# Separate function for login handling
def login_page(cr):
    st.title("Login Page")
    username = st.text_input("EMail ID")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        q = ("SELECT * FROM account WHERE emailID = %s AND Password = %s;")
        cr.execute(q, (username, password))
        recs = cr.fetchall()
        if (len(recs) == 1):
            st.success("Logged in as {}".format(username))
            st.session_state["logged_in"] = True  # Store login status
            return True
        else:
            st.error("Invalid username or password")
            return False

def main(cr):
    # Check for existing login status
    logged_in = st.session_state.get("logged_in", False)

    # Render login page only if not logged in
    if not logged_in:
        log = login_page(cr)

    # Proceed if login successful
    if log:
        current_page = st.session_state.get("current_page")
        if current_page == "Products":
            content_page(cr)
            st.session_state["current_page"] = None  # Clear session state after displaying products

mai(cr)









            
            
                
                
                
            
        
    


        
        
        
        
        
        
        
        
        
    
    
