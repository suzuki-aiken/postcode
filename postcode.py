"""
WebAPI

"""
import requests


def main():
    # 入力

    zipcode = input("郵便番号を入力: ")
    url = f'http://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}'

    response = requests.get(url)

    # 出力

    address = response.json()['results'][0]
    都道府県 = address['address1']
    市区町村 = address['address2']
    町域 = address['address3']

    address = f"{都道府県}{市区町村}{町域}"

    print(address)


if __name__ == '__main__':
    main()
