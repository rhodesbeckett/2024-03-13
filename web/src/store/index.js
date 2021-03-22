import Vuex from 'vuex'
import Vue from 'vue'
import axios from 'axios'

Vue.use(Vuex)
export default new Vuex.Store({

    state: {
        ime: "Uros",
        compDesc: {
            "title": "",
            "src": "",
            "editing": "",
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
        highlights: [{"min":null,"sec":null,"toAdd":null,"id":0}],
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
        getTesting() {
            const path = `http://localhost:5000/getTest/${Vue.$cookies.get("mcID")}`
            axios.get(path)
            .then((res) => {
                    this.commit('newTesting',res.data.test)
                }
            )
        },
        getCanCut() {
            let path = `http://localhost:5000/getCanCut/${Vue.$cookies.get('mcID')}`
            axios.get(path).
            then( (res) => {
                this.commit('newCanCut',(res.data.canCut == 'true'))
            })
        }
    },
    modules: {

    }
})
