from pipeline.config import Config
from pipeline.gold_layer import DataLoader
from pipeline.silver import Silver
from pipeline.bronze import Bronze
from pipeline.extract import Extract
from database.modals.base_modal import Database

def main():

    config = Config("config.ini")

    extractor = Extract(config)
    data = extractor.extract_data()

    bronze = Bronze(data)
    bronze.save_to_bronze()

    silver = Silver()
    cleaned = silver.clean_data()

    if cleaned is not None:

        cleaned.to_csv(
            "data/silver_data.csv",
            index=False
        )

    db = Database(config)
    db.create_tables()

    gold = DataLoader(
        config,
        "data/silver_data.csv"
    )

    gold.run()


if __name__ == "__main__":
    main()