# 8-12. Sandwiches
def sandwich_items(*items):
    print(f"\nMaking a sandwich with the following items: ")
    for item in items:
        print(f"- {item}")


sandwich_items('tuna')
sandwich_items('turkey', 'lettuce', 'tomato', 'avocado')
sandwich_items('meatballs', 'cheese')


# 8-13. User Profile
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile("blueberry", 'muffin', hobby = 'gaming', fav_food = 'pho', fav_drink = 'water')
print(user_profile)


# 8-14. Cars
def make_car(manufacturer, model, **car_info):
    car_info['manufacturer_'] = manufacturer
    car_info['model_'] = model
    return car_info

car = make_car('subaru', 'outback', color = 'blue', tow_package = 'True')
print(car)
