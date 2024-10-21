from datetime import datetime, timedelta
import time

birth = datetime(1994, 11, 2)
current_time = datetime.now() + timedelta(days=1, seconds=1000)
birthday_from_user_input_conversion = datetime.strptime('1994/11/2', '%Y/%m/%d')
dt = datetime.fromtimestamp(time.time())

# print(f'{dt.year}/{dt.month}')
# print(dt.strftime('%Y/%m'))

# print(current_time > birth)

duration = current_time - birth
print(duration)
print('days', duration.days)
print('seconds', duration.seconds)
print('total_seconds', duration.total_seconds())