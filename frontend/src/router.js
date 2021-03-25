import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      alias: "/HelloWorld",
      name: "Hello",
      component: () => import("./components/HelloWorld")
    },
    {
      path: "/Predict",
      alias: "/Predict",
      name: "Predict",
      component: () => import("./components/Predict")
    },
  ]
});