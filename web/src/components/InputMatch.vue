<template>
  <input type="text" v-model="src" @input="this.updateSrc" placeholder="full path" class="input matchInfo__input--half">
</template>

<script>
export default {
    data() {
        return {
            src: ""
        }
    },
    methods: {
        updateSrc(event) {
            this.$store.commit('updateSource',event.target.value)
        }
    }
}
</script>

<style>

</style>