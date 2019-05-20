import pyqrcode,json,png
data={"medicine_id":"sanglipunecipla","medicine":"cipla","quality":"GOOD","timestamp":"Wed Oct 3 07:23:13 2018"}
myJSON=json.dumps(data)
qr=pyqrcode.create(myJSON)
qr.png('medicine.png',scale=10)