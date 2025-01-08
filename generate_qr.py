import qrcode

class MyQR:
    def __init__(self, size: int, padding: int):
        self.qr = qrcode.QRCode(box_size= size, border= padding)



def main():
    qr: MyQR = MyQR(10,10)
    print(qr)
if __name__ == '__main__':
    main()

