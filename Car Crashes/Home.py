import streamlit as st
st.title('🚗 Car Crashes Dashboard')
# st.markdown("<h1 style='test-align:center'>🚗 Car Crashes Dashboard</h1>",unsafe_allow_html=True)
# sidebar
# st.sidebar.title("Navigation")
# page=st.sidebar.radio("Go to",["Home","About","Data Exploration"])
# add an image
st.image('assets/car1.webp',use_container_width=True)
st.markdown('----')
# description
st.markdown("<h2 style='text-align : cneter'>Dataset Overview</h2>",unsafe_allow_html=True)
st.write('''Welcome to the Car Crashes Dashboard !
The Car Crashes Dataset contains the complete analysis of accidents on many criteria. Some of them are listed below :''')
st.markdown('----')
st.markdown('## ✨Key Features')
st.write('''
- State
- Crashes involving Alcohol
- Crahses involving Speed
- Crashes where driver was not distracted
- Drivers involved with no previous accidents
- Average insurance premium
- Average insurance losses
''')
st.markdown('----')
st.markdown('## 📌What you will Learn')
st.write('''In this dashboard we have made the comparison easir by using Interactive Charts📊 & Visualizations
At the end of this dashboard, you will be able to understand the given points:
- Crash statistics by state
- Effect of speeding, alcohol, and distracted driving
- Insurance premium and losses comparison
''')
st.info('💁‍♂️IF YOU ARE READY TO EXPLORE THIS DASHBOARD , THEN CHOOSE YOUR PAGES FROM THE LEFT SIDEBAR👈')

# footer
st.markdown('----')
st.header('made with lots of love 💗')

