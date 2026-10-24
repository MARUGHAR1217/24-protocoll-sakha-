import { Filesystem } from '@capacitor/filesystem';
import { Share } from '@capacitor/share';
import { App } from '@capacitor/app';

// Expose the official Capacitor plugin proxies to the legacy, non-module app.
window.PDRNativePlugins = { Filesystem, Share, App };
