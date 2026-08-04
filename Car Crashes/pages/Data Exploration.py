import streamlit as st
import seaborn as sns

# load dataset
df=sns.load_dataset("car_crashes")

# title
st.title("🔍 Data Exploration")
st.markdown('---')

# heading
st.header('Data Overview')
st.write('Number of rows Dataset contains : ',df.shape[0])
st.write('Number of columns Dataset contains : ',df.shape[1])

st.markdown('---')

st.header('Data Statistics 📉')
st.write(df.describe())

st.markdown('---')
st.header('⚠ Missing Values ')
# missing_data = df.isnull().sum()
# st.write(missing_data[missing_data>0])
st.write(df.isnull().sum())
st.markdown('---')

st.header("Sample of dataset is given below ")
st.dataframe(df.head())

st.markdown('---')
# checkbox for full dataset
st.info("If you want to explore the complete dataset then tick the checkbox given below 👇")
if st.checkbox("Show full dataset"):
    st.write('### Full Dataset')
    st.dataframe(df)

st.markdown('---')

st.info('📌 If you are interested in analyzing the data with interactive charts 📊 and graphs then go to the "Data Visualization" ')
