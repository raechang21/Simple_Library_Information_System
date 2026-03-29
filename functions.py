import numpy as np


class User:
    def __init__(self, name, gender, birth, tel, email, password):
        self.name = name
        self.gender = gender
        self.birth = birth  # YYYY/MM/DD
        self.tel = tel
        self.email = email
        self.password = password
        self.borrowed = []  # 已借閱
        self.id = ""

    login = False

    # 產生借閱證號
    def generate_id(self, n):  # n 是目前累積的使用者數
        # 生日 6 碼+第n個使用者 4 碼
        self.id = self.birth[2:4] + self.birth[5:7] + self.birth[8:10] + str(n).zfill(4)

    # 還書（移出borrowed list）
    def return_resource(self, resource):
        self.borrowed.remove(resource)
        resource.available = True

    def list_info(self):
        info = ""
        info += '姓名：' + self.name + "\n"
        info += '性別：' + self.gender + "\n"
        info += '生日：' + self.birth + "\n"
        info += '電話：' + self.tel + "\n"
        info += '電子郵件：' + self.email + "\n"
        info += '已借閱館藏：\n'
        if len(self.borrowed) > 0:
            for i in range(len(self.borrowed)):
                info += self.borrowed[i].title + '\n'
        else:
            info += "尚未借出館藏！"
        return info

    def __str__(self):
        return self.list_info()


class Book:
    def __init__(self, title, author, publisher, id_no, classify_no):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.id_no = id_no
        self.classify_no = classify_no
        self.available = True  # 在館中與否，False表示尚未出借，True代表已出借
        self.rate = dict()
        self.comment = dict()
        self.cmt_lst = list()  # 沒有紀錄讀者、單純comment
        self.avg_rate = None

    def add_comment(self, id, rate, comment):  # 新增評論
        self.rate[id] = rate  # 1-5 星等
        self.comment[id] = comment  # 評語
        self.cmt_lst = list(self.comment.values())
        self.avg_rate = np.mean(list(self.rate.values()))  # 平均星等

    def list_info(self):
        info = "題名：" + self.title + "\n"
        info += "作者：" + self.author + "\n"
        info += "出版社：" + self.publisher + "\n"
        info += "識別號：" + self.id_no + "\n"
        info += "分類號：" + self.classify_no + "\n"
        if self.available:
            info += "館藏狀態：可借閱\n"
        else:
            info += "館藏狀態：已借出\n"
        if len(self.rate) == 0:
            info += "尚未有評分！"
            return info
        else:
            info += "評分：" + str(round(self.avg_rate, 1)) + "\n"  # 平均星等，去到小數點後第一位
            info += "評語：\n"
            for i in range(len(self.cmt_lst)):
                info += "「 " + self.cmt_lst[i] + " 」\n"
            return info

    def __str__(self):
        return self.list_info()


class Journal:
    def __init__(self, title, subject, publisher, format, frequency, id_no):
        self.title = title
        self.subject = subject
        self.publisher = publisher
        self.format = format
        self.frequency = frequency
        self.id_no = id_no

    def list_info(self):
        info = "題名：" + self.title + "\n"
        info += "主題：" + self.subject + "\n"
        info += "出版社：" + self.publisher + "\n"
        info += "格式：" + self.format + "\n"
        info += "刊期：" + self.subject + "\n"
        info += "識別號：" + self.id_no + "\n"

    def __str__(self):
        return self.list_info()


class Media:
    def __init__(self, title, author, genre, format, time, id_no, description):
        self.title = title
        self.author = author
        self.genre = genre
        self.format = format
        self.time = time
        self.id_no = id_no
        self.description = description
        self.available = True
        self.rate = dict()
        self.comment = dict()
        self.cmt_lst = list()  # 沒有紀錄讀者、單純comment
        self.avg_rate = None

    def add_comment(self, id, rate, comment):
        self.rate[id] = rate  # 1-5 星等
        self.comment[id] = comment  # 評語
        self.cmt_lst = list(self.comment.values())
        self.avg_rate = np.mean(list(self.rate.values()))  # 平均星等

    def list_info(self):
        info = "題名：" + self.title + "\n"
        info += "作者：" + self.author + "\n"
        info += "類型：" + self.genre + "\n"
        info += "格式：" + self.format + "\n"
        info += "媒體內容時長：" + self.time + "\n"
        info += "識別號：" + self.id_no + "\n"
        info += "摘要：" + self.description + "\n"
        if self.available:
            info += "館藏狀態：可借閱\n"
        else:
            info += "館藏狀態：已借出\n"
        if len(self.rate) == 0:
            info += "尚未有評分！"
            return info
        else:
            info += "評分：" + str(round(self.avg_rate, 1)) + "\n"  # 平均星等，去到小數點後第一位
            info += "評語：\n"
            for i in range(len(self.cmt_lst)):
                info += "「 " + self.cmt_lst[i] + " 」\n"
            return info

    def __str__(self):
        return self.list_info()


class Lbn:
    login_stat = False


from classes import Book
from classes import Journal
from classes import Media
from classes import User
from classes import Lbn


reader = []  # 存放所有讀者的list
collection = []  # 存放所有館藏的list
lbn_acct = "admin2023"  # 設定館員帳號
lbn_pw = "admin2023!pw"  # 設定館員密碼

# 預先存入兩位讀者
reader.append(User("Kelly", "F", "2003/08/18", "0907957388", "yuhan920818@gmail.com", "yuhan0818"))
reader[0].generate_id(1)
reader.append(User("Austine", "F", "2003/08/21", "0912254394", "austine.huang@gmail.com", "austine0821"))
reader[1].generate_id(2)

# 預先存入部分館藏
collection.append(Book("暮光之城", "史蒂芬妮.梅爾(Stephenie Meyer)",
                       "尖端出版社", "991025961389704786", "874.57 4810T 6624"))
collection.append(Book("Harry Potter and the prisoner of Azkaban", "Rowling, J.K.",
                       "New York : Scholastic Inc.", "991029666179704786", "PR6068.O94 H27 2001"))
collection.append(Book("The Hunger Games", "Collins, Suzanne.", "Singapore : Scholastic Singapore",
                       "991026563159704786", "PS3603.O4558 H86z 2009"))
collection.append(Journal("library and information science", "library science", "三田圖書館情報學會",
                          "online resource", "Semiannual, 1995-", "991038647425304786"))
collection.append(Journal("Cell.", "Cytology", "Netherlands : Elsevier", "online resource", "Biweekly, <1986->",
                          "991038440577904786"))
collection.append(Media("Harry Potter and the prisoner of Azkaban", "Rowling, J.K.", "Fiction films",
                        "2 videodiscs", "142 min", "991038499480204786",
                        "During his third year at Hogwarts School for Witchcraft and Wizardry, "
                        "Harry Potter must confront the devious and dangerous wizard "
                        "thought responsible for his parents' deaths."))
collection.append(Media("The Hunger Games", "Collins, Suzanne.", "電影片", "1張DVD", "141分", "991016842129704786",
                        "第七十四屆飢餓遊戲即將開始,這是場至死方休的無情決鬥.在這塊過去曾被稱為北美洲的廢墟大陸上,"
                        "有個新建立的國家\"施惠國\",該國內有一座富饒都城,都城四周被十二個行政區所圍繞.這座至高無上且專制殘酷的都城,"
                        "每年逼迫十二行政區交出十二歲至十八歲的少男少女各一名,將他們放在一年一度的\"飢餓遊戲\"當中讓他們自相殘殺,"
                        "直到出現最終勝利者,並以電視進行實況轉播,藉由此恐怖的手段來維持其威權統治以及國家秩序.十六歲的凱妮絲,"
                        "與寡母以及妹妹小櫻同住,當她自願代替在\"抽籤日\"被抽中的妹妹參加饑餓遊戲時,早已認命赴死."
                        "但是曾在垂死邊緣掙扎過的她,早已養成了強悍的求生野性,並在無意間成為了遊戲的有力競爭者.在通往生存的苦戰之路上,"
                        "她勢必將面臨重重艱難的抉擇,權衡生命,人性以及愛之間,何者才是真正寶貴的"))
collection.append(Book("鏡之孤城", "辻村, 深月.", "皇冠文化出版有限公司", "991038567920004786",
                       "861.57 3443-3 2019"))
collection.append(Media("Days of heaven Paramount", "Bert and Harold Schneider", "電影片", "1張DVD", "94分",
                        "991012151959704786", "在1910年，芝加哥的鋼鐵工人比爾意外殺死了他的監督。"
                                              "他帶著女友艾比和妹妹琳達逃到德克薩斯州的平原地區，"
                                              "在那裡他們在一個沉默寡言的農夫的麥田裡務工。"
                                              "當比爾得知農夫生病並且只有不到一年的壽命時，他鼓勵艾比接受農夫的關注。"
                                              "農夫和艾比結婚，她和她的「兄妹」們住在大房子裡，等待農夫去世，這樣艾比就能繼承財產。"
                                              "然而，愛似乎是萬能的良藥：農夫的健康似乎有所改善。"
                                              "而艾比也不再將這視為一場經濟交易的婚姻。"))


def menu():  # 主選單
    if User.login or Lbn.login_stat:  # 如果在登入狀態下，要顯示功能8（登出）
        print("歡迎使用圖書資訊系統")
        print("輸入1 查詢館藏資料")
        print("輸入2 進行館藏借閱")
        print("輸入3 進行館藏歸還")
        print("輸入4 進行借閱證註冊")
        print("輸入5 查詢讀者資料")
        print("輸入6 建立館藏資料")
        print("輸入7 新增館藏評價")
        print("輸入8 以登出離開")
        select = str(input())
    else:  # 否則顯示7個功能
        print("歡迎使用圖書資訊系統")
        print("輸入1 查詢館藏資料")
        print("輸入2 進行館藏借閱")
        print("輸入3 進行館藏歸還")
        print("輸入4 進行借閱證註冊")
        print("輸入5 查詢讀者資料")
        print("輸入6 建立館藏資料")
        print("輸入7 新增館藏評價")
        select = str(input())
    return select


def lbn_login():  # 館員登入
    while Lbn.login_stat is False:
        acct = input("請輸入館員帳號：")
        pw = input("請輸入館員密碼：")
        if acct == lbn_acct and pw == lbn_pw:
            Lbn.login_stat = True
            return True
        else:
            print("帳號或密碼錯誤！")
            choice_lbnlogin = input("是否繼續輸入？Y/N\n")
            if choice_lbnlogin == "Y":
                continue
            elif choice_lbnlogin == "N":
                return False


def signin(reader):  # 讀者登入
    login = False
    match = False
    while not login:
        id = str(input("請輸入借閱證號碼："))
        password = input("請輸入密碼：")
        for i in range(len(reader)):
            if id == reader[i].id:
                target_reader = i
                match = True
                target_password = reader[i].password
        if not match:  # not match = 沒有符合的借閱證號
            choice = input("借閱證號碼或密碼輸入錯誤！是否重新輸入？（Y/N）")
            if choice == "Y" or choice == "y":
                continue
            elif choice == "N" or choice == "n":
                return False
        if match:
            if password == target_password:
                print("嗨" + reader[target_reader].name + "，歡迎登入！")
                User.login = True
                using = reader[target_reader]
                return using
            else:
                choice = input("借閱證號碼或密碼輸入錯誤！是否重新輸入？（Y/N）")
                if choice == "Y" or choice == "y":
                    continue
                elif choice == "N" or choice == "n":
                    return False
                    break


def search_by_title(query, collection):  # 用題名查詢，引數：查詢關鍵字、館藏list
    results = []
    for item in collection:
        if item.title == query:
            results.append(item)
    return results


def search_by_author(query, collection):  # 用作者查詢
    results = []
    for item in collection:
        if isinstance(item, Book):
            if (
                    item.author == query
            ):
                results.append(item)
        elif isinstance(item, Media):
            if (
                    item.author == query
            ):
                results.append(item)
    return results


def search_by_id_no(query, collection):  # 用識別號查詢
    results = []
    for item in collection:
        if item.id_no == query:
            results.append(item)
    return results


def search_by_publisher(query, collection):  # 用出版社查詢
    results = []
    for item in collection:
        if isinstance(item, Book):
            if item.publisher == query:
                results.append(item)
    return results


def search_all_field(query, collection):  # 不限欄位查詢
    results = []
    for item in collection:
        if isinstance(item, Book):
            if (
                    item.title == query
                    or item.author == query
                    or item.publisher == query
                    or item.id_no == query
                    or item.classify_no == query
            ):
                results.append(item)
        elif isinstance(item, Journal):
            if (
                    item.title == query
                    or item.subject == query
                    or item.publisher == query
                    or item.format == query
                    or item.frequency == query
                    or item.id_no == query
            ):
                results.append(item)
        elif isinstance(item, Media):
            if (
                    item.title == query
                    or item.author == query
                    or item.genre == query
                    or item.format == query
                    or item.time == query
                    or item.id_no == query
                    or item.description == query
            ):
                results.append(item)
    return results


def main_search():  # 所有館藏查詢法之選單
    print("請選擇查詢方式：")
    print("輸入1 不限欄位查詢")
    print("輸入2 以題名查詢")
    print("輸入3 以作者查詢")
    print("輸入4 以出版社查詢")
    print("輸入5 以識別號查詢")
    way = str(input())

    results = []  # 將所有符合之館藏存入result
    if way == "1":
        query = input("將不限欄位進行查詢，請輸入查詢關鍵字：")
        results = search_all_field(query, collection)
    elif way == "2":
        query = input("將以題名進行查詢，請輸入查詢關鍵字：")
        results = search_by_title(query, collection)
    elif way == "3":
        query = input("將以作者進行查詢，請輸入查詢關鍵字：")
        results = search_by_author(query, collection)
    elif way == "4":
        query = input("將以出版社進行查詢，請輸入查詢關鍵字：")
        results = search_by_publisher(query, collection)
    elif way == "5":
        query = input("將以識別號進行查詢，請輸入查詢關鍵字：")
        results = search_by_id_no(query, collection)

    if len(results) != 0:
        print("查詢結果：")
        for item in results:
            print(str(results.index(item) + 1) + ":")
            print(item)
            print("------------------------")
    else:
        print("查無符合條件的館藏資料。")

    return results  # 回傳包含所有館藏的list


# ----------主程式碼開始----------
while True:
    select = menu()  # 選擇欲使用的功能

    # 功能1：查詢館藏資料
    if select == "1":
        con = True
        while con:
            main_search()  # 呼叫館藏查詢選單
            choice = input("是否繼續查詢館藏？ 請輸入Y/N\n")
            if choice == "N" or choice == "n":
                con = False
                break
            else:
                continue
        continue

    # 功能2：登記借書
    if select == "2":
        if User.login is False:  # 若尚未登入，呼叫登入函數
            using = signin(reader)
        if using is False:  # 若登入失敗並不重新登入，回到主選單
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
                elif choice == 'Y' or choice == 'y':
                    continue
            continue

    # 功能3：登記還書
    if select == "3":
        if User.login is False:  # 若尚未登入，呼叫登入函數
            using = signin(reader)
        if using is False:  # 若登入失敗並不重新登入，回到主選單
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

                # 確定id_no是否正確
                if found_resource is not None:
                    # 確定書籍是否被該位使用者借閱
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
            else:
                con = False
        continue

    # 功能5：查詢讀者資料
    if select == "5":
        if Lbn.login_stat is False:  # 若館員尚未登入，呼叫館員登入函數
            lbn_login_status = lbn_login()
        else:
            lbn_login_status = True
        if lbn_login_status is False:  # 若登入失敗並不重新登入，回到主選單
            continue

        con = True  # 是否繼續
        print("開始查詢讀者資料")
        while con and Lbn.login_stat:
            found = False  # 是否有這個讀者
            search_id = input("請輸入借閱證號碼：")
            for r in reader:
                if r.id == search_id:  # 找到讀者
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
        if Lbn.login_stat is False:  # 若館員尚未登入，呼叫館員登入函數
            lbn_login_status = lbn_login()
        else:
            lbn_login_status = True
        if lbn_login_status is False:  # 若登入失敗並不重新登入，回到主選單
            continue

        con = True  # 是否繼續
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
                results = main_search()
                if len(results) != 0:
                    choice = int(input("請選擇編號："))  # 搜尋結果中的編號
                    selected_col = results[choice - 1]  # 選擇的館藏
                    if isinstance(selected_col, Book) or isinstance(selected_col, Media):
                        valid = False
                        rate = 0
                        while valid is False:
                            rate = int(input("請輸入評分（1-非常不滿意，5-非常滿意）："))
                            if 1 <= rate <= 5:
                                valid = True
                                break
                            else:
                                print("評分不能小於 1 或大於 5 ！請重新輸入。")
                                continue
                        comment = input("請輸入評語：")
                        selected_col.add_comment(using.id, rate, comment)
                        print("評論新增成功！")
                choice = input("是否繼續新增？請輸入Y/N： ")
                if choice == "N" or choice == "n":
                    con = False
                    break
                else:
                    continue
            continue

    # 功能8：登出
    if select == "8":
        User.login = False
        Lbn.login_stat = False
        using = None
        print("---已登出！---")
        continue
