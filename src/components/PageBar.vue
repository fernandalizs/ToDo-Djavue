<template>
  <div>
    <v-app-bar fixed color="#448AFF" elevate-on-scroll>
      <v-app-bar-nav-icon
        color="white"
        class="#448AFF"
        @click.stop="drawer = !drawer"
      >
      </v-app-bar-nav-icon>

      <v-toolbar-title class="white--text">ToDo List</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon color="white">mdi-magnify</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon v-model="this.$vuetify.theme.dark" color="white"
          >mdi-brightness-4</v-icon
        >
      </v-btn>

      <v-btn icon>
        <v-icon color="white">mdi-logout</v-icon>
      </v-btn>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" app temporary>
      <v-list-item>
        <v-list-item-avatar>
          <v-avatar color="#536DFE">
            <span class="white--text text-h5"></span>
          </v-avatar>
        </v-list-item-avatar>

        <v-list-item-content>
          <v-list-item-title></v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list dense>
        <v-list-item
          v-for="item in items"
          :key="item.title"
          link
          :to="{ name: item.routes }"
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>
<script>
export default {
  data() {
    return {
      drawer: false,
      theme: { dark: false },
      items: [
        { title: "Home", icon: "mdi-home", routes: "list" },
        // { title: "Resumo", icon: "mdi-view-dashboard", routes: "info" },
        // {
        //   title: "Adicionar Projeto",
        //   icon: "mdi-folder-plus",
        //   routes: "projectForm",
        // },
        {
          title: "Tarefas",
          icon: "mdi-format-list-checkbox",
          routes: "list",
        },
        {
          title: "Adicionar Tarefa",
          icon: "mdi-playlist-plus",
          routes: "form",
        },
      ],
    };
  },
  methods: {
    logout() {
      localStorage.clear();
      this.$router.push({ name: "home" });
    },
  },
  computed: {
    getLoggedUser() {
      const userStr = localStorage.getItem("user");
      const user = JSON.parse(userStr);
      return user;
    },
  },
};
</script>
