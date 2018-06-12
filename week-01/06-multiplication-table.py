a = int(input ("몇 단을 출력하시겠습니까? "))
if a >= 1 and a < 10:
    for num in range (1, 10):
        print ("{} * {} = {}".format(a, num, num * a))
