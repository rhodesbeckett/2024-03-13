<template>
    <span class="matchComp-row">
        <h1 class="title compTitle" @click="setMatchID(comp._id.$oid)">{{ comp.compDesc.title }}</h1>
        <h3 class="halfTime">Editing:</h3>
        <RadioBtnHalfTime class="radio1" :radioClick="radioClick" :halfTime="1" :matchCompID="comp._id.$oid"/>
        <RadioBtnHalfTime class="radio2" :radioClick="radioClick" :halfTime="2" :matchCompID="comp._id.$oid"/>
        <a class="button btnMerge" @click="mergeVideos(comp._id.$oid)">Merge halfTime</a>
    </span>
</template>

<script>
import RadioBtnHalfTime from '../components/RadioBtnHalfTime.vue'
import { mapMutations,mapActions } from 'vuex'
import axios from 'axios'

export default {
    props: ['comp'],
    components: {RadioBtnHalfTime},
    methods: {
        ...mapMutations(['updateIsChosen','updateEditing']),
        ...mapActions(['getCompDesc','setCompDesc']),
        setMatchID(id) {
            this.$cookies.set('mcID',id,'1500d',true)
            this.$router.push('matchCompInfo')
        },
        radioClick(halfTime,matchCompID) {
            this.setMatchID(matchCompID)
            setTimeout( () => {
                this.updateIsChosen(true)
                if(halfTime == 1) {
                    this.updateEditing("firstHalf")
                }
                else {
                    this.updateEditing("secondHalf")
                }
                this.setCompDesc({"showMessage": function () {}})
            },1000) 
        },
        mergeVideos(ID) {
            axios.get(`http://localhost:5000/mergeVideos/${ID}`).then(
                (res) => {
                    console.log(res)
                }
            )
        }
    }
}
</script>

<style scoped>
    .matchComp-row {
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

</style>