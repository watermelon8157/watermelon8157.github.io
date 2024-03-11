<script setup lang="ts">
import { ref } from "vue";
</script>
<template>
  <nav
    class="navbar navbar-expand-lg bg-primary"
    style="position: sticky; top: 0; z-index: 1000"
    data-bs-theme="dark"
  >
    <div class="container-fluid">
      <RouterLink to="/" class="navbar-brand">HBR Tool</RouterLink>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarHBRTool"
        aria-controls="navbarHBRTool"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarHBRTool">
        <ul class="navbar-nav me-auto">
          <li class="nav-item">
            <a class="nav-link active" href="#">
              <RouterLink to="/about">about</RouterLink>
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Features</a>
          </li>
        </ul>
        <!-- <form class="d-flex">
          <input class="form-control me-sm-2" type="search" placeholder="Search" />
          <button class="btn btn-secondary my-2 my-sm-0" type="submit">Search</button>
        </form> -->
      </div>
    </div>
  </nav>
  <div class="mt-4">
    <RouterView />
  </div>
</template>
