<template>
  <div id="app">
    <nav class="navbar navbar-expand navbar-dark bg-dark">
      <router-link to="/" class="navbar-brand">MLPX</router-link>
      <div class="navbar-nav mr-auto">
        <li class="nav-item">
          <router-link to="/tutorials" class="nav-link">ML1</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/add" class="nav-link">ML2</router-link>
        </li>
      </div>
    </nav>
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <Predict/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import Predict from './components/Predict.vue'

export default {
  name: 'App',
  components: {
    HelloWorld,
    Predict,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}
</style>
