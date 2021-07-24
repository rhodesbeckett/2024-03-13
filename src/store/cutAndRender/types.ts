export interface CutAndRender {
  cutAndRender: CutAndRenderI;
}

export interface CutAndRenderI {
  currentProcess: string;
  canCut: boolean;
  canRender: boolean;
  cutProgress: number;
  renderProgress: number;
}
