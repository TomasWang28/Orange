# import json
# a = {"name":"Tom", "age":23}
# with open("test.json", "w", encoding='utf-8') as f:
#     # indent 超级好用，格式化保存字典，默认为None，小于0为零个空格
#     f.write(json.dumps(a, indent=4))
#     # json.dump(a,f,indent=4)   # 和上面的效果一样


# import json
# with open("test.json", "r", encoding='utf-8') as f:
#     aa = json.loads(f.read())
#     f.seek(0)
#     bb = json.load(f)    # 与 json.loads(f.read())
# print(aa)
# print(bb)

# import json
# with open("test.json", "r", encoding='utf-8') as f:
#     aa = f.read()
#     f.seek(0)
#     bb = f    # 与 json.loads(f.read())
# print(aa)
# print(bb)