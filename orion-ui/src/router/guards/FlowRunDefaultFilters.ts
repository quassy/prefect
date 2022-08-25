import { Filter, useFiltersStore, RouteGuard, hasFilter, getFlowRun } from '@prefecthq/orion-design'
import { RouteLocationNormalized } from 'vue-router'

export class FlowRunDefaultFilters implements RouteGuard {
  public async before(to: RouteLocationNormalized): Promise<void> {
    const filtersStore = useFiltersStore()

    const { name } = await getFlowRun(to.params.id as string)

    const defaultFilter: Required<Filter> = {
      object: 'flow_run',
      property: 'name',
      type: 'string',
      operation: 'equals',
      value: name!,
    }

    if (!hasFilter(filtersStore.all, defaultFilter)) {
      filtersStore.replaceAll([defaultFilter])
    }
  }
}