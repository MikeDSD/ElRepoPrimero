from datetime import datetime
from datetime import timedelta
# dt = datetime.now()
#
#print(dt)
#print(dt.year)
#print(dt.month)
#print(dt.day)
#
#print(dt.hour)
#print(dt.minute)
#
#dt2 = datetime(2021, 9,8, 22, 13)
#
#print(dt2.strftime("%A %d %B %Y %I:%M"))

birthday = datetime(2002, 5, 9, 16, 30)

actual = timedelta(days=7640)

resultado = birthday + actual

print(resultado)
