from pathlib import Path

class Bronze:

    def __init__(self, data):

        self.data = data
        self.bronze_path = Path(
            "data/bronze_data.csv"
        )

    def save_to_bronze(self):

        with open(
            self.bronze_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(self.data)

        print("Bronze layer loaded")