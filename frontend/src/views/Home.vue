<template>
  <v-app v-if="!recipeViewVisible">
    <v-app-bar color="green">
      <v-toolbar-title class="text-center flex-grow-1">{{ selection.charAt(0).toUpperCase() + selection.slice(1) }}</v-toolbar-title>
    </v-app-bar>
    <v-main class="mt-6">
      <Fridge v-if="selection === 'fridge'" :db_address="db_address"/>
      <Recipe v-if="selection === 'order'" :db_address="db_address" @switchView="changeViewRecipe"/>
      <About v-if="selection === 'about'"/>
      <BottomNav @navbar="changeView"/>
    </v-main>
  </v-app>
  <RecipeView v-if="recipeViewVisible" :id="selectedRecipe" @switchView="changeViewRecipe"/>
</template>

<script>
import Recipe from '../components/Recipe.vue';
import Fridge from '../components/Fridge.vue';
import About from '../components/About.vue';
import RecipeView from '../components/RecipeView.vue';
import BottomNav from '../components/BottomNav.vue';

export default {
  components: {
    About,
    Recipe,
    Fridge,
    RecipeView,
    BottomNav,
  },
  data() {
    return{
      db_address: "http://localhost:8000",
      selection: "order",
      recipeViewVisible: false,
      selectedRecipe: 0,
    }
  },
  methods: {
    changeViewRecipe(id) {
      this.recipeViewVisible = !this.recipeViewVisible;
      this.selectedRecipe = id;
    },
    changeView(item) {
      this.selection = item;
    },
  }
};
</script>