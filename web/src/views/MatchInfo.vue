<template>
    <div class="columns is-centered is-multiline">
        <div class="column is-12 matchInfo-container">
            <h1 class="title matchInfo__title">Title:</h1>
            <InputTitle />
            <h1 class="title matchInfo__title">Match:</h1>
            <InputMatch />
            <h1 class="title matchInfo__title">Editing</h1>
            <h2 class="matchInfo__editing-response" v-if="isChosen == true">{{ editing }}</h2>
            <div class="matchInfo__input--half matchInfo__radio-btns" v-if="isChosen == false">
                <RadioBtnHalfTime :radioClick="radioClick" :halfTime="1"/>
                <RadioBtnHalfTime :radioClick="radioClick" :halfTime="2"/>
            </div>
            <h1 class="title matchInfo__title">1st:</h1>
            <InputHalfTime v-if="editing == 'firstHalf'" editing="firstHalf"/>
            <h1 class="title matchInfo__title">2nd:</h1>
            <InputHalfTime v-if="editing == 'secondHalf'" editing="secondHalf"/>
            <a class="matchInfo__title button is-success" @click="saveBtn" style="margin-top: 0.75em;">SAVE
                <div class="message-server" ref="messageServer">
                MatchInfo saved!
                </div>
            </a>
        </div>
    </div>
</template>

<script>

import InputTitle from '../components/InputTitle.vue'
import InputMatch from '../components/InputMatch.vue'
import RadioBtnHalfTime from '../components/RadioBtnHalfTime.vue'
import InputHalfTime from '../components/InputHalfTime.vue'
import gsap from 'gsap'
import { mapGetters,mapMutations,mapActions } from 'vuex'

export default {
    components: {
        InputTitle,InputMatch,RadioBtnHalfTime,InputHalfTime
    },
    methods: {
      ...mapMutations(['updateIsChosen','updateEditing']),
      ...mapActions(['getCompDesc','setCompDesc']),
        radioClick(halfTime) {
          this.updateIsChosen(true)
          if(halfTime == 1) {
              this.updateEditing("firstHalf")
          }
          else {
              this.updateEditing("secondHalf")
          }
        },
        saveBtn() {
            this.setCompDesc(this)
        },
        showMessage() {
            let elemAnim = gsap.to(this.$refs.messageServer,{duration:0.3,scale:1.0})
            setTimeout(function () { elemAnim.reverse() },500)
        }
    },
    computed: 
    mapGetters(['isChosen','editing']),
    created() {
      if (this.$cookie.get('mcID') == "" || this.$cookie.get('mcID') == null) {
        this.$router.push('/')
      }
      else {
        this.getCompDesc()
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