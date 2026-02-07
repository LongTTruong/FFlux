import csv
import matplotlib.pyplot as plt

def main():
    days = []
    required_exercise = []

    with open("fat_loss_simulation.csv", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            days.append(int(row["Day"]))
            required_exercise.append(float(row["RequiredExercise_kcal"]))

    plt.figure()
    plt.plot(days, required_exercise)
    plt.xlabel("Day")
    plt.ylabel("Required Exercise (kcal/day)")
    plt.title("Required Exercise Thermogenesis to Maintain Max Fat Loss")
    plt.savefig("required_exercise_over_time.png")
    plt.close()

if __name__ == "__main__":
    main()
