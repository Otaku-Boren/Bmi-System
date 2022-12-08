import pandas as pd

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

user_data = dict(姓名=list(), 身高=list(), 體重=list(), BMI=list(), 健康狀態=list())


def getData():
    name = input("請輸入姓名:")
    while True:
        try:
            h = float(input("請輸入身高(cm):"))
        except ValueError:
            print("輸入應為數字，請重新輸入")
            continue
        break
    while True:
        try:
            w = float(input("請輸入體重(kg):"))
        except ValueError:
            print("輸入應為數字，請重新輸入")
            continue
        break
    bmi = round(w / ((h * 0.01) ** 2), 1)
    if bmi >= 24:
        if bmi < 27:
            user_data["健康狀態"].append("體重過重")
        elif bmi < 30:
            user_data["健康狀態"].append("輕度肥胖")
        elif bmi < 35:
            user_data["健康狀態"].append("中度肥胖")
        else:
            user_data["健康狀態"].append("重度肥胖")
    elif bmi >= 18.5:
        user_data["健康狀態"].append("體重適中")
    else:
        user_data["健康狀態"].append("體重過輕")
    user_data["姓名"].append(name)
    user_data["身高"].append(h)
    user_data["體重"].append(w)
    user_data["BMI"].append(bmi)
    return bmi


def start():
    print("目前為輸入階段 輸入數字可使用功能:")
    while True:
        print("功能如下:")
        print("1️⃣新增資料 2️結束並進行查詢")
        command_type = int(input("請選取功能數字:"))
        if command_type == 1:
            getData()
        elif command_type == 2:
            print("停止輸入階段\n---------------------------")

            break
        else:
            print("沒有這功能喔! 請重新輸入")


def sort_search(user_df):
    while True:
        print("排序種類如下:")
        print("1️⃣身高 2️⃣體重 3️⃣BMI 4️⃣離開")
        sort_type = int(input("請選取排序種類:"))
        if sort_type == 1:
            print(user_df.sort_values(by="身高"))
        elif sort_type == 2:
            print(user_df.sort_values(by="體重"))
        elif sort_type == 3:
            print(user_df.sort_values(by="BMI"))
        elif sort_type == 4:
            break
        else:
            print("沒有這種類喔! 請重新輸入")


def average_search(user_df):
    avg_h = round(user_df["身高"].mean(), 1)
    avg_w = round(user_df["體重"].mean(), 1)
    avg_bmi = round(user_df["BMI"].mean(), 1)
    print(f"身高平均為{avg_h} 體重平均為{avg_w} BMI平均為{avg_bmi}")


def status_search(user_df):
    while True:
        print("健康狀態種類如下:")
        print("1️⃣體重過輕 2️⃣體重適中 3️⃣體重過重 4️⃣離開")
        status_type = int(input("請選取健康狀態種類:"))
        if status_type == 1:
            low_df = user_df[user_df.BMI<18.5 ]
            print("以下為體重過輕者，請多補充營養")
            print(low_df)
        elif status_type == 2:
            mid_df = user_df[18.5 <= user_df.BMI < 24]
            print("以下為體重適中者，請繼續保持")
            print(mid_df)
        elif status_type == 3:
            up_df = user_df[user_df.BMI >= 24]
            print("以下為體重適中者，請多多運動")
            print(up_df)
        elif status_type == 4:
            break
        else:
            print("沒有這種類喔! 請重新輸入")


def search():
    user_df = pd.DataFrame(user_data)
    while True:
        print("目前為查詢階段 輸入數字可使用查詢功能:")
        print("查詢功能如下:")
        print("1️⃣一般 2️⃣排序 3️⃣平均 4️⃣健康狀態 5️⃣結束查詢")
        search_type = int(input("請選取查詢功能數字:"))
        if search_type == 1:
            print(user_df)
        elif search_type == 2:
            sort_search(user_df)
        elif search_type == 3:
            average_search(user_df)
        elif search_type == 4:
            status_search(user_df)
        elif search_type == 5:
            print("結束查詢階段\n---------------------------")
            break
        else:
            print("沒有這功能喔! 請重新輸入")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("🤖歡迎使用BMI系統")
    start()
    search()
    print("❌系統關閉")
