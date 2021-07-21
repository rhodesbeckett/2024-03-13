import store from "@/store";

export default function useNewRow(ID: string | undefined): any {
  function checkRow(ID: string|undefined): boolean {
    const row = store.getters.highlightsRow(ID);
    if (
      Number.isInteger(row.min) &&
      Number.isInteger(row.sec) &&
      Number.isInteger(row.toAdd)
    ) {
      return true;
    } else {
      return false;
    }
  }

  function checkAllRows(): boolean {
    const row = store.getters.highlights;
    for (let i = 0; i < row.length; i++) {
      if (checkRow(row[i].id) == true) {
        continue;
      } else {
        return false;
      }
    }
    return true;
  }

  function newRowTab() {
    if (checkRow(ID) == true) {
      if (checkAllRows()) {
        store.getters.highlightsRow(ID).editing = getEditing();
        store.commit("NEW_ROW",getEditing());
        store.dispatch("setHighlights");
      }
    }
  }

  function getEditing(): string {
    return store.getters.highlightsRow(ID).editing;
  }

  return { newRowTab };
}
