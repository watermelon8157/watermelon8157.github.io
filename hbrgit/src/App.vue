<script setup lang="ts">
import { ref } from "vue";
const imageSrc = ref("https://hbr.quest/hbr/RKayamoriSwim2022_R2_Thumbnail.webp");
</script>

<template>
  <img :src="imageSrc" />
</template>
