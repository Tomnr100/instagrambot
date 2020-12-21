from datetime import datetime

now = str(datetime.now())
now = now.replace(':', '-').replace(' ', '-').replace('.', '-')
print(now)