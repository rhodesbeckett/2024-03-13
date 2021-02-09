<template>
  <MainContainer>
    <template #content>
        <h4>Choose compilation</h4>
        <select>
            <option v-for="comp in matchComps"
            :key="comp._id.$oid"
            @click="setMatchID(comp._id.$oid)">
                {{ comp.compDesc.title }}
            </option>
        </select>
        <Button class="button-add-mc" v-on:click.native="setMatchID('')" buttonText="+"/>
    </template>
  </MainContainer>
</template>

<script>
import MainContainer from '@/components/MainContainer.vue'
import Button from '@/components/Button.vue'
import axios from 'axios'


export default {
    name: "Home",
    components: {
        MainContainer,Button
    },
    data() {
        return {
            matchComps: []
        }
    },
    methods: {
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
        }
    },
    created() {
        this.getAllComps()
    }
    
}
</script>

<style>

h4 {
    grid-column: 3 / 6;
}

.button-add-mc {
    grid-column: 6 / 7;
    border: 1.2px solid black;
    font-size: 1.5em;
}

</style>