import { contextBridge, ipcRenderer } from 'electron';
import { CounterState } from '../shared/types';

contextBridge.exposeInMainWorld('electronAPI', {
  incrementCounter: (): Promise<CounterState> =>
    ipcRenderer.invoke('increment-counter'),
});
