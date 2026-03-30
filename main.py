from pawpal_system import Owner, Pet, Task, Scheduler


def run_demo():
    print("\n--- PawPal+ Demo ---\n")

    # Create owner
    owner = Owner("Arthur")

    # Create pets
    dog = Pet("Rex", "Dog")
    cat = Pet("Whiskers", "Cat")

    owner.add_pet(dog)
    owner.add_pet(cat)

    # Add tasks (intentionally out of order + conflict)
    dog.add_task(Task("Feed dog", "08:00"))
    dog.add_task(Task("Walk dog", "09:00"))
    cat.add_task(Task("Feed cat", "08:00"))  # conflict time

    # Create scheduler
    scheduler = Scheduler(owner)

    # Display sorted schedule
    print("Today's Schedule (Sorted):")
    sorted_tasks = scheduler.sort_by_time()

    for task in sorted_tasks:
        print(f"{task.time} - {task.pet_name}: {task.description}")

    # Detect conflicts
    conflicts = scheduler.detect_conflicts()

    if conflicts:
        print("\n⚠ Conflicts detected at times:", conflicts)
    else:
        print("\nNo conflicts detected.")

    # Mark a task complete
    print("\nMarking first task complete...")
    scheduler.mark_task_complete(sorted_tasks[0])

    # Show completed tasks
    completed_tasks = scheduler.filter_tasks(completed=True)

    print("\nCompleted Tasks:")
    for task in completed_tasks:
        print(f"{task.time} - {task.pet_name}: {task.description}")


if __name__ == "__main__":
    run_demo()