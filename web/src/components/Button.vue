<template lang="pug">
    <input type="button" :value="this.buttonText"/>
</template>

<script>
export default {
    props: {
        buttonText: String
    }
}
</script>

<style>

</style>