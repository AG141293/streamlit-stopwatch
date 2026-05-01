import streamlit as st
import time

# Initialize session state
if "running" not in st.session_state:
    st.session_state.running = False
if "start_time" not in st.session_state:
    st.session_state.start_time = 0
if "elapsed" not in st.session_state:
    st.session_state.elapsed = 0

st.title("⏱ Stopwatch")

# Calculate current time
if st.session_state.running:
    current_time = st.session_state.elapsed + (time.time() - st.session_state.start_time)
else:
    current_time = st.session_state.elapsed

# Display time
st.markdown(f"## {time.strftime('%H:%M:%S', time.gmtime(current_time))}")

# Buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Start"):
        if not st.session_state.running:
            st.session_state.running = True
            st.session_state.start_time = time.time()

with col2:
    if st.button("Stop"):
        if st.session_state.running:
            st.session_state.elapsed += time.time() - st.session_state.start_time
            st.session_state.running = False

with col3:
    if st.button("Reset"):
        st.session_state.running = False
        st.session_state.elapsed = 0

# Auto refresh WITHOUT blocking UI
if st.session_state.running:
    time.sleep(1)
    st.rerun()