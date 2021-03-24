<template>
  <input type="text" :value="src" @input="this.updateSrc" placeholder="full path" class="input matchInfo__input--half">
</template>

<script>
import { mapGetters,mapMutations } from 'vuex'

export default {
    computed: mapGetters(['src']),
    methods: {
        ...mapMutations(['updateSource']),
        updateSrc(event) {
            this.updateSource(event.target.value)
        }
    }
}
</script>

<style>

</style>