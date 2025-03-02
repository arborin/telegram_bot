import ssl
import urllib.request


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

ip = "8.8.8.8"

contents = urllib.request.urlopen(f"https://ipapi.co/{ip}/json/", context=ctx).read()
print(contents)