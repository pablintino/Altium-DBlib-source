@echo off
set /p pass="Enter password: "
for %%G in (*.sql) do sqlcmd /S localhost /d altium_db -U librarian -P %pass% -i"%%G"