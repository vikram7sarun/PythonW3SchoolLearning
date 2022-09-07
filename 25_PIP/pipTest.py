# pip --version
# pip install camelcase
# pip uninstall camelcase


import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))