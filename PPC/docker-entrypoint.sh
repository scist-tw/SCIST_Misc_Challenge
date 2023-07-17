#!/bin/sh

socat TCP-LISTEN:33340,fork EXEC:"timeout 10 python3 /chal/Welcome/server.py" &
socat TCP-LISTEN:33342,fork EXEC:"timeout 120 python3 /chal/Count/server.py" & 
socat TCP-LISTEN:33341,fork EXEC:"timeout 10 python3 /chal/Nth/server.py" & 
socat TCP-LISTEN:33343,fork EXEC:"timeout 120 python3 /chal/Guess/server.py" & 
socat TCP-LISTEN:33344,fork EXEC:"timeout 120 python3 /chal/Calculator/server.py" & 
socat TCP-LISTEN:33345,fork EXEC:"timeout 120 python3 /chal/Alphabet/server.py" & 
socat TCP-LISTEN:33346,fork EXEC:"timeout 120 python3 /chal/Digit/server.py" & 
socat TCP-LISTEN:33347,fork EXEC:"timeout 120 python3 /chal/PI/server.py" & 
exec socat TCP-LISTEN:33348,fork EXEC:"timeout 120 python3 /chal/Hanoi/server.py"