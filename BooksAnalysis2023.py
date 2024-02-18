#from datetime import date

books_read_2023 = {
    "Atoms and Ashes: A Global History of Nuclear Disasters": 364, 
    "What My Bones Know: A Memoir of Healing from Complex Trauma": 331,
    "To Hold Up the Sky": 336,
    "Legends & Lattes": 305,
    "A Psalm for the Wild-Built": 160,
    }

# Update newly completed books to dictionary
books_read_2023.update({"Tomorrow, and Tomorrow, and Tomorrow": 418, 
    "A Prayer for the Crown-Shy": 152, "All Our Wrong Todays": 380, "The Echo of Old Books": 431,
    "A Darker Shade of Magic": 401, "Camp Zero": 320, "A Gathering of Shadows": 513, "A Conjuring of Light": 624, 
    "The Dictionary of Lost Words": 400, "Harry Potter and the Sorcerer's Stone": 309, "Harry Potter and the Chamber of Secrets": 357,
    "The Southern Book Club's Guide to Slaying Vampires": 424, "The Quite Tenant": 304, "Harry Potter and the Prisoner of Azkaban": 435,
    "Divine Rivals": 357, "The Coffee Bean": 105, "Godkiller": 304, "The Pumpkin Spice Cafe": 267, "Harry Potter and the Order of the Phoenix": 815,
    "Harry Potter and the Goblet of Fire": 734, "Spells for Forgetting": 368, "Sleeping Giants": 322
    })

# Print out list of books read for the year
def finished_books():
    for book in books_read_2023.keys():
        print(book)

print(finished_books())

# Calculate number of pages read this year
total_pages = 0
for pages in books_read_2023.values():
    total_pages += pages

print(str(total_pages) + " pages read in 2023.")

# Calculate number of books read this year
total_books = 0
for books in books_read_2023.keys():
    total_books += 1

print(str(total_books) + " books read in 2023")

# Calculate averge number of books read per month this year, rounded to nearest integer
# Accept user input month as integer
# At later date, create datetime calculation based on current year and today's date for accuracy
print("What month is it?")
answer = int(input("Enter month (1 - 12): "))

average_books = total_books / answer
print(str(round(average_books)) + " read books per month in 2023.")