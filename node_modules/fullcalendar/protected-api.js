export { DateEnv, addDays, addMs, asCleanDays, asRoughMinutes, asRoughMs, asRoughSeconds, createDuration, diffDayAndTime, diffWholeDays, diffWholeWeeks, formatDayString, greatestDurationDenominator, intersectRanges, isInt, isValidDate, multiplyDuration, padStart, parseMarker, rangeContainsMarker, rangesEqual, rangesIntersect, startOfDay, wholeDivideDurations } from '@full-ui/headless-calendar';
import 'preact';
export { u as EventImpl, ap as buildEventRangeKey, Z as buildValidInstanceRange, ar as combineEventUis, at as compareByFieldSpecs, J as computeViewBorderless, T as computeVisibleDayRange, c as createEventUi, e as createFormatter, f as filterHash, au as flexibleCompare, a4 as getDateSpanInstantEndMs, a3 as getDateSpanInstantStartMs, ai as getEventRangeMeta, $ as getRangeInstantEndMs, a0 as getRangeInstantStartMs, g as guid, i as identity, H as isArraysEqual, I as isPropsEqualShallow, n as mapHash, Y as mergeEventStores, av as parseFieldSpecs, Q as refineClassName, aw as refineClassNameGenerator, r as refineProps, ax as removeExact, ah as sortEventSegs, w as warn } from './chunks/6b921645.js';
export { C as CalendarApiImpl, d as CalendarDataManager, b as CalendarInner, a as CalendarMediaRoot, c as computeRootClassName, p as parseBusinessHours } from './chunks/e1b02ccd.js';
export { B as BaseComponent, C as ContentContainer, e as DateComponent, D as DelayedRunner, d as NowTimer, R as RenderId, S as Scroller, k as StandardEvent, h as ViewContainer, p as afterSize, o as buildNavLinkAttrs, g as generateClassName, i as getDateMeta, y as getFooterScrollbarSticky, c as getIsHeightAuto, x as getTableHeaderSticky, m as memoize, a as memoizeObjArg, s as setRef, w as watchHeight, u as watchSize, q as watchWidth } from './chunks/0447fce3.js';
export { h as computeEdges, e as computeInnerRect, g as getRectCenter } from './chunks/560fbc2a.js';
export { j as joinFuncishClassNames, m as mergeCalendarOptions, c as mergeContentInjectors, d as mergeLifecycleCallbacks, a as mergeViewOptionsMap } from './chunks/2cdb4bff.js';
export { E as Emitter, a as applyStyleProp, c as computeElIsRtl } from './chunks/e07fe584.js';
export { A as AllDaySplitter, D as DayTimeColsSlicer, N as NowIndicatorDot, a as NowIndicatorHeaderContainer, c as NowIndicatorLineContainer, S as Splitter, T as TimeGridLayout, d as buildDayCols, b as buildDayColsFromSeries, e as computeTimeGridPrintMode, o as organizeSegsByCol, s as splitInteractionByCol } from './chunks/2cb90dec.js';
export { e as requestJson, u as unpromisify } from './chunks/9495217e.js';
export { D as DateProfileGenerator, c as computeMajorUnit, i as isMajorUnit } from './chunks/f728e8d3.js';
export { B as BgEvent, z as DEFAULT_UNMEASURED_EVENT_THICKNESS, d as DaySeriesModel, e as DaySeriesSlicer, A as DayTableModel, D as DayTableSlicer, C as MeasuredHeightHarness, y as MoreLinkContainer, g as RefMap, R as Ruler, S as Slicer, E as buildDateDataConfigs, F as buildDateRenderConfig, f as buildDateRowConfig, b as buildDayTableModel, G as buildLevelLimitedLayout, H as buildPrintEventBands, I as buildPrintMoreLinkBand, J as computeLateralSpanBottom, c as createDayHeaderFormatter, K as getSliceKey, u as groupLaterallyIntersecting, L as planPrintDomCandidates, s as renderFill, w as sortByAxisOrder } from './chunks/3882a5f6.js';
export { E as ElementDragging, c as config, b as isPropsValid } from './chunks/9669995c.js';
export { D as DayGridLayout, F as FooterScrollbar } from './chunks/54adf0f6.js';

function debounce(fn, ms) {
    let timeoutStarted;
    let timeoutAdded;
    let timeoutId; // thruthiness indicates whether active timeout
    function runWithTimeout(timeout) {
        timeoutStarted = Date.now();
        timeoutAdded = 0;
        timeoutId = setTimeout(() => {
            if (timeoutAdded) {
                runWithTimeout(timeoutAdded);
            }
            else {
                timeoutId = undefined;
                fn();
            }
        }, timeout);
    }
    function request() {
        if (timeoutId) {
            timeoutAdded = Date.now() - timeoutStarted;
        }
        else {
            runWithTimeout(ms);
        }
    }
    function cancel() {
        if (timeoutId) {
            clearTimeout(timeoutId);
            timeoutId = undefined;
        }
    }
    return [request, cancel];
}

class Store {
    constructor() {
        this.handlers = [];
    }
    set(value) {
        this.currentValue = value;
        for (let handler of this.handlers) {
            handler(value);
        }
    }
    subscribe(handler) {
        this.handlers.push(handler);
        if (this.currentValue !== undefined) {
            handler(this.currentValue);
        }
    }
}

/*
Subscribers will get a LIST of CustomRenderings
*/
class CustomRenderingStore extends Store {
    constructor() {
        super(...arguments);
        this.map = new Map();
    }
    // for consistent order
    handle(customRendering) {
        const { map } = this;
        let updated = false;
        if (customRendering.isActive) {
            map.set(customRendering.id, customRendering);
            updated = true;
        }
        else if (map.has(customRendering.id)) {
            map.delete(customRendering.id);
            updated = true;
        }
        if (updated) {
            this.set(map);
        }
    }
}

// StrictMode always OFF
const strictModeFactor = 1;

export { CustomRenderingStore, debounce, strictModeFactor };
