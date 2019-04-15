import os

#u mean use unicode format
pre_html = u"""
<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
<title> 衛福部新聞發布資訊 </title>
</head>  
"""

post_html = u"""
<body>
<h2> 衛福部新聞發布資訊(取自衛福部網站) </h2>
<table width=600 border=1>
<tr><td>日期</td><td>新聞資訊</td></tr>
{body}
</table>
</body>
</html>
"""

def store_information_in_html(contents):
    body_template = '<tr><td>{date}</td><td><a href="{info_url}">{info}</a></td></tr>'
    body = ""
    # for content in contents:
    for content in contents:
        body += body_template.format(date=content[0], info_url=content[1], info=content[2])

    html_file = pre_html + post_html.format(body=body)

    # create directory to store images
    dir_path = r"C:/Users/user/files"
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
        print("create directory successfully!")

    # store image into the directory
    file_path = os.path.join(dir_path, 'nhi_news.html')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html_file)
        print("create file successfully")