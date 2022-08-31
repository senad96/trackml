// visualizationType: 'box', // 'box', 'sequence'
import * as React from 'react';

import { IQueryFormProps, IUIConfig } from 'modules/BaseExplorer/types';
import {
  Grouping,
  QueryForm,
  Visualizer,
} from 'modules/BaseExplorer/components';
import Controls from 'modules/BaseExplorer/components/Controls';

import LineChart from 'components/LineChart/LineChart';
import { HighlightEnum } from 'components/HighlightModesPopover/HighlightModesPopover';

import COLORS from 'config/colors/colors';

import { AlignmentOptionsEnum, CurveEnum, ScaleEnum } from 'utils/d3';
import { filterMetricsData } from 'utils/filterMetricData';

const ui: IUIConfig = {
  defaultBoxConfig: {
    width: 400,
    height: 400,
    gap: 0,
  },
  components: {
    queryForm: React.memo((props: IQueryFormProps) => (
      <QueryForm engine={props.engine} hasAdvancedMode />
    )),
    visualizations: [Visualizer],
    grouping: Grouping,
    box: function CustomeMetricVisualizer(props: any) {
      let data = props.allItems.map((item: any, i: number) => {
        let line = item.data;
        const { values, steps } = filterMetricsData(
          line,
          AlignmentOptionsEnum.STEP,
        );
        return {
          key: item.key,
          data: {
            xValues: steps,
            yValues: values,
          },
          color: COLORS[0][i % COLORS[0].length],
          dasharray: 'none',
          selectors: [item.key],
        };
      });

      return (
        <div
          style={{
            width: 'calc(100% - 2px)',
            height: '100%',
            position: 'relative',
          }}
        >
          <LineChart
            data={data}
            index={0}
            axesScaleType={{
              xAxis: ScaleEnum.Linear,
              yAxis: ScaleEnum.Linear,
            }}
            ignoreOutliers={false}
            highlightMode={HighlightEnum.Off}
            curveInterpolation={CurveEnum.Linear}
          />
        </div>
      );
    },
    controls: Controls,
  },
};

export default ui;
