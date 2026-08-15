run_date = str(input("Today's date: "))
run_time = float(input("How long was today's run: "))
type_of_distance = str(input("What type of distance was today's run in: "))
run_distance = float(input("How much distance was today's run: "))

calculated_pace = run_time / run_distance

print(f"Date: {run_date} | Time ran for: {run_time} | Distance type: {type_of_distance} | Distance: {run_distance} | Pace: {calculated_pace:.2f}")

with open("training_database.txt", "a") as file:
    file.write(f"Date: {run_date} | Time ran for: {run_time} | Distance type: {type_of_distance} | Distance: {run_distance} | Pace: {calculated_pace:.2f}")