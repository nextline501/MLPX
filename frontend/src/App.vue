<template>
  <div id="app">
    <nav class="navbar navbar-expand navbar-dark bg-dark">
      <router-link to="/" class="navbar-brand">Home</router-link>
      <div class="navbar-nav mr-auto">
        <li class="nav-item">
          <router-link to="/Mlr" class="nav-link">MLR</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/Svr" class="nav-link">SVR</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/Charts" class="nav-link">Statistics</router-link>
        </li>
      </div>
    </nav>
     <HelloWorld msg="Apple Stock Predictor"/>
    <router-view/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld,
  }
}

</script>

<style >
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #8b8b8b;
  margin-top: 0px;
}
</style>
