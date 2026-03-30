# PawPal+ Project Reflection

## 1. System Design

### a. Initial design

My initial UML design included four main classes: Task, Pet, Owner, and Scheduler. The Task class represents individual activities such as feeding or walking, storing attributes like description, time, and completion status. The Pet class manages a list of tasks for each pet. The Owner class stores multiple pets and provides access to all tasks. The Scheduler class acts as the main logic layer, responsible for organizing tasks, sorting them by time, filtering them, and detecting conflicts.

This design was chosen because it separates responsibilities clearly and reflects real-world relationships between owners, pets, and tasks.

---

### b. Design changes

Yes, my design changed during implementation. Initially, the system only focused on storing pets and tasks. As I continued building, I expanded the Scheduler class to include more functionality such as filtering tasks, detecting scheduling conflicts, and handling recurring tasks.

I made these changes because the original design was too basic and did not fully meet the project requirements. Adding more logic to the Scheduler improved the system’s ability to manage and organize tasks effectively.

---

## 2. Scheduling Logic and Tradeoffs

### a. Constraints and priorities

The scheduler considers time as the main constraint when organizing tasks. Tasks are sorted based on their time values, which allows the system to generate a structured daily schedule. The system also considers task completion status and pet association when filtering tasks.

Time was chosen as the most important constraint because it directly affects how a daily schedule is organized. While priority could be added, I focused on time-based organization to keep the system simple and functional.

---

### b. Tradeoffs

One major tradeoff in my scheduler is that conflict detection only checks for tasks with identical times. It does not detect overlapping time ranges or consider task duration.

This tradeoff is reasonable because it simplifies the implementation while still demonstrating the concept of conflict detection. For a beginner-level project, checking exact time matches is an effective way to show scheduling logic without adding unnecessary complexity.

---

## 3. AI Collaboration

### a. How you used AI

I used AI tools to help design the class structure, generate initial code, and guide the implementation of scheduling logic. AI was especially helpful when building the relationships between classes and creating methods for sorting and filtering tasks.

The most helpful prompts were those that asked for step-by-step implementations or explanations of how different parts of the system should interact.

---

### b. Judgment and verification

One example where I did not fully accept an AI suggestion was when more complex implementations were proposed. Some AI-generated solutions included unnecessary complexity that made the code harder to understand.

I chose to simplify those solutions to keep the code more readable and aligned with the project requirements. I verified the correctness of the code by running the CLI demo and using pytest to confirm that the system behaved as expected.

---

## 4. Testing and Verification

### a. What you tested

I tested several key behaviors, including marking a task as complete, adding tasks to a pet, sorting tasks by time, and detecting scheduling conflicts.

These tests were important because they verify that the core functionality of the system works correctly. Without these tests, it would be difficult to confirm that the scheduling logic behaves as intended.

---

### b. Confidence

I am confident that my scheduler works correctly for the core features implemented in this project. All tests pass successfully, and the CLI demo produces the expected output.

If I had more time, I would test additional edge cases such as empty task lists, multiple pets with large numbers of tasks, and more advanced conflict scenarios involving overlapping time ranges.

---

## 5. Reflection

### a. What went well

The part of the project I am most satisfied with is the Scheduler logic. It successfully organizes tasks, detects conflicts, and integrates with the rest of the system in a clean way.

---

### b. What you would improve

If I had another iteration, I would improve the scheduling system by adding task priorities and more advanced time management, such as handling durations and overlapping schedules.

---

### c. Key takeaway

One important thing I learned from this project is that designing a system step-by-step is very important. Breaking the project into smaller parts made it easier to manage and understand.

I also learned that AI is a useful tool for generating ideas and code, but it is important to review and adjust those suggestions to make sure they are correct and appropriate for the project.