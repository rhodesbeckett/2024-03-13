<template>
<div>
  <div class="columns highlight-row is-centered" v-for="(row,i) in highlightRows" v-bind:key="i" style="align-items:center;" >
    <div class="column is-1 is-2-mobile">
      <input class="input highlights-input"  size="3" maxlength="3" type="number"
      v-bind:value="row.min"
      v-on:input="row.min = parseInt($event.target.value)">
    </div>
    <div class="column is-1 is-2-mobile center-dot">
        :
    </div>
    <div class="column is-1 is-2-mobile ">
        <input class="input highlights-input" size="3" maxlength="3" type="number"
        v-bind:value="row.sec"
        v-on:input="row.sec = parseInt($event.target.value)">
    </div>
    <div class="column is-1 is-2-mobile center-dot">
      +
    </div>
    <div class="column is-1 is-2-mobile ">
      <input class="input highlights-input" size="3" maxlength="3" type="number"
      v-bind:value="row.toAdd"
      v-on:input="row.toAdd = parseInt($event.target.value)"
      @keydown.tab = "newRow(row)">
    </div>
    <div class="column is-1 is-2-mobile">
        <a class="button is-danger is-large is-2" @click="deleteRow(i)">Delete</a>
    </div>
  </div>
</div>

</template>

<script>


import axios from 'axios'

export default {
    components: {
      
    },
    data() {
      return {
        highlightRows: [ ],
      }
    },
    methods: {
      newRow(row) {
        if (this.checkRow(row) == true) {
          if(this.checkAllRows()) {
            console.log("moze novi red")
            this.createRow()
            this.updateServer()
          }
        }
      },
      createRow() {
        this.highlightRows.push({
            min: null,
            sec: null,
            toAdd: null
        })
      },
      checkRow(row) {
        if(Number.isInteger(row.min) && Number.isInteger(row.sec) && Number.isInteger(row.toAdd)) {
            return true
        }
      },
      checkAllRows() {
        for(let i=0;i<this.highlightRows.length;i++) {
          if (this.checkRow(this.highlightRows[i]) == true) {
            continue
          }
          else {
            return false
          }
        }
        return true
      },
      deleteRow(row) {
        this.highlightRows.splice(row,1)
        this.updateServer()
      },
      getHighlights() {
        const path = `http://localhost:5000/getHighlights/${this.$cookie.get('mcID')}`
        axios.get(path)
        .then((res) => {
          this.highlightRows = JSON.parse(res.data.highlights)
          if(this.highlightRows.length == 0) {
            this.createRow()
          }
        })
      },
      updateServer() {
        const path = `http://localhost:5000/update/${this.$cookie.get('mcID')}/highlights`
        axios.post(path,this.highlightRows).then(
          (res) => {
            console.log(res)
          }
        )
      }
    },
    created() {
      if (this.$cookie.get('mcID') == "" || this.$cookie.get('mcID') == null) {
        this.$router.push('/')
      }
      else {
        // get mc and set all data for page
        
        this.getHighlights()
        return ;
      }
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