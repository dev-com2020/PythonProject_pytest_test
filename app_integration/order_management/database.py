class Database:
    def __init__(self):
        self.orders = {}

    def save_order(self, order):
        self.orders[order['order_id']] = order

    def get_order(self, order_id):
        return self.orders.get(order_id)

    def clear_orders(self):
        self.orders.clear()
