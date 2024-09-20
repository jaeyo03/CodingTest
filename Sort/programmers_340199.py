def solution(wallet, bill):
    answer = 0
    wallet.sort(reverse=True)
    bill.sort(reverse=True)

    while bill[1] > wallet[1] or bill[0] > wallet[0]:
        if bill[0] > bill[1]:
            bill[0] = int(bill[0] / 2)
        else:
            bill[1] = int(bill[1] / 2)
        answer += 1
        bill.sort(reverse=True)

    return answer