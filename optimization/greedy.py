from dataclasses import dataclass


@dataclass
class Food:
    name: str
    value: int
    calories: int

    def get_value(self):
        return self.value

    def density(self):
        return self.value/self.calories


def greedy(foods, max_calories, sort_func):
    sorted_foods = sorted(foods, key=sort_func)
    curr_calories, curr_value = 0, 0
    selected_foods = []
    for food in sorted_foods:
        if curr_calories + food.calories <= max_calories:
            selected_foods.append(food)
            curr_calories += food.calories
            curr_value += food.value
        else:
            break
    return selected_foods, curr_value


def print_result(selection, value):
    total_cal = sum([getattr(food, "calories") for food in selection])
    print(f"Total value: {value} with {total_cal} cals")
    food_names = [getattr(food, "name") for food in selection]
    print(f"Content: {', '.join(food_names)}")


names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]
foods = [Food(names[i], values[i], calories[i]) for i, _ in enumerate(names)]


print("- Result with Food.density -")
selection, value = greedy(foods, 1500, Food.density)
print_result(selection, value)

print("- Result with Food.get_value -")
selection, value = greedy(foods, 1500, Food.get_value)
print_result(selection, value)


# testGreedys(foods, 1000)
