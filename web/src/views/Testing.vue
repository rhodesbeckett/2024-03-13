<template lang='pug'>
    MainContainer(style="text-align:left;")
        <template #content>
            h3(class='testing-label') Match
            h4(class="testing-response") {{ srcTest }}
            img(class="testing-photo" :src="imgSrc")
            h3(class='testing-label') Halftime
            h4(class="testing-response") {{ halfTimeTest }}
            h3(class='testing-label') Highlights
            h4(class="testing-response") {{ highlightsTest }}
            h3(class='testing-label') Test match
            div(class='testing-input')
                Input(:inputLength="3"
                v-bind:value="minutePhoto"
                v-on:input="minutePhoto = $event" type="number")

                span(class="testing-space") :

                Input(:inputLength="3"
                v-bind:value="secondPhoto"
                v-on:input="secondPhoto = $event" type="number")
            Button(class="testing-button" v-on:click.native="getImage" buttonText="Check photo")
        </template>
</template>

<script>
import MainContainer from '@/components/MainContainer.vue'
import Input from '@/components/Input.vue'
import Button from '@/components/Button.vue'
import axios from 'axios'

export default {
    components: {
        MainContainer,Input,Button
    },
    data() {
        return {
            srcTest: false,
            halfTimeTest: false,
            highlightsTest: false,
            imgSrc: "https://via.placeholder.com/600x300",
            minutePhoto: 0,
            secondPhoto: 0,
        }
    },
    methods: {
        getTest() {
            const path = `http://localhost:5000/getTest/${this.$cookies.get("mcID")}`
            axios.get(path)
            .then((res) => {
                    console.log(res.data)
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
                    console.log(res.data)
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
            }
            
            axios.post( path, canCut).
            then( (res) => {
                console.log(res)
            })
        }
    },
    created() {
        this.getTest()
    }
}
</script>

<style>

.testing-label {
    grid-column: 1 / 2;
}

.false-response {
    background-color: red;
}

.true-response {
    background-color: green;
}

.testing-response {
    grid-column: 2 / 3;
}

.testing-input {
    grid-column: 1 / 2;
    margin-bottom: 0.5em;
}
.testing-photo {
    grid-column: 3 / 8;
    grid-row: 1 / 8;
}

.testing-space {
    margin: 0 0.5em;
}

.testing-button {
    grid-column: 1 / 2;
}

</style>