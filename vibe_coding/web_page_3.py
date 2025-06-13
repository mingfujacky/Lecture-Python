'''
modify the layout to add a 650 pixels center frame, and move the trash buttons to the right of this links
'''
from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

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
    <meta name="viewport" content="width=650">
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
        .center-frame {
            width: 650px;
            background: rgba(24, 58, 29, 0.97);
            border-radius: 2rem;
            box-shadow: 0 4px 32px rgba(0,0,0,0.18);
            padding: 3rem 2rem 2rem 2rem;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .emoji {
            font-size: 7rem;
            margin-bottom: 2rem;
        }
        .links {
            width: 100%;
            display: flex;
            flex-direction: column;
            gap: 1.2rem;
            margin-bottom: 2rem;
        }
        .link-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: #22543d;
            border-radius: 2rem;
            padding: 0.8rem 1.5rem 0.8rem 2rem;
            position: relative;
            transition: background 0.2s;
        }
        .link-row:hover {
            background: #38a169;
        }
        .link {
            text-decoration: none;
            color: #fff;
            font-size: 1.2rem;
            transition: color 0.2s;
        }
        .link-row:hover .link {
            color: #183a1d;
        }
        .delete-btn {
            background: #e53e3e;
            color: #fff;
            border: none;
            border-radius: 50%;
            width: 1.7rem;
            height: 1.7rem;
            cursor: pointer;
            font-size: 1.1rem;
            margin-left: 1.2rem;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: background 0.2s;
        }
        .delete-btn:hover {
            background: #c53030;
        }
        .add-form {
            display: flex;
            gap: 1rem;
            margin-top: 1rem;
            width: 100%;
            justify-content: center;
        }
        .add-form input[type="text"], .add-form input[type="url"] {
            padding: 0.5rem 1rem;
            border-radius: 1rem;
            border: none;
            font-size: 1rem;
            width: 180px;
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
        @media (max-width: 700px) {
            .center-frame {
                width: 98vw;
                padding: 1rem 0.5rem;
            }
        }
    </style>
</head>
<body>
    <div class="center-frame">
        <div class="emoji">🌱</div>
        <div class="links">
            {% for link in links %}
            <div class="link-row">
                <a class="link" href="{{ link.url }}" target="_blank">{{ link.name }}</a>
                <form method="POST" action="{{ url_for('delete_link', idx=loop.index0) }}" style="margin:0;">
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
    </div>
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