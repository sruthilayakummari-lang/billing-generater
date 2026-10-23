# billing.py
# Calculates item totals, GST, and final amount

from products import items

GST_RATE = 5

def calculate_bill(cart):
    totalprice = 0

    for item, quantity in cart.items():
        totalprice += items[item] * quantity

    gst = totalprice * GST_RATE / 100
    finalamount = totalprice + gst
    return totalprice, gst, finalamount
