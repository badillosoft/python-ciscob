# _*_ coding: utf-8 _*_

import oxxcisco as ox

ox.insert_product({
    "name": "Coca-Cola 600ml",
    "brand": "Coca-Cola",
    "price": {
        "unitary": 6.5,
        "customer": 11.5
    },
    "bar_code": "A1728996-01"
})

ox.show_products()