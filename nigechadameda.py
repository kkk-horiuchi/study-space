name = input("お名前を教えてね：")

def answer():
    question1 = input(f"{name}、ヱヴァに乗れ:yes or no:")
    if question1 == "yes":
        print(f"「「「僕はヱヴァンゲリヲン初号機のパイロット、{name}です！！！」」」")
    elif question1 == "no":
        times = input("[⚠ ⚠ ⚠ WARNING!⚠ ⚠ ⚠ ] PLEASE INPUT NUMBER OF TIMES:")
        int_times = int(times)
        while int_times > 0:
            print("逃げちゃだめだ")
            int_times -= 1
            if int_times < 0:
                break
        answer()
    else:
        print("乗るのなら早くしろ。でなければ帰れ")
        answer()

answer()