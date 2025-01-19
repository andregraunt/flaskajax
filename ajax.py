from flask import Flask, render_template_string, jsonify
import markdown
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Auto-Refresh</title>
        <script>
            function refreshContent() {
                fetch('/content')
                    .then(response => response.text())
                    .then(data => {
                        document.getElementById('content').innerHTML = data;
                    });
            }
            setInterval(refreshContent, 1000);  // Обновление каждые 5 секунд
        </script>
    </head>
    <body>
        <div id="content">{{ content }}</div>
    </body>
    </html>
    ''', content=get_markdown_content())

@app.route('/content')
def content():
    return get_markdown_content()

def get_markdown_content():
    with open('index.md', 'r', encoding='utf-8') as f:
        content = f.read()
    return markdown.markdown(content)

if __name__ == '__main__':
    app.run(debug=True, port=7070)