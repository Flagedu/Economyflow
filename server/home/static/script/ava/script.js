function sbidLocalStorageEnabled() {
    try {
        return localStorage.setItem("_localStorageTest", "_localStorageValue"),
            "_localStorageValue" === localStorage.getItem("_localStorageTest")
    } catch (t) {
        return !1
    }
}
if (!window.sbidTracking || !window.sbidTracking.loadedScript) {
    window.sbidTracking && window.sbidTracking.q && (window.sbidTrackingTempQ = window.sbidTracking.q),
        window.sbidTracking && window.sbidTracking.settings ? window.sbidTrackingTempSettings = window.sbidTracking.settings : window.sbidTrackingTempSettings = {},
        window.sbidTracking = {
            itemTracked: 0,
            cidName: "cid",
            acID: "57",
            baseUrl: "https://analytics.avatrade.io",
            localStorageEnabled: sbidLocalStorageEnabled(),
            settings: window.sbidTrackingTempSettings,
            version: "0.70",
            advancedTracking: !0,
            retargetingEnabled: !0,
            crossDomainEnabled: !0,
            events: [],
            localMap: [],
            setItem: function (t, e, i) {
                try {
                    if (this.localMap[t] = e,
                        this.localStorageEnabled)
                        localStorage.setItem(t, e);
                    else {
                        var r = new Date;
                        r.setTime(r.getTime() + 31536e6);
                        var s = "expires=" + r.toUTCString();
                        document.cookie = t + "=" + e + ";" + s + ";path=/"
                    }
                    this.crossDomainEnabled && (i || this.iframeTrk.contentWindow.postMessage({
                        messageType: "setItem",
                        key: t,
                        value: e
                    }, "*"))
                } catch (t) {
                    console.warn("error setItem", t)
                }
            },
            getItem: function (t) {
                if (this.localMap[t])
                    return this.localMap[t];
                if (this.localStorageEnabled)
                    return localStorage.getItem(t);
                for (var e = t + "=", i = document.cookie.split(";"), r = 0; r < i.length; r++) {
                    for (var s = i[r]; " " == s.charAt(0);)
                        s = s.substring(1);
                    if (0 == s.indexOf(e))
                        return s.substring(e.length, s.length)
                }
                return ""
            },
            trackUrlChange: function () {
                setInterval(function () {
                    try {
                        this.lastTrackingUrl && this.lastTrackingUrl !== window.location.href && this.track()
                    } catch (t) { }
                }
                    .bind(this), 100)
            },
            fireRetargetingPixels: function (t) {
                if (this.retargetingEnabled) {
                    if ("disabled" === this.getItem("sbTrackTagsFired"))
                        return;
                    if ("tag_fired" === t.e)
                        return;
                    this.retargetingQueue || (this.retargetingQueue = []),
                        this.retargetingQueue.push(t);
                    var e = [];
                    if (this.retargetingEvents) {
                        var i = this.getItem("sbTrackCustomerID");
                        for (var r in i || (i = t.cu_id),
                            this.retargetingQueue)
                            if ("pv" == this.retargetingQueue[r].e && this.retargetingEvents.pv)
                                for (var s in this.retargetingEvents.pv) {
                                    var a = this.retargetingEvents.pv[s];
                                    if (window.location.href.indexOf(a.url) > -1 && (!a.has_cuid || i))
                                        for (var n in a.tags) {
                                            var c = a.tags[n];
                                            e.push(c)
                                        }
                                }
                            else if ("video_start" == this.retargetingQueue[r].e && this.retargetingEvents.video_start)
                                for (var s in this.retargetingEvents.video_start) {
                                    if ((!(a = this.retargetingEvents.video_start[s]).url || window.location.href.indexOf(a.url) > -1) && (!a.has_cuid || i))
                                        for (var n in a.tags) {
                                            c = a.tags[n];
                                            e.push(c)
                                        }
                                }
                            else if ("video_end" == this.retargetingQueue[r].e && this.retargetingEvents.video_end)
                                for (var s in this.retargetingEvents.video_end) {
                                    if ((!(a = this.retargetingEvents.video_end[s]).url || window.location.href.indexOf(a.url) > -1) && (!a.has_cuid || i))
                                        for (var n in a.tags) {
                                            c = a.tags[n];
                                            e.push(c)
                                        }
                                }
                            else if ("click_in" !== this.retargetingQueue[r].e && "click_out" !== this.retargetingQueue[r].e || !this.retargetingEvents.clicks) {
                                if ("pv" !== this.retargetingQueue[r].e && "click_in" !== this.retargetingQueue[r].e && "click_out" !== this.retargetingQueue[r].e && this.retargetingEvents.custom && this.retargetingEvents.custom[this.retargetingQueue[r].e] && (!this.retargetingEvents.custom[this.retargetingQueue[r].e].url || window.location.href.indexOf(this.retargetingEvents.custom[this.retargetingQueue[r].e].url) > -1))
                                    for (var n in this.retargetingEvents.custom[this.retargetingQueue[r].e].tags) {
                                        c = this.retargetingEvents.custom[this.retargetingQueue[r].e].tags[n];
                                        e.push(c)
                                    }
                            } else {
                                var o = ""
                                    , d = ""
                                    , h = "";
                                if (this.retargetingQueue[r].p)
                                    for (var g in this.retargetingQueue[r].p)
                                        this.retargetingQueue[r].p[g].click_text && (o = this.retargetingQueue[r].p[g].click_text),
                                            this.retargetingQueue[r].p[g].click_dst && (d = this.retargetingQueue[r].p[g].click_dst),
                                            this.retargetingQueue[r].p[g].element_id && (h = this.retargetingQueue[r].p[g].element_id);
                                for (var l in this.retargetingEvents.clicks) {
                                    var m = this.retargetingEvents.clicks[l];
                                    if ((!m.url || window.location.href.indexOf(m.url) > -1) && (!m.text || o && o.indexOf(m.text) > -1) && (!m.e_id || h === m.e_id) && (!m.dst_url || d && d.indexOf(m.dst_url) > -1) && (!m.has_cuid || i))
                                        for (var n in m.tags) {
                                            var c = m.tags[n];
                                            this.retargetingEvents.custom[this.retargetingQueue[r].e].has_cuid && !i || e.push(c)
                                        }
                                }
                            }
                        var u = this.getItem("sbTrackTagsFired")
                            , v = {}
                            , T = !1;
                        if (u) {
                            var b = u.split(",");
                            for (var f in b)
                                b[f].toString().length < 10 && (v[b[f]] = b[f])
                        }
                        var I = [];
                        for (var n in e) {
                            (c = e[n]).toString().length < 10 && (v[c.toString()] || (v[c.toString()] = c.toString(),
                                I.push(c.toString()),
                                T = !0))
                        }
                        if (i && !this.getItem("sbTrackWCustomerID") && (T = !0,
                            this.setItem("sbTrackWCustomerID", "1")),
                            T) {
                            b = [];
                            for (var k in v)
                                b.push(v[k]);
                            var p = b.join(",");
                            this.setItem("sbTrackTagsFired", p);
                            var w = this.baseUrl + "/pixel/trk_grp?tid=" + p + "&ac_id=" + this.acID + "&new_t=" + I.join(",")
                                , S = {
                                    e: "tag_fired",
                                    p: [{
                                        new_tags: I.join(",")
                                    }, {
                                        tags: p
                                    }]
                                };
                            i && (w = w + "&cusid=" + i,
                                S.cu_id = i),
                                w = w + "&aid=" + this.getItem("sbTrackArrivalID"),
                                this.getItem("sbTrackExternalClientID") && (w = w + "&clid=" + this.getItem("sbTrackExternalClientID")),
                                setTimeout(function () {
                                    var t = window.document.createElement("iframe");
                                    t.addEventListener("load", function () {
                                        this.track(S)
                                    }
                                        .bind(this)),
                                        t.setAttribute("src", w),
                                        t.width = 0,
                                        t.height = 0,
                                        t.style.display = "none",
                                        document.body ? document.body.appendChild(t) : document.head.appendChild(t)
                                }
                                    .bind(this), 11e3)
                        }
                        this.retargetingQueue = []
                    }
                }
            },
            getData: function () {
                var t = {};
                this.recalcUserIfNeeded(!1),
                    t.uid = this.getItem("sbTrackUID"),
                    t.uid || (t.is_empty = !0),
                    this.getItem("sbTrackArrivalID") && (t.aid = this.getItem("sbTrackArrivalID")),
                    this.getItem("sbTrackGKW") && (t.keywords = this.getItem("sbTrackGKW")),
                    this.getItem("sbTrackRef") && (t.ref = this.getItem("sbTrackRef")),
                    this.getItem("sbTrackArrivalPage") && (t.landing_page = this.getItem("sbTrackArrivalPage"));
                try {
                    var e = this.getItem("sbTrackStartSessionsHistory");
                    if (e) {
                        e = e.split(",").map(Number);
                        var i = -1
                            , r = 0;
                        for (var s in e)
                            e[s] > r && (r = e[s],
                                i = s);
                        t.common_utc_day = Math.floor(i / 24) + 1,
                            t.common_utc_hour = i % 24
                    }
                } catch (t) { }
                if (this.getItem("sbTrackDataStore"))
                    try {
                        var a = JSON.parse(this.getItem("sbTrackDataStore"));
                        for (var n in a)
                            t[n] = a[n]
                    } catch (t) { }
                return t
            },
            track: function (t) {
                try {
                    if (t || (t = {
                        e: "pv"
                    }),
                        t.e || (t.e = "pv"),
                        !this.initialized)
                        return window.sbidTrackingTempQ || (window.sbidTrackingTempQ = []),
                            void window.sbidTrackingTempQ.push(t);
                    this.recalcSessionIfNeeded(),
                        t.ts = (new Date).getTime();
                    var e = 0;
                    if (this.getItem("sbTrackLastTrackTime") && (e = parseInt(this.getItem("sbTrackLastTrackTime"))),
                        t.deltaTs = t.ts - e,
                        this.setItem("sbTrackLastTrackTime", t.ts),
                        t.sessionID = this.getItem("sbTrackSession"),
                        "1" === this.getItem("sbTrackNewSession") && (t.isNewSession = !0,
                            this.setItem("sbTrackNewSession", "0")),
                        t.sessionStartTime = this.getItem("sbTrackStartSessionTime"),
                        "pv" === t.e) {
                        if (this.lastTrackingUrl === window.location.href)
                            return;
                        this.lastTrackingUrl = window.location.href
                    }
                    this.advancedTracking ? this.events.push(t) : this.send(t),
                        this.fireRetargetingPixels(t)
                } catch (t) { }
            },
            advTrack: function (t) {
                var e = {
                    event: t.e
                }
                    , i = ""
                    , r = this.getItem("sbTrackCustomerID");
                (i = t.cu_id ? t.cu_id : this.getItem("sbTrackCustomerID")) && this.setItem("sbTrackCustomerID", i),
                    t.isNewSession && (e.n_sess = "1");
                try {
                    e.del_ts = t.deltaTs.toString()
                } catch (t) {
                    e.del_ts = "0"
                }
                return t.sessionStartTime && (e.sess_t = t.sessionStartTime.toString()),
                    e.sess = t.sessionID,
                    "1" === this.getItem("sbTrackNewUser") && (e.n_uid = "1"),
                    "1" === this.getItem("sbTrackNewArrival") && (e.n_arr = "1"),
                    "1" === this.getItem("sbTrackReset") && (e.reset = this.getItem("sbTrackReset")),
                    e.page = window.location.toString(),
                    i && (e.cu_id = i,
                        r || (e.n_cu_id = "1")),
                    t.p && (e.params = t.p),
                    t.gaid && (e.gaid = t.gaid),
                    t.idfa && (e.idfa = t.idfa),
                    t.ifa && (e.ifa = t.ifa),
                    t.apfid && (e.apfid = t.apfid),
                    t.clid ? this.setItem("sbTrackExternalClientID", t.clid) : this.getItem("sbTrackExternalClientID") && (t.clid = this.getItem("sbTrackExternalClientID")),
                    t.clid && (e.clid = t.clid),
                    this.setItem("sbTrackReset", "0"),
                    this.setItem("sbTrackNewUser", "0"),
                    this.setItem("sbTrackNewArrival", "0"),
                    e
            },
            send: function (t) {
                try {
                    var e = window.document.createElement("img")
                        , i = this.baseUrl + "/track?ac_id=" + this.acID + "&rnd=" + this.itemTracked + "&event=" + t.e + "&ver=" + this.version
                        , r = ""
                        , s = this.getItem("sbTrackCustomerID");
                    r = t.cu_id ? t.cu_id : this.getItem("sbTrackCustomerID");
                    try {
                        if (!t.clid && "undefined" != typeof Storage) {
                            var a = localStorage.getItem("aclid");
                            a && (t.clid = a)
                        }
                    } catch (t) { }
                    if (r && (this.setItem("sbTrackCustomerID", r),
                        s || (i += "&n_cu_id=1")),
                        t.isNewSession && (i += "&n_sess=1"),
                        i += "&del_ts=" + t.deltaTs.toString(),
                        t.sessionStartTime && (i += "&sess_t=" + t.sessionStartTime),
                        "1" === this.getItem("sbTrackNewUser") && (i += "&n_uid=1"),
                        "1" === this.getItem("sbTrackNewArrival") && (i += "&n_arr=1"),
                        this.getItem("sbTrackArrivalCID") && (i += "&arr_cid=" + this.getItem("sbTrackArrivalCID")),
                        this.getItem("sbTrackPrevArrivals") && (i += "&p_arr=" + this.getItem("sbTrackPrevArrivals")),
                        this.getItem("sbTrackPreArrivalImpression") && (i += "&p_imp=" + this.getItem("sbTrackPreArrivalImpression")),
                        this.getItem("sbTrackGclid") && (i += "&pub_cid=" + this.getItem("sbTrackGclid")),
                        this.getItem("sbTrackArrivalPage") && (i += "&a_page=" + encodeURIComponent(this.getItem("sbTrackArrivalPage"))),
                        "1" === this.getItem("sbTrackReset") && (i += "&reset=" + this.getItem("sbTrackReset")),
                        i += "&sess=" + t.sessionID,
                        i += "&uid=" + this.getItem("sbTrackUID"),
                        this.getItem("sbTrackArrivalID") && (i += "&aid=" + this.getItem("sbTrackArrivalID")),
                        i += "&page=" + encodeURIComponent(window.location.toString()),
                        "" !== this.getItem("sbTrackRef") && (i += "&ref=" + encodeURIComponent(this.getItem("sbTrackRef"))),
                        r && (i += "&cu_id=" + r),
                        t.p)
                        for (var n in t.p)
                            for (var c in t.p[n])
                                i += "&p_" + c + "=" + encodeURIComponent(t.p[n][c]);
                    t.gaid && (i += "&gaid=" + t.gaid),
                        t.idfa && (i += "&idfa=" + t.idfa),
                        t.ifa && (i += "&ifa=" + t.ifa),
                        t.apfid && (i += "&apfid=" + t.apfid),
                        t.clid ? this.setItem("sbTrackExternalClientID", t.clid) : this.getItem("sbTrackExternalClientID") && (t.clid = this.getItem("sbTrackExternalClientID")),
                        t.clid && (i += "&clid=" + t.clid),
                        e.setAttribute("src", i),
                        e.width = 0,
                        e.height = 0,
                        e.style.display = "none",
                        document.body ? document.body.appendChild(e) : document.head.appendChild(e),
                        this.setItem("sbTrackReset", "0"),
                        this.setItem("sbTrackNewUser", "0"),
                        this.setItem("sbTrackNewArrival", "0"),
                        this.itemTracked += 1
                } catch (t) { }
            },
            getSession: function () {
                try {
                    var t = this.getItem("sbTrackArrivalID");
                    return t || (t = this.getItem("sbTrackUID")),
                        t || "2"
                } catch (t) {
                    return "3"
                }
            },
            addSessionHistory: function () {
                try {
                    var t = new Date
                        , e = t.getUTCHours()
                        , r = t.getUTCDay()
                        , s = this.getItem("sbTrackStartSessionsHistory");
                    if (s)
                        s = s.split(",").map(Number);
                    else
                        for (s = [],
                            i = 0; i < 168; i++)
                            s.push(0);
                    s[24 * r + e] += 1,
                        this.setItem("sbTrackStartSessionsHistory", s.join(","))
                } catch (t) {
                    console.error(t)
                }
            },
            recalcSessionIfNeeded: function () {
                var t = this.getItem("sbTrackStartSessionTime")
                    , e = !1;
                t ? (t = parseInt(t),
                    Math.round(((new Date).getTime() - t) / 6e4) > 30 && (e = !0)) : e = !0;
                if (e) {
                    var i = this.generateID("s");
                    this.setItem("sbTrackSession", i),
                        this.setItem("sbTrackStartSessionTime", (new Date).getTime()),
                        this.setItem("sbTrackLastTrackTime", (new Date).getTime()),
                        this.setItem("sbTrackNewSession", "1"),
                        this.setItem("sbTrackSessionLastUrl", window.location.toString()),
                        this.addSessionHistory()
                }
            },
            addZeroToNumber: function (t) {
                return t < 10 ? "0" + t : t + ""
            },
            generateID: function (t) {
                var e = new Date
                    , i = function () {
                        return Math.floor(65536 * (1 + Math.random())).toString(16).substring(1)
                    };
                return this.addZeroToNumber(e.getFullYear()) + this.addZeroToNumber(e.getMonth() + 1) + this.addZeroToNumber(e.getDate()) + this.addZeroToNumber(e.getHours()) + this.addZeroToNumber(e.getMinutes()) + this.addZeroToNumber(e.getSeconds()) + "_" + t + "_" + i() + i() + i()
            },
            getFromUrl: function (t) {
                var e = "";
                try {
                    if (window.location.search.indexOf("?") > -1) {
                        var i = window.location.search.split("?")[1].split("&");
                        for (var r in i)
                            if (i[r].indexOf("=") > 0) {
                                var s = i[r].split("=")[0]
                                    , a = i[r].split("=")[1];
                                s === t && (e = a)
                            }
                    }
                } catch (t) { }
                return e
            },
            recalcUserIfNeeded: function (t) {
                var e = this.getItem("sbTrackUID")
                    , i = this.getFromUrl("prev_uid");
                if (i && i !== e) {
                    this.setItem("sbTrackUID", i);
                    var r = this.getFromUrl("prev_arrival_id");
                    r && this.setItem("sbTrackArrivalID", r);
                    var s = this.getFromUrl("prev_cid");
                    return s && this.setItem("sbTrackArrivalCID", s),
                        this.setItem("sbTrackReset", "0"),
                        this.setItem("sbTrackNewUser", "0"),
                        void this.setItem("sbTrackNewArrival", "0")
                }
                this.userID = e;
                var a = !1
                    , n = (this.getItem("sbTrackCustomerID"),
                        this.getFromUrl(this.cidName))
                    , c = this.getFromUrl("g_camp")
                    , o = this.getFromUrl("g_kw")
                    , d = this.getFromUrl("gclid")
                    , h = this.getFromUrl("enc_d");
                if (n)
                    this.getItem("sbTrackArrivalCID") !== n && (a = !0);
                else if (c) {
                    this.getItem("sbTrackGcamp") !== c && (a = !0)
                } else if (h) {
                    this.getItem("sbTrackEncd") !== h && (a = !0)
                } else if (d) {
                    this.getItem("sbTrackGclid") !== d && (a = !0)
                }
                var g = this.getFromUrl("tag");
                !a && g && (this.getItem("sbTrackTag") !== g && (a = !0));
                if (g && this.setItem("sbTrackTag", g),
                    a && (t = !0),
                    t && this.setItem("sbTrackReset", "1"),
                    e || (e = n && n.length > 10 ? n : this.generateID("u"),
                        this.setItem("sbTrackUID", e),
                        this.userID = e,
                        this.setItem("sbTrackNewUser", "1"),
                        t = !0),
                    t) {
                    var l = "";
                    this.addArrivalToHistory(),
                        l = n && n.length > 10 ? n : this.generateID("r"),
                        this.setItem("sbTrackArrivalID", l),
                        this.arrivalID = l,
                        this.setItem("sbTrackRef", document.referrer),
                        this.setItem("sbTrackArrivalCID", n),
                        this.setItem("sbTrackGcamp", c),
                        this.setItem("sbTrackGKW", o),
                        this.setItem("sbTrackEncd", h),
                        this.setItem("sbTrackGclid", d),
                        this.setItem("sbTrackArrivalPage", window.location.toString()),
                        this.setItem("sbTrackNewArrival", "1")
                }
            },
            setInDataStore: function (t, e) {
                var i = {};
                try {
                    this.getItem("sbTrackDataStore") && (i = JSON.parse(this.getItem("sbTrackDataStore")))
                } catch (t) { }
                i[t] = e,
                    this.setItem("sbTrackDataStore", JSON.stringify(i))
            },
            getFromDataStore: function (t) {
                var e = {};
                try {
                    this.getItem("sbTrackDataStore") && (e = JSON.parse(this.getItem("sbTrackDataStore")))
                } catch (t) { }
                return e[t]
            },
            addArrivalToHistory: function () {
                try {
                    var t = this.getItem("sbTrackArrivalID");
                    if (t) {
                        var e = this.getItem("sbTrackPrevArrivals");
                        e ? e += "-" : e = "",
                            e.length < 320 && (e += t,
                                this.setItem("sbTrackPrevArrivals", e))
                    }
                } catch (t) {
                    console.warn("warn prev arrivals")
                }
            },
            advSend: function () {
                if (!this.events || 0 === this.events.length)
                    return;
                var t = [];
                for (var e in this.events)
                    t.push(this.advTrack(this.events[e]));
                var i = {
                    events: t,
                    ac_id: this.acID,
                    ver: this.version
                };
                i.u_id = this.getItem("sbTrackUID"),
                    this.getItem("sbTrackArrivalID") && (i.a_id = this.getItem("sbTrackArrivalID")),
                    this.getItem("sbTrackPrevArrivals") && (i.p_arr = this.getItem("sbTrackPrevArrivals")),
                    this.getItem("sbTrackPreArrivalImpression") && (i.p_imp = this.getItem("sbTrackPreArrivalImpression")),
                    "" !== this.getItem("sbTrackRef") && (i.ref = this.getItem("sbTrackRef")),
                    this.getItem("sbTrackArrivalPage") && (i.a_page = this.getItem("sbTrackArrivalPage")),
                    this.getItem("sbTrackArrivalCID") && (i.arr_cid = this.getItem("sbTrackArrivalCID")),
                    this.getItem("sbTrackGclid") && (i.pub_cid = this.getItem("sbTrackGclid"));
                const r = JSON.stringify(i);
                this.events = [],
                    fetch(this.baseUrl + "/track", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        credentials: "include",
                        body: r
                    }).catch(function (t) { })
            },
            initRetargeting: function (t) {
                setTimeout(function () {
                    var e = {
                        ac_id: this.acID
                    };
                    const i = JSON.stringify(e);
                    fetch(this.baseUrl + "/track_re", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        credentials: "include",
                        body: i
                    }).then(function (t) {
                        try {
                            return 200 === t.status ? t.json() : {}
                        } catch (t) {
                            return {}
                        }
                    }).then(function (e) {
                        this.retargetingEvents = e,
                            t()
                    }
                        .bind(this))
                }
                    .bind(this), 200)
            },
            loadIframe: function () {
                function t(t) {
                    t.data && "iframeTrkInit" === t.data.messageType && this.init(t.data.initParams)
                }
                if (this.crossDomainEnabled) {
                    this.iframeTrk = window.document.createElement("iframe");
                    this.iframeTrk.setAttribute("src", "https://analytics-cdn.avatrade.io/analytics/57/iframe_track.html"),
                        this.iframeTrk.width = 0,
                        this.iframeTrk.height = 0,
                        this.iframeTrk.style.display = "none",
                        document.body ? document.body.appendChild(this.iframeTrk) : document.head.appendChild(this.iframeTrk),
                        window.addEventListener ? window.addEventListener("message", t.bind(this), !1) : window.attachEvent("onmessage", t.bind(this)),
                        setTimeout(function () {
                            this.init()
                        }
                            .bind(this), 1e4)
                } else
                    this.init()
            },
            init: function (t) {
                try {
                    if (t) {
                        var e = Object.keys(t);
                        for (var i in e) {
                            var r = e[i]
                                , s = t[r];
                            this.setItem(r, s, !0)
                        }
                    }
                    if (this.initialized)
                        return;
                    function a() {
                        if (this.recalcUserIfNeeded(!1),
                            this.recalcSessionIfNeeded(),
                            this.initialized = !0,
                            window.sbidTrackingTempQ)
                            for (var t in window.sbidTrackingTempQ) {
                                var e = window.sbidTrackingTempQ[t];
                                this.track(e)
                            }
                        if ("createEvent" in document) {
                            var i = document.createEvent("HTMLEvents");
                            i.initEvent("tracking_loaded", !1, !0),
                                (r = document.getElementById("sb_trk")) && r.dispatchEvent(i)
                        } else {
                            var r;
                            (r = document.getElementById("sb_trk")) && r.fireEvent("tracking_loaded")
                        }
                        this.advancedTracking && (setInterval(this.advSend.bind(this), 1e4),
                            (window.attachEvent || window.addEventListener)(window.attachEvent ? "onbeforeunload" : "beforeunload", function (t) {
                                for (var e in this.events)
                                    this.send(this.events[e])
                            }
                                .bind(this)))
                    }
                    if (this.initializing)
                        return;
                    this.initializing = !0,
                        this.retargetingEnabled ? this.initRetargeting(a.bind(this)) : a.bind(this)()
                } catch (t) {
                    console.warn("error initialize", t)
                }
            }
        },
        window.sbidTracking.loadIframe(),
        window.document.addEventListener("click", function (t) {
            try {
                var e = {
                    e: "click_in",
                    p: []
                };
                if (t.target.innerText && t.target.innerText.length < 32) {
                    var i = t.target.innerText;
                    i.length > 3 && e.p.push({
                        click_text: i
                    })
                }
                t.target.href && -1 == t.target.href.indexOf("javascript:") && (e.p.push({
                    click_dst: t.target.href
                }),
                    t.target.hostname !== window.location.hostname && (e.e = "click_out")),
                    t.target.id && e.p.push({
                        element_id: t.target.id
                    }),
                    e.p.length > 0 && window.sbidTracking.track(e)
            } catch (t) { }
        }, !0),
        window.document.addEventListener("play", function () {
            window.sbidTracking.track({
                e: "video_start"
            })
        }, !0),
        window.document.addEventListener("paused", function () {
            window.sbidTracking.track({
                e: "video_pause"
            })
        }, !0),
        window.document.addEventListener("ended", function () {
            window.sbidTracking.track({
                e: "video_end"
            })
        }, !0),
        window.sbidTracking.loadedScript = !0;
    var vimeoVids = document.querySelectorAll("iframe[src*='vimeo']");
    if (vimeoVids.length > 0) {
        var vimeoScript = document.createElement("script");
        vimeoScript.setAttribute("type", "text/javascript"),
            vimeoScript.setAttribute("src", "https://player.vimeo.com/api/player.js"),
            document.getElementsByTagName("body")[0].appendChild(vimeoScript),
            vimeoScript.readyState ? vimeoScript.onreadystatechange = function () {
                "loaded" !== vimeoScript.readyState && "complete" !== vimeoScript.readyState || (vimeoScript.onreadystatechange = null,
                    vimeo_listeners())
            }
                : vimeoScript.onload = function () {
                    vimeo_listeners()
                }
    }
    function vimeo_listeners() {
        for (var t = 0; t < vimeoVids.length; t++) {
            var e = vimeoVids[t]
                , i = new Vimeo.Player(e);
            i.on("ended", function () {
                const t = new Event("ended");
                document.dispatchEvent(t)
            }),
                i.on("play", function () {
                    const t = new Event("play");
                    document.dispatchEvent(t)
                }),
                i.on("pause", function () {
                    const t = new Event("paused");
                    document.dispatchEvent(t)
                })
        }
    }
    var youtubeVids = document.querySelectorAll("iframe[src*='youtube']");
    if (youtubeVids.length > 0) {
        var youtubeScript = document.createElement("script");
        youtubeScript.src = "//www.youtube.com/iframe_api";
        var player, currentVid, firstScriptTag = document.getElementsByTagName("script")[0];
        function onYouTubeIframeAPIReady() {
            for (var t = document.querySelectorAll("iframe[src*='youtube']"), e = 0; e < t.length; e++)
                (currentVid = t[e]).src.indexOf("?") > -1 ? currentVid.setAttribute("src", currentVid.src + "&enablejsapi=1") : currentVid.setAttribute("src", currentVid.src + "?enablejsapi=1"),
                    currentVid.id || currentVid.setAttribute("id", "yt_video_" + e),
                    player = new YT.Player(currentVid.id, {
                        events: {
                            onReady: onPlayerReady,
                            onStateChange: onPlayerStateChange
                        }
                    })
        }
        function onPlayerReady(t) { }
        function onPlayerStateChange(t) {
            switch (t.data) {
                case YT.PlayerState.PLAYING:
                    const e = new Event("play");
                    document.dispatchEvent(e);
                    break;
                case YT.PlayerState.PAUSED:
                    const i = new Event("paused");
                    document.dispatchEvent(i);
                    break;
                case YT.PlayerState.ENDED:
                    const r = new Event("ended");
                    document.dispatchEvent(r);
                    break;
                default:
                    return
            }
        }
        firstScriptTag.parentNode.insertBefore(youtubeScript, firstScriptTag)
    }
}
