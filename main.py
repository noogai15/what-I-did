import sys
import datetime

def generate_teams_message(finished_tasks, plan_tasks):
    bullet_point = "•"
    today = datetime.date.today()
    today_heading = "Heute ({:%d.%m})".format(today)
    if today.weekday() == 2:  # Wednesday
        tomorrow = today + datetime.timedelta(days=5)  # Next Monday
        plan_heading = "Montag ({:%d.%m})".format(tomorrow)
    else:
        tomorrow = today + datetime.timedelta(days=1)
        plan_heading = "Morgen ({:%d.%m})".format(tomorrow)

    message = "{}:\n".format(today_heading)
    message += "{} {}\n".format(bullet_point, ("\n{} ".format(bullet_point)).join(finished_tasks))
    message += "\n{}:\n".format(plan_heading)
    message += "{} {}\n".format(bullet_point, ("\n{} ".format(bullet_point)).join(plan_tasks))
    return message

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python teams_message_generator.py <finished_tasks> <plan_tasks>")
        sys.exit(1)

    finished_tasks = sys.argv[1].split(",")
    plan_tasks = sys.argv[2].split(",")

    teams_message = generate_teams_message(finished_tasks, plan_tasks)
    print(teams_message)

