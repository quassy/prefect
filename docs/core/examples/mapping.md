---
editLink: false
---


# Mapping

[Mapping](/core/concepts/mapping/) in Prefect can be used to apply the same
task (or tasks) to multiple inputs. To map a task, use its `.map` method
instead of calling the task itself.

```python
from prefect import task

@task
def add(x, y):
    return x + y

add(1, 2)  # 3
add.map([1, 10], [2, 3])  # [3, 13]
```

By default all arguments to `.map` expect iterables that can be mapped over. If
you want to pass in a non-iterable argument to be used by all branches in a
mapped task, you can wrap that argument in `unmapped`
([docs](/core/concepts/mapping/#unmapped-inputs)).

```python
from prefect import unmapped

add.map([1, 10], unmapped(2))  # [3, 12]
```

In this example we build a flow with 4 stages:

- `get_numbers` returns a list of `n` numbers
- `inc` maps across this list, running once per input
- `add` maps across the output of `inc`, running once per input. `unmapped` is
  used to pass `2` as a second "unmapped" argument.
- The total list is then passed to `compute_sum` to calculate a total.

```
             ┌── inc ── add(2) ──┐
             │                   │
get_numbers ─┼── inc ── add(2) ──┼─ compute_sum
             │                   │
             ⋮                   ⋮
             └── inc ── add(2) ──┘
```

Note that the number of inputs to a mapped task doesn't need to be known until
runtime. By default this flow will run with `3` mapped branches - try
providing different values for the parameter `n` to see how it affects
execution.

See the [mapping docs](/core/concepts/mapping/) for more information.


!!! tip "Registering with Prefect Cloud/Server"
    This example can be registered in Prefect Cloud or Server by running:

    ```
    prefect register --json https://docs.prefect.io/examples.json \
        --name 'Example: Mapping' \
        --project 'Prefect Examples'
    ```

    (To register in a different project, replace `'Prefect Examples'` with your project name).

```python
from prefect import Flow, Parameter, task, unmapped


@task
def get_numbers(n):
    return range(1, n + 1)


@task
def inc(x):
    return x + 1


@task
def add(x, y):
    return x + y


@task(log_stdout=True)
def compute_sum(nums):
    total = sum(nums)
    print(f"total = {total}")
    return total


with Flow("Example: Mapping") as flow:
    # The number of branches in the mapped pipeline
    n = Parameter("n", default=3)

    # Generate the initial items to map over
    nums = get_numbers(n)  # [1, 2, 3]

    # Apply `inc` to every item in `nums`
    nums_2 = inc.map(nums)  # [2, 3, 4]

    # Apply `add` to every item in `nums_2`, with `2` as the second argument.
    nums_3 = add.map(nums_2, unmapped(2))  # [4, 5, 6]

    # Compute the sum of all items in `nums_3`
    total = compute_sum(nums_3)  # 15


if __name__ == "__main__":
    flow.run()
```

Output:

```bash
$ python examples/mapping.py
INFO | Beginning Flow run for 'Example: Mapping'
INFO | Task 'n': Starting task run...
INFO | Task 'n': Finished task run for task with final state: 'Success'
INFO | Task 'get_numbers': Starting task run...
INFO | Task 'get_numbers': Finished task run for task with final state: 'Success'
INFO | Task 'inc': Starting task run...
INFO | Task 'inc': Finished task run for task with final state: 'Mapped'
INFO | Task 'inc[0]': Starting task run...
INFO | Task 'inc[0]': Finished task run for task with final state: 'Success'
INFO | Task 'inc[1]': Starting task run...
INFO | Task 'inc[1]': Finished task run for task with final state: 'Success'
INFO | Task 'inc[2]': Starting task run...
INFO | Task 'inc[2]': Finished task run for task with final state: 'Success'
INFO | Task 'add': Starting task run...
INFO | Task 'add': Finished task run for task with final state: 'Mapped'
INFO | Task 'add[0]': Starting task run...
INFO | Task 'add[0]': Finished task run for task with final state: 'Success'
INFO | Task 'add[1]': Starting task run...
INFO | Task 'add[1]': Finished task run for task with final state: 'Success'
INFO | Task 'add[2]': Starting task run...
INFO | Task 'add[2]': Finished task run for task with final state: 'Success'
INFO | Task 'compute_sum': Starting task run...
INFO | total = 15
INFO | Task 'compute_sum': Finished task run for task with final state: 'Success'
INFO | Flow run SUCCESS: all reference tasks succeeded
```


*The flow source is available on GitHub [here](https://github.com/PrefectHQ/prefect/blob/master/examples/mapping.py).*