import pandas as pd
import plotly.express as px

data = pd.read_csv("World University Rankings 2023.csv")

result  = data.groupby(['Location'])['University Rank'].count().reset_index()
result1  = data.groupby(['Location'])['Industry Income Score'].mean().reset_index()
merge_data = pd.merge(result, result1)

fig = px.scatter(merge_data, x="Industry Income Score", y="University Rank", color="Location",
                 size='University Rank')
fig.update_layout(
    title="Analysing Top Universities",
    xaxis_title="Mean of Industry Income Score",
    yaxis_title="Count of Top Universities")
fig.show()
