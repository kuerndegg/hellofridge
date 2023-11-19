<template>
    <v-bottom-navigation active color="lime">
        <v-btn @click="navbarSelect('fridge')">
            <v-icon>mdi-fridge</v-icon>

            Supplies
        </v-btn>

        <v-btn @click="navbarSelect('order')">
            <v-icon>mdi-silverware-fork-knife</v-icon>

            Order
        </v-btn>

        <v-btn @click="navbarSelect('about')">
            <v-icon>mdi-information</v-icon>

            About
        </v-btn>
    </v-bottom-navigation>
</template>

<script>
export default {
    data: () => ({
        at_home: 1,
    }),
    methods: {
        navbarSelect(item) {
            this.$emit('navbar', item)
        },
    },
}

</script>
