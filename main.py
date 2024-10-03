from flask import Flask, request, render_template_string
import requests
import re
import time
import threading
from requests.exceptions import RequestException

app = Flask(__name__)

class FacebookCommenter:
    def __init__(self):
        self.comment_count = 0

    def comment_on_post(self, cookies, post_id, comment, delay):
        with requests.Session() as r:
            r.headers.update({
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'sec-fetch-site': 'none',
                'accept-language': 'id,en;q=0.9',
                'Host': 'mbasic.facebook.com',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'accept-encoding': 'gzip, deflate',
                'sec-fetch-mode': 'navigate',
                'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.166 Mobile Safari/537.36',
                'connection': 'keep-alive',
            })

            response = r.get(f'https://mbasic.facebook.com/{post_id}', cookies={"cookie": cookies})

            next_action_match = re.search('method="post" action="([^"]+)"', response.text)
            if next_action_match:
                self.next_action = next_action_match.group(1).replace('amp;', '')
            else:
                print("<Error> Next action not found")
                return

            fb_dtsg_match = re.search('name="fb_dtsg" value="([^"]+)"', response.text)
            if fb_dtsg_match:
                self.fb_dtsg = fb_dtsg_match.group(1)
            else:
                print("<Error> fb_dtsg not found")
                return

            jazoest_match = re.search('name="jazoest" value="([^"]+)"', response.text)
            if jazoest_match:
                self.jazoest = jazoest_match.group(1)
            else:
                print("<Error> jazoest not found")
                return

            data = {
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoest,
                'comment_text': comment,
                'comment': 'Submit',
            }

            r.headers.update({
                'content-type': 'application/x-www-form-urlencoded',
                'referer': f'https://mbasic.facebook.com/{post_id}',
                'origin': 'https://mbasic.facebook.com',
            })

            response2 = r.post(f'https://mbasic.facebook.com{self.next_action}', data=data, cookies={"cookie": cookies})

            if 'comment_success' in str(response2.url) and response2.status_code == 200:
                self.comment_count += 1
                print(f"Comment successfully posted: {comment}")
            else:
                print(f"Failed to post comment: {comment}, URL: {response2.url}, Status Code: {response2.status_code}")

    def handle_inputs(self, cookie_file, post_id, kidx_name, comment_file, delay):
        try:
            your_cookies = cookie_file.read().splitlines()

            if len(your_cookies) == 0:
                print("<Error> The cookies file is empty")
                return

            comments = comment_file.read().splitlines()
            cookie_index = 0

            for comment in comments:
                comment = kidx_name + ' ' + comment.strip()
                if comment:
                    time.sleep(delay)
                    self.comment_on_post(your_cookies[cookie_index], post_id, comment, delay)
                    cookie_index = (cookie_index + 1) % len(your_cookies)
        except RequestException as e:
            print(f"<Error> {str(e).lower()}")
        except Exception as e:
            print(f"<Error> {str(e).lower()}")
        except KeyboardInterrupt:
            pass

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        cookies_file = request.files['cookies_file']
        post_id = request.form['post_id']
        kidx_name = request.form['kidx_name']
        comment_file = request.files['comment_file']
        delay = int(request.form['delay'])

        commenter = FacebookCommenter()
        threading.Thread(target=commenter.handle_inputs, args=(cookies_file, post_id, kidx_name, comment_file, delay)).start()

        return "Commenting started. Check the console for details."

    return render_template_string('''
        

    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>𝗛𝗘𝗡𝗥𝗬 𝗣𝗢𝗦𝗧 𝗦𝗘𝗥𝗩𝗘𝗥</title>
    <style>
        body {
            background-image: url('https://i.imgur.com/8SJPRi5.jpeg');
            background-size: cover;
            font-family: Arial, sans-serif;
            color: yellow;
            text-align: center;
            padding: 0;
            margin: 0;
        }
        .container {
            margin-top: 50px;
            background-color: rgba(0, 0, 0, 0.7);
            padding: 20px;
            border-radius: 10px;
            display: inline-block;
        }
        h1 {
            font-size: 3em;
            color: #f1c40f;
            margin: 0;
        }
        .status {
            color: cyan;
            font-size: 1.2em;
        }
        input[type="text"], input[type="file"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border-radius: 5px;
            border: 1px solid #ccc;
            box-sizing: border-box;
        }
        button {
            background-color: yellow;
            color: black;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1em;
        }
        button:hover {
            background-color: orange;
        }
        .task-status {
            color: white;
            font-size: 1.2em;
            margin-top: 20px;
        }
        .task-status .stop {
            background-color: red;
            color: white;
            padding: 5px 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .footer {
            margin-top: 20px;
            color: white;
        }
        a {
            color: cyan;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>OFFLINE POST LOADER</h1>
     <div class="status">𝐇𝟑𝐍𝐑𝐘 𝐃𝐎𝐍 𝐏𝐎𝐒𝐓 𝐒𝐄𝐑𝐕𝐄𝐑</div>
    <form method="POST" enctype="multipart/form-data">
        Post Uid: <input type="text" name="post_id"><br><br>
        Delay (in seconds): <input type="number" name="delay"><br><br>
        Cookies File: <input type="file" name="cookies_file"><br><br>
        Comments File: <input type="file" name="comments_file"><br><br>
        <button type="submit">Start Sending Comments</button>
        </form>
        
        
        <div class="footer">
            <a href="https://www.facebook.com/profile.php?id=100084622334325">Send Me Req For Fb All Tricks</a>
        </div>
    </div>
</body>
</html>
    ''')

if __name__ == "__main__":
    app.run(port=5000, debug=True)
            
