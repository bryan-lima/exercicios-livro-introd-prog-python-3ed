# Escreva um programa que pergunte o valor inicial de uma dívida e juro mensal
# Pergunte também o valor mensal que será pago
# Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago

debtValue = float(input("Valor da dívida: R$ "))
rate = float(input('Juros mensal (%): '))
monthlyPayment = float(input('Valor mensal que será pago: R$ '))
month = 1

if debtValue * (rate/100) > monthlyPayment:
    print("Sua dívida não será paga nunca, pois os juros são superiores ao pagamento mensal.")
else:
    balance = debtValue
    interestPaid = 0
    while balance > monthlyPayment:
        interest = balance * rate / 100
        balance = balance + interest - monthlyPayment
        interestPaid = interestPaid + interest
        print(f"Saldo da dívida no mês {month} é de R${balance:6.2f}.")
        month += 1
    print(f"Para pagar uma dívida de R${debtValue:.2f}, a {rate:.2f} % de juros,")
    print(f"você precisará de {month - 1} meses, pagando um total de R${interestPaid:.2f} de juros.")
    print(f"No último mês, você teria um saldo residual de R${balance:.2f} a pagar.")
