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
