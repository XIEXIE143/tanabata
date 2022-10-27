# IDを入力してもらう
id = input('IDを入力してください: ')
print(id)
  
# パスワードを入力してもらう
pwd = input('パスワードを入力してください: ')
print(pwd)
  
# データファイル( aloha.txt )を開いて、データをもらう
file = open('aloha.txt', 'r')
  
# 1行ずつ、データをもらう & IDとパスワード確認する
for line in file:
    if id in line and pwd in line:
        flag = 1
        break
    else:
        flag = 0

if flag == 1:
   print('IDとパスワード、OKです。')
else:
    print('IDとパスワード、違います!')

# ファイルを閉じる
file.close()