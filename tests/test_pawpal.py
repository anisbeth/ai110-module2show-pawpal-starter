from pawpal_system import Task, Pet, Owner, Scheduler


def test_task_complete():
    task = Task("Feed dog", "08:00")
    task.mark_complete()
    assert task.completed is True


def test_add_task_to_pet():
    pet = Pet("Rex", "Dog")
    task = Task("Walk dog", "09:00")

    pet.add_task(task)

    assert len(pet.tasks) == 1
    assert pet.tasks[0].description == "Walk dog"


def test_sorting_tasks():
    owner = Owner("Arthur")
    pet = Pet("Rex", "Dog")

    owner.add_pet(pet)

    pet.add_task(Task("Task 1", "10:00"))
    pet.add_task(Task("Task 2", "08:00"))

    scheduler = Scheduler(owner)
    sorted_tasks = scheduler.sort_by_time()

    assert sorted_tasks[0].time == "08:00"


def test_conflict_detection():
    owner = Owner("Arthur")
    pet = Pet("Rex", "Dog")

    owner.add_pet(pet)

    pet.add_task(Task("Task 1", "08:00"))
    pet.add_task(Task("Task 2", "08:00"))

    scheduler = Scheduler(owner)
    conflicts = scheduler.detect_conflicts()

    assert "08:00" in conflicts