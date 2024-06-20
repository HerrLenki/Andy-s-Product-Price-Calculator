import math

product_prices = []
product_amounts = []

result = float("{:.4f}".format(float(input("Gewünschter Gesammtpreis: "))))
current_result = float("{:.4f}".format(float(input("Was ist der derzeitige Gesammtpreis?: "))))
result_difference = result - current_result
product_number = int(float(input("Wie viele Arten von Produkten gibt es?: ")))
if product_number == 3:
    product_amounts.append(int(input("Was ist die Produktmenge des ersten Produkts?: ")))
    product_prices.append(float("{:.4f}".format(float(input("Was ist der derzeitige Preis des Produktes?: ")))))

    product_amounts.append(int(float(input("Was ist die Produktmenge des zweiten Produkts?: "))))
    product_prices.append(float("{:.4f}".format(float(input("Was ist der derzeitige Preis des Produktes?: ")))))
    for i in range(1, 3):
        divided_product_amount = str(product_amounts[2] / math.pow(10, i)).split(".")
        if divided_product_amount[1] == "0":
            print("Hello world")
            product_amounts.append(divided_product_amount[0])

    product_amounts.append(int(float(input("Was ist die Produktmenge des dritten Produkts?: "))))
    product_prices.append(float("{:.4f}".format(float(input("Was ist der derzeitige Preis des Produktes?: ")))))
    for i in range(1, 3):
        divided_product_amount = str(product_amounts[4] / math.pow(10, i)).split(".")
        if divided_product_amount[1] == "0":
            print("Hello world")
            product_amounts.append(divided_product_amount[0])


else:
    product_amounts.append(int(input("Was ist die Produktmenge des ersten Produkts?: ")))
    product_prices.append(float("{:.4f}".format(float(input("Was ist der derzeitige Preis des Produktes?: ")))))

    product_amounts.append(int(input("Was ist die Produktmenge des zweiten Produkts?: ")))
    product_prices.append(float("{:.4f}".format(float(input("Was ist der derzeitige Preis des Produktes?: ")))))
    for i in range(1, 3):
        divided_product_amount = str(product_amounts[1] / math.pow(10, i)).split(".")
        if divided_product_amount[1] == "0":
            product_amounts.append(int(divided_product_amount[0]) * math.pow(10, -2))
            break

while True:
    product_prices[0] += 0.0001
    if product_number == 3:
        current_result = round(product_amounts[0] * product_prices[0] + product_amounts[1] * product_prices[1] + product_amounts[3] * product_prices[2], 2)
        result_difference = round(result, current_result, 2)
        if round(result_difference % product_amounts[2], 2)== 0:
            current_result = round(product_amounts[0] * product_prices[0] + product_amounts[1] * product_prices[1] + product_amounts[3] * product_prices[2], 2)
            result_difference = round(result, current_result, 2)
            while True:
                if current_result == result:
                    print("Preis des ersten Produktes:", float("{:.4f}".format(product_prices[0])))
                    print("Preis des zweiten Produktes:", float("{:.4f}".format(product_prices[1])))
                    print("Preis des dritten Produktes:", float("{:.4f}".format(product_prices[2])))
                    print("Ergebniss:", round(product_amounts[0] * product_prices[0] + product_amounts[1] * product_prices[1] + product_amounts[3] * product_prices[2], 2))
                    break
                if current_result > result:
                    product_prices[3] -= 0.0001
                elif current_result < result:
                    product_prices[3] += 0.0001
                
        break
    else:
        current_result = round(product_amounts[0] * product_prices[0] + product_amounts[1] * product_prices[1], 2)
        result_difference = round(result - current_result, 2)
        if round(result_difference % product_amounts[2], 2) == 0:
            while True:
                current_result = round(product_amounts[0] * float("{:.4f}".format(product_prices[0])) + product_amounts[1] * float("{:.4f}".format(product_prices[1])), 2)
                result_difference = round(result - current_result, 2)
                if current_result == result:
                    print("Preis des ersten Produktes:", float("{:.4f}".format(product_prices[0])))
                    print("Preis des zweiten Produktes:", float("{:.4f}".format(product_prices[1])))
                    print("Ergebniss:", round(product_amounts[0] * product_prices[0] + product_amounts[1] * product_prices[1], 2))
                    break
                if current_result > result:
                    product_prices[1] -= 0.0001
                elif current_result < result:
                    product_prices[1] += 0.0001  
        if current_result == result:
            break

