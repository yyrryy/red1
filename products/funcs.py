import requests as req
from main.models import Order, Orderitem, Represent, Client, Produit
def updatestockinremoteserver(products, serverip):
    url = f"http://{serverip}/products/updatestockfromthread"
    headers = {'Content-Type': 'application/json'}
    try:
        response = req.post(url, json=products, headers=headers)
        response.raise_for_status()
        return True
    except req.exceptions.RequestException as e:
        print(f"Error updating stock on remote server: {e}")
        return False

# create orders that will come from the server
def createorders(orders):
    print(f"Creating {len(orders)} orders...", orders)
    for o in orders:
        # 1. Create order
        order = Order.objects.create(
            date=o['date'],
            total=o['total'],
            note=o['note'],
            client=Client.objects.get(code=o['clientcode']),
            order_no=o['order_no'],
            isclientcommnd=o['isclientcommnd'],
        )
        try:
            salseman=Represent.objects.get(pk=o['salsemanid'])
            order.salseman=salseman
            order.save()
        except Represent.DoesNotExist:
            print(f"Salesman with ID {o['salsemanid']} does not exist.")
            pass

        items = o['items']

        # 2. Collect uniqcodes
        uniqcodes = [item['uniqcode'] for item in items]

        # 3. Fetch products in ONE query
        produits = Produit.objects.filter(uniqcode__in=uniqcodes)
        produit_map = {p.uniqcode: p for p in produits}

        # 4. Prepare Orderitem objects
        order_items = [
            Orderitem(
                order=order,
                product=produit_map[item['uniqcode']],
                qty=item['qty'],
                price=item['price'],
                total=item['total'],
            )
            for item in items
        ]

        # 5. Bulk insert
        Orderitem.objects.bulk_create(order_items)