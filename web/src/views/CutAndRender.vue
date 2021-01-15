<template lang="pug">
  MainContainer
    <template #content>
        Button(class="cut-button" buttonText="CUT")
        div(class="progress-bar") %
        Button(class="cut-button" buttonText="RENDER")
        div(class="progress-bar") %
    </template>
</template>

<script>
import MainContainer from '@/components/MainContainer.vue'
import Button from '@/components/Button.vue'

export default {
    components: {
        MainContainer,Button
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