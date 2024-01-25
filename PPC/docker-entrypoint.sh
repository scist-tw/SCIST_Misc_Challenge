#!/bin/sh

socat TCP-LISTEN:50000,fork EXEC:"timeout 10 python3 /chal/Welcome/server.py" &
socat TCP-LISTEN:50001,fork EXEC:"timeout 120 python3 /chal/Count/server.py" & 
socat TCP-LISTEN:50002,fork EXEC:"timeout 10 python3 /chal/Nth/server.py" & 
socat TCP-LISTEN:50003,fork EXEC:"timeout 120 python3 /chal/Guess/server.py" & 
socat TCP-LISTEN:50004,fork EXEC:"timeout 120 python3 /chal/Calculator/server.py" & 
socat TCP-LISTEN:50005,fork EXEC:"timeout 120 python3 /chal/Alphabet/server.py" & 
socat TCP-LISTEN:50006,fork EXEC:"timeout 120 python3 /chal/Digit/server.py" & 
socat TCP-LISTEN:50007,fork EXEC:"timeout 120 python3 /chal/PI/server.py" & 
exec socat TCP-LISTEN:50008,fork EXEC:"timeout 120 python3 /chal/Hanoi/server.py"