// matchInfo
export interface MatchInfo {
  compDesc: CompDesc;
}
export interface CompDesc {
  title: string;
  src: string;
  editing: string;
  time: CompTime;
}

export interface CompTime {
  isChosen: boolean;
  firstHalf: Halftime;
  secondHalf: Halftime;
}

export interface Halftime {
  min: null | number;
  sec: null | number;
}
