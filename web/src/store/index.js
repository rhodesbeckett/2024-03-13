import Vuex from 'vuex'
import Vue from 'vue'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({

    state: {
        
        compDesc: {
            "title": "",
            "src": "",
            "editing": "firstHalf",
            "time": {
                "isChosen": false,
                "firstHalf": {"min": null,"sec":null},
                "secondHalf": {"min": null,"sec":null}
                }
        },
        testing: {
            "src":false,
            "halfTime":false,
            "highlights":false,
        },
        highlights: [],
        canCut: false,
        canRender: false,
        cutProgress:0,
        renderProgress:0
        
    },
    mutations: {
        novoIme(store,ime) {
            store.ime = ime
        },
        newCompDesc(store,compDesc) {
            store.compDesc = compDesc
        },
        newHighlights(store,highlights) {
            store.highlights = highlights
        },
        newTesting(store,testing) {
            store.testing = testing
        },
        newCanCut(store,canCut) {
            store.canCut = canCut
        },
        // specific updates
        updateTitle(store,title) {
            store.compDesc.title = title
        },
        updateSource(store,src) {
            store.compDesc.src = src
        },
        updateEditing(store,editing) {
            store.compDesc.editing = editing
        },
        updateStartFirstHalf(store,obj) {
            store.firstHalf = obj
        },
        updateStartSecondHalf(store,obj) {
            store.secondHalf = obj
        },
        updateHighlightRow(store,index,row) {
            store.highlights[index] = row
        },
        updateFirstHalfMin(store,min) {
            store.compDesc.time.firstHalf.min = min
        },
        updateFirstHalfSec(store,sec) {
            store.compDesc.time.firstHalf.sec = sec
        },
        updateSecondHalfMin(store,min) {
            store.compDesc.time.secondHalf.min = min
        },
        updateSecondHalfSec(store,sec) {
            store.compDesc.time.secondHalf.sec = sec
        },
        updateIsChosen(store,isChosen) {
            store.compDesc.time.isChosen = isChosen
        },
        updateHighlightsRowMin(store,{id,value}) {
            store.highlights.find(item => item.id === id).min = value
        },
        updateHighlightsRowSec(store,{id,value}) {
            store.highlights.find(item => item.id === id).sec = value
        },
        updateHighlightsRowToAdd(store,{id,value}) {
            store.highlights.find(item => item.id === id).toAdd = value
        },
        newRow(store) {
            let id = Math.floor(Math.random() * (10000 - 1 + 1)) + 1
            store.highlights.push({"min":null,"sec":null,"toAdd":null,"id":id,"editing":store.compDesc.editing})
        },
        deleteRow(store,id) {
            store.highlights = store.highlights.filter( item => { if(item.id != id) return item })
        }

    },
    actions: {
        getIme() {
            axios.get('http://localhost:5000/getAll').then ( response => {
                this.commit('novoIme',JSON.parse(response.data.allComps)[0].compDesc.title)
            })
        },
        getCompDesc() {
            const path = `http://localhost:5000/getMC/${Vue.$cookies.get("mcID")}`
            axios.get(path)
            .then((res) => {
                let compDesc = JSON.parse(`${res.data.compDesc}`)
                this.commit('newCompDesc',compDesc)
            })
        },
        getHighlights() {
            const path = `http://localhost:5000/getHighlights/${Vue.$cookies.get("mcID")}`
            axios.get(path)
            .then((res) => {
                let highlightRows = JSON.parse(res.data.highlights)
                if (highlightRows.length > 0) {
                    this.commit('newHighlights',highlightRows)
                }
            })
        },
        getTesting(store,vueMethod) {
            const path = `http://localhost:5000/getTest/${Vue.$cookies.get("mcID")}`
            axios.get(path)
            .then((res) => {
                    this.commit('newTesting',res.data.test)
                    vueMethod()
                }
            )
        },
        getCanCut() {
            let path = `http://localhost:5000/getCanCut/${Vue.$cookies.get('mcID')}`
            axios.get(path).
            then( (res) => {
                this.commit('newCanCut',(res.data.canCut == 'true'))
            })
        },
        //update server
        setCompDesc(store,payload) {
            const path = `http://localhost:5000/update/${Vue.$cookies.get('mcID')}/compDesc`
            axios.post(path,store.state.compDesc)
            .then( (res) => {
                if (res.data.msg) {
                    payload.showMessage()
                    return null
                }
            })
        },
        setHighlights(store) {
            const path = `http://localhost:5000/update/${Vue.$cookies.get('mcID')}/highlights`
            axios.post(path,store.state.highlights)
            .then( (res) => {
                if (res.data.msg == "success") {
                    return null
                  }
            })  
        }

    },
    modules: {

    },
    getters: {
        title(state) {
            return state.compDesc.title
        },
        src(state) {
            return state.compDesc.src
        },
        isChosen(state) {
            return state.compDesc.time.isChosen
        },
        editing(state) {
            return state.compDesc.editing
        },
        highlights(state) {
            return state.highlights.filter( item => item.editing === state.compDesc.editing)
        },
        highlightsRow(state) {
            return id => {
                return state.highlights.find(item => item.id === id)
            }
        },
        testSrc(state) {
            return state.testing.src
        },
        testHalftime(state) {
            return state.testing.halfTime
        },
        testHighlights(state) {
            return state.testing.highlights
        },
        updatedTesting(state) {
            if (state.testing.src == true && state.testing.halfTime == true && state.testing.highlights == true) {
                return true
            }
            else {
                return false
            }
        }
    }
})
