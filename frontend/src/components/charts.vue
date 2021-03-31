<template>
  <canvas id="myChart"></canvas>
</template>

<script>
// To install chart.js run: npm install chart.js --save
// and do not forget to import it in the component thats gonna use charts.
import Chart from "chart.js";

export default {
  data() {
    return {
      canvas: "",
      chart: "",
      data: [10, 36, 25, 41]
    };
  },

  // Rendering chart in mounted hook so we can see it as soon as component is created
  mounted() {

    // 
    let canvas = document.getElementById("myChart");
    let ctx = canvas.getContext("2d");
    this.canvas = ctx;
    this.createChart()
    this.addChartData('Purple', 32, 'purple')
    this.addLineChart(this.data)
  },

  methods: {
    createChart() {
       this.chart = new Chart(this.canvas, {
        // The type of chart we want to create
        type: "line",

        // The data for our dataset
        data: {
          labels: [
            "Red",
            "Blue",
            "Green",
          ],
          datasets: [
            {
              label: "Dataset",
              backgroundColor: ['red', 'blue', 'green'],
              borderWidth: 2,
              borderColor: [],
              data: [30, 15, 20 ],
              order: 0
            },
          ],
        },
        // Configuration options go here
        options: {
          onClick(e){
            // console.log(this.chart.getElementAtEvent(e))
            let point = this.chart.getElementAtEvent(e)[0]
            // console.log(point)
            if(point){
              let label = this.chart.data.labels[point._index]
              let value = this.chart.data.datasets[point._datasetIndex].data[point._index]
              console.log(label, value)
            }
          }
        },
      });
    },

    addChartData(label, data, color ){
      let chartDataset = this.chart.data.datasets[0]

      this.chart.data.labels.push(label)
      chartDataset.data.push(data)
      chartDataset.backgroundColor.push(color)
      chartDataset.borderColor = 'black'

      this.chart.update()
    },

    addLineChart(data){
      this.chart.data.datasets.push({
        label: 'Line Dataset',
        data,
        type: 'line',
        backgroundColor: 'blue',
        borderColor: 'orange',
        order: 1
      })

      // console.log(this.chart.data.datasets[1])
      // We need to update chart after changes
      this.chart.update()
    }
  },
};
</script>
<style scoped>
#myChart {
  max-width: 800px;
  max-height: 800px;
}
</style>