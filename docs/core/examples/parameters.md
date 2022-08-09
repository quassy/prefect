---
editLink: false
---


# Parameters

A `Parameter` is a special type of `Task` representing an input that can vary
per flow run. For example:

```python
x = Parameter("x", default=1)
```

Parameters have a name (`"x"` in this case), and may optionally include a
default value. Parameters lacking a default value require an explicit value be
configured for each flow run. Parameters with a default value may use the
default, or optionally provide a different value at runtime. Parameters can be
specified through the UI or CLI when running with Prefect Cloud/Server (see
[here](/orchestration/tutorial/parameters/)) or through the `parameters`
kwarg when running locally with `flow.run`.

For more information, see the [Parameter docs](/core/concepts/parameters/).


!!! tip "Registering with Prefect Cloud or Server"
    This example can be registered in Prefect Cloud or Server by running:

    ```
    prefect register --json https://docs.prefect.io/examples.json \
        --name 'Example: Mapping' \
        --project 'Prefect Examples'
    ```

    (To register in a different project, replace `'Prefect Examples'` with your project name).

```python
from prefect import Flow, Parameter, task


@task(log_stdout=True)
def print_total(x, y, total):
    print(f"{x} + {y} = {total}")


with Flow("Example: Parameters") as flow:
    x = Parameter("x", default=1)
    y = Parameter("y", default=2)

    print_total(x, y, x + y)

if __name__ == "__main__":
    # When running a flow where all parameters have default values
    # no parameters need to be specified at runtime.
    print("Running with default values")
    flow.run()

    # One or more parameters can be specified at runtime through the use of the
    # `parameters` argument. Here we set `x` to 8 and `y` to 9.
    print("\nRunning with `x = 8` and `y = 9`")
    flow.run(parameters={"x": 8, "y": 9})
```

Output:

```bash
$ python examples/parameters.py
Running with default values
INFO | Beginning Flow run for 'Example: Parameters'
INFO | Task 'x': Starting task run...
INFO | Task 'x': Finished task run for task with final state: 'Success'
INFO | Task 'y': Starting task run...
INFO | Task 'y': Finished task run for task with final state: 'Success'
INFO | Task 'Add': Starting task run...
INFO | Task 'Add': Finished task run for task with final state: 'Success'
INFO | Task 'print_total': Starting task run...
INFO | 1 + 2 = 3
INFO | Task 'print_total': Finished task run for task with final state: 'Success'
INFO | Flow run SUCCESS: all reference tasks succeeded

Running with `x = 8` and `y = 9`
INFO | Beginning Flow run for 'Example: Parameters'
INFO | Task 'x': Starting task run...
INFO | Task 'x': Finished task run for task with final state: 'Success'
INFO | Task 'y': Starting task run...
INFO | Task 'y': Finished task run for task with final state: 'Success'
INFO | Task 'Add': Starting task run...
INFO | Task 'Add': Finished task run for task with final state: 'Success'
INFO | Task 'print_total': Starting task run...
INFO | 8 + 9 = 17
INFO | Task 'print_total': Finished task run for task with final state: 'Success'
INFO | Flow run SUCCESS: all reference tasks succeeded
```

*The flow source is available on GitHub [here](https://github.com/PrefectHQ/prefect/blob/master/examples/parameters.py).*