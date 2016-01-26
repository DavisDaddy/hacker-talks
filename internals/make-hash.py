fin = open("first-file", 'r')
content = fin.read()
print(content)

######content = "what is up, doc?"
header  = "blob {0}\0".format(len(content))
##print(repr(header))

store = header + content
##print(repr(store))

import hashlib
sha1 = hashlib.sha1()

sha1.update(store)
##print("SHA:)
##print(repr(sha1))

sha1_digest = sha1.hexdigest()
print("SHA hexdigest:")
print(repr(sha1_digest))

import zlib
zlib_content = zlib.compress(store)

print("zlib_content:")
print(repr(zlib_content))

fout = open("zlc_python", 'w')
fout.write(zlib_content)
fout.close()


