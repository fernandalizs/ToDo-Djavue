<template>
  <div>
    <page-bar />
    <v-main class="pt-16 px-16">
      <v-snackbar
        v-model="snackbar.show"
        :value="true"
        color="red"
        timeout="2000"
        absolute
        left
        top
      >
        <h3 style="font-size: 20 px">
          {{ snackbar.message }}
        </h3>
      </v-snackbar>
      <v-form ref="form" v-model="valid" lazy-validation class="px-16">
        <v-text-field
          :rules="[(v) => !!v || 'O campo tarefa é obrigatório']"
          v-model="task.title"
          label="Tarefa"
          name="title"
          required
        ></v-text-field>

        <v-select
          v-model="project"
          :items="items"
          :rules="[(v) => !!v || 'O campo item é obrigatório']"
          label="Projeto"
          name="project"
          required
        ></v-select>

        <v-text-field
          v-model="task.date"
          type="date"
          label="Data"
          name="date"
          required
          :rules="[(v) => !!v || 'O campo data é obrigatório']"
        >
        </v-text-field>

        <v-btn
          :disabled="!valid"
          :loading="loading"
          color="success"
          class="mr-4"
          @click="addTask"
        >
          Salvar
        </v-btn>

        <v-btn color="error" class="mr-4" :to="{ name: 'list' }">
          Cancelar
        </v-btn>
      </v-form>
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
  data: () => ({
    valid: true,
    snackbar: {
      show: false,
      message: "",
    },
    loading: false,
    task: { title: "", date: "" },
    project: null,
    items: ["Estudos", "Trabalho", "Financeiro", "Outros"],
  }),
  methods: {
    addTask() {
      this.loading = true;
      const newTask = {
        title: this.task.title,
        project: this.project,
        date: this.task.date,
      };
      console.log(newTask);
      TaskApi.createTask((newTask) => {
        console.log("iuyftg", newTask);
        this.$router.push({ name: "list" });
      });
      this.loading = false;
    },
  },
};
</script>
