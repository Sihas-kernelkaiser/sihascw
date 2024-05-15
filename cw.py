import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Set page configuration
st.set_page_config(page_title='MINGER DATA', page_icon=':chart:', layout='wide')
st.title('MINGER DATA ANALYTICS')
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

# Load data
df = pd.read_excel('cleaned_dataset_global.xlsx')

# Sidebar filters
segment_df = df[df['Segment'] == st.sidebar.selectbox('Choose Segment', df['Segment'].unique())]
state_df = df[df['State'] == st.sidebar.selectbox('Choose State', df['State'].unique())]
market_df = df[df['Market'] == st.sidebar.selectbox('Choose Market', df['Market'].unique())]
subcategory_df = df[df['Sub-Category'] == st.sidebar.selectbox('Choose Sub-Category', df['Sub-Category'].unique())]
category_df = df[df['Category'] == st.sidebar.selectbox('Category', df['Category'].unique())]

# Create a grid layout
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

# Visualizations
with col1:
    # Pie chart: Sales of Categories in Each Market
    fig_pie_sales = px.pie(category_df, values='Sales', names='Market', title='Sales of Categories in Each Market')
    st.plotly_chart(fig_pie_sales)

with col2:
    # Bar chart: Profit of Subcategories in Each State
    fig_bar_profit = px.bar(state_df, x='Sub-Category', y='Profit', color='State', barmode='group', title='Profit of Subcategories in Each State')
    st.plotly_chart(fig_bar_profit)

with col3:
    #barchart: Order priority of each category in each segment 
    fig_bar_priority = px.bar(subcategory_df, x='Order Priority', y='Quantity', color='Sub-Category', barmode='group', title='Order priority of each subcategory wise segment ')
    st.plotly_chart(fig_bar_priority)

with col4:
    #scatter plot for profit vs discount in each segment 
    fig_scatter_profit_discounts = px.scatter(segment_df, x='Profit', y='Discount', color='Segment', title='Profit vs Discounts')
    st.plotly_chart(fig_scatter_profit_discounts)

# Additional insights section
st.subheader('Additional Insights')

# Show a line chart: Sales over time
fig_line_sales = px.line(df, x='Order Date', y='Sales', title='Sales over Time')
st.plotly_chart(fig_line_sales)

# Show a scatter plot: Profit vs Sales
fig_scatter_profit_sales = px.scatter(market_df, x='Sales', y='Profit', color='Market', title='Profit vs Sales')
st.plotly_chart(fig_scatter_profit_sales)
