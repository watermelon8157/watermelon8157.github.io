<script setup lang="ts">
import { ref } from "vue";
import charactersJson from "@/assets/charactersCard/characters.json";
import { findIndex } from "lodash-es";
const characters = ref(charactersJson);
const tierA = ref(false);
const tierS = ref(false);
const tierSS = ref(true);
const WifeCardList = ref([]);

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
  <div class="d-flex flex-row bd-highlight mb-3">
    <div class="mx-2">Tier :</div>
    <div class="mx-2 form-check form-switch">
      <input class="form-check-input" type="checkbox" v-model="tierA" id="tierA" />
      <label class="form-check-label" for="tierA">A</label>
    </div>
    <div class="mx-2 form-check form-switch">
      <input class="form-check-input" type="checkbox" v-model="tierS" id="tierS" />
      <label class="form-check-label" for="tierS">S</label>
    </div>
    <div class="mx-2 form-check form-switch">
      <input class="form-check-input" type="checkbox" v-model="tierSS" id="tierSS" />
      <label class="form-check-label" for="tierSS">SS</label>
    </div>
  </div>
  <div class="container-fluid">
    <template v-for="Wife in characters" :key="'Wife' + Wife.id">
      <template v-for="WifeCards in Wife.cards" :key="'WifeCards' + WifeCards.id">
        <span v-if="showCards(WifeCards)" class="m-2">
          <input
            class="d-none"
            type="checkbox"
            v-model="WifeCardList"
            :id="WifeCards.image"
            :value="WifeCards.image"
          />
          <label class="form-check-label position-relative" :for="WifeCards.image">
            <img
              :src="'charactersCard/' + WifeCards.image"
              :style="{ filter: showCard(WifeCards) }"
            />
            <!-- <span class="position-absolute bottom-0 end-0">
              <span
                class="badge rounded-pill m-2"
                :class="[showCardCount(WifeCards)]"
                style="font-size: 1rem"
              >
                0
              </span>
            </span> -->
          </label>
        </span>
      </template>
    </template>
  </div>
</template>
