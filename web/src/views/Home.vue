<template lang="pug">
  MainContainer
    <template #content>
      h3(class="home-label") Title:
      div(class="home-input")
        Input(:inputLength="100")
      h3(class="home-label") Match
      Button(class="home-button" buttonText="UPLOAD")
      h3(class="home-label") Editing
      div(class="home-button")
        label 1st
          input(type="radio" name="halfTime" value="1st" @click="radioClick(1)" checked='true')
        label 2nd
          input(type="radio" name="halfTime" value="2nd" @click="radioClick(2)" ) 

      h3(class="home-label") 1st:
      div(class="halftime-input" ref="firstHalfTime")
        Input(:inputLength="3")
        span(class="halftime-dots") :
        Input(:inputLength="3")
      
      h3(class="home-label") 2nd:
      div(class="halftime-input" ref="secondHalfTime")
        Input(class="user-input--disabled" :inputLength="3")
        span(class="halftime-dots") :
        Input(class="user-input--disabled" :inputLength="3")
    </template>
</template>

<script>
// @ is an alias to /src
import MainContainer from '@/components/MainContainer.vue'
import Input from '@/components/Input.vue'
import Button from '@/components/Button.vue'


export default {
  name: 'Home',
  components: {
    MainContainer,Input,Button
  },
  data() {
    return {
      halfTime: ""
    }
  },
  methods: {
    radioClick(halfTime) {
      
      if(halfTime == 1) {
        this.toggleHalfTime(this.$refs.secondHalfTime,true)
        this.toggleHalfTime(this.$refs.firstHalfTime,false)
      }
      else {
        this.toggleHalfTime(this.$refs.firstHalfTime,true)
        this.toggleHalfTime(this.$refs.secondHalfTime,false)
      }
      
    },
    toggleHalfTime(elem,value) {
      for(let i = 0;i<2;i++) {
        elem.querySelectorAll("input")[i].disabled = value;
        elem.querySelectorAll("input")[i].classList.toggle("user-input--disabled")
      }
    }
  }
  
}
</script>


<style>

.home-label {
  grid-column: 1 / 2;
}

.home-input {
  grid-column: 2 / 6;
}

.home-input > input {
  width: 100%;
}

.home-button {
  grid-column: 2 / 3;
  display: flex;
  justify-content: space-around;
}

.halftime-input {
  grid-column: 2 / 3;
}

.halftime-dots {
  margin: 0 0.5em;
}
</style>