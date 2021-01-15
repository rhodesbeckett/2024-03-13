export default class Row {
    min = null;
    sec = null;
    toAdd = null;

    check() {
        if(Number.isInteger(this.min) && Number.isInteger(this.sec) && Number.isInteger(this.toAdd)) {
            return true
        }
    }
}