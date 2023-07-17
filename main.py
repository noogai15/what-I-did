import datetime
import sys

# Set the weekdays on which you start and end your work week
# 0 => Mon;
# 1 => Tue
# 2 => Wed
# 3 => Thu
# 4 => Fri
# 5 => Sat
# 6 => Sun

weekday_first = 0
weekday_last = 1
bullet_point = "•"


def create_message(finished_tasks, plan_tasks):
    today = datetime.date.today()
    today_heading = "Heute ({:%d.%m})".format(today)
    if today.weekday() == weekday_last:
        delta = weekday_first - today.weekday()  # calculate time until weekday_first
        if delta <= 0:
            delta += 7
        next_workday = today + datetime.timedelta(days=delta)
        plan_heading = f"{next_workday.strftime('%A')} ({next_workday:%d.%m})"
    else:
        next_workday = today + datetime.timedelta(days=1)
        plan_heading = f"Tomorrow ({next_workday:%d.%m})"

    finished_tasks_str = f"\n{bullet_point} ".join(finished_tasks)
    plan_tasks_str = f"\n{bullet_point} ".join(plan_tasks)

    message = (
        f"Heute ({today:%d.%m}):\n{bullet_point} {finished_tasks_str}\n\n"
        f"{plan_heading}:\n{bullet_point} {plan_tasks_str}\n"
    )
    return message


def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <finished_tasks> <plan_tasks>")
        sys.exit(1)

    finished_tasks = sys.argv[1].split(",")
    plan_tasks = sys.argv[2].split(",")

    teams_message = create_message(finished_tasks, plan_tasks)
    print(teams_message)


if __name__ == "__main__":
    main()
