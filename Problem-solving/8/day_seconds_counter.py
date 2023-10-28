from datetime import datetime

def calculate_seconds_from_start_of_day():
    now = datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = now - midnight

    # تعداد ثانیه‌های گذشته
    seconds = delta.total_seconds()
    return int(seconds)

# محاسبه تعداد ثانیه‌های گذشته از ابتدای روز جاری
seconds_passed = calculate_seconds_from_start_of_day()
print(f'تعداد ثانیه‌ها از ابتدای امروز: {seconds_passed} ثانیه')