
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Global AI Adoption in Education</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #f4f6f9;
            }
            header {
                background: #172554;
                color: white;
                padding: 20px;
                text-align: center;
            }
            iframe {
                width: 100%;
                height: 850px;
                border: none;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Global AI Adoption in Education</h1>
            <p>Global Education Analytics Dashboard</p>
        </header>

        <iframe
src="https://public.tableau.com/views/Global_AI_Education_final/GlobalAIEducationIntelligenceDashboard?:showVizHome=no&:embed=true">
</iframe>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(debug=True)
