import hashlib
text = 'hello'
m = hashlib.md5(text.encode('utf-8'))
print("md5: ",m.hexdigest())
