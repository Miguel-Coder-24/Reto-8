class MenuItem:
    def __init__(self, name: str, price: float, quantity: int = 1) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self) -> float:
        return self.price * self.quantity

    def __repr__(self) -> str:
        return f"{self.name} x{self.quantity} - ${self.total_price():.2f}"


class Beverage(MenuItem):
    def __init__(self, name: str, price: float, quantity: int = 1, is_alcoholic: bool = False) -> None:
        super().__init__(name, price, quantity)
        self.is_alcoholic = is_alcoholic

    def total_price(self) -> float:
        base_price = super().total_price()
        if self.is_alcoholic and self.quantity >= 5:
            return base_price * 0.9  # 10% descuento si son 5+ bebidas alcohólicas
        return base_price

    def __repr__(self) -> str:
        alc = " (Alcoholic)" if self.is_alcoholic else ""
        return f"Beverage: {self.name}{alc} x{self.quantity} - ${self.total_price():.2f}"


class Appetizer(MenuItem):
    def __init__(self, name: str, price: float, quantity: int = 1, with_sauce: bool = False) -> None:
        super().__init__(name, price, quantity)
        self.with_sauce = with_sauce

    def __repr__(self) -> str:
        sauce = " with sauce" if self.with_sauce else ""
        return f"Appetizer: {self.name}{sauce} x{self.quantity} - ${self.total_price():.2f}"


class MainCourse(MenuItem):
    def __init__(self, name: str, price: float, quantity: int = 1, is_vegetarian: bool = False) -> None:
        super().__init__(name, price, quantity)
        self.is_vegetarian = is_vegetarian

    def total_price(self) -> float:
        base_price = super().total_price()
        if self.is_vegetarian:
            return base_price * 0.85  # 15% descuento para platos vegetarianos
        return base_price

    def __repr__(self) -> str:
        veg = " (Vegetarian)" if self.is_vegetarian else ""
        return f"Main Course: {self.name}{veg} x{self.quantity} - ${self.total_price():.2f}"


class Order:
    def __init__(self) -> None:
        self.items = []

    def add_item(self, item: MenuItem) -> None:
        self.items.append(item)

    def calculate_total(self) -> float:
        total = 0
        for item in self.items:
            total += item.total_price()
        if total > 100:
            total *= 0.95  # 5% descuento si el total supera 100
        return total

    def show_order(self) -> None:
        print("Order Summary:")
        for item in self:
            print(item)
        print(f"Total: ${self.calculate_total():.2f}")

    def __iter__(self):
        return iter(self.items)  # Ahora es iterable


# PRUEBA PRINCIPAL

order = Order()

order.add_item(Beverage("Coca-Cola", 2.5, quantity=3))
order.add_item(Beverage("Red Wine", 10.0, quantity=6, is_alcoholic=True))
order.add_item(Appetizer("Spring Rolls", 5.0, quantity=2, with_sauce=True))
order.add_item(Appetizer("Garlic Bread", 4.0))
order.add_item(MainCourse("Grilled Chicken", 15.0, quantity=1))
order.add_item(MainCourse("Vegetarian Lasagna", 12.0, quantity=2, is_vegetarian=True))
order.add_item(MainCourse("Steak", 22.0, quantity=1))
order.add_item(Beverage("Orange Juice", 3.5, quantity=2))
order.add_item(Appetizer("Stuffed Mushrooms", 6.5, quantity=1))
order.add_item(MainCourse("Fish and Chips", 14.0, quantity=1))

order.show_order()

# Ejemplo adicional usando la iteración:
print("\n--- Iterating over order items ---")
for item in order:
    print(f"{item.name}: ${item.total_price():.2f}")

# OTRO USO DESDE __main__ 

if __name__ == "__main__":
    orden = Order()

    # Agregar 2 main courses, 1 appetizer, 2 beverages
    orden.add_item(MainCourse("Grilled Chicken", 15.00))
    orden.add_item(MainCourse("Vegetarian Lasagna", 10.20, is_vegetarian=True))
    orden.add_item(Appetizer("Spring Rolls", 5.00, with_sauce=True))
    orden.add_item(Beverage("Coca-Cola", 2.50))
    orden.add_item(Beverage("Red Wine", 9.00, is_alcoholic=True))

    orden.show_order()

    # Ejemplo de bucle externo
    print("\nDetalles individuales del pedido:")
    for item in orden:
        print(f"- {item.__class__.__name__}: {item.name} × {item.quantity} => ${item.total_price():.2f}")
