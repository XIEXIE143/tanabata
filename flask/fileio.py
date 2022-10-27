# # w => write （書く）
# file = open('aloha.txt', 'w')
# file.write('tanaka,masahiko')  
# file.close()

# # データを`追加(append)`するプログラム
# file = open('aloha.txt', 'a')
# file.write('tanaka,masahiko\n')  # \n: 次の行にいく; 改行(new_line)
# file.close()

#データを読み(`read`)、表示するプログラム
# data = file.read()
# print(data)
# file.close()

# ファイルを開く　（読むため; r）
file = open('aloha.txt', 'r')
  
# データを読む（もらう）
data = file.read()
  
#　読んだデータを表示する
print(data)
  
# ファイルを閉じる(close)
file.close()