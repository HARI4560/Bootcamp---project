import hashlib
text = 'hello'
m = hashlib.sha512(text.encode('utf-8'))
print("sha512: ", m.hexdigest());

m = hashlib.sha1(text.encode('utf-8'))
print ("sha1: ", m.hexdigest());

m= hashlib.sha224(text.encode('utf-8'))
print("sha224: ", m.hexdigest())
