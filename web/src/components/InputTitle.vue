<template>
  <input type="text" :value="title" @input="this.changeTitle" class="input matchInfo__input">
</template>

<script>
import { mapGetters,mapMutations } from 'vuex';

export default {
    computed: 
        mapGetters(['title'])
    ,
    methods: {
        ...mapMutations(['updateTitle']),
        changeTitle(event) {
            this.updateTitle(event.target.value)
        }
    }
}
</script>

<style>
    .matchInfo__input {
        grid-column: title-end / input-end;
    }
</style>