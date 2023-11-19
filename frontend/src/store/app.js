import { defineStore } from 'pinia';

export const useAppStore = defineStore('app',{

  state: () => {
    if (sessionStorage.getItem("selectedIngredients")){
      return {
        selectedIngredients: JSON.parse(sessionStorage.getItem("selectedIngredients")),
      };
    } else {
      return {
        selectedIngredients: [],
      };
    }
  },

  getters: {
    getSelectedIngredients: (state) =>  state.selectedIngredients,
  },

  actions: {
    addIngredient(ingredient) {
      this.selectedIngredients.push(ingredient);
      sessionStorage.setItem('selectedIngredients', JSON.stringify(this.selectedIngredients));
    },

    removeIngredient(ingredient) {
      this.selectedIngredients.splice(this.selectedIngredients.indexOf(ingredient), 1);
      sessionStorage.setItem('selectedIngredients', JSON.stringify(this.selectedIngredients));
    },
    clearIngredients() {
      this.selectedIngredients = [];
      sessionStorage.clear();
    }
  },
  
});
