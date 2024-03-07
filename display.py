import streamlit as st

selected_video = st.selectbox("Select a video you want to watch", ["Select one video", "Overview", 
                                                                   "Set Up an Environment", 
                                                                   "Data Structures: List"], index=0)

if selected_video == "Overview":
    my_video = open("videos/overview.mkv", "rb")
    my_video_in_bytes = my_video.read()
    st.video(my_video_in_bytes)

if selected_video == "Set Up an Environment":
    my_video = open("videos/environment.mkv", "rb")
    my_video_in_bytes = my_video.read()
    st.video(my_video_in_bytes)

if selected_video == "Data Structures: List":
    my_video = open("videos/data_structures_list.mkv", "rb")
    my_video_in_bytes = my_video.read()
    st.video(my_video_in_bytes)
