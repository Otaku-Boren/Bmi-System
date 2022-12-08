import pandas as pd

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

user_data = dict(Àä¼ÃÑ©=list(), ??¯\=list(), İÓ?¾·=list(), BMI=list(), Áç?®«ôñ£áñd?=list())


def getData():
    name = input("¿XìÎ¤Lîã??Áí?:")
    while True:
        try:
            h = float(input("¿XìÎ¤Lîã??İÓ?(cm):"))
        except ValueError:
            print("¨@½Z?ÂìÌBÔa?½Z???Òµ?á¦Ï`¨@½Z?")
            continue
        break
    while True:
        try:
            w = float(input("¿XìÎ¤Lîã?Ò»??(kg):"))
        except ValueError:
            print("¨@½Z?ÂìÌBÔa?½Z???Òµ?á¦Ï`¨@½Z?")
            continue
        break
    bmi = round(w / ((h * 0.01) ** 2), 1)
    if bmi >= 24:
        if bmi < 27:
            user_data["Áç?®«ôñ£áñd?"].append("İÓ?¾·è¦Ñu¾·")
        elif bmi < 30:
            user_data["Áç?®«ôñ£áñd?"].append("¨@òK®`Æ^?ì»")
        elif bmi < 35:
            user_data["Áç?®«ôñ£áñd?"].append("®ş?®`Æ^?ì»")
        else:
            user_data["Áç?®«ôñ£áñd?"].append("??®`Æ^?ì»")
    elif bmi >= 18.5:
        user_data["Áç?®«ôñ£áñd?"].append("İÓ?¾·è¦?µÆ")
    else:
        user_data["Áç?®«ôñ£áñd?"].append("İÓ?¾·è¦Î¶Öé")
    user_data["Àä¼ÃÑ©"].append(name)
    user_data["??¯\"].append(h)
    user_data["İÓ?¾·"].append(w)
    user_data["BMI"].append(bmi)
    return bmi


def start():
    print("öa?åMôï?¤Lîã?âh?? ¨@½Z??½Z?îí???£¶ÎoùV?:")
    while True:
        print("Áî??Àá³ÆÓB:")
        print("1???ócªO?Àó?? 2?ÉàŞó??¨jè§¯ù?óh??")
        command_type = int(input("¿XìÖ¥íîí?ÎoùVªãåÅÃs?:"))
        if command_type == 1:
            getData()
        elif command_type == 2:
            print("Áç·É?¨@½Z?îòÎ·?\n---------------------------")

            break
        else:
            print("®[?Ùóè§÷âÎoùVÂÇ?! ¿XìÖ¾·óc©Õ¤Lîã?")


def sort_search(user_df):
    while True:
        print("?Õ¤ğf???Àá³ÆÓB:")
        print("1?????¯\ 2???İÓ?¾· 3???BMI 4???Áó??")
        sort_type = int(input("¿XìÖ¥íîíÑï?ºSÉà???:"))
        if sort_type == 1:
            print(user_df.sort_values(by="??¯\"))
        elif sort_type == 2:
            print(user_df.sort_values(by="İÓ?¾·"))
        elif sort_type == 3:
            print(user_df.sort_values(by="BMI"))
        elif sort_type == 4:
            break
        else:
            print("®[?Ùóè§÷à????! ¿XìÖ¾·óc©Õ¤Lîã?")


def average_search(user_df):
    avg_h = round(user_df["??¯\"].mean(), 1)
    avg_w = round(user_df["İÓ?¾·"].mean(), 1)
    avg_bmi = round(user_df["BMI"].mean(), 1)
    print(f"??¯\??âvôï?avg_h} İÓ?¾·??âvôï?avg_w} BMI??âvôï?avg_bmi}")


def status_search(user_df):
    while True:
        print("Áç?®«ôñ£áñdìÒ????®ş?:")
        print("1???İÓ?¾·è¦Î¶Öé 2???İÓ?¾·è¦?µÆ 3???İÓ?¾·è¦Ñu¾· 4???Áó??")
        status_type = int(input("¿XìÖ¥íîí?ÉººS??ñdìÒ???:"))
        if status_type == 1:
            low_df = user_df[user_df.BMI<18.5 ]
            print("ÒW?ÓBôï¬xÒ»?á«?¨@?£á?ÓQ¿XÀ§?·èŞ[Í÷ôîêU?")
            print(low_df)
        elif status_type == 2:
            mid_df = user_df[18.5 <= user_df.BMI < 24]
            print("ÒW?ÓBôï¬xÒ»?á«?®ş?£á?ÓQ¿XìÒ¶d?ÉÖÂ·??")
            print(mid_df)
        elif status_type == 3:
            up_df = user_df[user_df.BMI >= 24]
            print("ÒW?ÓBôï¬xÒ»?á«?®ş?£á?ÓQ¿XÀ§?¿GÉ¡?îá?")
            print(up_df)
        elif status_type == 4:
            break
        else:
            print("®[?Ùóè§÷à????! ¿XìÖ¾·óc©Õ¤Lîã?")


def search():
    user_df = pd.DataFrame(user_data)
    while True:
        print("öa?åMôï¯MŞvºÁ?âh?? ¨@½Z??½Z?îí???£·ŞvºÁ?ÎoùV?:")
        print("óh??Áî??Àá³ÆÓB:")
        print("1???®ş£áùs? 2????Õ¤ğf 3?????âv 4???Áç?®«ôñ£áñd? 5?????æUóh??")
        search_type = int(input("¿XìÖ¥íîíÑïŞvºÁ?ÎoùVªãåÅÃs?:"))
        if search_type == 1:
            print(user_df)
        elif search_type == 2:
            sort_search(user_df)
        elif search_type == 3:
            average_search(user_df)
        elif search_type == 4:
            status_search(user_df)
        elif search_type == 5:
            print("??æUóh??îòÎ·?\n---------------------------")
            break
        else:
            print("®[?Ùóè§÷âÎoùVÂÇ?! ¿XìÖ¾·óc©Õ¤Lîã?")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("??Îg??ÒF¸óÙuBMI???")
    start()
    search()
    print("??×ë?¹MÙĞ??")
