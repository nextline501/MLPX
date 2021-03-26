<template>
  <div class="submit-form">
    <div v-if="!submitted">
      <button @click="getPredPrice" class="btn btn-success">Predict Price</button>
    </div>

    <div v-else>
      <h4>{{ predData }}</h4>
      <button class="btn btn-success" @click="newPred">Cool</button>
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
      submitted: false
    };
  },
  methods: {
    getPredPrice() {
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