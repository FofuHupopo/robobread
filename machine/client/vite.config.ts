import {defineConfig} from 'vite';
import react from '@vitejs/plugin-react-swc';
import vitePluginSvgr from 'vite-plugin-svgr';

export default defineConfig({
    plugins: [react(), vitePluginSvgr()],
    resolve: {
        alias: {
            src: '/src',
        },
    },
});
