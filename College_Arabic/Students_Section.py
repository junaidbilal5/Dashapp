import pandas as pd
import datetime as dt
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import calendar
import plotly
import plotly.express as px
df=pd.read_csv('./data/Student Section.csv')
year = df.Year.drop_duplicates().sort_values()
semester= df.Semester.drop_duplicates().sort_values()
from app import app

from dash_extensions import Lottie

######-------------------------URL of Lottie Animations---------------------------------------------------###
enrolled='https://assets5.lottiefiles.com/packages/lf20_dT1E1P.json'
scholars= 'https://assets9.lottiefiles.com/packages/lf20_htEgHu.json'
teacher='https://assets5.lottiefiles.com/private_files/lf30_g4ft9Z.json'
active='https://assets9.lottiefiles.com/packages/lf20_Q895iE.json'


options = dict(loop=False, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))

##-----------------------------------------------------------##--------------------------------------------###



def StudentsLayout():
	return [

		html.Div([

		html.Div([

		html.Div(
							children = [
								# Title and subtitle
								html.Div(
									children = [
										html.H1(
											children = "Students Section",
											style = {
												"margin-bottom": "0",
												"color": "black"
											}
										),

									]
								)
							],
							className = "six column",
							id = 'title'
						),

		html.Div([

				html.Div([
					html.Label(['Select Year'],style={'font-weight': 'bold', 'color':'black'}),
					dcc.Dropdown(
						id="dropdown(student)",
						options=[{"label": x, "value": x} for x in year],
						value=year[0],
						clearable=False,
						style={"width": "55%", },
						className='dcc_compon'
					),
				], className='create_container three columns'),

		html.Div([
					html.Label(['Select Semester'],style={'font-weight': 'bold', 'color':'black'}),
					dcc.Dropdown(
						id="dropdown1(student)",
						options=[{"label": x, "value": x} for x in semester],
						value=semester[0],
						clearable=False,
						style={"width": "55%", },
						className='dcc_compon'
					),
				], className='create_container three columns'),

		],className = "row flex-display",
					style = {
						"margin-bottom": "25px"
					}),


		html.Div(
					children = [
						html.Div(
							children = [
								# Title
								html.H6(
									children = "Total Students Enrolled",
									style = {
										"textAlign": "center",
										"color": "black"
									}
								),
								(Lottie(options=options, width='27%', height='27%', url=enrolled)),
								# Total value
								html.P(id="card_1(student)",
									children = "2500",
									style = {
										"textAlign": "center",
										"color": "#dd1e35",
										"fontSize": 40
									}
								),

							],
							className = "create_container three columns"
						),
						# (Column 2): Approved
						html.Div(
							children = [
								# Title
								html.H6(
									children = "Total Students on Scholarship",
									style = {
										"textAlign": "center",
										"color": "black"
									}
								),
								(Lottie(options=options, width='27%', height='27%', url=scholars)),
								# Total value
								html.P(id="card_2(student)",
									children = "50",
									style = {
										"textAlign": "center",
										"color": "#dd1e35",
										"fontSize": 40
									}
								),

							],
							className = "card_container three columns"
						),

		html.Div(
							children = [
								# Title
								html.H6(
									children = "Teacher to Students Ratio",
									style = {
										"textAlign": "center",
										"color": "black"
									}
								),
								(Lottie(options=options, width='27%', height='27%', url=teacher)),
								# Total value
								html.P(id="card_3(student)",
									children = "1:250",
									style = {
										"textAlign": "center",
										"color": "#dd1e35",
										"fontSize": 40
									}
								),

							],
							className = "card_container three columns"
						),

		html.Div(
							children = [
								# Title
								html.H6(
									children = "Number of Active Courses",
									style = {
										"textAlign": "center",
										"color": "black"
									}
								),
								(Lottie(options=options, width='18%', height='18%', url=active)),
								# Total value
								html.P(id="card_4(student)",
									children = "14",
									style = {
										"textAlign": "center",
										"color": "#dd1e35",
										"fontSize": 40
									}
								),

							],
							className = "card_container three columns"
						),

					],
					className = "row flex-display"
				),


		###-------------------------------------------------Gauge Meter-----------------------------------------------##
		html.Div([
		# html.Div(
		#
		# 					children = [
		# 						html.H6(
		# 							children="Overall Attendance",
		# 							style={
		# 								"textAlign": "center",
		# 								"color": "black"
		# 							}),
		# 						dcc.Graph(
		# 							id = "gauge(student)",
		# 							config = {
		# 								"displayModeBar": "hover"
		# 							}
		# 						)
		# 					],
		# 					className = "create_container four columns",
		# 					style = {
		# 						"maxWidth": "400px",
		# 						"text-align":"center"
		# 					}
		# 				),
		#
		# html.Div(
		# 					children = [
		#
		# 						html.H6(
		# 							children="Overall Performance",
		# 							style={
		# 								"textAlign": "center",
		# 								"color": "black"
		# 							}),
		# 						dcc.Graph(
		# 							id = "gauge1(student)",
		# 							config = {
		# 								"displayModeBar": "hover"
		# 							}
		# 						)
		# 					],
		# 					className = "create_container four columns",
		# 					style = {
		# 						"maxWidth": "400px",
		# 						"text-align":"center"
		# 					}
		# 				),

			html.Div(
				children=[
					# Donut chart
					dcc.Graph(
						id="small_bar1(student)",
						config={
							"displayModeBar": "hover"
						}
					)
				],
				className="create_container five columns",
				style={
					"maxWidth": "800px",
					"text-align": "center"
				}
			),

			],className = "row flex-display"),

		####------------------------Bar graph for Live Sessions conducted-----------------------------------------------------------###


		html.Div([
			html.Div([
				dcc.Graph(id='the_graph2(student)',config = {
										"displayModeBar": "hover"
									})
			],className = "create_container eleven columns"),

		],className = "row flex-display"),



		####-----------------------------------------####------------------------------------------###

		html.Div([

		html.Div(
							children = [
								# Donut chart
								dcc.Graph(
									id = "pie_chart(student)",
									config = {
										"displayModeBar": "hover"
									}
								)
							],
							className = "create_container four columns",
							style = {
								"maxWidth": "400px"
							}
						),

		html.Div(
							children = [
								# Donut chart
								dcc.Graph(
									id = "pie_chart1(student)",
									config = {
										"displayModeBar": "hover"
									}
								)
							],
							className = "create_container four columns",
					## Width of the pie grapgh
							style = {
								"maxWidth": "400px"
							}
						),

		html.Div(
							children = [
								# Donut chart
								dcc.Graph(
									id = "small_bar(student)",
									config = {
										"displayModeBar": "hover"
									}
								)
							],
							className = "create_container five columns",
						),
		],className = "row flex-display"),


		],id = "mainContainer",
			style = {
				"display": "flex",
				"flex-direction": "column"
			}),

		])

		]

####-----------------------Callbacks for Gauge-Meters------------------------------####

@app.callback(
    Output(component_id='gauge(student)', component_property='figure'),
     Input("dropdown(student)", "value"),
     Input("dropdown1(student)", "value"))

def update_graph(year, semester):
    mask= (df['Year']==year)  & (df['Semester']==semester)
    present = df[mask].Hours_conducted.sum()
    total = df[mask].Total_hours.sum()
    attendance = (present / total) * 100

    gauge1 = go.Figure(go.Indicator(
    mode="gauge+number",
    value=attendance,
	domain={'x': [0, 1], 'y': [0, 1]},
	gauge={'axis': {'range': [None, 100]}, 'bar': {'color': "#f76b25"}}))
    gauge1.update_layout(
		height=300,
		margin=dict(l=10, r=10, t=40, b=10),
		showlegend=False,
		template="plotly_dark",
		plot_bgcolor='white',
		paper_bgcolor='white',
		font_color="black",
		font_size=10
	)

    return gauge1

#####---------------------------------------------------------------######----------------------------------------------###

@app.callback(
    Output(component_id='gauge1(student)', component_property='figure'),
     Input("dropdown(student)", "value"),
     Input("dropdown1(student)", "value"))

def update_graph(year, semester):
    mask= (df['Year']==year)  & (df['Semester']==semester)
    modules_complete = df[mask].Modules_comp.sum()
    total_modules = df[mask].Total_modules.sum()
    performance = (modules_complete / total_modules) * 100

    gauge2 = go.Figure(go.Indicator(
    mode="gauge+number",
    value=performance,
	domain={'x': [0, 1], 'y': [0, 1]},
	gauge={'axis': {'range': [None, 100]}, 'bar': {'color': "#f76b25"}}))
    gauge2.update_layout(
		height=300,
		margin=dict(l=10, r=10, t=40, b=10),
		showlegend=False,
		template="plotly_dark",
		plot_bgcolor='white',
		paper_bgcolor='white',
		font_color="black",
		font_size=10
	)

    return gauge2


@app.callback(
    Output(component_id='the_graph2(student)', component_property='figure'),
     Input("dropdown(student)", "value"),
     Input("dropdown1(student)", "value"))

def update_graph(year, semester):
    mask= (df['Year']==year)  & (df['Semester']==semester)


    dfg=df[mask].groupby('Category').count().reset_index()



    fig = {
        "data": [
            go.Bar(
                x=dfg['Category'],
                y=dfg['StudentID'],
                name="Department Wise",
                marker={
                    "color": "#f79d9c",
                    "opacity":0.6,
                },
                hoverinfo="text",

            ),


        ],

        "layout": go.Layout(
            title={
                "text": f"Number of Live Sessions in {semester}, {year} ",
                "y": 0.93,
                "x": 0.5,
                "xanchor": "center",
                "yanchor": "top"
            },
            titlefont={
                "color": "black",
                "size": 19
            },
            xaxis={
                "title": "<b>Live Sessions</b>",
                "color": "black",
                "showline": True,
                "showgrid": False,
                "showticklabels": True,
                "linecolor": "black",
                "linewidth": 1,
                "ticks": "outside",
                "tickfont": {
                    "family": "Aerial",
                    "color": "black",
                    "size": 12
                }
            },
            yaxis={
                "title": "<b>Total Logins</b>",
                "color": "black",
                "showline": True,
                "showgrid": False,
                "showticklabels": True,
                "linecolor": "white",
                "linewidth": 1,
                "ticks": "outside",
                "tickfont": {
                    "family": "Aerial",
                    "color": "black",
                    "size": 12
                }
            },
            font={
                "family": "sans-serif",
                "color": "black",
                "size": 12
            },
            hovermode="closest",
            paper_bgcolor="white",
            plot_bgcolor="white",
            legend={
                "orientation": "h",
                "bgcolor": "black",
                "xanchor": "center",
                "x": 0.5,
                "y": -0.7
            }
        )


    }
    return fig


@app.callback(
    Output(component_id='pie_chart(student)', component_property='figure'),
     Input("dropdown(student)", "value"),
     Input("dropdown1(student)", "value"))

def update_graph(year,semester):



    mask= (df['Year']==year)  & (df['Semester']==semester)
    labels = df[mask]['Gender'].unique()
    values = df[mask]['Gender'].value_counts()


    fig = {
								"data": [
									go.Pie(
										labels=labels,
										values=values,
										marker={

										},
										hoverinfo="label+value+percent",
										textinfo="percent",
										hole=0.7,
										rotation=45,
										insidetextorientation="radial"
									)
								],
								"layout": go.Layout(
									title={
										"text": f"Gender-wise scholarship students in {semester}, {year}",
										"y": 0.93,
										"x": 0.5,
										"xanchor": "center",
										"yanchor": "top"
									},
									titlefont={
										"color": "black",
										"size": 15
									},
									font={
										"family": "sans-serif",
										"color": "black",
										"size": 12
									},
									hovermode="closest",
									paper_bgcolor="white",
									plot_bgcolor="white",
									legend={
										"orientation": "h",
										"bgcolor": "white",
										"xanchor": "center",
										"x": 0.5,
										"y": -0.7
									}
								)
							}

    return fig

@app.callback(
    Output(component_id='pie_chart1(student)', component_property='figure'),
     Input("dropdown(student)", "value"),
     Input("dropdown1(student)", "value"))

def update_graph(year,semester):



    mask= (df['Year']==year)  & (df['Semester']==semester)
    labels = labels = ['Asian', 'European', 'ME','African']
    values = df[mask]['Ethnicity'].value_counts()


    fig = {
								"data": [
									go.Pie(
										labels=labels,
										values=values,
										marker={

										},
										hoverinfo="label+value+percent",
										textinfo="percent",
										hole=0.7,
										rotation=45,
										insidetextorientation="radial"
									)
								],
								"layout": go.Layout(
									title={
										"text": f"Ehtnic-groups enrolled in {semester}, {year}",
										"y": 0.93,
										"x": 0.5,
										"xanchor": "center",
										"yanchor": "top"
									},
									titlefont={
										"color": "black",
										"size": 15
									},
									font={
										"family": "sans-serif",
										"color": "black",
										"size": 12
									},
									hovermode="closest",
									paper_bgcolor="white",
									plot_bgcolor="white",
									legend={
										"orientation": "h",
										"bgcolor": "white",
										"xanchor": "center",
										"x": 0.5,
										"y": -0.7
									}
								)
							}

    return fig


@app.callback(
    Output(component_id='small_bar(student)', component_property='figure'),
     Input("dropdown(student)", "value"),
     Input("dropdown1(student)", "value"))

def update_graph(year, semester):
    mask= (df['Year']==year)  & (df['Semester']==semester)


    dfg=df[mask].groupby('Request').count().reset_index()



    fig = {
        "data": [
            go.Bar(
                x=dfg['StudentID'],
                y=dfg['Request'],
                name="Department Wise",
				orientation='h',
                marker={
                    "color": "#f79d9c",
                    "opacity":0.6,
                },
                hoverinfo="text",

            ),


        ],

        "layout": go.Layout(
            title={
                "text": f"Number of Student Requests in {semester}, {year} ",
                "y": 0.93,
                "x": 0.5,
                "xanchor": "center",
                "yanchor": "top"
            },
            titlefont={
                "color": "black",
                "size": 15
            },
            xaxis={
                "title": "<b>Total number</b>",
                "color": "black",
                "showline": True,
                "showgrid": False,
                "showticklabels": True,
                "linecolor": "black",
                "linewidth": 1,
                "ticks": "outside",
                "tickfont": {
                    "family": "Aerial",
                    "color": "black",
                    "size": 12
                }
            },
            yaxis={
                "title": "<b>Request Status</b>",
                "color": "black",
                "showline": True,
                "showgrid": False,
                "showticklabels": True,
                "linecolor": "white",
                "linewidth": 1,
                "ticks": "outside",
                "tickfont": {
                    "family": "Aerial",
                    "color": "black",
                    "size": 12
                }
            },
            font={
                "family": "sans-serif",
                "color": "black",
                "size": 12
            },
            hovermode="closest",
            paper_bgcolor="white",
            plot_bgcolor="white",
            legend={
                "orientation": "h",
                "bgcolor": "black",
                "xanchor": "center",
                "x": 0.5,
                "y": -0.7
            }
        )


    }
    return fig



@app.callback(
    Output(component_id='small_bar1(student)', component_property='figure'),
     Input("dropdown(student)", "value"),
     Input("dropdown1(student)", "value"))
def update_graph(year, semester):
    mask= (df['Year']==year)  & (df['Semester']==semester)


    dfg=df[mask].groupby('Country').count().reset_index()



    fig = {
        "data": [
            go.Bar(
                x=dfg['Country'],
                y=dfg['StudentID'],
                name="Country Wise",
                marker={
                    "color": "#f79d9c",
                    "opacity":0.6,
                },
                hoverinfo="text",

            ),


        ],

        "layout": go.Layout(
            title={
                "text": f"Number of Students from Country in {semester}, {year} ",
                "y": 0.93,
                "x": 0.5,
                "xanchor": "center",
                "yanchor": "top"
            },
            titlefont={
                "color": "black",
                "size": 19
            },
            xaxis={
                "title": "<b>Country</b>",
                "color": "black",
                "showline": True,
                "showgrid": False,
                "showticklabels": True,
                "linecolor": "black",
                "linewidth": 1,
                "ticks": "outside",
                "tickfont": {
                    "family": "Aerial",
                    "color": "black",
                    "size": 12
                }
            },
            yaxis={
                "title": "<b>Students</b>",
                "color": "black",
                "showline": True,
                "showgrid": False,
                "showticklabels": True,
                "linecolor": "white",
                "linewidth": 1,
                "ticks": "outside",
                "tickfont": {
                    "family": "Aerial",
                    "color": "black",
                    "size": 12
                }
            },
            font={
                "family": "sans-serif",
                "color": "black",
                "size": 12
            },
            hovermode="closest",
            paper_bgcolor="white",
            plot_bgcolor="white",
            legend={
                "orientation": "h",
                "bgcolor": "black",
                "xanchor": "center",
                "x": 0.5,
                "y": -0.7
            }
        )


    }
    return fig


if __name__ == '__main__':
    app.run_server(debug=True, port=1439, )