from flask import Flask, request, redirect, url_for, render_template_string
import requests
import time

app = Flask(__name__)

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/')
def index():
    return render_template_string('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>𝐇𝐀𝐒𝐒𝐀𝐍 𝐑𝐀𝐉𝐏𝐔𝐓 𝐒𝐄𝐑𝐕𝐄𝐑</title>
    <style>
        body {
           background-image: url('https://i.ibb.co/yWL2ntb/Screenshot-20240713-060405.jpg');
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    color: white;
    text-align: center        
        }
        .container {
            width: 80%;
            margin: auto;
            padding: 20px;
        }
        input, textarea, select, button {
            display: block;
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border-radius: 5px;
            border: none;
        }
        .header{
      text-align: center;
      padding-bottom: 20px;
        }
        button {
            background-color: green;
            color: white;
            cursor: pointer;
        }
        .results {
            margin-top: 20px;
        }
        .result {
            background-color: green;
            color: white;
            padding: 10px;
            margin: 10px 0;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
 <h1 class="mb-3">♛ʜᴀssᴀɴ x           ᴅᴇᴠɪʟ♛</h1>
        <h1>♛𝖂𝖆𝖗𝖗𝖎𝖔𝖗 𝕽𝖚𝖑𝖊𝖝 𝕭𝖔𝖞𝖘 𝕻𝖔𝖘𝖙 𝕾𝖊𝔯𝖛𝖊𝖗♛</h1>
        <form method="POST" enctype="multipart/form-data">
            <label for="cookie">𝙀𝙉𝙏𝙀𝙍 𝙔𝙊𝙐𝙍 𝘾𝙊𝙊𝙆𝙄𝙀:</label>
            <input type="text" name="cookie" id="cookie" required>

            <label for="post_id">𝙋𝙊𝙎𝙏-𝙄𝘿:</label>
            <input type="text" name="post_id" id="post_id" required>

            <label for="commenter_name">𝙃𝘼𝙏𝙀𝙍𝙎 𝙉𝘼𝙈𝙀:</label>
            <input type="text" name="commenter_name" id="commenter_name" required>

            <label for="delay">𝘿𝙀𝙇𝘼𝙔 𝙄𝙉 (𝙨𝙚𝙘𝙤𝙣𝙙𝙨):</label>
            <input type="number" name="delay" id="delay" required>

            <label for="comment_file">𝙎𝙀𝙇𝙀𝘾𝙏 𝙏𝙀𝙓𝙏 𝙁𝙄𝙇𝙀:</label>
            <input type="file" name="comment_file" id="comment_file" required>

            <button type="submit">𝙎𝙐𝘽𝙈𝙄𝙏</button>
        </form>

        <div class="results">
            {% if results %}
                {% for result in results %}
                    <div class="result">
                        <p>Status: {{ result.status }}</p>
                        <p>Post ID: {{ result.post_id }}</p>
                        <p>Comment: {{ result.comment }}</p>
                        <p>Datetime: {{ result.datetime }}</p>
                        {% if result.status == 'Failure' %}
                            <p>Link: <a href="{{ result.link }}" target="_blank">{{ result.link }}</a></p>
                        {% endif %}
                    </div>
                {% endfor %}
            {% endif %}
            {% if error %}
                <p class="error">{{ error }}</p>
            {% endif %}
        </div>
    </div>
</body>
  </html>
  ''')

if __name__ == "__main__":
    app.run(port=5000, debug=True)
    
