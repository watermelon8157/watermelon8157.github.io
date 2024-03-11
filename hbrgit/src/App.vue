<script setup lang="ts">
import { ref } from "vue";
import charactersJson from "@/assets/charactersCard/characters.json";
const characters = ref(charactersJson);
</script>

<template>
  <template v-for="Wife in characters" :key="'Wife' + Wife.id">
    <template v-for="WifeCards in Wife.cards" :key="'WifeCards' + WifeCards.id">
      <img :src="'charactersCard/'+ WifeCards.image" />
    </template>
  </template>
</template>
