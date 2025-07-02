import qrcode

#taking upi id as input
upi_id = input("Enter your UPI ID = ")

#payment URL

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'


#create qr code

phonepe_qr = qrcode.make(phonepe_url)
google_pay_qr = qrcode.make(google_pay_url)
paytm_qr = qrcode.make(paytm_url)

#save the qr code to image file

phonepe_qr.save('phonepe_qr.png')
google_pay_qr.save('google_pay_qr.png')
paytm_qr.save('paytm_qr.png')


#display the qr code
phonepe_qr.show()
google_pay_qr.show()
paytm_qr.show()