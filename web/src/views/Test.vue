<template>

<transition-group>
    <p v-for="i in lista" v-bind:key="i"> {{ i.ime }}</p>
</transition-group>


  
</template>

<script>

export default {
    data() {
        return {
            poruka : 'test',
            lista: [{ime:"Ime1"},{ime:"Ime2"},{ime: "Ime3"}]
        }
    },
    methods: {
        
    }
}
</script>

<style>

</style>