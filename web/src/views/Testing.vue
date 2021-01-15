<template lang='pug'>
    MainContainer(style="text-align:left;")
        <template #content>
            h3(class='testing-label') Match
            img(class="testing-photo" src="https://via.placeholder.com/600x300")
            h3(class='testing-label') First half
            h3(class='testing-label') Second half
            h3(class='testing-label') Highlights
            h3(class='testing-label') Test match
            div(class='testing-input')
                Input(:inputLength="3")
                span(class="testing-space") :
                Input(:inputLength="3")
            Button(class="testing-button" buttonText="Check photo")
        </template>
</template>

<script>
import MainContainer from '@/components/MainContainer.vue'
import Input from '@/components/Input.vue'
import Button from '@/components/Button.vue'

export default {
    components: {
        MainContainer,Input,Button
    }
}
</script>

<style>

.testing-label {
    grid-column: 1 / 3;
}

.testing-input {
    grid-column: 1 / 2;
    margin-bottom: 0.5em;
}
.testing-photo {
    grid-column: 3 / 8;
    grid-row: 1 / 8;
}

.testing-space {
    margin: 0 0.5em;
}

.testing-button {
    grid-column: 1 / 2;
}

</style>