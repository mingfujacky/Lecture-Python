""" write a python program for a personal page with an emoji in the center, dark green background and links to youtube, google and netflix, keep the design modern and minimalist
"""

from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Personal Page</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            background: #183a1d;
            color: #fff;
            min-height: 100vh;
            margin: 0;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            font-family: 'Segoe UI', Arial, sans-serif;
        }
        .emoji {
            font-size: 7rem;
            margin-bottom: 2rem;
        }
        .links {
            display: flex;
            gap: 2rem;
        }
        .link {
            text-decoration: none;
            color: #fff;
            background: #22543d;
            padding: 0.8rem 2rem;
            border-radius: 2rem;
            font-size: 1.2rem;
            transition: background 0.2s, color 0.2s;
        }
        .link:hover {
            background: #38a169;
            color: #183a1d;
        }
    </style>
</head>
<body>
    <div class="emoji">🌱</div>
    <div class="links">
        <a class="link" href="https://www.youtube.com/" target="_blank">YouTube</a>
        <a class="link" href="https://www.google.com/" target="_blank">Google</a>
        <a class="link" href="https://www.netflix.com/" target="_blank">Netflix</a>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)