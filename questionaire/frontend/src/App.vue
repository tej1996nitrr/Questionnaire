<template>
  <div id="app">
    <div id="nav">
      <NavbarComponent/>
      
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div>
    <router-view />
  </div>
</template>
<script>
import NavbarComponent from "./components/Navbar.vue";
export default {
  name:"App",
  components:{
    NavbarComponent
  }
}
</script>
<style>
html, body{
  
   height: 100%;
        font-family: "Playfair Display", serif;
        background: linear-gradient(-45deg, #9cdeee, #b2ecfa, #ffffff, #e6e5e5);
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
  .btn:focus{
    box-shadow: none !important;
  }

</style>
