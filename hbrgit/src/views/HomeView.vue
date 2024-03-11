<script setup lang="ts">
import { ref, computed, onMounted } from "vue";
import charactersJson from "@/assets/charactersCard/characters.json";
import { findIndex } from "lodash-es";

const Iimgpath = ref("/src/assets/charactersCard/charactersCard_Thumbnall/");
const imageModulesGlob = import.meta.glob(
  "/src/assets/charactersCard/charactersCard_Thumbnall/*.webp"
);

let imageModules: { [key: string]: any } = {};
for (const path in imageModulesGlob) {
  imageModulesGlob[path]().then((module: any) => {
    imageModules[path] = module.default;
  });
}
console.log(imageModules);
const characters = ref(charactersJson);
const tierA = ref(false);
const tierS = ref(false);
const tierSS = ref(true);
const homeLoding = ref(true);
const WifeCardList = ref([]);

onMounted(() => {
  setTimeout(() => {
    homeLoding.value = false;
  }, 500);
});

function showCards(pTier: any) {
  if (pTier.tier === "A" && tierA.value) {
    return true;
  }
  if (pTier.tier === "S" && tierS.value) {
    return true;
  }
  if (pTier.tier === "SS" && tierSS.value) {
    return true;
  }
  return false;
}
function showCard(pCard: any) {
  const index = findIndex(WifeCardList.value, (o: any) => o === pCard.image);
  return index >= 0 ? "grayscale(0%)" : "grayscale(100%)";
}
function showCardCount(pCard: any) {
  const index = findIndex(WifeCardList.value, (o: any) => o === pCard.image);
  return index >= 0 ? "bg-danger" : "bg-secondary";
}
</script>
<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-12 input-group mb-3">
        <span class="mx-2">Tier :</span>
        <span class="mx-2 form-check form-switch">
          <input class="form-check-input" type="checkbox" v-model="tierA" id="tierA" />
          <label class="form-check-label" for="tierA">A</label>
        </span>
        <span class="mx-2 form-check form-switch">
          <input class="form-check-input" type="checkbox" v-model="tierS" id="tierS" />
          <label class="form-check-label" for="tierS">S</label>
        </span>
        <span class="mx-2 form-check form-switch">
          <input class="form-check-input" type="checkbox" v-model="tierSS" id="tierSS" />
          <label class="form-check-label" for="tierSS">SS</label>
        </span>
      </div>
    </div>
    <div v-if="!homeLoding" class="row">
      <template v-for="Wife in characters">
        <div
          v-for="WifeCards in Wife.cards"
          class="col-6 col-md-4 col-lg-3 col-xl-2 p-2"
          :class="{ 'd-none': !showCards(WifeCards) }"
          :key="'Wife' + Wife.id + 'WifeCards' + WifeCards.id"
        >
          <label class="form-check-label position-relative" :for="WifeCards.image">
            <input
              class="d-none"
              type="checkbox"
              v-model="WifeCardList"
              :id="WifeCards.image"
              :value="WifeCards.image"
            />
            <img
              :src="imageModules[Iimgpath + WifeCards.image]"
              :style="{ filter: showCard(WifeCards) }"
            />
            <span class="position-absolute bottom-0 end-0 d-none">
              <span
                class="badge rounded-pill m-2"
                :class="[showCardCount(WifeCards)]"
                style="font-size: 1rem"
              >
                0
              </span>
            </span>
          </label>
        </div>
      </template>
    </div>
  </div>
</template>
