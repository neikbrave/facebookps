import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Thiết lập thông tin email
from_email = "kinofficial.2002@gmail.com"
to_email = "kinofficial.202@gmail.com"
subject = "You've been invited to join"
body_html = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Invitation Email</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f6f7;
            margin: 0;
            padding: 0;
        }

        .container {
            max-width: 600px;
            margin: 20px auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        .header {
            text-align: center;
        }

        .header img {
            width: 50px;
        }

        .header h2 {
            font-size: 24px;
            margin: 10px 0;
        }

        .content {
            text-align: center;
        }

        .content p {
            font-size: 16px;
            line-height: 1.5;
            color: #333;
        }

        .content a {
            display: inline-block;
            margin: 20px 0;
            padding: 10px 20px;
            background-color: #007bff;
            color: #fff;
            text-decoration: none;
            border-radius: 4px;
        }

        .content a:hover {
            background-color: #0056b3;
        }

        .footer {
            font-size: 12px;
            color: #888;
            margin-top: 20px;
            text-align: center;
        }

        .footer a {
            color: #888;
            text-decoration: none;
        }

        .footer a:hover {
            text-decoration: underline;
        }
    </style>
</head>

<body>
    <div class="container">
        <div class="header">
            <img src="meta-logo.png" alt="Meta Logo">
            <h2>You're invited to join Zeynep Hurcan</h2>
        </div>
        <div class="content">
            <p><strong>Kami sama</strong> invited you to join <strong>Zeynep Hurcan</strong>'s business portfolio on
                Meta Business Suite.</p>
            <p>This invitation will expire on Nov 23, 2024 and you won’t be able to accept the invite anymore.</p>
            <p>You may need to log in with your managed Meta account if it’s required by your organization.</p>
            <a href="#">View invitation</a>
            <a href="#">Learn more</a>
        </div>
        <div class="content">
            <h3>Everything in One Place</h3>
            <p>See and access all of the Pages and ad accounts you need to work on in one convenient place.</p>
            <h3>Work faster and better</h3>
            <p>Save time by using your Facebook login to access all your Pages and ad accounts.</p>
            <h3>Keep work separate</h3>
            <p>You don’t need to be friends with anyone from work to get access to Pages and ad accounts.</p>
        </div>
        <div class="footer">
            <p>This message was sent to kinoficial202@gmail.com</p>
            <p>If you don’t want to receive these emails from Meta in the future, please <a href="#">unsubscribe</a>.
            </p>
            <p>Meta Platforms, Inc., Attention: Community Support, 1 Meta Way, Menlo Park, CA 94025</p>
        </div>
    </div>
</body>

</html>
"""

# Tạo đối tượng email
msg = MIMEMultipart('alternative')
msg['Subject'] = subject
msg['From'] = from_email
msg['To'] = to_email

# Đính kèm nội dung HTML
msg.attach(MIMEText(body_html, 'html'))

# Kết nối đến máy chủ SMTP và gửi email
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(from_email, "k7112002")
    server.sendmail(from_email, to_email, msg.as_string())
