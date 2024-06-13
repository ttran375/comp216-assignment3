class Shopper:
    __prices = {"apple": 1.99, "bread": 2.19, "milk": 4.96, "pepper": 1.25}
    __sale_items = "pepper banana".split()
    __credit_threshold = 6
    __default_price = 2.50
    __volume_discount = 0.9
    __sales_discount = 0.85

    def __init__(self, name, cash):
        self.__name = name
        self.__cash = cash
        self.__purchases = []

    @property
    def name(self):
        return self.__name

    @classmethod
    def price_list(cls):
        return cls.__prices

    @classmethod
    def sale_items(cls):
        return cls.__sale_items

    def purchase(self, items):
        total_cost = 0
        for item in items:
            price = self.__prices.get(item, self.__default_price)
            if item in self.__sale_items:
                price *= self.__sales_discount
            self.__purchases.append((item, price))
            total_cost += price

        if total_cost > self.__credit_threshold:
            total_cost *= self.__volume_discount

        self.__cash -= total_cost

    def __str__(self):
        purchases_str = ", ".join(
            [f"('{item}', {price})" for item, price in self.__purchases]
        )
        return f"{self.__name} cash in hand ${self.__cash:.2f}\n  items:\n  [{purchases_str}]"


# Test harness
if __name__ == "__main__":
    print(f"Price dict: {Shopper.price_list()}")
    print(f"Sales list: {Shopper.sale_items()}")

    nar = Shopper("Narendra", 20)  # create a shopper object
    print(f"\n{nar}")  # display the object

    items = "bread milk".split()  # list of items to buy
    print(f"\n{nar.name} is purchasing: {items}")
    nar.purchase(items)  # buy the items
    print(f"{nar}")  # display the object

    items = "apple pepper cauliflower".split()
    print(f"\n{nar.name} is purchasing: {items}")
    nar.purchase(items)
    print(f"{nar}")  # display the object

    # you don't need to understand the code below
    # it is for verification purposes
    members = [member for member in dir(Shopper) if not member.startswith("_")]
    print(f"\nPublic members of the class: {members}")
    properties = [
        member for member in members if not callable(getattr(Shopper, member))
    ]
    print(f"Public properties: {properties}")
    methods = [member for member in members if callable(getattr(Shopper, member))]
    print(f"Public methods: {methods}")
