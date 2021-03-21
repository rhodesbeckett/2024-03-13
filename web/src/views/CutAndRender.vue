<template>
    <div class="columns is-centered is-multiline final-container">
        <div class="column is-2">
            <a class="button is-success is-medium" @click="cut">Cut</a>
        </div>
        <div class="column is-10">
        </div>
        <div class="column is-12">
            <progress class="progress is-primary is-medium cut-progress" :value="this.cutProgress" max="100">15%</progress>
        </div>

        <div class="column is-2 ">
            <a class="button is-success is-medium" @click="render">Render</a>
        </div>
        <div class="column is-10">
        </div>
        <div class="column is-12">
            <progress class="progress is-primary is-medium" :value="this.renderProgress" max="100">15%</progress>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    components: {
        
    },
    data() {
        return {
            canCut : false,
            cutProgress:0,
            renderProgress:0,
            currentProcess: ""
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
            if (this.canCut == true || this.currentProcess == "") {
                let path = `http://localhost:5000/cut/${this.$cookie.get('mcID')}`
                axios.get(path).
                then( (res) => {
                    if (res.data.msg) {
                        return null
                    }
                })
                this.updateProgress()
                this.currentProcess = "cut"
            }
            else {
                //
            }
        },
        render() {
            if (this.canCut == true || this.currentProcess == "") {
                let path = `http://localhost:5000/render/${this.$cookie.get('mcID')}`
                axios.get(path).
                then( (res) => {
                    console.log(res)
                })
                this.updateRenderProgress()
                this.currentProcess = "render"
            }
        },
        updateProgress() {
            let cutInterval = setInterval( () => {
              axios.get(`http://localhost:5000/getCutProgress/${this.$cookie.get('mcID')}`).then(
                res => {
                    this.cutProgress = res.data.cutProgress
                    if(res.data.cutProgress == 100.0) {
                        clearInterval(cutInterval);
                        this.currentProcess = ""
                    }
                })
            },1000)
        },
        updateRenderProgress() {
            let cutInterval = setInterval( () => {
              axios.get(`http://localhost:5000/getRenderProgress/${this.$cookie.get('mcID')}`).then(
                res => {
                    this.renderProgress = res.data.renderProgress
                    if(res.data.renderProgress == 100.0) {
                        clearInterval(cutInterval);
                        this.currentProcess = ""
                    }
                })
            },1000)
        }
    },
    created() {
        this.getCanCut()
    }
}
</script>

<style>

.final-container {
    max-width: 1080px;
    margin: 0 auto;
}

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

.cut-progress {
    transition: all 0.5s;
}

progress[value]::-moz-progress-bar {
    transition: value 0.5s;
}

</style>