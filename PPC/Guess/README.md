# Guess
## Challenge
```
Timeout : 120s

Author : Curious

---

`nc lab.scist.org 33343`
```

---
## Hints
````
二分搜尋法
```python
# range_list[0] <= ans < range_list[1]
range_list = [1, 1073741825]

while True:
    guess_num = (range_list[0] + range_list[1]) // 2

    if ans < guess_num:
        range_list[1] = guess_num
    elif ans > guess_num:
        range_list[0] = guess_num + 1
    else:
        assert guess_num == ans
        break
```
````

---
## Files
- `server.py`

---
## Flag
```
SCIST{D3vid3...dIviD3...D1v1dE...G0t_yOu!}
```