def solution(phone_book):
    phone_book.sort()
    for num1, num2 in zip(phone_book, phone_book[1:]):
        if num2.startswith(num1):
            return False
    return True

# def solution(phone_book):
#     phone_book.sort()
#     ans = dict(zip(phone_book, [None]*len(phone_book)))
#     for num in reversed(phone_book):
#         for sli in list(map(len,phone_book)):
#             tmp = num[:sli]
#             if tmp in ans and tmp != num:
#                 return False
#     return True


if __name__=="__main__":
    print(solution(["119", "97674223", "1195524421"]))
    print(solution(["123", "456", "789"]))
    print(solution(["12", "123", "1235", "567", "88"]))