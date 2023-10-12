def solution(s):
    answer = ''
    number=''
    number_dict={'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    temp = ""
    
    for char in s:
        if char.isdigit():
            answer+=char
        else:
            temp+=char
            if temp in number_dict:
                answer+= number_dict[temp]
                temp=''
    return int(answer)
    
