<template>
    <v-container>
        <v-row justify="space-between" class="mx-5">
            <v-btn v-for="category in categories" :key="category.name" round :color="getButtonColor(category)" icon @click="toggle(category)">
                <v-icon color="green">{{ category.icon }}</v-icon>
            </v-btn>
        </v-row>
        <v-row>
            <v-col cols="3" v-for="ingredient in filteredIngredients" :key="ingredient.name"
                class="d-flex justify-center">
                <IngredientCard :imageSrc="ingredient.image" :name="ingredient.name" @toggle="addToSelected" />
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import IngredientCard from './IngredientCard.vue';
import axios from 'axios';

export default {
    components: {
        IngredientCard,
    },
    data() {
        return {
            categories: [
                { name: 'Vegetables', icon: 'mdi-carrot' },
                { name: 'Proteins', icon: 'mdi-food-drumstick' },
                { name: 'Grains and Starches', icon: 'mdi-barley' },
                { name: 'Dairy', icon: 'mdi-cheese' },
                { name: 'Condiments', icon: 'mdi-shaker' }
            ],
            ingredients: [
                { name: "balsamic-vinegar", imageSrc: this.db_address.toString() + "/images/balsamic-vinegar.png" },
            ],
            selectedCategory: { name: 'Vegetables', icon: 'mdi-carrot' },
            filteredIngredients: [],
        }
    },
    props: {
        db_address: {
            type: String,
            required: true,
        },
    },
    methods: {
        toggle(category) {
            this.selectedCategory = category;
            this.filterIngredients();
        },
        getIngredients() {
            axios.get(this.db_address.toString() + "/ingredients")
                .then(response => {
                    this.ingredients = response.data;
                    this.filterIngredients();
                })
                .catch(error => {
                    console.log(error);
                });
        },
        filterIngredients() {
            if (!this.selectedCategory) {
                this.filteredIngredients = this.ingredients;
                return;
            }
            this.filteredIngredients = this.ingredients.filter(ingredient => ingredient.category === this.selectedCategory.name);
        },
        getButtonColor(category) {
            return this.selectedCategory.name === category.name ? 'light_green' : 'white';
        },
        addToSelected(name, isSelected) {

        }
    },
    mounted() {
        this.getIngredients();
    },
}
</script>

<style>
/* Add your custom styles here */
</style>
