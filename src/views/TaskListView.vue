<template>
  <div>
    <page-bar />
    <v-main class="overflow-hidden mt-4 pt-16">
      <v-container>
        <v-row>
          <v-col class="pa-1" cols="12" v-for="task in tasks" :key="task.id">
            <v-card>
              <v-card-text>
                <div>{{ task.id }}</div>
                <p class="ma-0 pa-0 text-h5 text--primary">{{ task.title }}</p>
                <div class="d-flex justify-space-between">
                  <p>{{ task.project }}</p>
                  <p>{{ task.date }}</p>
                </div>
              </v-card-text>
              <v-card-actions>
                <v-list-item class="grow">
                  <v-row align="center" justify="end">
                    <v-btn
                      x-small
                      icon
                      color="blue"
                      :to="{ name: 'form', params: { id: task.id } }"
                      ><v-icon>fas fa-pen fa-xs</v-icon></v-btn
                    >
                    <v-btn x-small icon color="red" @click="deleteTask(task.id)"
                      ><v-icon>far fa-trash-alt fa-xs</v-icon></v-btn
                    >
                  </v-row>
                </v-list-item>
              </v-card-actions>
            </v-card>
          </v-col>
          <div class="my-2">
            <v-btn color="#2979FF" fab dark :to="{ name: 'form' }">
              <v-icon>mdi-plus</v-icon>
            </v-btn>
          </div>
        </v-row>
      </v-container>
    </v-main>
    <page-footer />
  </div>
</template>

<script>
import PageBar from "@/components/PageBar.vue";
import PageFooter from "@/components/PageFooter.vue";
import TaskApi from "@/TaskApi.js";

export default {
  components: { PageBar, PageFooter },
  data() {
    return {
      tasks: [],
    };
  },
  methods: {
    taskList() {
      TaskApi.getTasks((data) => {
        this.tasks = data;
      });
    },
    // deleteTasks() {
    //   TaskApi.deleteTask(taskID, () => {
    //     this.taskList();
    //   });
    // },
  },
  created() {
    this.taskList();
  },
};
</script>
