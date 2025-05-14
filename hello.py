import pandas as pd
import plotly.express as px
from preswald import connect, get_df, query, table, text, plotly

# 1. Initialize connection and load data
connect()
df = get_df("olympics") 

# 2. Query/manipulate the data
filtered_df = query("""
    SELECT * FROM olympics 
    WHERE Year > 2000 
    AND Sport IN ('Athletics', 'Swimming', 'Gymnastics')
""", "olympics")

# 3. Build the UI
text("# 🏅 Summer Olympics Analysis")
text("Exploring medal data from 1896 to 2012")


# Visualization 1: Medals by Year
medals_by_year = df.groupby("Year").size().reset_index(name="Medals")
fig1 = px.line(medals_by_year, x="Year", y="Medals", 
              title="Olympic Medals Awarded by Year")
plotly(fig1)

# Visualization 2: Top Countries
top_countries = df['Country'].value_counts().head(10).reset_index()
fig2 = px.bar(top_countries, x='Country', y='count', 
             title='Top 10 Countries by Medal Count',
             color='count', color_continuous_scale='Blues')
plotly(fig2)

# Visualization 3: Gender Participation
gender_counts = df['Gender'].value_counts().reset_index()
fig3 = px.pie(gender_counts, values='count', names='Gender',
             title='Gender Participation Breakdown')
plotly(fig3)

# Visualization 5: Sport Distribution
top_sports = df['Sport'].value_counts().head(15).reset_index()
fig4 = px.treemap(top_sports, path=['Sport'], values='count',
                 title='Medal Distribution by Sport')
plotly(fig4)