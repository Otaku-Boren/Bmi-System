import pandas as pd

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

user_data = dict(���ѩ=list(), ??�\=list(), ��?��=list(), BMI=list(), ��?������d?=list())


def getData():
    name = input("�X�ΤL��??��?:")
    while True:
        try:
            h = float(input("�X�ΤL��??��?(cm):"))
        except ValueError:
            print("�@�Z?���B�a?�Z???ҵ?��`�@�Z?")
            continue
        break
    while True:
        try:
            w = float(input("�X�ΤL��?һ??(kg):"))
        except ValueError:
            print("�@�Z?���B�a?�Z???ҵ?��`�@�Z?")
            continue
        break
    bmi = round(w / ((h * 0.01) ** 2), 1)
    if bmi >= 24:
        if bmi < 27:
            user_data["��?������d?"].append("��?����u��")
        elif bmi < 30:
            user_data["��?������d?"].append("�@�K�`�^?�")
        elif bmi < 35:
            user_data["��?������d?"].append("��?�`�^?�")
        else:
            user_data["��?������d?"].append("??�`�^?�")
    elif bmi >= 18.5:
        user_data["��?������d?"].append("��?���?��")
    else:
        user_data["��?������d?"].append("��?���ζ��")
    user_data["���ѩ"].append(name)
    user_data["??�\"].append(h)
    user_data["��?��"].append(w)
    user_data["BMI"].append(bmi)
    return bmi


def start():
    print("�a?�M��?�L��?�h?? �@�Z??�Z?��???���o�V?:")
    while True:
        print("��??����B:")
        print("1???�c�O?��?? 2?����??�j觯�?�h??")
        command_type = int(input("�X�֥���?�o�V�����s?:"))
        if command_type == 1:
            getData()
        elif command_type == 2:
            print("���?�@�Z?��η?\n---------------------------")

            break
        else:
            print("�[?������o�V��?! �X�־��c�դL��?")


def sort_search(user_df):
    while True:
        print("?դ�f???����B:")
        print("1?????�\ 2???��?�� 3???BMI 4???��??")
        sort_type = int(input("�X�֥�����?�S��???:"))
        if sort_type == 1:
            print(user_df.sort_values(by="??�\"))
        elif sort_type == 2:
            print(user_df.sort_values(by="��?��"))
        elif sort_type == 3:
            print(user_df.sort_values(by="BMI"))
        elif sort_type == 4:
            break
        else:
            print("�[?�����????! �X�־��c�դL��?")


def average_search(user_df):
    avg_h = round(user_df["??�\"].mean(), 1)
    avg_w = round(user_df["��?��"].mean(), 1)
    avg_bmi = round(user_df["BMI"].mean(), 1)
    print(f"??�\??�v��?avg_h} ��?��??�v��?avg_w} BMI??�v��?avg_bmi}")


def status_search(user_df):
    while True:
        print("��?������d��????��?:")
        print("1???��?���ζ�� 2???��?���?�� 3???��?����u�� 4???��??")
        status_type = int(input("�X�֥���?ɺ�S??�d��???:"))
        if status_type == 1:
            low_df = user_df[user_df.BMI<18.5 ]
            print("�W?�B��xһ?�?�@?��?�Q�X��?���[�����U?")
            print(low_df)
        elif status_type == 2:
            mid_df = user_df[18.5 <= user_df.BMI < 24]
            print("�W?�B��xһ?�?��?��?�Q�X�Ҷd?��·??")
            print(mid_df)
        elif status_type == 3:
            up_df = user_df[user_df.BMI >= 24]
            print("�W?�B��xһ?�?��?��?�Q�X��?�Gɡ?��?")
            print(up_df)
        elif status_type == 4:
            break
        else:
            print("�[?�����????! �X�־��c�դL��?")


def search():
    user_df = pd.DataFrame(user_data)
    while True:
        print("�a?�M��M�v��?�h?? �@�Z??�Z?��???���v��?�o�V?:")
        print("�h??��??����B:")
        print("1???�����s? 2????դ�f 3?????�v 4???��?������d? 5?????�U�h??")
        search_type = int(input("�X�֥������v��?�o�V�����s?:"))
        if search_type == 1:
            print(user_df)
        elif search_type == 2:
            sort_search(user_df)
        elif search_type == 3:
            average_search(user_df)
        elif search_type == 4:
            status_search(user_df)
        elif search_type == 5:
            print("??�U�h??��η?\n---------------------------")
            break
        else:
            print("�[?������o�V��?! �X�־��c�դL��?")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("??�g??�F���uBMI???")
    start()
    search()
    print("??��?�M��??")
