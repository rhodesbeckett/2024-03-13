export interface HighlightRow {
  min: null | number;
  sec: null | number;
  toAdd: null | number;
  id: string;
  editing: string;
}
export interface Editor {
  highlights: HighlightRow[];
}
