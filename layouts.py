import dash_core_components as dcc
import dash_html_components as html

tabs_styles = {
    'height': '51px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '2px',
    'fontWeight': 'bold',
    'vertical-align': 'middle',
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': 'white',
    'color': 'blue',
    'padding': '10px',
    "font-size": 20
}

dis = html.Div([html.Div(children=
                         [html.Div(className='bg-yellow', id="total", children=[html.Img(src='assets/images/covid.png',
                                                                                         alt='position status',
                                                                                         style={'height': '40%',
                                                                                                'width': '40%'}),
                                                                                html.H5(id="confirm-display"),
                                                                                html.P('Confirm Cases')], style={
                             'display': 'inline-block',
                             "textAlign": "center",
                             "width": "130px",
                         }),
                          html.Div(className='bg-blue', id="active",
                                   children=[html.Img(src='assets/images/icon-infected.png',
                                                      alt='active status'),
                                             html.H5(id="active-display"), html.P('Active Cases')], style={
                                  'display': 'inline-block',
                                  "textAlign": "center",
                                  "width": "140px",
                              }),
                          html.Div(className='bg-green', id="cure",
                                   children=[html.Img(src='assets/images/icon-inactive.png',
                                                      alt='cured status'),
                                             html.H5(id="recovered-display"),
                                             html.P('Recovered Cases')], style={
                                  'display': 'inline-block',
                                  "textAlign": "center",
                                  "width": "140px",
                              }),
                          html.Div(className='bg-red', id="death",
                                   children=[html.Img(src='assets/images/icon-death.png',
                                                      alt='death status'), html.H5(id="death-display"),
                                             html.P('Deaths')], style={
                                  'display': 'inline-block',
                                  "textAlign": "center",
                                  "width": "140px",
                              }),
                          html.Div(className='bg-orange', id="states", children=[html.Img(src='assets/images/india.png',
                                                                                          alt='states UTs status',
                                                                                          style={'height': '32%',
                                                                                                 'width': '32%'}),
                                                                                 html.H5(id='counts-display'),
                                                                                 html.P('Affected States')],
                                   style={
                                       'display': 'inline-block',
                                       "textAlign": "center",
                                       "width": "140px",
                                   }),
                          html.Div(className='bg-info', id="source",
                                   children=[html.A(html.Img(src='assets/images/icon-state.png',
                                                             alt='states-data',
                                                             style={'height': '300%',
                                                                    'width': '95%'}
                                                             ), href="#state-data"),
                                             html.H5("Data Source"),
                                             html.A("MoHFW", href='https://www.mohfw.gov.in/',
                                                    style={'font-size': "23px"}),
                                             ],
                                   style={
                                       'display': 'inline-block',
                                       "textAlign": "center",
                                       "width": "140px",
                                   }
                                   )
                          ], className="row container-display", style={'textAlign': 'center'})
                ], className="row", style={'background': '#b8bdd4', 'vertical-align': 'middle'})

layout = html.Div([html.H1("COVID19 India Tracker",
                           style={
                               'textAlign': 'center',
                               "background": "lightgreen"}),
                   dis,
                   html.Div(id='graph-input'),
                   dcc.Tabs(id="all-tabs-inline", value='tab-1', children=[
                       dcc.Tab(label='All Cases', value='tab-1', style=tab_style,
                               selected_style=tab_selected_style),
                       dcc.Tab(label='Cases Analysis', value='tab-2', style=tab_style,
                               selected_style=tab_selected_style),
                    #    dcc.Tab(label='News', value='tab-3', style=tab_style,
                    #            selected_style=tab_selected_style),
                    #    dcc.Tab(label='Help and Information', value='tab-4', style=tab_style,
                    #            selected_style=tab_selected_style),
                   ], style=tabs_styles,
                            colors={
                                "border": "yellow",
                                "primary": "red",
                                "background": "orange"
                            }),
                   html.Div(id='graph-output'),  # Tab output
                   html.Div(id='api-data', style={'display': 'none'}),
                #    html.Div(children=[dcc.Markdown(  # markdown
                #        "Primary Data Resources: [Ministry of Health and Family Welfare | GoI]("
                #        "https://www.mohfw.gov.in/) "
                #        " and [covid19india API](https://api.covid19india.org/data.json) ")], style={
                #        'textAlign': 'center',
                #        "background": "yellow"}),
                #    html.Div(children=[dcc.Markdown(  # markdown
                #        "© 2020 [VISHNU](https://github.com/dc-aichara/COVID19-India-Tracker)  All Rights "
                #        "Reserved.")], style={
                #        'textAlign': 'center',
                #        "background": "yellow"}),
                   html.Div(id='dummy-id'),

                   ], style={
    "background": "#000080"}
                  )
