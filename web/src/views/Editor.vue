<template>
<div>
  <transition-group
  name="highlights"
  enter-active-class="highlights-add"
  leave-active-class="highlights-remove"
  >
    <div class="columns highlight-row is-centered" v-for="row in highlightRows" v-bind:key="row.id" style="align-items:center;" >
      <div class="column is-1 is-2-mobile">
        <input class="input highlights-input" min="0" max="999" size="3" maxlength="3" type="text"
        v-bind:value="row.min"
        v-on:input="updateRowInput(row, 'min', $event.target.value)">
      </div>
      <div class="column is-1 is-2-mobile center-dot">
          :
      </div>
      <div class="column is-1 is-2-mobile ">
          <input class="input highlights-input" size="3" min="0" max="999" maxlength="3" type="text"
          v-bind:value="row.sec"
          v-on:input="updateRowInput(row, 'sec', $event.target.value)">
      </div>
      <div class="column is-1 is-2-mobile center-dot">
        +
      </div>
      <div class="column is-1 is-2-mobile ">
        <input class="input highlights-input" size="3" maxlength="3" type="text"
        v-bind:value="row.toAdd"
        v-on:input="updateRowInput(row, 'toAdd', $event.target.value)"
        @keydown.tab = "newRow(row)">
      </div>
      <div class="column is-1 is-2-mobile">
          <a class="button is-danger is-large is-2" @click="deleteRow(row.id)">Delete</a>
      </div>
    </div>
  </transition-group>
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
        poruka: ""
      }
    },
    methods: {
      newRow(row) {
        if (this.checkRow(row) == true) {
          if(this.checkAllRows()) {
            this.createRow()
            this.updateServer()
          }
        }
      },
      createRow() {
        this.highlightRows.push({
            min: null,
            sec: null,
            toAdd: null,
            id: this.randomID()
        })
      },
      randomID() {
        return Math.floor(Math.random() * (10000 - 1 + 1)) + 1; 
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
      deleteRow(id) {
        this.highlightRows = this.highlightRows.filter( item => { return item.id != id})
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
              if (res.data.msg == "success") {
                return null
              }
          }
        )
      },
      updateRowInput(row,part,value) {
        if(value == "") {
          this.updateDetail(row,part,0)
        }
        else {
          this.updateDetail(row,part,value)
        }
      },
      updateDetail(row,part,value) {
        if (part == "min") {
          row.min = parseInt(value)
        }
        else if(part == "sec") {
          row.sec = parseInt(value)
        }
        else if(part == "toAdd") {
          row.toAdd = parseInt(value)
        }
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

.highlights-add {
  animation: highlights-add 0.6s;
}

@keyframes highlights-add {
  0% {
    transform: rotateX(45deg);
    opacity: 0.0;
  }
  100% {
    transform: rotateX(0deg);
    opacity: 1.0;
  }
}

.highlights-remove {
  animation: highlights-remove 0.8s;
}

@keyframes highlights-remove {
  0% {
    transform: rotateX(0deg);
    opacity: 1.0;
  }
  100% {
    transform: rotateX(45deg);
    opacity: 0.0;
  }
}

.highlights-update {
  animation: highlights-update 1.8s;
}

@keyframes highlights-update {
  0% {
    transform: rotateX(0deg);
    opacity: 1.0;
  }
  50% {
    transform: rotateX(45deg);
    opacity: 0.5;
  }
  100% {
    transform: rotateX(0deg);
    opacity: 1.0;
    position: absolute;
  }
}

.highlights-move {
  transition: transform 5s;
}

</style>