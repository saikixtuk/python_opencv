@echo off

if not exist ./analyses/img/push (
    mkdir analyses\img\push
)

if not exist ./analyses/img/push/later (
    mkdir analyses\img\push\later
)

python ./analyses/img/rename.py

python ./analyses/anly.py

pause