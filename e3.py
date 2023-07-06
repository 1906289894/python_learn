"""
中英文翻译
要求：
1.在命令行窗口运行
2.当程序运行时，对输入的英文或中文进行翻译
3.输入 exit 结束程序
"""
import requests

url = 'https://fanyi.baidu.com/sug'

while True:
    text = input(f'请输入中文或者英文：')

    if text == 'exit':
        break

    data = {'kw': text}

    resp = requests.post(url, data)

    found = False

    if resp.status_code == 200:
        data = resp.json()
        if data['errno'] == 0:
            ds = data['data']
            for kv in ds:
                if kv['k'] == text:
                    found = True
                    print(kv['v'])
        else:
            print(data)
    else:
        print(resp.content)