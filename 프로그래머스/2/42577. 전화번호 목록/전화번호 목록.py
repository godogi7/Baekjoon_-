def solution(phone_book):
    phone_book.sort()
    for number in range(1, len(phone_book)):
        if phone_book[number][:len(phone_book[number-1])] == phone_book[number-1]:
            return False
    return True
        
