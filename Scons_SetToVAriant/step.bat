@echo OFF
@echo OFF
rem %1 is component name
rem %2 is the ACTION
rem %3 is the batch file to call

setlocal
SET PATH=%PATH%;%~dp3


rem call %3

IF  %2==Cleaning (

title %1   %4/%5:%2    Command: %3 -c
cd %~dp3
call %3 -c

)else IF  %2==Building (

title %1   %4/%5:%2    Command: %3
cd %~dp3
call %3

)Else (

echo "Not Valid"

)
exit
