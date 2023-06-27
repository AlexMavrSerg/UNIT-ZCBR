import json
import ftplib
from json2html import *

path = '/vita-dev.com/public_html'
filename = 'output.json'
ftp = ftplib.FTP("e97891sb.beget.tech")
ftp.login("e97891sb_nayrest", "i4tpx70As!")
ftp.cwd(path)
ftp.retrbinary("RETR " + filename, open(filename, 'wb').write)
ftp.quit()

with open("output.json", encoding="utf-8") as f:
    d = json.load(f)
    scanOutput = json2html.convert(json=d)
    htmlReportFile = r"D:\Web Development\json2html\UNIT-ZCBR\index.html"
    with open(htmlReportFile, 'w', encoding='utf-8') as htmlfile:
        htmlfile.write(str(scanOutput))
        print("Json file converted into html successfully.")