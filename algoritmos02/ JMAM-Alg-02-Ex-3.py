import time
t = time.localtime()
print('Data: {}:{}:{}\nHora: {}:{}:{}'.format(t.tm_mday,t.tm_mon,t.tm_year,t.tm_hour,t.tm_min,t.tm_sec))