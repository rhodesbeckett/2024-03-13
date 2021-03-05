<template>

<div>
    <button @click="del">  Shuffle</button>
    <transition-group
        name="test">
    <p v-for="(i,j) in lista"  @click="del(j)" v-bind:key="i.ime"> {{ i.ime }}</p>
</transition-group>
</div>



  
</template>

<script>

export default {
    data() {
        return {
            poruka : 'test',
            lista: [{ime:"Ime1"},{ime:"Ime2"},{ime: "Ime3"},{ime:"Ime4"},{ime:"Ime5"}]
        }
    },
    methods: {
        shuffle() {
            this.lista = this.lista.sort( () => .5 - Math.random() );
        },
        del(index) {
            this.lista.splice(index,1)
        }
    }
}
</script>

<style>

.test-move {
    transition: transform 1s;
}
.test-enter, .test-leave-to {
    opacity: 0;
    transform: translateY(30px);
}

.test-leave-active {
position: absolute;
}
</style>