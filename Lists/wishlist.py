books = [
  "Learning Python - Mark Lutz",
  "Automate the Boring Stuff with Python - Al Sweigart",
  "Python For Data Analysis - Wes McKinney",
  "Fluent Python - Luciano Ramalho",
  "Python for Kids - Jason Briggs",
  "Hello World App - Tracy Osbourne",
]

video_games = [
    "The Legend of Zelda: Breath of the Wild",
    "Splatoon 2",
    "Super Mario Odyssey",
]

def display_wishlist(display_name, wishes):
  items = wishes.copy()
  print(display_name + ":")
  suggested_gift = items.pop(0)
  print("=====>", suggested_gift, "<=====")
  for item in items:
    print("* " + item)
  print()

display_wishlist("Books", books)
display_wishlist("Video Games", video_games)
