import re

#gmail 格式
email = "Random@gmail.com"
print(re.search("(@gmail.com)$",email))