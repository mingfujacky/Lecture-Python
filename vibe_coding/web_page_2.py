'''
modify the code so that the user can add or delete links from the website directly in the browser
'''
from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for links (reset on server restart)
links = [
    {"name": "YouTube", "url": "https://www.youtube.com/"},
    {"name": "Google", "url": "https://www.google.com/"},
    {"name": "Netflix", "url": "https://www.netflix.com/"},
]

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
            margin-bottom: 2rem;
        }
        .link {
            text-decoration: none;
            color: #fff;
            background: #22543d;
            padding: 0.8rem 2rem;
            border-radius: 2rem;
            font-size: 1.2rem;
            transition: background 0.2s, color 0.2s;
            position: relative;
        }
        .link:hover {
            background: #38a169;
            color: #183a1d;
        }
        .delete-btn {
            position: absolute;
            top: -10px;
            right: -10px;
            background: #e53e3e;
            color: #fff;
            border: none;
            border-radius: 50%;
            width: 1.5rem;
            height: 1.5rem;
            cursor: pointer;
            font-size: 1rem;
            line-height: 1.5rem;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .add-form {
            display: flex;
            gap: 1rem;
            margin-top: 1rem;
        }
        .add-form input[type="text"], .add-form input[type="url"] {
            padding: 0.5rem 1rem;
            border-radius: 1rem;
            border: none;
            font-size: 1rem;
        }
        .add-form button {
            padding: 0.5rem 1.5rem;
            border-radius: 1rem;
            border: none;
            background: #38a169;
            color: #fff;
            font-size: 1rem;
            cursor: pointer;
            transition: background 0.2s;
        }
        .add-form button:hover {
            background: #22543d;
        }
    </style>
</head>
<body>
    <div class="emoji">🌱</div>
    <div class="links">
        {% for link in links %}
        <div style="position:relative;">
            <a class="link" href="{{ link.url }}" target="_blank">{{ link.name }}</a>
            <form method="POST" action="{{ url_for('delete_link', idx=loop.index0) }}" style="display:inline;">
                <button class="delete-btn" title="Delete" onclick="return confirm('Delete this link?');">&times;</button>
            </form>
        </div>
        {% endfor %}
    </div>
    <form class="add-form" method="POST" action="{{ url_for('add_link') }}">
        <input type="text" name="name" placeholder="Link Name" required>
        <input type="url" name="url" placeholder="https://example.com" required>
        <button type="submit">Add Link</button>
    </form>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    return render_template_string(HTML, links=links)

@app.route("/add", methods=["POST"])
def add_link():
    name = request.form.get("name", "").strip()
    url = request.form.get("url", "").strip()
    if name and url:
        links.append({"name": name, "url": url})
    return redirect(url_for('home'))

@app.route("/delete/<int:idx>", methods=["POST"])
def delete_link(idx):
    if 0 <= idx < len(links):
        links.pop(idx)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)