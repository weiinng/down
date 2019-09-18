from django.test import TestCase

# Create your tests here.
import re



ret = re.match("^/users/delete/(\d+)$", "/users/delete/1/")
print(ret)

# ret = re.match("\d+", "1")
# print(ret)