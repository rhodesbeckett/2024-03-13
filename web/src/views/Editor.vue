<template lang="pug">
  div(class="editor-container")
   MainContainer(class="editor-main-container--default-edit" v-for="row,i in highlightRows" :key="i")
    <template #content>
      h3(class="editor-label-row") Start
      div(class="editor-input-min")
        Input(
          v-bind:value="row.min"
          :inputLength="3"
          v-on:input="row.min = $event"
        type="number")
      h3(class="editor-label-row") :
      div(class="editor-input-sec")
        Input(
          :inputLength="3"
          v-bind:value="row.sec"
          type="number"
          v-on:input="row.sec = $event")
      h3(class="editor-label-row") +
      div(class="editor-input-to-add")
        Input(
          :inputLength="3"
          type="number"
          v-bind:value="row.toAdd"
          v-on:input="row.toAdd = $event"
          @test="newRow(row)" )
      Button(class="editor-delete-button" v-on:click.native="deleteRow(i)" buttonText="delete")
    </template>
    

    
</template>

<script>
import MainContainer from '@/components/MainContainer.vue'
import Button from '@/components/Button.vue'
import Input from '@/components/Input.vue'
import FlexContainer from '@/components/FlexContainer.vue'
import Row from '@/assets/Row.js'

export default {
    components: {
      MainContainer,Button,Input,FlexContainer,
    },
    data() {
      return {
        highlightRows: [ ],
      }
    },
    methods: {
      newRow(row) {
        if (row.check() == true) {
          if(this.checkAllRows()) {
            let row = new Row();
            this.highlightRows.push(row)
          }
        }
      },
      checkAllRows() {
        for(let i=0;i<this.highlightRows.length;i++) {
          if (this.highlightRows[i].check() == true) {
            continue
          }
          else {
            return false
          }
        }
        return true
      },
      deleteRow(row) {
        console.log(row);
        this.highlightRows.splice(row,1)
      }
    },
    created() {
      let row = new Row();
      this.highlightRows.push(row)
    },
    computed: {
      
    }
}
</script>

<style>

.editor-container {
  display: flex;
  flex-direction: column;
  max-width: 1080px;
  margin: 0 auto;
}

.editor-input-min {
  grid-column: 2 / 3;
}

.editor-input-sec {
  grid-column: 4 / 5;
}

.editor-input-to-add {
  grid-column: 6/7;
}

.editor-delete-button {
  grid-column: 7;
}

.editor-main-container--default-edit {
  max-width: none;
  margin: 0;
}

</style>