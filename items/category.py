cateList = [
'Beverages->Energy Drink',
'Beverages->Fresh Juice',
'Beverages->Juice->Allens',
'Beverages->Juice->Compliments',
'Beverages->Juice->Minute Maid&FiveAlive',
'Beverages->Juice->Oasis ',
'Beverages->Juice->OceanSpray',
'Beverages->Juice->Other Juice',
'Beverages->Juice->V8&Motts',
'Beverages->Soft Drink->7up&Schweppes&MontainDew',
'Beverages->Soft Drink->CocaCola&Pepsi',
'Beverages->Soft Drink->Compliments',
'Beverages->Soft Drink->Crush&Cplus',
'Beverages->Soft Drink->Fruitopia&Fuze ',
'Beverages->Soft Drink->Root Beer',
'Beverages->Soft Drink->Sprite&Canada Dry',
'Beverages->Soft Drink->Tea Beverage',
'Beverages->Water->Flavoured Water&Vitamin Water',
'Beverages->Water->Sparkling Water',
'Beverages->Water->Spring Water',
'Home & Lifestyle->Home Appliances->Light Bulbs ',
'Home & Lifestyle->Home Supplies->Air Freshners ',
'Home & Lifestyle->Home Supplies->Bathroom & All Purpose Cleaning',
'Home & Lifestyle->Home Supplies->Bathroom Tissue',
'Home & Lifestyle->Home Supplies->Cleaning Supplies ',
'Home & Lifestyle->Home Supplies->Dishwashing Liquid',
'Home & Lifestyle->Home Supplies->Facial Tissue',
'Home & Lifestyle->Home Supplies->Foil & Baking Pans ',
'Home & Lifestyle->Home Supplies->Garbage Bags',
'Home & Lifestyle->Home Supplies->Laundry',
'Home & Lifestyle->Home Supplies->Paper Towel',
'Home & Lifestyle->Home Supplies->Plastic Wrap & Freezer Bags',
'Home & Lifestyle->Oral Care->Oral Rinse',
'Home & Lifestyle->Oral Care->Tooth Paste',
'Home & Lifestyle->Oral Care->Toothbrush',
'Home & Lifestyle->Personal Care->Antiperspirant & Deodorant',
'Home & Lifestyle->Personal Care->Body Wash',
'Home & Lifestyle->Personal Care->Feminine Hygiene',
'Home & Lifestyle->Personal Care->Hair Enhancement ',
'Home & Lifestyle->Personal Care->Hand Wash',
'Home & Lifestyle->Personal Care->Shampoo & Conditioner ',
'Pet Care->Cat Foods',
'Pet Care->Dog Foods ',
'Produce->Bakery->Breads',
'Produce->Bakery->Other Bakery Products ',
'Snacks & Candies->Candies & Chocolates->Candies',
'Snacks & Candies->Candies & Chocolates->Chocolate Bars',
'Snacks & Candies->Candies & Chocolates->Chocolate Packs',
'Snacks & Candies->Candies & Chocolates->Gum',
'Snacks & Candies->Chips & Popcorn->Compliments & Sensations',
'Snacks & Candies->Chips & Popcorn->Dips ',
'Snacks & Candies->Chips & Popcorn->Doritos ',
'Snacks & Candies->Chips & Popcorn->Lays ',
'Snacks & Candies->Chips & Popcorn->Miss Vickies ',
'Snacks & Candies->Chips & Popcorn->Popchips & Rickworks',
'Snacks & Candies->Chips & Popcorn->Popcorn ',
'Snacks & Candies->Chips & Popcorn->Pringles ',
'Snacks & Candies->Chips & Popcorn->Ruffles ',
'Snacks & Candies->Chips & Popcorn->SunChips & Cheetos & Fritos ',
'Snacks & Candies->Chips & Popcorn->Tostitos ',
'Snacks & Candies->Cookies & Biscuits->Biscuits ',
'Snacks & Candies->Cookies & Biscuits->Cookies',
'Snacks & Candies->Cookies & Biscuits->Crackers',
'Snacks & Candies->Dried Fruit & Fruit Snacks->Fruit Cups ',
'Snacks & Candies->Dried Fruit & Fruit Snacks->Fruit Snacks',
'Snacks & Candies->Pudding & Jello->Pudding ',
'Groceries->Cereal & Breakfast->Cereal',
'Groceries->Cereal & Breakfast->Granola Bars & Tarts Bars',
'Groceries->Cereal & Breakfast->Oatmeal',
'Groceries->Coffee & Tea->Coffee ',
'Groceries->Coffee & Tea->Hot Chocolate',
'Groceries->Coffee & Tea->Tea',
'Groceries->Eggs',
'Groceries->Dairy Products->Butter & Margarine',
'Groceries->Dairy Products->Cheese',
'Groceries->Dairy->Kids Yogurt&Yogurt Beverage ',
'Groceries->Dairy->Milk',
'Groceries->Dairy->Yogurt',
'Groceries->Dried Side Dishes ',
'Groceries->Canned Foods->Canned Beans & Peas',
'Groceries->Condiments & Sauces->Honey & Syrup',
'Groceries->Condiments & Sauces->Jam',
'Groceries->Condiments & Sauces->Ketchup & Mustard',
'Groceries->Condiments & Sauces->Mayonnaise',
'Groceries->Condiments & Sauces->Salad Dressing',
'Groceries->Condiments & Sauces->Salt & Sugar',
'Groceries->Condiments & Sauces->Spreads',
'Groceries->Condiments & sauces->Pickles, Relish & Olives',
'Groceries->Nuts & Seeds->Nuts',
'Groceries->Oil,Spices & Seasonning->Oil',
'Groceries->Pasta & Sauce->Pasta',
'Groceries->Soup & Cans->Canned Corn and Other Vegetables ',
'Groceries->Soups & Cans->Canned Fruits',
'Groceries->Soups & Cans->Canned Meal ',
'Groceries->Soups & Cans->Canned Meat & Seafood',
'Groceries->Soups & Cans->Canned Soups ',
'Groceries->Soups & Cans->Canned Tomatoes ',
'Groceries->Soups & Cans->Dried Soups & Instant Noodles',
'Groceries->Ham & Sausages ',
'Groceries->Frozen Foods->Frozen Breakfast',
'Groceries->Frozen Foods->Frozen Fishes',
'Groceries->Frozen Foods->Frozen Fries & Onion Rings',
'Groceries->Frozen Foods->Frozen Juices and Fruits',
'Groceries->Frozen Foods->Frozen Meal ',
'Groceries->Frozen Foods->Frozen Vegetables',
'Groceries->Frozen Foods->Ice Cream ',
'Groceries->Frozen Foods->Pizza ',
'Groceries->Frozen Foods->Pizza Pops and Others ',
'Groceries->Frozen Foods->Prepared and Frozen Meat',
]
category = {};

for c in cateList:
  c = c.split('->')
  assert len(c) >= 2, 'incalid category format: %s' % c
  if c[0] not in category:
    category[c[0]]={}
  if c[1] not in category[c[0]]:
    category[c[0]][c[1]]=[]
  if len(c) == 3:
    category[c[0]][c[1]].append(c[2])
