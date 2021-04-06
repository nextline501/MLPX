<template>
<div>
  <br>
  <h3>Support Vector Regressor</h3>
  <div v-if="!submitted">
    <button @click="getSvr" class="btn btn-success">Predict</button>
  </div>
  
  <div v-else>
    <h4>{{ predData2 }}</h4>
    <button class="btn btn-success" @click="resetSvr">Reset</button>
  </div>
</div>
</template>

<script>
import DataService from '../services/dataService'

export default {
  name: "Predict",
  data() {
    return {
      predData2: [],
      submitted: false,
    };
  },
  methods: {
    getSvr(){
      DataService.getSvr().then(response => {
        console.log(response);
        this.predData2 = response.data;
        this.submitted = true;
      });
    },
    resetSvr(){
      this.submitted = false;
    }
  }
};

</script>

<style scoped>

</style>