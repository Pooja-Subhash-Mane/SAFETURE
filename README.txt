1. Connect to the IoT devices.
2. Add manually the entry(as per the manufacturer) into the website (index.html)  regarding the source, destination, medicine name, quantity, and medicine required temperature and click on add record.
3. Go to the Safeture folder and run blockchain_final.py file. Then the server will get started.
4. Type 10.60.1.103:5000/chain in the browser and the chain will appear.
5. To see the container summary, enter 10.60.1.103:5000/track_order in the browser.
6. By redirecting to 10.60.1.103:5000/add_block the block automatically gets added into the chain as per the location sensed by the GPS.
7. If an accident occurs then it is detected and notified to the manufacturer and retailer via mail.
8. Finally, when the pharmaceuticals reach the retailer and he is selling it, the customer will scan the QR code present on the medicine using an Android App and check whether the quality of medicine is good or bad .