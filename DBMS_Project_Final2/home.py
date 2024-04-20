from time import sleep
import mysql.connector
import streamlit as st
import sys
#from streamlit.state.session_state import SessionState


db = mysql.connector.connect(
    
    host = "localhost",
    user = "root",
    password = "Duppu0903)()#",
    database = "mydb"
    
    
)

cr = db.cursor()
cr.execute("use mydb")

if "accountid" not in st.session_state:
    st.session_state["accountid"] = 15

if "sessionid" not in st.session_state:
    st.session_state["sessionid"] = 14
    
if "prodid" not in st.session_state:
    st.session_state["prodid"] = 33




st.set_page_config(initial_sidebar_state="collapsed")

st.session_state["pages"] = [r"C:\Users\vijva\Documents\DBMS\Project\pages\implementation.py",r"C:\Users\vijva\Documents\DBMS\Project\pages\cat.py",r"C:\Users\vijva\Documents\DBMS\Project\pages\prods.py",r"C:\Users\vijva\Documents\DBMS\Project\pages\cart.py"]
st.session_state["cur_page"] = 0
#st.session_state["attempts"] = 0

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

def updatea():
    st.session_state["attempts"]+=1
    #st.write(st.session_state["attempts"])
    st.error("Invalid username or password. Attempts left: {}".format(3-st.session_state["attempts"]))
    
    if(st.session_state["attempts"]!=3):
       #st.rerun()
       
       pass
    else:
        #st.write("fffff")
        #sleep(2)
        st.error("Maximum attempts reached. App closing...")
        sleep(2)
        return 0



        
def login_page(cr):
    max_attempts = 3
    st.title("Login Page")
    if "attempts" not in st.session_state:
        st.session_state["attempts"] = 0  

    #attempts = 0
    #st.session_state["attempts"] = 0
    #attempts = st.session_state["attempts"]
    #if st.session_state["attempts"]<max_attempts:
    username = st.text_input("EMail ID")
    password = st.text_input("Password", type="password")
    n = 9
    if st.button("Login") and n==9:
        # Check credentials here
        q = ("SELECT * FROM account WHERE emailID = %s AND Password = %s;")
        cr.execute(q,(username,password))

        recs = cr.fetchall()

        if(len(recs)==1):
            st.success("Logged in as {}".format(username))
            sleep(2)
            return 0
        else:
            #st.session_state["attempts"]+= 1
            s = updatea()
            if(s==0):
                
                #st.experimental_rerun()
                n=2
                return 2
            
            #st.error("Invalid username or password. Attempts left: {}".format(max_attempts-st.session_state["attempts"]-1))
            
    else:
        return 1
        
        

def mai(cr):
    log = login_page(cr)
    #sleep(5)
    
    
    if(log==0):
        st.write("success")
        #sleep(3)
        
        st.switch_page(r"pages\cat.py")
    if(log==2):
        st.stop()
        
        return
    
def home():
    
    a, b = st.columns(2)
    
    if(st.button("LOGIN as User")):
            st.switch_page(r"pages\implementation.py")
            
    if(st.button("Login as EMployee")):
        st.switch_page(r"pages\emplog.py")
    
    if(st.button("REGISTER")):
            st.switch_page(r"pages\reg.py")
            
   
            
    

# Separate 

home()