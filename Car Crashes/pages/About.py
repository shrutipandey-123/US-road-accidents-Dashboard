import streamlit as st
# for heading : header is use
st.header('About this Dashboard 📅')

st.write('''
Here's the quick information about this Dashboard! 👇
         
This dashborad is created to make people aware about the consequences of car accident and the reason behind these crashes.
We have collected the data with proper research. After reading dashboard user will understand the actual reason behind the crashes with proper analysis.  ''')

st.markdown('---')

# heading : dataset information
st.markdown('Dataset Information 📅')
st.info('''This dataset is taken from the 'Seaborn' library. For further information about this library you can visit it's official website ,https://seaborn.pydata.org
The dashboard is completely based on only US data.''')
st.write(''' 
Columns and its short description is given below 👇''')
st.info('This will help you to understand the columns beacuse in dataset column names is written in short form.')
st.write(''' 
- state : Names of US states
- total : Total crashes per billion miles
- speeding : Proportion of car crashes with speeding as one of the factor
- alcohol :  Proportion of car crashes in which alcohol is involved as the factor
- not_distracted : Proportion of car crashes in which the driver is not distracted
- no_previous : Proprotion of crashes in which driver doesn't have any past accident records
- ins_premium : Average insurance premium (per driver, in USD)
- ins_losses : Average insurance losses (per insured vehicle) ''')

st.markdown('---')

#  heading :technologies used
st.header('🚀 Technologies Used ⚙')
st.write(''' 
- ⚡ Python -> Main Programming language
- 📊 Pandas -> Data CLeaning, manipulation & analysis
- 🔢 NumPy -> Numerical Computation
- 🎨 Seaborn & Matplotlib -> Data Visualization(charts & plots)
- 🌐 Plotly -> Interactive Charts and Graphs
- 🖥 Streamlit -> Web app framework for creating dashboard
- VS Code / Jupyter Notebook -> Development Environment
''')

st.markdown('---')

# heading : how to use dashboard
st.header('📌 How to Use Dashboard ')
st.write(''' 
The complete overview of the dataset is given above. If you want further information about the dataset 'Car Crashes' then you can select page of your choice fro the sidebar given in left. 
We have done complete analysis of the dataset and visualized by interactive graphs 📊. 
- 📊 Use the **Home Page** to get dataset overview and columns explanation
- 📉 Navigate to **Analysis Pages** to explore  interactive graphs
- 🔍 You can filter ,zoom, and interact with plots for deep insights
- 📁 Use sidebar to switch between pages quickly.''')

st.markdown('---')

st.success("We hope our dataset and it's analysis will help you and upgrade your knowledge 💕")