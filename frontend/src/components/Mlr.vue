<template>
  <div class="submit-form">
    <h3>Multiple Linear Regression</h3>
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
      
      <button v-if= "!showSpinner"  id="MlrPred" @click="getPredPrice" class="btn btn-success">Predict Price</button>

     <button v-else class="btn btn-success" id="MlrPred" type="button" disabled>
        <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
        Loading...
      </button>

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
  name: "Mlr",
  data() {
    return {
      predData: [],
      predModel: {
        openPrice: "",
        highPrice: "",
        lowPrice: "",
        vol: "",
      },
      submitted: false,
      showSpinner: false
    };
  },
  methods: {
    getPredPrice() {
      this.showSpinner = true
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
      this.showSpinner = false;
      this.submitted = false;
    }
  }
};
</script>

<style>

body {

background-color: rgb(243, 243, 243)

}

.submit-form {
  max-width: 300px;
  margin: auto;
  margin-top: 50px;
  margin-bottom: 20px;
}


#MlrPred{
  margin-top:20px
}

h3{
  font-size: 25px;
}
.btn-success, .btn-success:hover, .btn-success:active, .btn-success:visited {
    background-color: darkblue !important;
}
footer{
  text-align: center;
  background-color: #343a40;
  color: white;
  position: fixed;
  left: 0;
  bottom: 0;
  width: 100%;

}

</style>