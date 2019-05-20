import serial
import pyqrcode,json,png
ser=serial.Serial('COM4',9600)
arr=[]
arr1=[]
x=0

while x<10:
    t=ser.readline()
    z=int(t)
    print(z)
    if z<=40 and z>=20:
        arr.append(z)
    x+=1
    

print(arr)
for i in arr:
    if i<=30 and i>=25:
        arr1.append("yes")
    else:
        arr1.append("no")

for j in arr1:
    if j=="no":
        print("BAD")
        data={"medicine_id":"sanglipunecipla","medicine":"cipla","quality":"BAD","timestamp":"Wed Oct 3 07:23:13 2018"}
        myJSON=json.dumps(data)
        qr=pyqrcode.create(myJSON)
        qr.png('medicine.png',scale=10)
        break
    else:
        print("GOOD")
        data={"medicine_id":"sanglipunecipla","medicine":"cipla","quality":"GOOD","timestamp":"Wed Oct 3 07:23:13 2018"}
        myJSON=json.dumps(data)
        qr=pyqrcode.create(myJSON)
        qr.png('medicine.png',scale=10)
        break











