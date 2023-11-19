<template>
    <v-container>
        <v-row>
            <v-col cols="12" md="6" lg="4" v-for="recipe in recipes" :key="recipe.id">
                <RecipeCard :imageSrc="recipe.image" :title="recipe.title" :tags="recipe.tags" :servings="recipe.servings" :at_home="recipe.at_home" :id="recipe.id" @switchView="this.$emit('switchView', recipe.id)" />
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import RecipeCard from './RecipeCard.vue';
import axios from 'axios';

export default {
    name: 'Recipe',
    components: {
        RecipeCard,
    },
    data: () => ({
        recipes: [],
        
    }),
    props: {
        db_address: {
            type: String,
            required: true,
        },
    },
    methods: {
        getRecipe() {
            axios.get(this.db_address.toString() + "/recipes")
                .then(response => {
                    this.recipes = response.data;
                })
                .catch(error => {
                    console.log(error);
                });
        }
    },
    mounted() {
        this.getRecipe();
    }
}

</script>
