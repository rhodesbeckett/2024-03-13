<template>
    <div class="columns is-centered is-multiline message-container">
        <div class="message-server message-server--centered message-server--not-visible" ref="messageServer">
            You can cut and render!
        </div>
        <div class="column is-12 testing-container">
        <h1 class="title" style="grid-area: matchTest;">Match</h1>
        <h2 class="title is-6" style="grid-area: matchValue;">{{ srcTest }}</h2>

        <h1 class="title" style="grid-area: halfTimeTest;">Halftime</h1>
        <h2 class="title is-6" style="grid-area: halfTimeValue;">{{ halfTimeTest }}</h2>

        <h1 class="title" style="grid-area: highlightsTest;" >Highlights</h1>
        <h2 class="title is-6" style="grid-area: highlightsValue;">{{ highlightsTest }}</h2>

        <h1 class="title" style="grid-area: testPicture;">Test match
        </h1>
        <div style="grid-area: pictureInput;">
            <input type="number" size="3" maxlength="3" class="user-input"
            v-bind:value="minutePhoto"
            v-on:input="minutePhoto = $event.target.value;">
            <span class="testing-space">:</span>
            <input type="number" size="3" maxlength="3" class="user-input"
            v-bind:value="secondPhoto"
            v-on:input="secondPhoto = $event.target.value;">
        </div>

        <a class="button is-success checkBtn " @click="getImage" style="grid-area: checkBtn;">Check
        </a>

        <img style="grid-area: picture;" :src="imgSrc"/>

        </div>
    </div>
</template>

<script>
import axios from 'axios'
import gsap from 'gsap'

export default {
    components: {
        
    },
    data() {
        return {
            srcTest: false,
            halfTimeTest: false,
            highlightsTest: false,
            imgSrc: "https://via.placeholder.com/600x300",
            minutePhoto: 0,
            secondPhoto: 0,
            canCutAndRender: false
        }
    },
    methods: {
        getTest() {
            const path = `http://localhost:5000/getTest/${this.$cookies.get("mcID")}`
            axios.get(path)
            .then((res) => {
                    this.srcTest = res.data.test.src
                    this.halfTimeTest = res.data.test.halfTime
                    this.highlightsTest = res.data.test.highlights
                    this.updateCanRun()
                }
            )
        },
        getImage() {
            const path = `http://localhost:5000/getPhoto/${this.minutePhoto}/${this.secondPhoto}`
            axios.get(path)
            .then((res) => {
                    this.imgSrc = res.data.imgSrc
                }
            )
        },
        updateCanRun() {
            let path = `http://localhost:5000/update/${this.$cookie.get('mcID')}/canCut`
            let canCut = false;
            if (this.srcTest == true && this.halfTimeTest == true && this.highlightsTest == true) {
                // update code
                canCut = true;
                this.showMessage(this.$refs.messageServer)
                
            }
            else {
                this.$refs.messageServer.remove()
            }
            axios.post( path, canCut).
            then( (res) => {
                if (res.data.msg) {
                    return null
                }
            })
        },
        showMessage(element) {
            setTimeout(
                function() {
                    let elemAnim = gsap.to(element,{duration:0.5,opacity:1.0})
                    setTimeout( function () { elemAnim.reverse() },700)
                    setTimeout(element.remove,100)
                },1000
            )
        }
    },
    created() {
        this.getTest()
    }
    
}
</script>

<style>

    .testing-container {
        display: grid;
        grid-template-columns: 5fr 5fr auto;
        grid-template-rows: auto;
        grid-template-areas: 
        "matchTest matchValue picture"
        "halfTimeTest halfTimeValue picture"
        "highlightsTest highlightsValue picture"
        "testPicture testPicture picture"
        "pictureInput pictureInput picture"
        "checkBtn blankSpace picture";
        justify-content: center;
        max-width: 1080px;
        margin: 0 auto;
    }
    @media(max-width: 860px) {
      .testing-container {
        grid-template-columns: 1fr 2fr auto;
        grid-template-areas: 
        "matchTest matchTest matchTest"
        "matchValue matchValue matchValue"
        "halfTimeTest halfTimeTest halfTimeTest"
        "halfTimeValue halfTimeValue halfTimeValue"
        "highlightsTest highlightsTest highlightsTest"
        "highlightsValue highlightsValue highlightsValue"
        "testPicture testPicture testPicture"
        "pictureInput pictureInput pictureInput"
        "checkBtn blankSpace blankSpace"
        "picture picture picture"
      }
      .checkBtn {
        margin-bottom: 0.5em;
      }
      .testing-container > h2 {
        text-decoration: underline;
      }
    }
    .testing-container__title {
        font-size: 1.2em;
    }
    
    .checkBtn {
        margin-top: 1.15em;
    }
    @media(max-width: 1024px) {
      .testing-container > h1 {
        font-size: 1.2em;
      }

      .testing-container > h2 {
        font-size: 0.8em;
      }
    }
</style>