def trade_action(current_shares, purchase_price, market_price, available_funds):
    transaction_cost = 10
    if (market_price < purchase_price) and (market_price + transaction_cost <= available_funds):
        number_shares_to_buy = (available_funds - transaction_cost) // market_price
        profit = number_shares_to_buy * (purchase_price - market_price)
        if profit > transaction_cost:
            return "Buy " + str(number_shares_to_buy) + " shares"
    return "Hold Shares"
