from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Task:
    description: str
    time: str
    frequency: str = "once"
    completed: bool = False
    pet_name: str = ""

    def mark_complete(self):
        self.completed = True

    def create_next_task(self):
        if self.frequency == "daily":
            return Task(self.description, self.time, "daily", False, self.pet_name)
        elif self.frequency == "weekly":
            return Task(self.description, self.time, "weekly", False, self.pet_name)
        return None


@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        task.pet_name = self.name
        self.tasks.append(task)


class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

    def get_all_tasks(self):
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.tasks)
        return all_tasks


class Scheduler:
    def __init__(self, owner):
        self.owner = owner

    def get_all_tasks(self):
        return self.owner.get_all_tasks()

    def sort_by_time(self):
        return sorted(self.get_all_tasks(), key=lambda task: task.time)

    def filter_tasks(self, completed: Optional[bool] = None, pet_name: Optional[str] = None):
        tasks = self.get_all_tasks()

        if completed is not None:
            tasks = [t for t in tasks if t.completed == completed]

        if pet_name is not None:
            tasks = [t for t in tasks if t.pet_name.lower() == pet_name.lower()]

        return tasks

    def detect_conflicts(self):
        conflicts = []
        tasks = self.get_all_tasks()

        for i in range(len(tasks)):
            for j in range(i + 1, len(tasks)):
                if tasks[i].time == tasks[j].time:
                    conflicts.append(tasks[i].time)

        return conflicts

    def mark_task_complete(self, task):
        task.mark_complete()
        new_task = task.create_next_task()

        if new_task:
            for pet in self.owner.pets:
                if pet.name == task.pet_name:
                    pet.add_task(new_task)