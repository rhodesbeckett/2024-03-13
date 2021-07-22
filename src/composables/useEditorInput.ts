import store from "@/store/index";

export default function useEditorInput(
  ID: string | undefined,
  inputType: string | undefined
): any {
  function getMin(): number {
    return store.getters.highlightsRow(ID).min;
  }
  function getSec() {
    return store.getters.highlightsRow(ID).sec;
  }
  function getToAdd() {
    return store.getters.highlightsRow(ID).toAdd;
  }

  function updateMin(event: { target: { value: string } }) {
    store.commit("UPDATE_HIGHLIGHTS_ROW_MIN", {
      id: ID,
      value: toInt(event.target.value),
    });
  }
  function updateSec(event: { target: { value: string } }) {
    store.commit("UPDATE_HIGHLIGHTS_ROW_SEC", {
      id: ID,
      value: toInt(event.target.value),
    });
  }
  function updateToAdd(event: { target: { value: string } }) {
    store.commit("UPDATE_HIGHLIGHTS_ROW_TO_ADD", {
      id: ID,
      value: toInt(event.target.value),
    });
  }
  function toInt(value: string): null | number {
    if (value == "") {
      return null;
    } else {
      return parseInt(value);
    }
  }
  return { getMin, getSec, getToAdd, updateMin, updateSec, updateToAdd };
}
