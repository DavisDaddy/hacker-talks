content = "what is up, doc?"
header = "blob #{content.length}\0"

store = header + content

require 'digest/sha1'
sha1 = Digest::SHA1.hexdigest(store)
print "SHA hexdigest:\n"
print sha1, "\n"

require 'zlib'
zlib_content = Zlib::Deflate.deflate(store)
print "zlib_content:\n"
print zlib_content.inspect, "\n"

require 'fileutils'
File.open('./zlc_ruby', 'w') { |f| f.write zlib_content }

