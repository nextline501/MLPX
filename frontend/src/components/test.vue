<!--<template>
  <v-container>
<form>
          <v-text-field
            v-model="dop"
            placeholder = "DailyOpenPrice..."
            label="DailyOpenPrice"
            required
          ></v-text-field>
          <v-text-field
            v-model="chp"
            placeholder="CurrentHighPrice..."
            label="CurrentHighPrice"
            required
          ></v-text-field>
          <v-text-field
            v-model="clp"
            placeholder="CurrentLowPrice..."
            label="CurrentLowPrice"
            required
          ></v-text-field>
          <v-text-field
            v-model="cv"
            placeholder ="CurrentVolume..."
            label="CurrentVolume"
            required
          ></v-text-field>
<v-btn @click="submit">submit</v-btn>
          <v-btn @click="clear">clear</v-btn>
        </form>
<br/>
        <br/>
<h1 v-if="predictedPrice">Predicted Price is: {{ predictedPrice }}</h1>
 END: IMPORTANT PART! 
  </v-container>
</template>
<script>

import axios from 'axios'
  export default {
     name: 'HelloWorld',
     data: () => ({
       dailyOpenPrice: '',
       currentHighPrice: '',
       currentLowPrice: '',
       currentVolume: '',
       predictedPrice: ''
    }),

    methods: {
    submit () {
      axios.post('http://127.0.0.1:5501/predict', {
        daily_open_price: this.dailyOpenPrice,
        current_high_price: this.currentHighPrice,
        current_low_price: this.currentLowPrice,
        current_volume: this.currentVolume
      })
      .then((response) => {
        this.predictedPrice = response.data.class
      })
    },
    clear () {
      this.dailyOpenPrice = ''
      this.currentHighPrice = ''
      this.currentLowPrice = ''
      this.currentLowPrice = ''
    }
  }
}
</script>-->