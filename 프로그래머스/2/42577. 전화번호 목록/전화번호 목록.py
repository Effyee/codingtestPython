def solution(phone_book):
    phone_book.sort()
    for i,k in zip(phone_book,phone_book[1:]):
        if k.startswith(i):
            return False
    return True