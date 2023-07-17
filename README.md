# What I did

Are you required to document what you did today and will do tomorrow at the end of every work shift?  
Looking for, copying, pasting your previous entry to edit it is annoying (even more so in Teams because it doesn't copy over the formatting) and this is a bit more convenient.

## Requirements

Python 3.6 or higher

## Usage

Run the script from the command line with two arguments:  
A comma-separated list of finished tasks and another for planned tasks.

Example:  
`python main.py "Task 1,Task 2,Task 3" "Task 4,Task 5"`

## Output

```
Today (01.01):
• Task 1
• Task 2
• Task 3

Tomorrow (02.01):
• Task 4
• Task 5
```

You can customize the start and end days of your work week by modifying the weekday_first and weekday_last variables at the top of the script.
The days of the week are represented as integers, where Monday is 0 and Sunday is 6.
