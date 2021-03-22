<template>
  <input type="text" v-model="title" @input="this.changeTitle" class="input matchInfo__input">
</template>

<script>

export default {
    data() {
        return {
            title: ""
        }
    },
    methods: {
        changeTitle(event) {
            this.$store.commit('updateTitle',event.target.value)
        }
    }
}
</script>

<style>
    .matchInfo__input {
        grid-column: title-end / input-end;
    }
</style>