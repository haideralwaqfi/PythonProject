import qrcode


class MyQR:
    def __init__(self, size: int, padding: int):
        self.qr = qrcode.main.QRCode(box_size=size, border=padding)

    def create_qr(self, file_name: str, fg: str, bg: str):
        user_input: str = input('Enter your text: ')

        try:
            self.qr.add_data(user_input)
            qr_image = self.qr.make_image(fill_color=fg, back_color=bg)
            qr_image.save(file_name)
            print(f'Successfully created! ({file_name})')
        except Exception as e:
            print(f'Error: {e}')


def main():
    qr: MyQR = MyQR(30, 2)
    qr.create_qr('sample.png',
                 fg='black',
                 bg='white')


if __name__ == '__main__':
    main()
