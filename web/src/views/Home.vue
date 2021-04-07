<template>
    <div>
        <div class="columns is-centered is-multiline">
            <div class="column" style="align-self:center;flex:none;">
                <a class="add-btn" @click="setMatchID('')"><i class="fas fa-plus-circle"></i></a>
            </div>
        </div>
        
        <transition-group class="columns is-centered is-multiline" tag="div" name="matchComp">
            <div v-for="comp in matchComps" :key="comp._id.$oid" class="column is-7 row-test">
                <h1 class="title compTitle" @click="setMatchID(comp._id.$oid)">{{ comp.compDesc.title }}</h1>
                <h3 class="halfTime">Editing:</h3>
                <RadioBtnHalfTime class="radio1" :radioClick="radioClick" :halfTime="1"/>
                <RadioBtnHalfTime class="radio2" :radioClick="radioClick" :halfTime="2"/>
                <a class="button btnMerge">Merge halfTime</a>
            </div>
        </transition-group>
    </div>
</template>

<script>
import axios from 'axios'
import RadioBtnHalfTime from '../components/RadioBtnHalfTime.vue'
import { mapMutations } from 'vuex'

export default {
    name: "Home",
    components: {
        RadioBtnHalfTime
    },
    data() {
        return {
            matchComps: []
        }
    },
    methods: {
        ...mapMutations(['updateIsChosen','updateEditing']),
        getAllComps() {
            const path = 'http://localhost:5000/getAll'
            axios.get(path)
            .then((res) => {
                this.matchComps = JSON.parse(res.data.allComps)
            })
        },
        setMatchID(id) {
            if (id == "") {
                this.createMC()
                // dobij nov id i redirect na sledecu stranicu
                
            }
            else {
                this.$cookies.set('mcID',id,'1500d',true)
                this.$router.push('matchCompInfo')
            }
            
        },
        createMC() {
            const path = 'http://localhost:5000/insert'
            axios.get(path)
            .then((res) => {
                console.log(res)
                this.$cookies.set('mcID',res.data.mcID,'1500d',true)
                this.$router.push('matchCompInfo')
            })
        },
        radioClick(halfTime) {
          this.updateIsChosen(true)
          if(halfTime == 1) {
              this.updateEditing("firstHalf")
          }
          else {
              this.updateEditing("secondHalf")
          }
        }
    },
    created() {
        this.getAllComps()
    }
    
}
</script>

<style>
    .row-test {
        display: grid;
        grid-template-areas:
        "compTitle compTitle compTitle"
        "halfTime radio1 radio2"
        "btnMerge . .";
        justify-content: space-between;
        background: url('~@/assets/test.svg');
        background-repeat: no-repeat;
        transition: all 0.5s;
    }
    
    #path1481:hover {
    fill: #DA4567;
    }

    .compTitle {
        grid-area: compTitle;
    }

    .compTitle:hover {
        cursor:pointer;
    }

    .compTitle:active{
        color: rgb(141, 137, 137);
    }
    
    .halfTime {
        grid-area: halfTime;
    }

    .radio1 {
        grid-area: radio1;
    }

    .radio2 {
        grid-area: radio2;
    }

    .btnMerge {
        grid-area: btnMerge;
        margin-top: 0.5em;
    }

    @keyframes matchComp {
        0%{
            transform: skewX(60deg)  rotate(-5deg);
            opacity:0.7;
        }

        100% {
            transform: skewX(0deg) rotate(0deg);
            opacity:1;
        }
    }

    .matchComp-enter-active {
       animation: matchComp 0.5s; 
    }

    .matchComp-leave-active {
        animation: matchComp 0.5s;
    }
    
</style>