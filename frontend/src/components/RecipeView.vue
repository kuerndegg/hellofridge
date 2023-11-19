<template>
    <v-card class="w-100 h-100 rounded-0">
        <v-toolbar color="green">
            <v-btn icon @click="this.$emit('switchView', null)">
                <v-icon>mdi-arrow-left</v-icon>
            </v-btn>

            <v-toolbar-title>Recipe Overview</v-toolbar-title>

            <v-btn icon>
                <v-icon>mdi-dots-vertical</v-icon>
            </v-btn>
        </v-toolbar>
        <v-img class="align-end text-white" height="200" :src="recipe.image" cover>
        </v-img>
        <v-card-title class="text-h5">{{ recipe.title }}</v-card-title>
        <v-card-text>
            <v-divider></v-divider>

            <p class="text-subtitle-2">Category:</p>
            <p class="text-body-2">{{ recipe.tags.join(', ') }}</p>

            <v-divider class="my-2"></v-divider>
            <span class="text-h6">Ingredients</span>
            <v-list>
                <v-list-item-group>
                    <v-list-item v-for="ingredient in recipe.ingredients" :key="ingredient.item">
                        <v-list-item-content>
                            <v-list-item-title>
                                {{ ingredient.item }}
                                <v-chip v-if="store.getSelectedIngredients.includes(ingredient.item)" color="lime"
                                    class="justify-end">
                                    <v-icon>mdi-check</v-icon>
                                </v-chip>
                            </v-list-item-title>
                            <v-list-item-subtitle>{{ ingredient.amount }}</v-list-item-subtitle>
                        </v-list-item-content>
                    </v-list-item>
                </v-list-item-group>
            </v-list>

            <v-divider class="my-2"></v-divider>

            <span class="text-h6">Steps</span>
            <v-list>
                <v-list-item-group>
                    <v-list-item v-for="step in recipe.steps" :key="step">
                        <v-list-item-content>
                            <v-card>
                                {{ step }}
                            </v-card>
                        </v-list-item-content>
                    </v-list-item>
                </v-list-item-group>
            </v-list>


        </v-card-text>
    </v-card>
</template>

<script>
import axios from 'axios';
import { useAppStore } from '@/store/app';

export default {
    name: 'Recipe',
    data: () => ({
        at_home: 1,
        number_selected: 0,
        servings: 2,
        imageSrc: "https://images.unsplash.com/photo-1581093458791-9d8a1e3b1e6f?ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8c2V0dGluZ3MlMjB3aXRoJTIwZnJpZGF5JTIwY2FyZCUyMHN0b3JlZCUyMHNlcnZpbmd8ZW58MHx8MHx8&ixlib=rb-1.2.1&w=1000&q=80",
        recipe: {
            title: "Loading...",
            tags: [],
            image: "https://images.unsplash.com/photo-1581093458791-9d8a1e3b1e6f?ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8c2V0dGluZ3MlMjB3aXRoJTIwZnJpZGF5JTIwY2FyZCUyMHN0b3JlZCUyMHNlcnZpbmd8ZW58MHx8MHx8&ixlib=rb-1.2.1&w=1000&q=80",
        }
    }),
    props: {
        id: {
            type: Number,
            required: true
        }
    },
    methods: {
        incrementSelected() {
            this.number_selected += 1
        },
        decrementSelected() {
            if (this.number_selected > 0)
                this.number_selected -= 1
        },
        getRecipe() {
            axios.get('http://localhost:8000/recipe/' + this.id + '/')
                .then(response => {
                    console.log(response)
                    this.recipe = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        },

    },
    mounted() {
        this.getRecipe();
    },
    setup() {
        const store = useAppStore()
        return { store }
    }
}

</script>
