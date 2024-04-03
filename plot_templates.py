import pandas as pd
import plotly.graph_objs as go


def create_bar_chart(data, title):
    # Create the bar chart using Plotly
    fig = go.Figure()

    # Add bars for onshore and offshore data
    fig.add_trace(go.Bar(
        x=data['Country'],
        y=data['by_nationality_onshore'],
        name='By nationality: Onshore',
        marker_color='rgb(158,202,225)',
        customdata=data['economy_type'],
        visible=True
    ))

    fig.add_trace(go.Bar(
        x=data['Country'],
        y=data['by_nationality_offshore'],
        name='By nationality: Offshore',
        marker_color='rgb(211,157,190)',
        customdata=data['economy_type'],
        visible=True
    ))

    # Add points for residence data
    fig.add_trace(go.Scatter(
        x=data['Country'],
        y=data['by_residence'],
        mode='markers',
        name='By residence',
        marker=dict(color='rgb(0,0,0)', size=8),
        customdata=data['economy_type'],
        visible=True
    ))

    # Update layout with title and uniform axes
    fig.update_layout(
        title=title,
        barmode='stack',
        xaxis=dict(title='Country code'),
        yaxis=dict(title='Trillions of US dollars'),
        legend=dict(
            x=0.6,
            y=0.8,
            traceorder='normal',
            font=dict(
                size=12,
            )
        ),
        plot_bgcolor='rgba(0,0,0,0)',
    )



    # Use the same y-axis range for both plots based on the maximum value of by_residence to ensure consistency
    max_y_value = max(data['by_residence'].max(), 
                      (data['by_nationality_onshore'] + data['by_nationality_offshore']).max())
    fig.update_yaxes(range=[0, max_y_value*1.1])  # 10% more than the max value for some headroom

    return fig