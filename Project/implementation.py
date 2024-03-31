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

st.session_state["pages"] = [r"C:\Users\vijva\Documents\DBMS\Project\pages\implementation.py",r"C:\Users\vijva\Documents\DBMS\Project\pages\cat.py",r"C:\Users\vijva\Documents\DBMS\Project\pages\prods.py",r"C:\Users\vijva\Documents\DBMS\Project\pages\cart.py"]
st.session_state["cur_page"] = 0

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
        
        st.switch_page(r"C:\Users\vijva\Documents\DBMS\Project\pages\cat.py")
    
        
        
        

        


# Separate 

mai(cr)
