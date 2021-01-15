<template lang="pug">
  input(class="user-input"
  :style="userStyle"
  type="text"
  :size="inputLength"
  :maxlength="inputLength"
  v-on:keydown.tab="$emit('test')"
  v-bind:value="value"
  v-on:input="$emit('input',parseInt($event.target.value))")

</template>

<script>
export default {
    props: {
        userStyle: {
            type: Object
        },
        inputLength: {
            type: Number
        },
        inputId: {
          type: Number
        },
        value: {
          type: Number
        }
    },
    methods: {
    }
}
</script>

<style>

.user-input {
  width: 25%;
  border: 1px solid black;
  border-radius: 0.2em;
  padding: 0.2em;
}

.user-input--disabled {
  background-color: gray;
  color: gray;
  cursor: default;
}

</style>