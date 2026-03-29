from models import Book
from models import Journal
from models import Media
from models import User
from models import Lbn

def init_data():
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
    
    return reader, collection, lbn_acct, lbn_pw