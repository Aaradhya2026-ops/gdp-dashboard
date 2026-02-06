import streamlit as s
from PIL import Image
import time

#Text styles
s.write("Hello World")
s.title('This is the title')
s.header('This is the header')
s.subheader('This is the subheader')
s.write('Hello')
s.caption('This is the caption')
s.code('This is the code')

#Adding images
s.title("________________________________")
s.title("This is my pc background")
image=Image.open('abc.png')
s.image(image)

#Adding buttons
if s.button("Click me for a surprise"):
    s.balloons()

#Adding Checkbox
s.title("________________________________")
s.write("Favourite sports:")
check1=s.checkbox('Cricket')
check2=s.checkbox('Football')
check3=s.checkbox('Badminton')

#Adding Selectbox
s.title("________________________________")
selected_country= s.selectbox('Select your country:',
['','India','Canada','France','UK'])
s.write(f"You've selected {selected_country}.Good choice!")

#Adding Multiselect
s.title("________________________________")
colours=s.multiselect("Select colours",['Red','Blue','Green','Yellow'])
s.write(f"selected colour(s)= {colours}")

#Adding Slider
s.title("________________________________")
age=s.slider("Select your age:",min_value=0,max_value=100,value=0)
s.write(f"Selected Age= {age}")

#Adding Selected Value Slider
s.title("________________________________")
s.write("Please rate my website")
rating=s.select_slider("Select rating:",options=[0,1,2,3,4,5])
if rating==0:
    s.write("Please select a rating")
elif rating == 1:
    s.write("I'm sorry! Please let me know where can I improve.")
elif rating== 2:
    s.write(f"You've rated us a {rating}.Please tell us where we went wrong.")
elif rating== 3:
    s.write(f"You've rated us a {rating}.Please tell us where we went wrong.")
elif rating== 4:
    s.write(f"You've rated us a {rating}.Thank you so much. I really appreciate your review")
else:
    s.write(f"You've rated us a {rating}.Thank you so much. I really appreciate your review.")
#s.write(f"Selected rating: {rating}. Thank you for your time !")

#Adding Text input
s.title("________________________________")
name=s.text_input("Enter Your Name:")
s.write(f"Hello, {name}!")

#Adding Text Area 
s.title("________________________________")
review=s.text_area("Leave a review",height=67)
s.write(f"Your review: {review}")

#Adding File Uploader
s.title("________________________________")
file= s.file_uploader("Choose an Image", type=['jpg','png','jpeg'])
if file is not None:
    s.write("File Uploaded!")
    s.image(file)

#Adding Audio file
s.title("________________________________")
s.write('Carols:')
file='song.mp3'
s.audio(file,format='audio/mp3')

#Adding Video file
s.title("________________________________")
s.write("Video file:")
file='Video.mp4'
s.video(file,format='video/mp4',start_time=4)

#Adding Sidebar
s.title("________________________________")
name=s.sidebar.text_input("Enter your name","")
s.write(f"Hello, {name}!")

#Adding Columns
s.title("________________________________")
col1,col2= s.columns(2)
with col1:
    s.header("Column 1")
    s.write("This is column 1.")
with col2:
    s.header("Column 2")
    s.write("This is column 2")

#Adding Tabs
s.title("________________________________")
tabs=s.tabs(["Tab 1",'Tab 2'])
with tabs[0]:
    s.header('Tab 1')
with tabs[1]:
    s.header("Tab 2")

#Adding Containers
s.title("________________________________")
with s.container():
    s.write("This is inside the container")
s.write("This is outside the container")

#Adding Spinner
s.title("________________________________")
with s.spinner("Almost there..."):
    time.sleep(5)
s.success("Done!")

#Adding Success and Warning buttons
s.title("________________________________")
s.warning("This is a warning message.")
s.success("This is a success message.")

#Creating Forms
s.title("________________________________")
with s.form("MyForm"):
    name=s.text_input("Enter your name","")
    age=s.number_input("Enter your age",min_value=0,max_value=100)
    hobbies= s.multiselect("Select your hobbies:",['Reading','Gaming','Traveling','Sports'])
    submitted= s.form_submit_button("Submit")
if submitted==True:
    s.success("You have submitted the form.")
