<template>
    <div>
        <vue-aspect-ratio ar="16:9" width="90%">
            <v-chart 
                :init-options="init"
                :options="makePlot(data)" 
                :theme="theme" 
                style="width: 100%; height: 100%" 
                :autoresize="true"
                />
        </vue-aspect-ratio>
    </div>
</template>

<script>

export default {
    name: "StatBar",
    data () {
        return {
            init: {renderer: 'svg'}
        }
    },
    props: {
        theme: { type: String, default: "shine" },
        data: { required: true },
        yTitle: { type: String, default: "" },
        name: { type: String, default: "stats" },
    },
    methods: {
        makePlot (data) {
            let legendData = [];
            let xAxis = [];
            let values = [];
            for (let val of data) {
                legendData.push(val.tissue)
                xAxis.push(val.tissue)
                values.push(val.num);
            }

            return {
                toolbox: {
                    show: true,
                    orient: 'vertical',
                    left: 'right',
                    top: 'center',
                    feature: {
                        mark: {show: true},
                        dataView: {
                            show: true, readOnly: false,  title: "show data",
                            lang: ["Data view", "Close", "Refresh"]
                        },
                        magicType: {
                            show: true,
                            type: ['line', 'bar', 'stack', 'tiled'],
                            title: {
                                line: "switch to line plot",
                                bar: "switch to bar plot",
                                stack: "switch to stacked bar plot",
                                tiled: "switch tiled plot"
                            }
                        },
                        restore: {show: true, title: "restore"},
                        saveAsImage: {show: true, title: "save svg", type: "svg", name: this.$props.name}
                    }
                },
                tooltip : {
                    trigger: 'axis',
                    axisPointer : {            // 坐标轴指示器，坐标轴触发有效
                        type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                    }
                },
                grid: {
                    left: '5%',
                    top: '15%',
                    right: '5%',
                    bottom: '0%',
                    containLabel: true
                },
                yAxis:  {
                    type: 'value',
                    name: this.$props.yTitle,
                    nameGap: 30, nameLocation: "middle",
                    nameTextStyle: { fontSize: 16 },
                },
                dataZoom: [
                    {
                        show: true
                    }, 
                    {
                        show: true
                    }
                ],
                xAxis: {
                    type: 'category',
                    axisLabel: {rotate: 90},
                    data: xAxis
                },
                series: {
                    data: values,
                    type: "bar"
                },
            }
        }
    }
}
</script>

<style scoped>
</style>
