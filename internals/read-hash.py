
fin = open("commit_file", 'r')
zip_content = fin.read()

import zlib

file_content = zlib.decompress(zip_content)

print("file_content:")
print(file_content)

fin.close()

fin = open("tree", 'r')

zip_content = fin.read()
tree_content = zlib.decompress(zip_content)
tree_content_repr = repr(tree_content)
tree_content_repr.replace("\\x", "")
print("\n\ntree_content:")
print(repr(tree_content_repr))




