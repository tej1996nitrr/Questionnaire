<template>
  <div class="home">
    
   
  </div>
</template>

<script>
// @ is an alias to /src
import {apiService} from "../common/api.service"
export default {
  name: "Home",
  data(){
    return{
      questions:[]
    }
  },
  methods:{
    getQuestions(){
      let endpoint = 'api/questions/'
      apiService(endpoint).then(data => {this.questions.push(...data)})
    }
  },
  created(){
    this.getQuestions()
    console.log(this.questions)
  }
};
</script>
