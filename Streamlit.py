#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install streamlit')


# In[2]:


import os
import streamlit as st
#import face_recognition

def is_face_in_image(image_path):
    image = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(image)
    return len(face_locations) > 0

def main():
    st.title('Face Detection')
    uploaded_file = st.file_uploader('Choose an image...', type=['jpg', 'png', 'jpeg'])
    
    if uploaded_file is not None:
        with open('temp_image.jpg', 'wb') as f:
            f.write(uploaded_file.getvalue())
            
        result = is_face_in_image('temp_image.jpg')
        
        if result:
            st.write('Result: Face detected in the image.')
        else:
            st.write('Result: No face detected in the image.')
        
if __name__ == '__main__':
    main()


# In[ ]:




