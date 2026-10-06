import { C as Calendar$1 } from '../chunks/41b24878.js';
import { i as interactionPlugin } from '../chunks/7b17d829.js';
import { d as dayGridPlugin } from '../chunks/f098b4fb.js';
import { t as timeGridPlugin } from '../chunks/9ec8f18e.js';
import { l as listPlugin } from '../chunks/b600ef0c.js';
import { m as multiMonthPlugin } from '../chunks/a2a69877.js';

const plugins = [
    interactionPlugin,
    dayGridPlugin,
    timeGridPlugin,
    listPlugin,
    multiMonthPlugin,
];
class Calendar extends Calendar$1 {
    constructor(el, optionOverrides = {}) {
        super(el, {
            ...optionOverrides,
            plugins: [
                ...plugins,
                ...(optionOverrides.plugins || []),
            ]
        });
    }
}

export { Calendar, Calendar as default, plugins };
