
class TaxMan:
    def __init__(self, items, tax):
        self.items = items
        self.tax = tax
        self.total = 0
        self.tax_percentage = None

    def get_total(self):
        self.tax_percentage = float(self.tax.strip("%")) / 100
        self.total = self.total + (self.total * self.tax_percentage)
        return self.total

    def calc_total(self):
        if self.items is None:
            return None

        self.total = sum(item['price'] for item in self.items)


"""
    tax_percentage = float(tax.strip("%")) / 100

    total_with_tax = total + (total*tax_percentage)
    formatted_total = "${:,.2f}".format(total_with_tax)
    """