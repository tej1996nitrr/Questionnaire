<template>
  <div id="app">
    <NavbarComponent/>
    <HomeComponent/>
     
    <router-view/>
  </div>
</template>

<script>
import NavbarComponent from './components/Navbar.vue'
import HomeComponent from './components/Home.vue'

export default {
  name: 'App',
  components: {
    NavbarComponent,
    HomeComponent,
    
  }
}
</script>

<style>
html, body {
        height: 100%;
        font-family: "Playfair Display", serif;
        background: linear-gradient(-45deg, #e96e49, #af0c4b, #23a6d5, #13af8b);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;  
    }
    @keyframes gradient {
        0% {
            background-position: 0% 50%;
        }
        50% {
            background-position: 100% 50%;
        }
        100% {
            background-position: 0% 50%;
        }
    }
</style>
