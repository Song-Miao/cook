# -*- coding:utf-8 -*-


def t01():
    from datetime import timedelta
    a = timedelta(days=2, hours=6)
    b = timedelta(hours=4.5)
    c = a + b
    print(c.days, c.seconds / 3600)
    print(c.total_seconds() / 3600)

    from datetime import datetime
    a = datetime(2019, 1, 1)
    b = datetime(2019, 1, 2)
    print(b - a)


def t02():
    # strptime()的性能要比你想象中的差很多，
    # 因为它是使; 用纯; Python; 实现，
    # 并且必须处理所有的系统本地设置
    from datetime import datetime
    text = '2019-02-01'
    y = datetime.strptime(text, '%Y-%m-%d')
    z = datetime.now()
    print(z - y)
    print(datetime.strftime(y, '%Y-%m-%d %H:%M:%S'))


def t03():
    from datetime import datetime, timedelta, timezone
    utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
    print(utc_dt)
    cn_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
    print(cn_dt)
    jan_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
    print(jan_dt)
    cn_2_jan_dt = cn_dt.astimezone(timezone(timedelta(hours=9)))
    print(cn_2_jan_dt)


if __name__ == '__main__':
    t03()
