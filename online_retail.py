import pandas as pd

class ReadTransform():
    def __init__(self):
        return

    def execute(self):
        self.transform(self.read())

    def read(self):
        data = pd.read_csv('online_retail.csv', delimiter=';')

        print(data)

        return data
    # untuk mentransform data
    def transform(self, data):
        data['Quantity'] = data['Quantity'].astype(int)
        data['UnitPrice'] = data['UnitPrice'].str.replace(',', '.').astype(float)

        data['total_price'] = data['Quantity'] * data['UnitPrice']
        data['InvoiceDate'] = data['InvoiceDate'].str.split().str[0]

        customer_spend = data.groupby(by='CustomerID').agg({'total_price': 'sum'})
        daily_revenue = data.groupby(by='InvoiceDate').agg({'total_price': 'sum'})
        country_sales = data.groupby(by='Country').agg({'InvoiceNo': 'count'})

        customer_spend.to_csv('output/customer_spend.csv')
        daily_revenue.to_csv('output/daily_revenue.csv')
        country_sales.to_csv('output/country_sales.csv')

if __name__ == '__main__':
    ReadTransform().execute()
