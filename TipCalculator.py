import decimal


def notPositive(data):
    if data <=0:
        raise NotPositiveError
    else:
        return data

def totalBill(billAmount, tipRate):
    tipAmount = billAmount * (tipRate / 100)
    totalAmount = billAmount + tipAmount
    return totalAmount

while True:
    try:
        billAmount = notPositive(decimal.Decimal(input("Please Enter the Bill amount: ")))
        tipRate = notPositive(decimal.Decimal(input("Please Enter the tip rate: ")))
        print("Total: {}".format(round(totalBill(billAmount, tipRate), 2)))
        break
    except:
        print("Please Enter a valid number")
