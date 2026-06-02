import pandas as pd
from pipeline.config import Config
from database.modals.base_modal import Database
from database.modals.database_model import (
    Customer,
    Product,
    Order,
    Payment,
    Date,
    Shipping,
    FactSales
)


class DataLoader:

    def __init__(self, config, file_path):

        self.db = Database(config)
        self.session = self.db.get_session()

        self.df = pd.read_csv(file_path)

        # convert date once
        self.df["Order_date"] = pd.to_datetime(
            self.df["Order_date"],
            errors="coerce"
        )

        # surrogate key maps
        self.customer_map = {}
        self.product_map = {}
        self.order_map = {}
        self.payment_map = {}
        self.date_map = {}
        self.shipping_map = {}

    # ---------------- CUSTOMER ----------------

    def load_customers(self):

        for _, row in self.df.drop_duplicates(
            subset=["Customer_id"]
        ).iterrows():

            obj = Customer(
                customer_id=row["Customer_id"],
                customer_name=row["Customer_name"],
                customer_email=row["Email"],
                customer_phone=row["Phone"],
                customer_address=row["Shipping_address"],
                customer_state=row["State"],
                customer_country=row["Country"]
            )

            self.session.add(obj)
            self.session.flush()

            self.customer_map[
                row["Customer_id"]
            ] = obj.customer_sr_key

    # ---------------- PRODUCT ----------------

    def load_products(self):

        for _, row in self.df.drop_duplicates(
            subset=["Product_id"]
        ).iterrows():

            obj = Product(
                product_id=row["Product_id"],
                product_name=row["Product_name"],
                product_category=row["Category"]
            )

            self.session.add(obj)
            self.session.flush()

            self.product_map[
                row["Product_id"]
            ] = obj.product_sr_key

    # ---------------- ORDER ----------------

    def load_orders(self):

        for _, row in self.df.drop_duplicates(
            subset=["Order_id"]
        ).iterrows():

            obj = Order(
                order_id=row["Order_id"],
                order_status=row["Order_status"],
                order_date=row["Order_date"]
            )

            self.session.add(obj)
            self.session.flush()

            self.order_map[
                row["Order_id"]
            ] = obj.order_sr_key

    # ---------------- PAYMENT ----------------

    def load_payments(self):

        for _, row in self.df.drop_duplicates(
            subset=["Payment_method"]
        ).iterrows():

            obj = Payment(
                payment_method=row["Payment_method"]
            )

            self.session.add(obj)
            self.session.flush()

            self.payment_map[
                row["Payment_method"]
            ] = obj.payment_sr_key

    # ---------------- DATE ----------------

    def load_dates(self):

        for _, row in self.df.drop_duplicates(
            subset=["Order_date"]
        ).iterrows():

            d = row["Order_date"]

            obj = Date(
                date=d,
                day=d.day,
                month=d.month,
                year=d.year
            )

            self.session.add(obj)
            self.session.flush()

            self.date_map[
                row["Order_date"]
            ] = obj.date_sr_key

    # ---------------- SHIPPING ----------------

    def load_shipping(self):

        for _, row in self.df.drop_duplicates(
            subset=["Shipping_address"]
        ).iterrows():

            obj = Shipping(
                shipping_address=row["Shipping_address"],
                shipping_city=row["City"],
                delivery_days=row["Delivery_days"]
            )

            self.session.add(obj)
            self.session.flush()

            self.shipping_map[
                row["Shipping_address"]
            ] = obj.shipping_sr_key

    # ---------------- FACT ----------------

    def load_fact(self):

        facts = []

        for _, row in self.df.iterrows():

            obj = FactSales(

                customer_sr_key=
                self.customer_map[row["Customer_id"]],

                product_sr_key=
                self.product_map[row["Product_id"]],

                order_sr_key=
                self.order_map[row["Order_id"]],

                payment_sr_key=
                self.payment_map[row["Payment_method"]],

                date_sr_key=
                self.date_map[row["Order_date"]],

                shipping_sr_key=
                self.shipping_map[row["Shipping_address"]],

                unit_price=row["Unit_price"],
                quantity=row["Quantity"],
                discount=row["Discount"],
                total_amount=row["Total_amount"]
            )

            facts.append(obj)

        self.session.add_all(facts)

    # ---------------- RUN ----------------

    def run(self):

        try:

            print("Loading Started...")

            self.load_customers()
            print("Customers Loaded")

            self.load_products()
            print("Products Loaded")

            self.load_orders()
            print("Orders Loaded")

            self.load_payments()
            print("Payments Loaded")

            self.load_dates()
            print("Dates Loaded")

            self.load_shipping()
            print("Shipping Loaded")

            self.load_fact()
            print("Fact Loaded")

            self.session.commit()

            print("All Data Loaded Successfully")

        except Exception as e:

            self.session.rollback()

            print("ERROR:", e)

        finally:

            self.session.close()


