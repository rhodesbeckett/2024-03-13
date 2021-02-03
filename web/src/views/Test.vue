<template>
  <p> {{ poruka }} </p>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            poruka : 'saa'
        }
    },
    methods: {
        getPoruka() {
            const path = 'http://localhost:5000/testJSON'
            console.log("getPoruka")
            axios.get(path)
            .then((res) => {
                this.poruka = res.data.poruka
            })
        }
    },
    created() {
        this.getPoruka()
    }
}
</script>

<style>

</style>