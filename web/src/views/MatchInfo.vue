<template>
    <div class="columns is-centered is-multiline">
      
      <div class="column is-12 matchInfo-container">
          <h1 class="title matchInfo__title">Title:</h1>
          <input type="text" v-model="title" class="input matchInfo__input">
          <h1 class="title matchInfo__title">Match:</h1>
          <input type="text" v-model="src" placeholder="full path" class="input matchInfo__input--half">
          <h1 class="title matchInfo__title">Editing</h1>
          <h2 class="matchInfo__editing-response" v-if="time.isChosen == true">{{ editing }}</h2>
          <div class="matchInfo__input--half matchInfo__radio-btns" v-if="time.isChosen == false">
            <label>
              1st
              <input type="radio" class="title" name="halfTime" value="1st" @click="radioClick(1)">
            </label>
            <label>
            2nd
              <input type="radio" class="title" name="halfTime" value="2nd" @click="radioClick(2)">
          </label>
          </div>
          <h1 class="title matchInfo__title">1st:</h1>
          <div v-if="editing == 'firstHalf'" class="matchInfo__halfTimeInput">
            <div>
            <input type="number" size="3" maxlength="3" class="input"
             :v-bind="time.firstHalf.min"
             :value="time.firstHalf.min"
             v-on:input="time.firstHalf.min = parseInt($event.target.value)">
            </div>
          <span style="margin: 0 1.5em;">:</span>
          <div>
            <input type="number" size="3" maxlength="3" class="input"
            :v-bind="time.firstHalf.sec"
            :value="time.firstHalf.sec"
            v-on:input="time.firstHalf.sec = parseInt($event.target.value)">
            </div>
          </div>
          <h1 class="title matchInfo__title">2nd:</h1>
          <div v-if="editing == 'secondHalf'"  class="matchInfo__halfTimeInput">
            <div>
            <input type="number" size="3" maxlength="3" class="input"
            :v-bind="time.secondHalf.min"
            :value="time.secondHalf.min"
            v-on:input="time.secondHalf.min = parseInt($event.target.value)">
            </div>
          <span style="margin: 0 1.5em;">:</span>
          <div>
            <input type="number" size="3" maxlength="3" class="input"
            :v-bind="time.secondHalf.sec"
            :value="time.secondHalf.sec"
            v-on:input="time.secondHalf.sec = parseInt($event.target.value)">
            </div>
          </div>
        <a class="matchInfo__title button is-success" @click="saveBtn" style="margin-top: 0.75em;">SAVE
            <div class="message-server" ref="messageServer">
              MatchInfo saved!
            </div>
        </a>
      </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import gsap from 'gsap'

export default {
  name: 'Home',
  components: {
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
    updateHighlightValue(inputElem,event) {
      console.log(event)
    },
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
    
    saveBtn() {
      let obj = {
        compDesc: {
        title: this.title,
        editing: this.editing,
        src: this.src,
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
        if (res.data.msg) {
          this.showMessage()
          return null
        }
      })
    },
    showTimeInput() {
      if(this.editing == "firstHalf") {
        this.radioClick(1)
      }
      else if(this.editing == "secondHalf") {
        this.radioClick(2)
      }
    },
    showMessage() {
      let elemAnim = gsap.to(this.$refs.messageServer,{duration:0.3,scale:1.0})
      setTimeout(function () { elemAnim.reverse() },500)
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
  },
  
  
}
</script>


<style>


  .matchInfo-container {
      display: grid;
      grid-template-columns:
        [title-start] 1fr
        [title-end] 2fr
        [input-start] 2fr
        [half-of-input] 4fr
        [input-end];
      grid-template-rows: repeat(6,1fr);
      justify-content: center;
      max-width: 1080px;
      margin: 0 auto;
  }

  .matchInfo__title {
    grid-column: title;
  }

  @media(max-width: 1027px) {
    .matchInfo__title {
      font-size: 1.8em;
    }
  }

  .matchInfo__input {
    grid-column: title-end / input-end;
  }

  .matchInfo__editing-response {
    grid-column: title-end / input-start;
    justify-self: center;
  }

  .matchInfo__input--half {
    grid-column: title-end / half-of-input;
  }

  .matchInfo__radio-btns, .matchInfo__halfTimeInput {
    display: flex;
    justify-content: space-around;
    align-items: center;
  }

  @media(max-width: 1027px) {
    .matchInfo__radio-btns, .matchInfo__halfTimeInput {
      align-items: flex-start;
    }
  }
  @media(max-width: 768px) {
    .matchInfo__halfTimeInput {
      grid-column: title-start / input-end;
      justify-content:start;
    }
  }
  .matchInfo__saveBtn {
    grid-column: title-start / input-start;
  }

</style>