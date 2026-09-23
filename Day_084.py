# ========================= Question ========================
# Build a data pipeline using generators for processing
# payment records from a CSV file.
#
# Stage 1:
# read_records(filepath)
# - Read raw CSV rows as strings.
#
# Stage 2:
# parse_records(rows)
# - Convert CSV rows into dictionaries.
#
# Stage 3:
# filter_paid(records)
# - Yield only records whose status is "paid".
#
# Stage 4:
# add_tax(records, rate)
# - Add tax and total to each paid record.
#
# Connect all generators into one pipeline and print
# the final records.
# ============================================================


# Solution:
# Read raw rows from the CSV file.
def read_records(filepath):
    with open(filepath, "r") as file:
        for line in file:
            line = line.strip()

            if line:
                yield line


# Convert raw CSV strings into dictionaries.
def parse_records(rows):

    header = next(rows).split(",")
  
    for row in rows:
        values = row.split(",")

        record = dict(zip(header, values))
        record["id"] = int(record["id"])
        record["amount"] = float(record["amount"])

        yield record


# Yield only paid payment records.
def filter_paid(records):

    for record in records:
        if record["status"] == "paid":
          
            yield record



# Add tax and total amount.
def add_tax(records, rate):

    for record in records:
        tax = record["amount"] * rate
        record["tax"] = tax
        record["total"] = record["amount"] + tax
      
        yield record


# ========================= Create Pipeline ==================
# Data flows from one generator into another.
pipeline = add_tax(
    filter_paid(
        parse_records(
            read_records("payments.csv")
        )
    ),
    0.18
)


# ========================= Consume Pipeline ================
# Nothing is actually processed until the pipeline is consumed.

for record in pipeline:
    print(record)
