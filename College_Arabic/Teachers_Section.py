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
df=pd.read_csv('./data/Teachers.csv')

from app import app
year = df.Year.drop_duplicates().sort_values()
semester= df.Semester.drop_duplicates().sort_values()

from dash_extensions import Lottie

######-------------------------URL of Lottie Animations---------------------------------------------------###
teacher='https://assets1.lottiefiles.com/private_files/lf30_g4ft9Z.json'
quiz='https://assets7.lottiefiles.com/private_files/lf30_6ocpfdil.json'
assignment='https://assets9.lottiefiles.com/private_files/lf30_VrsZnP.json'

options = dict(loop=2, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))



def TeachersLayout():
	return [


		html.Div([

		html.Div([

		html.Div(
							children = [
								# Title and subtitle
								html.Div(
									children = [
										html.H1(
											children = "Teachers Section/قسم المعلمين",
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
					html.Label(['Select Year/عام'],style={'font-weight': 'bold', 'color':'black'}),
					dcc.Dropdown(
						id="dropdown(teacher)",
						options=[{"label": x, "value": x} for x in year],
						value=year[0],
						clearable=False,
						style={"width": "55%", },
						className='dcc_compon'
					),
				], className='create_container three columns'),

		html.Div([
					html.Label(['Select Semester/حدد الفصل الدراسي'],style={'font-weight': 'bold', 'color':'black'}),
					dcc.Dropdown(
						id="dropdown1(teacher)",
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
									children = "Total Teachers/مجموع المعلمين",
									style = {
										"textAlign": "center",
										"color": "black"
									}
								),
								(Lottie(options=options, width='27%', height='27%', url=teacher)),
								# Total value
								html.P(id="card_1(teacher)",
									children = "300",
									style = {
										"textAlign": "center",
										"color": "orange",
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
									children = "Total Assignments Given/مجموع التعيينات الممنوحة",
									style = {
										"textAlign": "center",
										"color": "black"
									}
								),
								(Lottie(options=options, width='27%', height='27%', url=assignment)),

								# Total value
								html.P(id="card_2(teacher)",
									children = "150",
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
									children = "Total Tests Taken/مجموع الاختبارات التي تم إجراؤها",
									style = {
										"textAlign": "center",
										"color": "black"
									}
								),
								(Lottie(options=options, width='47%', height='47%', url=quiz)),
								# Total value
								html.P(id="card_3(teacher)",
									children = "200",
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
		# html.Div([
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
		# 							id = "gauge(teacher)",
		# 							config = {
		# 								"displayModeBar": "hover"
		# 							}
		# 						)
		# 					],
		# 					className = "create_container four columns",
		# 					style = {
		# 						"maxWidth": "400px"
		# 					}
		# 				),
		#
		# html.Div(
		# 					children = [
		#
		# 						html.H6(
		# 							children="Overall Feedback",
		# 							style={
		# 								"textAlign": "center",
		# 								"color": "black"
		# 							}),
		# 						dcc.Graph(
		# 							id = "gauge1(teacher)",
		# 							config = {
		# 								"displayModeBar": "hover"
		# 							}
		# 						)
		# 					],
		# 					className = "create_container four columns",
		# 					style = {
		# 						"maxWidth": "400px"
		# 					}
		# 				),
		#
		# 	],className = "row flex-display"),


		####-----------------------------------------####------------------------------------------###

		html.Div([



		html.Div(
							children = [
								# Donut chart
								dcc.Graph(
									id = "pie_chart1(teacher)",
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
									id = "small_bar(teacher)",
									config = {
										"displayModeBar": "hover"
									}
								)
							],
							className = "create_container five columns",
						),

			html.Div(
				children=[
					# Donut chart
					dcc.Graph(
						id="small_bar1(teacher)",
						config={
							"displayModeBar": "hover"
						}
					)
				],
				className="create_container five columns",
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
    Output(component_id='gauge(teacher)', component_property='figure'),
     Input("dropdown(teacher)", "value"),
     Input("dropdown1(teacher)", "value"))

def update_graph(year, semester):
    mask= (df['Year']==year)  & (df['Semester']==semester)
    present = df[mask].Attendance.value_counts().p
    absent=df[mask].Attendance.value_counts().a
    total=present+absent
    attendance = (present / total) * 100

    gauge1 = go.Figure(go.Indicator(
    mode="gauge+number",
    value=attendance,
	domain={'x': [0, 1], 'y': [0, 1]},
	gauge={'axis': {'range': [None, 100]}, 'bar': {'color': "blue"}}))
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
    Output(component_id='gauge1(teacher)', component_property='figure'),
     Input("dropdown(teacher)", "value"),
     Input("dropdown1(teacher)", "value"))

def update_graph(year, semester):
    mask= (df['Year']==year)  & (df['Semester']==semester)
    review = df[mask].Review.sum()
    total_review = df[mask].Total.sum()
    performance = (review / total_review) * 100

    gauge2 = go.Figure(go.Indicator(
    mode="gauge+number",
    value=performance,
	domain={'x': [0, 1], 'y': [0, 1]},
	gauge={'axis': {'range': [None, 100]}, 'bar': {'color': "blue"}}))
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
    Output(component_id='pie_chart(teacher)', component_property='figure'),
     Input("dropdown(teacher)", "value"),
     Input("dropdown1(teacher)", "value"))



@app.callback(
    Output(component_id='pie_chart1(teacher)', component_property='figure'),
     Input("dropdown(teacher)", "value"),
     Input("dropdown1(teacher)", "value"))

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
										"text": f"Ehtnicity of teachers/عرقية المعلمين ",
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
    Output(component_id='small_bar(teacher)', component_property='figure'),
     Input("dropdown(teacher)", "value"),
     Input("dropdown1(teacher)", "value"))

def update_graph(year, semester):
    mask= (df['Year']==year)  & (df['Semester']==semester)


    dfg=df[mask].groupby('Country').count().reset_index()



    fig = {
        "data": [
            go.Bar(
                x=dfg['Country'],
                y=dfg['Teacher_Name'],
                name="Country-wise teachers",
                marker={
                    "color": "rgb(219, 191, 249)",
                    "opacity":0.6,
                },
                hoverinfo="text",

            ),


        ],

        "layout": go.Layout(
            title={
                "text": f"Number of Teachers from Countries /عدد المعلمين من البلدان ",
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
                "title": "<b> Country/دولة</b>",
                "color": "black",
                "showline": True,
                "showgrid": False,
                "showticklabels": True,
				'categoryorder': 'total descending',
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
                "title": "<b>Teachers/معلمون</b>",
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
    Output(component_id='small_bar1(teacher)', component_property='figure'),
     Input("dropdown(teacher)", "value"),
     Input("dropdown1(teacher)", "value"))


def update_graph(year, semester):
    mask= (df['Year']==year)  & (df['Semester']==semester)


    dfg=df[mask].groupby('College').count().reset_index()



    fig = {
        "data": [
            go.Bar(
                x=dfg['College'],
                y=dfg['Teacher_Name'],
                name="College-wise teachers",
                marker={
                    "color": "rgb(219, 191, 249)",
                    "opacity":0.6,
                },
                hoverinfo="text",

            ),


        ],

        "layout": go.Layout(
            title={
                "text": f"College Wise Number of Teachers /عدد المعلمين الحكيم في الكلية ",
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
                "title": "<b> College/كلية</b>",
                "color": "black",
                "showline": True,
                "showgrid": False,
                "showticklabels": True,
				'categoryorder': 'total descending',
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
                "title": "<b>Teachers/معلمون</b>",
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
    app.run_server(debug=True, port=1440, )