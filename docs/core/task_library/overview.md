# Overview

The Prefect task library is a constantly growing list of pre-defined tasks that provide off-the-shelf
functionality for working with a wide range of tools anywhere from shell script execution to kubernetes
job management to sending tweets. A majority of the task library is community supported and thus opens
the door for users who want to contribute tasks for working with any number of tools. Tasks in the task
library are created with a specific goal in mind such as creating a Kubernetes job with
[`CreateNamespacedJob`](/api-ref/latest/tasks/kubernetes/#createnamespacedjob) or invoking an AWS lambda
function with [`LambdaInvoke`](/api-ref/latest/tasks/aws/#lambdainvoke).

Below is a table showcasing some of the tasks that have been contributed to the task library for
interfacing with varying tools and services that users have deemed useful. For a full list of tasks in
the library and more information on how to use them visit the API [reference documentation](/api-ref/latest)
for the `prefect.tasks` module.

Tasks marked with the <Badge text="Verified" type="success" vertical="middle"></Badge> badge have been reviewed and approved by Prefect.

<ClientOnly>
<table>
  <tr>
    <td><Badge text="Verified" type="success"></Badge><img src="/img/logos/airbyte.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/airbyte/">Airbyte</a></td>
    <td><img src="/img/logos/airtable.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/airtable/">Airtable</a></td>
    <td><img src="/img/logos/asana_logo.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/asana/">Asana</a></td>
    <td><img src="/img/logos/aws.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/aws/">AWS</a></td>
    <td><img src="/img/logos/azure.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/azure/">Azure</a></td>
  </tr>
  <tr>
    <td><img src="/img/logos/azure_ml.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/azureml/">Azure ML</a></td>
    <td><Badge text="Verified" type="success"></Badge><img src="/img/logos/census.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/census/">Census</a></td>
    <td><img src="/img/logos/cubejs.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/cubejs/">CubeJS</a></td>
    <td><Badge text="Verified" type="success"></Badge><img src="/img/logos/databricks.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/databricks/">Databricks</a></td>
    <td><Badge text="Verified" type="success"></Badge><img src="/img/logos/dbt.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/dbt/">dbt</a></td>
  </tr>
  <tr>
    <td><img src="/img/logos/docker.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/docker/">Docker</a></td>
    <td><img src="/img/logos/dremio.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/dremio/">Dremio</a></td>
    <td><img src="/img/logos/dropbox.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/dropbox/">Dropbox</a></td>
    <td><img src="/img/logos/email.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/notifications/#emailtask">Email</a></td>
    <td><Badge text="Verified" type="success"></Badge><img src="/img/logos/firebolt.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/firebolt/">Firebolt</a></td>
  </tr>
  <tr>
    <td><Badge text="Verified" type="success"></Badge><img src="/img/logos/fivetran.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/fivetran/">Fivetran</a></td>
    <td><img src="/img/logos/github.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/github/">GitHub</a></td>
    <td><Badge text="Verified" type="success"></Badge><img src="/img/logos/google_cloud.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/gcp/">Google Cloud</a></td>
    <td><img src="/img/logos/sheets.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/gsheets/">Google Sheets</a></td>
    <td><Badge text="Verified" type="success"></Badge><img src="/img/logos/ge.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/great_expectations/">Great Expectations</a></td>
  </tr>
  <tr>
    <td><img src="/img/logos/jira.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/jira/">Jira</a></td>
    <td><img src="/img/logos/jupyter.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/jupyter/">Jupyter</a></td>
    <td><img src="/img/logos/kubernetes.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/kubernetes/">Kubernetes</a></td>
    <td><img src="/img/logos/mixpanel.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/mixpanel/">Mixpanel</a></td>
    <td><img src="/img/logos/monday.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/monday/">Monday</a></td>
  </tr>
  <tr>
    <td><Badge text="Verified" type="success"></Badge><img src="/img/logos/monte_carlo.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/monte_carlo/">Monte Carlo</a></td>
    <td><img src="/img/logos/mysql.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/mysql/">MySQL</a></td>
    <td><img src="/img/logos/postgres.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/postgres/">PostgreSQL</a></td>
    <td><img src="/img/logos/prometheus.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/prometheus/">Prometheus</a></td>
    <td><img src="/img/logos/pushbullet.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/notifications/#pushbullettask">Pushbullet</a></td>
  </tr>
  <tr>
    <td><img src="/img/logos/python.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/function/">Python</a></td>
    <td><img src="/img/logos/redis.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/redis/">Redis</a></td>
    <td><img src="/img/logos/rlogo.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/rss/">RSS</a></td>
    <td><img src="/img/logos/sendgrid.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/sendgrid/">SendGrid</a></td>
    <td><img src="/img/logos/shell.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/shell/">Shell</a></td>
  </tr>
  <tr>
    <td><img src="/img/logos/slack.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/notifications/#slacktask">Slack</a></td>
    <td><Badge text="Verified" type="success"></Badge><img src="/img/logos/snowflake.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/snowflake/">Snowflake</a></td>
    <td><img src="/img/logos/spacy.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/spacy/">spaCy</a></td>
    <td><img src="/img/logos/sqlserverlogo.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/sql_server/">SQL Server</a></td>
    <td><Badge text="Verified" type="success"></Badge><img src="/img/logos/sqlite.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/sqlite/">SQLite</a></td>
  </tr>
  <tr>
    <td><Badge text="Verified" type="success"></Badge><img src="/img/logos/transform.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/transform/">Transform</a></td>
    <td><img src="/img/logos/trello.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/trello/">Trello</a></td>
    <td><img src="/img/logos/tlogo.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/twitter/">Twitter</a></td>
    <td><img src="/img/logos/zendesk.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://docs-v1.prefect.io/api-ref/latest/tasks/zendesk/">Zendesk</a></td>
    <td></td>
  </tr>
</table>
</ClientOnly>

## Task library in action

Just like any other Prefect [task](/core/concepts/tasks.html), tasks in the task library can be
used by importing and adding them to your flow.

Functional API:

```python
from prefect import task, Flow
from prefect.tasks.shell import ShellTask

ls_task = ShellTask(command="ls", return_all=True)

@task
def show_output(std_out):
    print(std_out)

with Flow("list_files") as flow:
    ls = ls_task()
    show_output(ls)
```

Imperative API:

```python
from prefect import Task, Flow
from prefect.tasks.shell import ShellTask

class ShowOutput(Task):
    def run(self, std_out):
        print(std_out)

ls_task = ShellTask(command="ls", return_all=True)
show_output = ShowOutput()

flow = Flow("list_files")
show_output.set_upstream(ls_task, key="std_out", flow=flow)
```


Keyword arguments for tasks imported from the task library can either be set at initialization for reuse
purposed or optionally set and overwritten when defining the flow.

Functional API:

```python
from prefect import task, Flow
from prefect.tasks.shell import ShellTask

# Will only return the listed files
ls_task = ShellTask(command="ls", return_all=True)

@task
def show_output(std_out):
    print(std_out)

with Flow("count_files") as flow:
    ls = ls_task()
    show_output(ls)

    # Override command to count listed files
    ls_count = ls_task(command="ls | wc -l")
    show_output(ls_count)
```

Imperative API:

```python
from prefect import Task, Flow
from prefect.tasks.shell import ShellTask

class ShowOutput(Task):
    def run(self, std_out):
        print(std_out)

ls_task = ShellTask(command="ls", return_all=True)
show_output = ShowOutput()

ls_count = ShellTask(command="ls | wc -l", return_all=True)
show_output2 = ShowOutput()

flow = Flow("count_files")
show_output.set_upstream(ls_task, key="std_out", flow=flow)
show_output2.set_upstream(ls_count, key="std_out", flow=flow)
```


For more information on the tasks available for use in the task library visit the API
[reference documentation](/api-ref/latest) for the `prefect.tasks` and if you are interested in contributing to the task library visit the [contributing page](/core/task_library/contributing/)!
