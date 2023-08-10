#!/usr/bin/env python
# coding: utf-8

# In[4]:


pip install flask


# In[6]:


pip install streamlit


# In[9]:


pip install opencv-python


# In[10]:


from flask import Flask
import streamlit as st
import io
import cv2

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, this is a Streamlit app embedded in Flask!"

@app.route('/face_detection', methods=['GET', 'POST'])
def face_detection():
    if st.button("Open Webcam"):
        stframe = st.empty()
        cap = cv2.VideoCapture(0)

        while st.button("Close Webcam") == False:
            ret, frame = cap.read()

            if not ret:
                break

            # Convert the frame to grayscale for face detection
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Load a pre-trained face detection model from OpenCV
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)

            # Draw rectangles around detected faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Convert OpenCV image to Streamlit format
            stframe.image(frame, channels='BGR', use_column_width=True)

        cap.release()

if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:





# In[ ]:





# In[ ]:




