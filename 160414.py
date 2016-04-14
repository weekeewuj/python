json_result = json.loads(content)
content_list = json_result['showapi_res_body']['contentlist']
minlen = 10000
for item in content_list:
    if len(item['text'])<minlen:
        title = item['title']
        text = item['text']
        minlen = len(item['text'])
