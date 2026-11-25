import os

def generate_entry():
    # Deadpan 1-star review of gravity (concise, sharp grievance, under 160 chars)
    review = "Gravity: Drops everything without warning, provides zero customer support, refuses to let go of keys under the bed. 1/5 stars."
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(review.strip())

if __name__ == "__main__":
    generate_entry()
