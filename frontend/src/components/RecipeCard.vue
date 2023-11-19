<template>
    <v-card class="mx-3" max-width="400" color="green">
        <v-card class="mx-1 my-1" max-width="400">
            <v-img class="align-end text-white" height="200" :src="imageSrc" cover @click="this.$emit('switchView')">
                <div class="d-flex justify-end align-end">
                    <v-chip v-if="at_home >= 1" class="ma-2" variant="flat" color="lime" label>{{ at_home }} ingredients at
                        Home</v-chip>
                </div>
            </v-img>
            <v-card-title class="text-subtitle-1">{{ title }}</v-card-title>
            <v-card-text>
                <v-chip v-for="tag in tags" :key="tag" color="blue">{{ tag }}</v-chip>
            </v-card-text>
        </v-card>
        <v-card-actions>
            <v-btn icon @click="decrementSelected">
                <v-icon>mdi-minus</v-icon>
            </v-btn>
            <div class="flex-grow-1 d-flex justify-center">
                <div>
                    <div class="d-flex justify-center">{{ number_selected }} in your Box</div>
                    <div class="d-flex justify-center text-caption">({{ number_selected * servings }} Servings)</div>
                </div>
            </div>
            <v-btn icon @click="incrementSelected">
                <v-icon>mdi-plus</v-icon>
            </v-btn>
        </v-card-actions>
    </v-card>
</template>

<script>

export default {
    name: 'Recipe',
    data: () => ({
        number_selected: 0,
        servings: 2,
    }),
    props: {
        imageSrc: {
            type: String,
            required: true,
        },
        title: {
            type: String,
            required: true,
        },
        tags: {
            type: Array,
            required: true,
        },
        id: {
            type: Number,
            required: true,
        },
        at_home: {
            type: Number,
            required: true,
        },
    },
    methods: {
        incrementSelected() {
            this.number_selected += 1
        },
        decrementSelected() {
            if (this.number_selected > 0)
                this.number_selected -= 1
        },


    }
}

</script>
