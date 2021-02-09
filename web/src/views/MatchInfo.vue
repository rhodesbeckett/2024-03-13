<template lang="pug">
  MainContainer
    <template #content>
      h3(class="home-label") Title:
      div(class="home-input")
        input(class="user-input" v-model="title" :inputLength="100")
      h3(class="home-label") Match
      input(class="home-button" type='file' text="UPLOAD" ref="videoSrc")
      h3(class="home-label") Editing
      p(class="home-button" v-if="time.isChosen == true") {{ editing }}
      div(class="home-button" v-if="time.isChosen == false")
        label 1st
          input(type="radio" name="halfTime" value="1st" @click="radioClick(1)")
        label 2nd
          input(type="radio" name="halfTime" value="2nd" @click="radioClick(2)" ) 

      h3(class="home-label") 1st:
      div(class="halftime-input" v-if="editing == 'firstHalf' && editing == 'firstHalf' " ref="firstHalfTime")
        Input(:inputLength="3" :v-bind="time.firstHalf.min" :value="time.firstHalf.min" v-on:input="time.firstHalf.min = $event")
        span(class="halftime-dots") :
        Input(:inputLength="3" :v-bind="time.firstHalf.sec" :value="time.firstHalf.sec" v-on:input="time.firstHalf.sec = $event")
      
      h3(class="home-label") 2nd:
      div(class="halftime-input" v-if="editing == 'secondHalf' && editing == 'secondHalf'" ref="secondHalfTime")
        Input(:inputLength="3" :v-bind="time.secondHalf.min" :value="time.secondHalf.min" v-on:input="time.secondHalf.min = $event")
        span(class="halftime-dots") :
        Input(:inputLength="3" :v-bind="time.secondHalf.sec" :value="time.secondHalf.sec" v-on:input="time.secondHalf.sec = $event")
      
      Button(class="home-label" buttonText="SAVE" v-on:click.native="saveBtn")
    </template>
</template>

<script>
// @ is an alias to /src
import MainContainer from '@/components/MainContainer.vue'
import Input from '@/components/Input.vue'
import Button from '@/components/Button.vue'
import axios from 'axios'

export default {
  name: 'Home',
  components: {
    MainContainer,Input,Button
  },
  data() {
    return {
      title: "",
      src: "",
      editing: "",
      time: {
            "isChosen": false,
            "firstHalf": {"min": null,"sec":null},
            "secondHalf": {"min": null,"sec":null}
        }
    }
  },
  methods: {
    radioClick(halfTime) {
      this.time.isChosen = true
      if(halfTime == 1) {
        this.editing = "firstHalf"
        this.toggleHalfTime(this.$refs.secondHalfTime,true)
        this.toggleHalfTime(this.$refs.firstHalfTime,false)
      }
      else {
        this.editing = "secondHalf"
        this.toggleHalfTime(this.$refs.firstHalfTime,true)
        this.toggleHalfTime(this.$refs.secondHalfTime,false)
      }
      this.isChosen = true
    },
    toggleHalfTime(elem,value) {
      try {
        for(let i = 0;i<2;i++) {
        elem.querySelectorAll("input")[i].disabled = value;
        /* elem.querySelectorAll("input")[i].classList.toggle("user-input--disabled") */
        }
      } catch(error) {
        return ;
      }
      
    },
    getMC() {
      const path = `http://localhost:5000/getMC/${this.$cookies.get("mcID")}`
      axios.get(path)
      .then((res) => {
          let compDesc = JSON.parse(`${res.data.compDesc}`)
          this.title = compDesc.title
          this.editing = compDesc.editing
          this.src = compDesc.src
          this.time = compDesc.time
          this.isChosen = compDesc.time.isChosen
          this.showTimeInput()
      })
    },
    getVideoSrc() {
      if (this.$refs.videoSrc.files.length > 0) {
        return this.$refs.videoSrc.files[0].name
      }
      else {
        return this.src
      }
      
    },
    saveBtn() {
      let obj = {
        compDesc: {
        title: this.title,
        editing: this.editing,
        src: this.getVideoSrc(),
        time:{}
        }
      }
      obj.compDesc.time = this.time
      this.updateServer(obj)
    },
    updateServer(obj) {
      const path = `http://localhost:5000/update/${this.$cookie.get('mcID')}/compDesc`
      axios.post(path,obj.compDesc)
      .then( (res) => {
        console.log(res)
      })
    },
    showTimeInput() {
      if(this.editing == "firstHalf") {
        this.radioClick(1)
      }
      else if(this.editing == "secondHalf") {
        this.radioClick(2)
      }
    }
  },
  created() {
      if (this.$cookie.get('mcID') == "" || this.$cookie.get('mcID') == null) {
        this.$router.push('/')
      }
      else {
        // get mc and set all data for page
        this.getMC()
        return ;
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