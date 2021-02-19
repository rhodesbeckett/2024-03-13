<template>
    <div class="columns is-centered is-multiline">
        <div class="column is-3">
            <h1 class="title">Choose compilation:</h1>
        </div>
        <div class="column is-2" >
            <select class="comp-choices">
                <option v-for="comp in matchComps"
                :key="comp._id.$oid"
                @click="setMatchID(comp._id.$oid)">
                    {{ comp.compDesc.title }}
                </option>
            </select>
        </div>
        <div class="column is-1" style="align-self:center;">
            <a class="add-btn" @click="setMatchID('')"><i class="fas fa-plus-circle"></i></a>
        </div>
    </div>
</template>

<script>
import axios from 'axios'


export default {
    name: "Home",
    components: {
        
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


</style>