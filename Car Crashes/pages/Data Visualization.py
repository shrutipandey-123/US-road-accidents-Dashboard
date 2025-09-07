import streamlit as st
import plotly.express as px
import seaborn as sns

# load dataset
df=sns.load_dataset("Car_Crashes")
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


# unique_abbrev = st.sidebar.multiselect('Abbrevation',
#                                 options = df['abbrev'].unique(),
#                                 default = df['abbrev'].unique())

filtered_df = df[
    (df['speeding']>=min_speeding)&
    (df['speeding']<=max_speeding)&
    (df['alcohol']>=min_alcohol)&
    (df['alcohol']<=max_alcohol)&
    (df['ins_premium']>=min_premium)&
    (df['ins_premium']<=max_premium)&
    (df['total']>=min_total)&
    (df['total']<=max_total)
    # (df['abbrev'].isin(unique_abbrev)
]

# heading
st.title('Data Visualization 📊')
st.markdown('---')

st.markdown('### In this page, we will visualize different aspects of the dataset')

st.markdown('## Bar Chart 📊')
# chart 1 : crashes as per state
fig =px.bar(filtered_df,x='total',
             title='total accident by state',
             labels={'abbrev':'State','total':'Total Accident'},
             color='total',
             template='plotly_dark',
             orientation='v'
             )
st.plotly_chart(fig)

st.markdown('---')

# crashes as per state
st.write('This graph makes the comparison of total crashes as per state US')
fig =  px.bar(filtered_df,x='total',y='state',
             title ='Comparisonn between total crashes per state',
             labels={'total':'Total Crashes','state':'State'},
             color='state',
             template='plotly_dark',
             orientation='v'
             )
st.plotly_chart(fig)

st.markdown('---')

# state vs alcohol
fig =px.bar(filtered_df,x='state',y='alcohol',
             title='Total Crashes as per State due to Alcohol 👇',
             labels={'state':'Name of States ➡','alcohol':'crashes due to alcohol ➡'},
             color='state',
             template='plotly_dark',
             orientation = 'v'
             )
st.plotly_chart(fig)

st.markdown('---')

# state vs not_distracted
fig =px.bar(filtered_df,x='state',y='not_distracted',
             title='Total crashes as per state when the driver was not distracted 👇',
             labels={'state':'Names of States ➡','not_distracted':'crashes when the driver was not distracted ➡'},
             color='state',
             template='plotly_dark',
             orientation='v'
             )
st.plotly_chart(fig)

st.markdown('---')

# state vs ins_premium
fig =px.bar(filtered_df,x='state',y='ins_premium',
             title='Total crashes as per state where the car has insurance 👇',
             labels={'state':'Name of States ➡','ins_premium':'crashes where the car has insurance ➡'},
             color='state',
             template='plotly_dark',
             orientation='v'
             )
st.plotly_chart(fig)

st.markdown('---')

# state vs no_previous
fig =px.bar(filtered_df,x='state',y='no_previous',
             title="Total crashes as per state when there's no past record of crash 👇",
             labels={'state':'Name of States ➡','no_previous':"Driver does't have previous crash record ➡"},
             color='state',
             template='plotly_dark',
             orientation='v'
             )
st.plotly_chart(fig)

st.markdown('---')

# stacked bar chart
fig=px.bar(filtered_df,x='state',y='speeding',
           title='Total Crashes according to State due to Speeding 👇',
           labels = {'state':'State','speeding':'Due to Speeding'},
           color = 'state',
           template = 'plotly_dark',
           orientation = 'v'
           )
st.plotly_chart(fig)

st.markdown('---')

# percentage of speeding accidents 
fig = px.pie(filtered_df,values='speeding',names='abbrev',
             title = 'percentage of speeding accidents by state',
             labels={'abbrev':'State','speeding':'Speeding Accidents'},
             template='plotly_dark',
             color='speeding'
             )
fig.update_traces(textinfo='label+percent',textposition ='inside')
st.plotly_chart(fig)

st.markdown('---')

fig = px.sunburst(filtered_df,
                  path=['speeding','abbrev','ins_premium'],
                  title='chart based on some filter like speeding,abbrev,insurance premium',
                  values='total')
st.plotly_chart(fig)

st.markdown('---')

# scatter chart
st.markdown('## Scatter Chart ✨')

# alcohol vs speeding
fig = px.scatter(filtered_df,x='speeding',
                 y='alcohol',
                 color = 'abbrev',
                 size = 'total',
                 title= 'Speeding vs Alcoholic Accidents',
                 )
st.plotly_chart(fig)

st.markdown('---')

# Insuarance Premium VS Insurance Losses
fig = px.scatter(filtered_df,x='ins_premium',
                 y='ins_losses',
                 color = 'ins_premium',
                 size = 'ins_premium',
                 template='plotly_dark',
                 title= 'Insuarance Premium VS Insurance Losses',
                 labels={'ins_premium':'Vehicles have Insurance Premium','ins_losses':'Insurance Losses'},
                 )
st.plotly_chart(fig)

st.markdown('---')

st.markdown('## Chart based on Top 10 States')

# state vs ins_premium
top10 = filtered_df .sort_values('ins_premium',ascending=False).head(10)
fig=px.bar(top10,x='state',y='ins_premium',
            title = 'top 10 states by insurance premium',
            labels = {'state':'State','ins_premium':'Insurance Premium'},
            color = 'state',
            template='plotly_dark'
           )
st.plotly_chart(fig)

st.markdown('---')

# state vs alcohol
top10 = filtered_df .sort_values('alcohol',ascending=False).head(10)
fig=px.bar(top10,x='state',y='alcohol',
            title = 'Top 10 states by Alcohol',
            labels = {'state':'State','alcohol':'Alcohol'},
            color = 'state',
            template='plotly_dark'
           )
st.plotly_chart(fig)

# state vs speed
top10 = filtered_df .sort_values('speeding',ascending=False).head(10)
fig=px.bar(top10,x='state',y='speeding',
            title = 'Top 10 states due to high speed',
            labels = {'state':'State','Alcohol':'Speed'},
            color = 'state',
            template='plotly_dark'
           )
st.plotly_chart(fig)

# 4. Correlation Heatmap
# px.fig(figsize=(8,6))
# sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
# px.title("Correlation Heatmap")
# px.show()

