import { createApp } from 'vue';
import navbar from 'navbar';
import footnote from 'footnote';

createApp({}).component('navbar', navbar).mount('#navbar-container');
createApp({}).component('footnote', footnote).mount('#footer-el');
