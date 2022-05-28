# Custom imports 
from multipage import MultiPage, st
from pages import data_upload, sign_form #, machine_learning, metadata, data_visualize, redundant, inference # import your pages here

# Create an instance of the app 
app = MultiPage()

st.set_page_config(
page_title="Ex-stream-ly Cool App",
page_icon="random",
layout="wide",
initial_sidebar_state="collapsed")


# Add all your applications (pages) here
app.add_page("Sighn Form", sign_form.app)
app.add_page("Upload Data", data_upload.app)
# app.add_page("Machine Learning", machine_learning.app)
# app.add_page("Data Analysis",data_visualize.app)
# app.add_page("Y-Parameter Optimization",redundant.app)

# The main app
app.run()