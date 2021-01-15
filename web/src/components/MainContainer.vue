<template>
    <div class="main-container">
        <slot name="content"/>
    </div>
</template>

<script>
export default {
    
}
</script>

<style>

.main-container {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    max-width: 1080px;
    margin: 0 auto;
    align-items: center;
}



</style>