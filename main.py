from models import Book
from models import Journal
from models import Media
from models import User
from models import Lbn

from data import init_data

reader, collection, lbn_acct, lbn_pw = init_data()


def menu():
    print("歡迎使用圖書資訊系統")
    print("輸入1 查詢館藏資料")
    print("輸入2 進行館藏借閱")
    print("輸入3 進行館藏歸還")
    print("輸入4 進行借閱證註冊")
    print("輸入5 查詢讀者資料")
    print("輸入6 建立館藏資料")
    print("輸入7 新增館藏評價")
    if User.login or Lbn.login_stat:
        print("輸入8 以登出離開")
    return str(input())


def run():
    using = None
    try:
        while True:
            select = menu()

            # 功能1：查詢館藏資料
            if select == "1":
                con = True
                while con:
                    main_search(collection)
                    choice = input("是否繼續查詢館藏？ 請輸入Y/N\n")
                    if choice == "N" or choice == "n":
                        con = False
                        break
                    continue
                continue

            # 功能2：登記借書
            if select == "2":
                if User.login is False:
                    using = signin(reader)
                if using is False:
                    continue
                if User.login is True:
                    situation = True
                    print("開始登記借書")
                    while situation:
                        id_no = input('請輸入欲借閱館藏的識別號：')
                        count = 0
                        for resource in collection:
                            count += 1
                            if id_no == resource.id_no:
                                if len(using.borrowed) <= 5:
                                    if resource.available is True:
                                        using.borrowed.append(resource)
                                        resource.available = False
                                        print('借閱成功！' + using.name + '（' + using.id + '）' + '已借了' + str(
                                            len(using.borrowed)) + '本書籍')
                                        print('已借出的書籍：', end='')
                                        for i in range(len(using.borrowed)):
                                            if i != len(using.borrowed) - 1:
                                                print(using.borrowed[i].title + '，', end='')
                                            else:
                                                print(using.borrowed[i].title)
                                        break
                                    else:
                                        print('此館藏已借出')
                                        break
                                else:
                                    print('已超出借閱本數(5)限制！請歸還後再行借閱')
                                    situation = False
                                    break
                        if count == len(collection)-1:
                            print("查無此書")

                        choice = input("繼續借閱？Y/N\n")
                        while choice != 'Y' and choice != 'N' and choice != 'y' and choice != 'n':
                            choice = input("輸入錯誤！\n是否繼續借閱？Y/N\n")
                        if choice == 'N' or choice == 'n':
                            situation = False
                            break
                        if choice == 'Y' or choice == 'y':
                            continue
                    continue

            # 功能3：登記還書
            if select == "3":
                if User.login is False:
                    using = signin(reader)
                if using is False:
                    continue
                if User.login is True:
                    situation = True
                    print("開始登記還書")
                    while situation:
                        id_no = input('請輸入館藏識別號:')
                        found_resource = None
                        for resource in using.borrowed:
                            if id_no == resource.id_no:
                                found_resource = resource
                                break

                        if found_resource is not None:
                            if found_resource in using.borrowed:
                                using.return_resource(found_resource)
                                print(using.name + "，" + found_resource.title + " 歸還成功！")
                            else:
                                print("您並沒有借閱該書籍！")
                        elif found_resource is None:
                            print("識別號輸入錯誤！")

                        choice = input("是否繼續歸還？Y/N\n")
                        if choice == 'N' or choice == 'n':
                            situation = False
                        elif choice == "Y" or choice == "y":
                            continue
                    continue

            # 功能4：註冊借閱證
            if select == "4":
                con = True
                print("開始註冊借閱證")
                while con is True:
                    name = input("請輸入姓名：")
                    gender = input("請輸入性別（F/M）：")
                    while gender != "F" and gender != "M":
                        gender = input("輸入錯誤，請重新輸入性別（F/M）：")
                    birth = input("請輸入生日(YYYY/MM/DD)：")
                    tel = input("請輸入電話：")
                    while len(tel) != 10:
                        tel = input("輸入錯誤，請重新輸入輸入電話：")
                    email = input("請輸入電子信箱：")
                    password = input("請設定密碼：")
                    reader.append(User(name, gender, birth, tel, email, password))
                    reader[-1].generate_id(len(reader))
                    print("註冊借閱證成功，借閱證號碼為" + reader[-1].id)
                    choice = input("是否繼續註冊借閱證？Y/N\n")
                    if choice == "Y" or choice == "y":
                        continue
                    con = False
                continue

            # 功能5：查詢讀者資料
            if select == "5":
                if Lbn.login_stat is False:
                    lbn_login_status = lbn_login(lbn_acct, lbn_pw)
                else:
                    lbn_login_status = True
                if lbn_login_status is False:
                    continue

                con = True
                print("開始查詢讀者資料")
                while con and Lbn.login_stat:
                    found = False
                    search_id = input("請輸入借閱證號碼：")
                    for r in reader:
                        if r.id == search_id:
                            found = True
                            print(r)
                    if not found:
                        print("查無此讀者！")
                    choice = input("是否繼續查詢讀者？Y/N\n")
                    if choice == "N" or choice == "n":
                        con = False
                    else:
                        continue
                continue

            # 功能6：建立館藏
            if select == "6":
                if Lbn.login_stat is False:
                    lbn_login_status = lbn_login(lbn_acct, lbn_pw)
                else:
                    lbn_login_status = True
                if lbn_login_status is False:
                    continue

                con = True
                while con and Lbn.login_stat:
                    choice = input("---請選擇館藏種類---\n1-書籍 2-期刊 3-多媒體（請輸入數字）：")
                    while choice != '1' and choice != '2' and choice != '3':
                        choice = input("輸入錯誤！\n---請選擇館藏種類---\n1-書籍 2-期刊 3-多媒體（請輸入數字）：")

                    if choice == '1':
                        title = input("請輸入題名：")
                        author = input("請輸入作者：")
                        publisher = input("請輸入出版社：")
                        id_no = input("請輸入識別號：")
                        classify_no = input("請輸入索書號：")
                        book = Book(title, author, publisher, id_no, classify_no)
                        exist = False
                        for item in collection:
                            if item.id_no == book.id_no:
                                exist = True
                        if not exist:
                            print("成功新增館藏！")
                        else:
                            print("館藏已存在！")
                    elif choice == '2':
                        title = input("請輸入題名：")
                        subject = input("請輸入主題：")
                        publisher = input("請輸入出版社：")
                        format = input("請輸入格式：")
                        frequency = input("請輸入刊期：")
                        id_no = input("請輸入識別號：")
                        journal = Journal(title, subject, publisher, format, frequency, id_no)
                        exist = False
                        for item in collection:
                            if item.id_no == journal.id_no:
                                exist = True
                        if not exist:
                            print("成功新增館藏！")
                        else:
                            print("館藏已存在！")
                    elif choice == '3':
                        title = input("請輸入題名：")
                        author = input("請輸入作者：")
                        genre = input("請輸入類型：")
                        format = input("請輸入格式：")
                        time = input("請輸入媒體內容時長：")
                        id_no = input("請輸入識別號：")
                        description = input("請輸入摘要：")
                        media = Media(title, author, genre, format, time, id_no, description)
                        exist = False
                        for item in collection:
                            if item.id_no == media.id_no:
                                exist = True
                        if not exist:
                            print("成功新增館藏！")
                        else:
                            print("館藏已存在！")

                    choice = input('是否繼續輸入？Y/N\n')
                    while choice != 'Y' and choice != 'N' and choice != 'y' and choice != 'n':
                        choice = input("輸入錯誤！\n是否繼續輸入？（Y/N）\n")
                    if choice == 'N' or choice == 'n':
                        con = False
                    elif choice == 'Y' or choice == 'y':
                        continue

            # 功能7：為館藏新增評論
            if select == "7":
                if User.login is False:
                    using = signin(reader)
                if using is False:
                    continue
                if User.login is True:
                    con = True
                    while con:
                        results = main_search(collection)
                        if len(results) != 0:
                            choice = int(input("請選擇編號："))
                            selected_col = results[choice - 1]
                            if isinstance(selected_col, Book) or isinstance(selected_col, Media):
                                valid = False
                                rate = 0
                                while valid is False:
                                    rate = int(input("請輸入評分（1-非常不滿意，5-非常滿意）："))
                                    if 1 <= rate <= 5:
                                        valid = True
                                        break
                                    print("評分不能小於 1 或大於 5 ！請重新輸入。")
                                    continue
                                comment = input("請輸入評語：")
                                selected_col.add_comment(using.id, rate, comment)
                                print("評論新增成功！")
                        choice = input("是否繼續新增？請輸入Y/N： ")
                        if choice == "N" or choice == "n":
                            con = False
                            break
                        continue
                    continue

            # 功能8：登出
            if select == "8":
                User.login = False
                Lbn.login_stat = False
                using = None
                print("---已登出！---")
                continue
    except KeyboardInterrupt:
        print("\n程式已結束。")


if __name__ == "__main__":
    run()
