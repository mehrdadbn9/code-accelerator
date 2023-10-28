from datetime import datetime

def calculate_date_difference(target_date):
    today = datetime.now().date()
    delta = target_date - today

    if delta.days < 0:
        return f'{abs(delta.days)} روز گذشته'
    elif delta.days > 0:
        return f'{delta.days} روز باقی مانده'
    else:
        return 'امروز'

# ورودی: "YYYY-MM-DD"
target_date_str = input("لطفاً یک تاریخ را وارد کنید (مثال: 2022-07-15): ")
target_date = datetime.strptime(target_date_str, "%Y-%m-%d").date()

result = calculate_date_difference(target_date)
print(result)