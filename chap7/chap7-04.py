number = [1,2,3,4,5]

while True:
    answer = input("正解の数字を入力するかｐで終了します。")
    if answer == q:
        break
    try:
        answer = int(answer)
    except ValueError:
        print ("数字を入力するか、ｑで終了します。")
    if answer in numbers:
        print ("正解")


    
