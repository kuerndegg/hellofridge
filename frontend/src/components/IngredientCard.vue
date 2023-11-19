<template>
  <v-container>
    <v-row>
      <v-col cols="auto" class="d-flex justify-center">
        <div class="selectable-image" @click="toggle">
          <v-avatar size="65" class="elevation-6">
            <v-img :src="imageSrc" height="100%" width="100%" class="rounded-circle" :alt="name"></v-img>
          </v-avatar>
          <v-sheet v-if="isSelected" class="checkmark" color="green" shaped>
            <v-icon size="15">mdi-check</v-icon>
          </v-sheet>
          <v-sheet v-else class="checkmark" color="white" shaped>
            <v-icon size="15">mdi-check</v-icon>
          </v-sheet>
        </div>
      </v-col>
    </v-row>
    <span class="text-caption text-center d-flex justify-center" style="max-width: 65px; max-height: 5px;">
      {{ name }}
    </span>
  </v-container>
</template>
  
<script>
import { useAppStore } from '@/store/app';

export default {
  data() {
    return {
      isSelected: false,
    };
  },
  props: {
    imageSrc: {
      type: String,
      required: true,
    },
    name: {
      type: String,
      required: true,
    },
  },
  methods: {
    toggle() {
      this.isSelected = !this.isSelected;
      this.$emit('toggle', this.name, this.isSelected);
    },
  },
  mounted() {
    const store = useAppStore();
    this.isSelected = store.getSelectedIngredients.includes(this.name);
  },

  setup() {
        const store = useAppStore()
        return { store }
    }
};
</script>
  
<style scoped>
.selectable-image {
  position: relative;
  cursor: pointer;
  display: inline-block;
}

.v-avatar {
  border: 2px solid white;
  /* Adds white border to avatar */
  box-shadow: 0 0 0 2px #44C767;
  /* Green border around the avatar */
}

.checkmark {
  position: absolute;
  display: flex;
  align-items: center;
  justify-content: center;
  bottom: 0px;
  right: 0px;
  border-radius: 50%;
  height: 20px;
  width: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  /* Optional: add shadow for better visibility */
}
</style>
  