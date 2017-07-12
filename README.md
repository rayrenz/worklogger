Django Exercise: Worklogger

Create a website where I could sign in and log my hours for the day.
After signing in, there should be a form where I could input a new time log, and below it is a list of all my logs for the day.

Example:

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxx
x                                                                            x
x Hello Jayjay!                                                             x
x                                                                            x
x LOG YOUR TIME BELOW:                                                      x
x  DURATION        PROJECT                      REMARKS                    x
x  ___________    __________________________   ______________________      x
x [___________]  [________________________|v] [______________________]     x
x                                                                            x
x TOTAL LOG FOR THE DAY: 5.75 hours                                         x
x                                                                            x
x  DURATION        PROJECT                      REMARKS                    x
x ------------------------------ ------------------------------ --------     x
x    3.0h          EMS Service                  Created models.            x
x ------------------------------ ------------------------------ --------     x
x    1.0h          EMS Service                  Setup project.             x
x ------------------------------ ------------------------------ --------     x
x    1.75h         PinasCongMahal.com           Meeting with client.       x
x ------------------------------ ------------------------------ --------     x
x                                                                            x
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxx

Implement this page, along with the following features:

Administrators:
Ability to add/edit/remove projects through Django admin. (5pts)
Add/edit/delete users through Django admin. (5pts)
Modifying hours already logged through Django admin. (5pts)
Deleting projects should not delete hours logged for that project. The project assigned for those hours can be NULL. (5pts)

Users:
Log hours for any selected day. (10pts)
See logs for the day. (5pts)
See total logged hours for the week and month based on selected day. (5pt)
Ability to select a day and load logs for that day (10pts)
Bonus: use a calendar layout to select the day (6pts)
Bonus: mark late logs with red text (a log for the selected day is late if it was created after the given day) (4pts)# worklogger
