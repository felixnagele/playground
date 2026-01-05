import { contextBridge, ipcRenderer } from 'electron';
import { CounterState } from '../shared/types';

function isCounterState(value: unknown): value is CounterState {
  if (value === null || typeof value !== 'object') {
    return false;
  }

  // NOTE: Extend this check if CounterState gains required properties.
  return true;
}

contextBridge.exposeInMainWorld('electronAPI', {
  incrementCounter: async (): Promise<CounterState> => {
    const result = await ipcRenderer.invoke('increment-counter');

    if (!isCounterState(result)) {
      throw new TypeError('Invalid CounterState received from main process');
    }

    return result;
  },
});
