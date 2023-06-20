import json
from json2html import *

with open("D:\display-html\output.json", encoding="utf-8") as f:
    d = json.load(f)
    scanOutput = json2html.convert(json=d)
    htmlReportFile = "D:\display-html\index.html"
    with open(htmlReportFile, 'w', encoding='utf-8') as htmlfile:
        htmlfile.write(str(scanOutput))
        print("Json file converted into html successfully.")
