import time

todayDate=time.strftime("%d/%m/%Y");
gelenDate="17/04/2018";

a="abc" + "_"+ gelenDate
print("a =" +a)
if(todayDate==gelenDate):
    print("Bugünün tarihi")
else:
    print("Değil")

