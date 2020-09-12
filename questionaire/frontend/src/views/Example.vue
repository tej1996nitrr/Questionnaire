<template>
  <div class="Example">
    <h1>This is an Example page</h1>
    <h3>{{message}}</h3>
  </div>
</template>
<script>
export default {
    name: 'Example',
    data(){
        return {
            message:"Hello World"
        }
    }
}
</script>
<style scoped>
h1{
    color: crimson;
}
</style>
