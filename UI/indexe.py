from reactpy import component, html, run


]

@component
def App():
    return html.div(
    {
        "style": {
            "width": "100%",
            "height": "50%",
            "font-family": "system-ui",    
            "margin_left": "0%",
            "background-color": "#F7F7F7"
        },
    },
    html.div(
            html.h1(
        {
            "style": {
                "margin_top": "0px",
                "color": "black"
            },
        },
        "My Todo List",
    ),
                html.h3(
        {
            "style": {
             
                "color": "black"
            },
        },
        "My Todo List",
    ),
    ),
    html.ul(
        html.li("Build a cool new app"),
        html.li("Share it with the world!"),
    ),
)


run(App)    




