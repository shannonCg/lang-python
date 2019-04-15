import json

obj = {'key1':('每每','立立'), 'key2':('aa', 'bb')}
encode_json = json.dumps(obj, ensure_ascii=False)
print(repr(obj))
print(encode_json)

file_path = "./json_file.txt"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(encode_json)
    print("create file successfully")