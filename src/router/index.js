import Vue from "vue";
import VueRouter from "vue-router";
import TaskListView from "../views/TaskListView.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "list",
    component: TaskListView,
  },
  {
    path: "/form",
    name: "form",
    component: () => import("../views/TaskFormView.vue"),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
