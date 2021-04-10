<template>
<div>
    <transition-group
    name="highlights"
    enter-active-class="highlights-add"
    leave-active-class="highlights-remove">
        <div class="columns highlight-row is-centered" v-for="row in highlights" :key="row.id" style="align-items:center;">
            <InputHighlightSecond :id="row.id" part="Min" />
            <div class="column is-1 is-2-mobile center-dot">
            :
            </div>
            <InputHighlightSecond :id="row.id" part="Sec" />
            <div class="column is-1 is-2-mobile center-dot">
            +
            </div>
            <InputHighlightSecond :id="row.id" part="ToAdd" />
            <div class="column is-1 is-2-mobile">
                <a class="button is-danger is-large is-2" @click="deleteRow(row.id);setHighlights()">Delete</a>
            </div>
        </div>
    </transition-group>
</div>


</template>

<script>
import InputHighlightSecond from '../components/InputHighlightSecond'
import { mapMutations,mapActions,mapGetters } from 'vuex'
export default {
    components: {
       InputHighlightSecond
    },
    methods: {
      ...mapMutations(['deleteRow','newRow']),
      ...mapActions(['setHighlights','getHighlights','getCompDesc']),
    },
    computed: {
        ...mapGetters(['highlights'])
    },
    created() {
      if (this.$cookie.get('mcID') == "" || this.$cookie.get('mcID') == null) {
        this.$router.push('/')
      }
      else {
        // get highlights and set all data for page
        this.getHighlights()
        return ;
      }
    },
    watch: {
      highlights: {
        handler: function(val) {
          if (val.length == 0) {
            this.newRow()
          }
        }
      }
    }
    
}
</script>

<style scoped>

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