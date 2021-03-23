<template>
  <input type="text" :value="getTitle" @input="this.changeTitle" class="input matchInfo__input">
</template>

<script>

export default {
    data() {
        return {
            title: this.$store.state.compDesc.title
        }
    },
    computed: {
        getTitle() {
            return this.$store.state.compDesc.title
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