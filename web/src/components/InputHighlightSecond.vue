<template>
    <div class="column is-1 is-2-mobile">
        <input class="input highlights-input" min="0" max="999" size="3" maxlength="3" type="text"
        :value="getValue"
        @input="this.updateValue"
        @keydown.tab = "newRow()"
        >
    </div>
</template>

<script>
export default {
    props: ['id','part'],
    methods: {
        updateValue(event) {
            this.$store.commit(`updateHighlightsRow${this.part}`,{"id":this.id,"value":parseInt(event.target.value)})
        },
        checkRow(id) {
            let row = this.$store.getters.getHighlights(id)
            if(Number.isInteger(row.min) && Number.isInteger(row.sec) && Number.isInteger(row.toAdd)) {
                return true
            }
        },
        checkAllRows() {
            let row = this.$store.state.highlights
            for(let i=0;i<row.length;i++) {
                if (this.checkRow(row[i].id) == true) {
                    continue
                }
                else {
                    return false
                }
            }
            return true
        },
        newRow() {
            if (this.part == "ToAdd") {
                if (this.checkRow(this.id) == true) {
                    if(this.checkAllRows()) {
                        this.$store.commit('newRow')
                        this.$store.dispatch('setHighlights')
                    }
                }
            }
        }
        
    },
    computed: {
        getValue() {
            if (this.part == "Min") {
                return this.$store.getters.getHighlights(this.id).min
            }
            else if (this.part == "Sec") {
                return this.$store.getters.getHighlights(this.id).sec
            }
            else {
                return this.$store.getters.getHighlights(this.id).toAdd
            }
        }
    }
}
</script>

<style>

</style>