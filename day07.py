import re


def get_prerequisites(instructions):
    prerequisites = {}
    for instruction in instructions:
        instruction_search = re.search("Step ([A-Z]) must be finished before step ([A-Z]) can begin.", instruction)
        if instruction_search:
            before = instruction_search.group(1)
            after = instruction_search.group(2)

            if before not in prerequisites:
                prerequisites[before] = set()

            if after not in prerequisites:
                prerequisites[after] = {before}
            else:
                prerequisites[after].add(before)

    return prerequisites


def build_steps(instructions):
    prerequisites = get_prerequisites(instructions)

    steps = ""
    while prerequisites:
        next_step = min([k for k, v in prerequisites.items() if v == set()])
        steps += next_step
        prerequisites.pop(next_step)

        for prerequisite in prerequisites:
            if next_step in prerequisites[prerequisite]:
                prerequisites[prerequisite].remove(next_step)

    return steps


def step_length(step, duration_increase):
    return ord(step) - ord('A') + 1 + duration_increase


def get_free_workers(workers):
    free_workers = []

    for worker in workers:
        if workers[worker][0] == 0:
            free_workers.append(worker)

    return free_workers


def busy(workers):
    for worker in workers:
        if workers[worker][0]:
            return True
    return False


def assign_jobs_to_free_workers(prerequisites, workers, duration_increase):
    next_steps = [k for k, v in prerequisites.items() if v == set()]
    free_workers = get_free_workers(workers)
    while next_steps and free_workers:
        next_step = min(next_steps)
        free_worker = free_workers[0]
        workers[free_worker] = (step_length(next_step, duration_increase), next_step)

        prerequisites.pop(next_step)
        next_steps.remove(next_step)
        free_workers.remove(free_worker)

    return prerequisites, workers


def clean_up_finished_jobs(prerequisites, workers):
    free_workers = get_free_workers(workers)
    for free_worker in free_workers:
        job_finished = workers[free_worker][1]
        if job_finished is not None:
            for prerequisite in prerequisites:
                if job_finished in prerequisites[prerequisite]:
                    prerequisites[prerequisite].remove(job_finished)
        workers[free_worker] = (0, None)

    return prerequisites, workers


def work_one_second(prerequisites, workers):
    for worker in workers:
        time_remaining = workers[worker][0]
        task = workers[worker][1]
        if time_remaining:
            workers[worker] = (time_remaining - 1, task)

    return clean_up_finished_jobs(prerequisites, workers)


def time_to_complete(instructions, num_workers, duration_increase):
    prerequisites = get_prerequisites(instructions)

    workers = {}
    for worker in range(0, num_workers):
        workers[worker] = (0, None)

    time_taken = 0
    while prerequisites or busy(workers):
        prerequisites, workers = assign_jobs_to_free_workers(prerequisites, workers, duration_increase)
        prerequisites, workers = work_one_second(prerequisites, workers)
        time_taken += 1

    return time_taken


def test1():
    print("Test 1: ")

    with open("inputs/input07.txt", "r") as f:
        instructions = f.readlines()
    print(build_steps(instructions))


def test2():
    print("Test 2: ")

    with open("inputs/input07.txt", "r") as f:
        instructions = f.readlines()
    print(time_to_complete(instructions, 5, 60))


if __name__ == "__main__":
    test1()
    test2()