from datetime import datetime, timedelta, timezone

now = datetime.now()
print(now)
print(type(now))

dt = datetime(2015, 4, 19, 12, 20, 22)
print(dt)
ts = dt.timestamp()
print(ts)

t = 1429417200.0
print(datetime.fromtimestamp(t))

t = 1429417200.0
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))

cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))

now = datetime.now()
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=12))

tz_utc_8 = timezone(timedelta(hours=8))  # 创建时区UTC+8:00
now = datetime.now()
print(now)

dt = now.replace(tzinfo=tz_utc_8)
print(dt)

utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# astimezone()将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
# astimezone()将转换时区为东京时间:
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
# astimezone()将bj_dt转换时区为东京时间:
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)
