<template lang="pug">
  MainContainer
    <template #content>
        Button(class="cut-button" v-on:click.native="cut()" buttonText="CUT")
        div(class="progress-bar") {{ canCut }}
        Button(class="cut-button" v-on:click.native="render()" buttonText="RENDER")
        div(class="progress-bar") {{ canCut }}
    </template>
</template>

<script>
import MainContainer from '@/components/MainContainer.vue'
import Button from '@/components/Button.vue'
import axios from 'axios'

export default {
    components: {
        MainContainer,Button
    },
    data() {
        return {
            canCut : false
        }
    },
    methods: {
        getCanCut() {
            let path = `http://localhost:5000/getCanCut/${this.$cookie.get('mcID')}`
            axios.get(path).
            then( (res) => {
                this.canCut = (res.data.canCut == 'true')
            })
        },
        cut() {
            if (this.canCut == true) {
                let path = `http://localhost:5000/cut/${this.$cookie.get('mcID')}`
                axios.get(path).
                then( (res) => {
                    console.log(res)
                })
            }
            else {
                //
            }
        },
        render() {
            if (this.canCut == true) {
                let path = `http://localhost:5000/render/${this.$cookie.get('mcID')}`
                axios.get(path).
                then( (res) => {
                    console.log(res)
                })
            }
        }
    },
    created() {
        this.getCanCut()
    }
}
</script>

<style>

.cut-button {
    grid-column: 1 / 2;
}

.progress-bar {
    grid-column: 1 / 7;
    display: flex;
    background-color: gray;
    border: 2px solid black;
    border-top: 0px solid transparent;
    width: 100%;
    margin: 0.5em 0;
}

</style>