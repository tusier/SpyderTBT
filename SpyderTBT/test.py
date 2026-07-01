import requests

result=requests.get('https://www.sac.gov.cn/xw/tzgg/index.html')
print(result.text)
