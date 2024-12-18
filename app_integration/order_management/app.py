from order_management.database import Database
from order_management.payment_service import process_payment

db = Database()

def create_order(product, quantity, db):
    order = {
        "order_id": None,
        "product": product,
        "quantity": quantity,
        "payment_status": "Pending",
    }
    if process_payment(order):
        order['payment_status'] = "Processed"
        db.save_order(order)
    return order
