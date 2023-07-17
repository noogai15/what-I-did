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

wk_start = 0
wk_end = 1
bullet = "•"


def create_message(done_tasks, todo_tasks):
    today = datetime.date.today()
    today_head = f"Today ({today:%d.%m})"
    if today.weekday() == wk_end:
        delta = wk_start - today.weekday()
        if delta <= 0:
            delta += 7
        next_day = today + datetime.timedelta(days=delta)
        plan_head = f"{next_day.strftime('%A')} ({next_day:%d.%m})"
    else:
        next_day = today + datetime.timedelta(days=1)
        plan_head = f"Tomorrow ({next_day:%d.%m})"

    done_str = f"\n{bullet} ".join(done_tasks)
    todo_str = f"\n{bullet} ".join(todo_tasks)

    msg = (
        f"{today_head}:\n{bullet} {done_str}\n\n" f"{plan_head}:\n{bullet} {todo_str}\n"
    )
    return msg


def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <done_tasks> <todo_tasks>")
        sys.exit(1)

    done_tasks = sys.argv[1].split(",")
    todo_tasks = sys.argv[2].split(",")

    msg = create_message(done_tasks, todo_tasks)
    print(msg)


if __name__ == "__main__":
    main()
