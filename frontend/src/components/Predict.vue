<template>
  <div class="submit-form">
    <div v-if="!submitted">
      <input 
        type="text" 
        placeholder="Daily Open Price..."
        class="form-control"
        id="openPrice"
        required v-model="predictModel.openPrice"
        name="openPrice"
      >
      
      <input 
        type="text" 
        placeholder="Current High Price..."
        class= "form-control"
        id = "highPrice"
        required v-model="predictModel.highPrice"
        name = "highPrice"
      >

      <input 
        type="text" 
        placeholder="Current Low Price..."
        class = "form-control"
        id="lowPrice"
        required v-model="predictModel.lowPrice"
        name = "lowPrice"
      >

      <input 
        type="text" 
        placeholder="Current Volume..."
        class= "form-control"
        id = "vol"
        required v-model="predictModel.vol"
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
      predictModel: {
        id: null,
        openPrice: "",
        highPrice: "",
        lowPrice: "",
        vol: "",
        published: false
      },
      submitted: false
    };
  },
  methods: {
    postSendData(){
      let data = {
        openPrice: this.predictModel.openPrice,
        highPrice: this.predictModel.highPrice,
        lowPrice: this.predictModel.lowPrice,
        vol: this.predictModel.vol
      }

      DataService.sendData(data).then(response => {
        console.log(response.data)
      })
    },

    getPredPrice() {
      this.postSendData();
      
      DataService.getPred().then(response => {
        this.predData= response.data;
        console.log(this.predData)
        this.showPrice();
      })
      .catch(e => {
        console.log(e);
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



