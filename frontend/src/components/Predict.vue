<template>
  <div class="submit-form">
    <div v-if="!submitted">
      <input 
        type="text" 
        placeholder="Daily Open Price..."
        class="form-control"
        id="openPrice"
        required v-model="predModel.openPrice"
        name="openPrice"
      >
      
      <input 
        type="text" 
        placeholder="Current High Price..."
        class= "form-control"
        id = "highPrice"
        required v-model="predModel.highPrice"
        name = "highPrice"
      >

      <input 
        type="text" 
        placeholder="Current Low Price..."
        class = "form-control"
        id="lowPrice"
        required v-model="predModel.lowPrice"
        name = "lowPrice"
      >

      <input 
        type="text" 
        placeholder="Current Volume..."
        class= "form-control"
        id = "vol"
        required v-model="predModel.vol"
        name = "vol"
      >
      
      <button @click="getPredPrice" class="btn btn-success">Predict Price</button>
    </div>

    <div v-else>
      <h4>{{ predData }}</h4>
      <button class="btn btn-success" @click="newPred">Reset</button>
    </div>
  </div>
</template>

<script>
import DataService from "../services/dataService";

export default {
  name: "Predict",
  data() {
    return {
      predData: [],
      predModel: {
        openPrice: "",
        highPrice: "",
        lowPrice: "",
        vol: "",
      },
      submitted: false
    };
  },
  methods: {
    getPredPrice() {
      let data = {
        openPrice: this.predModel.openPrice,
        highPrice: this.predModel.highPrice,
        lowPrice: this.predModel.lowPrice,
        vol: this.predModel.vol
      }
      
      DataService.sendData(data).then(response => {
        console.log(response)
      }).then(response => {
        DataService.getPred().then(response => {
        this.predData = response.data;
        console.log(this.predData)
        this.showPrice();
      });
        console.log(response)
      })
      .catch(e => {
        console.log(e)
      });
    },

    showPrice() {
      this.submitted = true;
    },

    newPred() {
      this.submitted = false;
      this.tutorial = {};
    }
  }
};
</script>

<style>
.submit-form {
  max-width: 300px;
  margin: auto;
}
</style>



