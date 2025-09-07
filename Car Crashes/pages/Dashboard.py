import streamlit as st
import seaborn as sns
import plotly.express as px



st.title('data based on car crashes')

df=sns.load_dataset('car_crashes')

# add new coloumn 'state' as the full form of abbrev

state_map = {
    "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas", "CA": "California",
    "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware", "FL": "Florida", "GA": "Georgia",
    "HI": "Hawaii", "ID": "Idaho", "IL": "Illinois", "IN": "Indiana", "IA": "Iowa",
    "KS": "Kansas", "KY": "Kentucky", "LA": "Louisiana", "ME": "Maine", "MD": "Maryland",
    "MA": "Massachusetts", "MI": "Michigan", "MN": "Minnesota", "MS": "Mississippi",
    "MO": "Missouri", "MT": "Montana", "NE": "Nebraska", "NV": "Nevada", "NH": "New Hampshire",
    "NJ": "New Jersey", "NM": "New Mexico", "NY": "New York", "NC": "North Carolina",
    "ND": "North Dakota", "OH": "Ohio", "OK": "Oklahoma", "OR": "Oregon", "PA": "Pennsylvania",
    "RI": "Rhode Island", "SC": "South Carolina", "SD": "South Dakota", "TN": "Tennessee",
    "TX": "Texas", "UT": "Utah", "VT": "Vermont", "VA": "Virginia", "WA": "Washington",
    "WV": "West Virginia", "WI": "Wisconsin", "WY": "Wyoming"
}

df['state'] = df['abbrev'].map(state_map)

# Manually map states to region
region_map = {
    'CT': 'Northeast', 'ME': 'Northeast', 'MA': 'Northeast', 'NH': 'Northeast', 'RI': 'Northeast', 'VT': 'Northeast',
    'NJ': 'Northeast', 'NY': 'Northeast', 'PA': 'Northeast',
    'IL': 'Midwest', 'IN': 'Midwest', 'MI': 'Midwest', 'OH': 'Midwest', 'WI': 'Midwest',
    'IA': 'Midwest', 'KS': 'Midwest', 'MN': 'Midwest', 'MO': 'Midwest', 'NE': 'Midwest', 'ND': 'Midwest', 'SD': 'Midwest',
    'DE': 'South', 'FL': 'South', 'GA': 'South', 'MD': 'South', 'NC': 'South', 'SC': 'South', 'VA': 'South', 'DC': 'South',
    'WV': 'South', 'AL': 'South', 'KY': 'South', 'MS': 'South', 'TN': 'South', 'AR': 'South', 'LA': 'South', 'OK': 'South', 'TX': 'South',
    'AZ': 'West', 'CO': 'West', 'ID': 'West', 'MT': 'West', 'NV': 'West', 'NM': 'West', 'UT': 'West', 'WY': 'West',
    'AK': 'West', 'CA': 'West', 'HI': 'West', 'OR': 'West', 'WA': 'West'
}

# Add region column using abbrev
df['region'] = df['abbrev'].map(region_map)
st.dataframe(df)

st.markdown("""
    <style>
        .stApp {
              background-color:purple-pink mix;
              color : white;
            }
            [data-testid='stSidebar']{
                background-color:deeep purple !important;
            }
            [data-testid='stSidebar']*{
                color : off-white !important;
            }
        </style>""",unsafe_allow_html=True)

min_speeding,max_speeding = st.sidebar.slider('Speeding',
                                     min_value = float(df['speeding'].min()),
                                     max_value = float(df['speeding'].max()),
                                     value = (float(df['speeding'].min()), float(df['speeding'].max())))

min_alcohol,max_alcohol = st.sidebar.slider('Alcohol',
                                     min_value = float(df['alcohol'].min()),
                                     max_value = float(df['alcohol'].max()),
                                     value = (float(df['alcohol'].min()), float(df['alcohol'].max())))

min_premium,max_premium = st.sidebar.slider('Insurance Premium',
                                        min_value = float(df['ins_premium'].min()),
                                        max_value = float(df['ins_premium'].max()),
                                        value = (float(df['ins_premium'].min()),float(df['ins_premium'].max())))

min_total,max_total = st.sidebar.slider('Total Accidents',
                                 min_value = float(df['total'].min()),
                                 max_value = float(df['total'].max()),
                                 value = (float(df['total'].min()),float(df['total'].max())))

unique_abbrev = st.sidebar.multiselect('Abbrevation',
                                options = df['abbrev'].unique(),
                                default = df['abbrev'].unique())

filtered_df = df[
    (df['speeding']>=min_speeding)&
    (df['speeding']<=max_speeding)&
    (df['alcohol']>=min_alcohol)&
    (df['alcohol']<=max_alcohol)&
    (df['ins_premium']>=min_premium)&
    (df['ins_premium']<=max_premium)&
    (df['total']>=min_total)&
    (df['total']<=max_total)&
    (df['abbrev'].isin(unique_abbrev))
]

fig =px.bar(filtered_df,x='abbrev',y='total',
             title='total accident by state',
             labels={'abbrev':'State','total':'Total Accident'},
             color='total',
             template='plotly_dark'
             )
st.plotly_chart(fig)

top10 = filtered_df .sort_values('ins_premium',ascending=False).head(10)
fig=px.bar(top10,x='abbrev',y='ins_premium',
            title = 'top 10 states by insurance premium',
            labels = {'abbrev':'State','ins_premium':'Insurance Premium'},
            color = 'ins_premium',
            template='plotly_dark'
           )
st.plotly_chart(fig)

# percentage of speeding accidents 
fig = px.pie(filtered_df,values='speeding',names='abbrev',
             title = 'percentage of speeding accidents by state',
             labels={'abbrev':'State','speeding':'Speeding Accidents'},
             template='plotly_dark',
             color='speeding'
             )
fig.update_traces(textinfo='label+percent',textposition ='inside')
st.plotly_chart(fig)

fig = px.sunburst(filtered_df,
                  path=['speeding','abbrev','ins_premium'],
                  title='chart based on some filter like speeding,abbrev,insurance premium',
                  values='total')
st.plotly_chart(fig)

# alcohol vs speeding
fig = px.scatter(filtered_df,x='speeding',
                 y='alcohol',
                 color = 'abbrev',
                 size = 'total',
                 title= 'Speeding vs Alcoholic Accidents',
                 )
st.plotly_chart(fig)
