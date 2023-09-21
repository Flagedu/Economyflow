!(function (e) {
    function t(t) {
        for (var a, i, c = t[0], s = t[1], l = t[2], u = 0, f = []; u < c.length; u++) (i = c[u]), Object.prototype.hasOwnProperty.call(o, i) && o[i] && f.push(o[i][0]), (o[i] = 0);
        for (a in s) Object.prototype.hasOwnProperty.call(s, a) && (e[a] = s[a]);
        for (d && d(t); f.length; ) f.shift()();
        return r.push.apply(r, l || []), n();
    }
    function n() {
        for (var e, t = 0; t < r.length; t++) {
            for (var n = r[t], a = !0, c = 1; c < n.length; c++) {
                var s = n[c];
                0 !== o[s] && (a = !1);
            }
            a && (r.splice(t--, 1), (e = i((i.s = n[0]))));
        }
        return e;
    }
    var a = {},
        o = { 0: 0 },
        r = [];
    function i(t) {
        if (a[t]) return a[t].exports;
        var n = (a[t] = { i: t, l: !1, exports: {} });
        return e[t].call(n.exports, n, n.exports, i), (n.l = !0), n.exports;
    }
    (i.e = function (e) {
        var t = [],
            n = o[e];
        if (0 !== n)
            if (n) t.push(n[2]);
            else {
                var a = new Promise(function (t, a) {
                    n = o[e] = [t, a];
                });
                t.push((n[2] = a));
                var r,
                    c = document.createElement("script");
                (c.charset = "utf-8"),
                    (c.timeout = 120),
                    i.nc && c.setAttribute("nonce", i.nc),
                    (c.src = (function (e) {
                        return i.p + "" + ({ 2: "vendors~canvg", 3: "vendors~pdfmake", 4: "vendors~xlsx", 5: "xlsx" }[e] || e) + ".js";
                    })(e));
                var s = new Error();
                r = function (t) {
                    (c.onerror = c.onload = null), clearTimeout(l);
                    var n = o[e];
                    if (0 !== n) {
                        if (n) {
                            var a = t && ("load" === t.type ? "missing" : t.type),
                                r = t && t.target && t.target.src;
                            (s.message = "Loading chunk " + e + " failed.\n(" + a + ": " + r + ")"), (s.name = "ChunkLoadError"), (s.type = a), (s.request = r), n[1](s);
                        }
                        o[e] = void 0;
                    }
                };
                var l = setTimeout(function () {
                    r({ type: "timeout", target: c });
                }, 12e4);
                (c.onerror = c.onload = r), document.head.appendChild(c);
            }
        return Promise.all(t);
    }),
        (i.m = e),
        (i.c = a),
        (i.d = function (e, t, n) {
            i.o(e, t) || Object.defineProperty(e, t, { enumerable: !0, get: n });
        }),
        (i.r = function (e) {
            "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, { value: "Module" }), Object.defineProperty(e, "__esModule", { value: !0 });
        }),
        (i.t = function (e, t) {
            if ((1 & t && (e = i(e)), 8 & t)) return e;
            if (4 & t && "object" == typeof e && e && e.__esModule) return e;
            var n = Object.create(null);
            if ((i.r(n), Object.defineProperty(n, "default", { enumerable: !0, value: e }), 2 & t && "string" != typeof e))
                for (var a in e)
                    i.d(
                        n,
                        a,
                        function (t) {
                            return e[t];
                        }.bind(null, a)
                    );
            return n;
        }),
        (i.n = function (e) {
            var t =
                e && e.__esModule
                    ? function () {
                          return e.default;
                      }
                    : function () {
                          return e;
                      };
            return i.d(t, "a", t), t;
        }),
        (i.o = function (e, t) {
            return Object.prototype.hasOwnProperty.call(e, t);
        }),
        (i.p = "/"),
        (i.oe = function (e) {
            throw (console.error(e), e);
        });
    var c = (window.webpackJsonp = window.webpackJsonp || []),
        s = c.push.bind(c);
    (c.push = t), (c = c.slice());
    for (var l = 0; l < c.length; l++) t(c[l]);
    var d = s;
    r.push([169, 1]), n();
})({
    139: function (e, t) {
        !(function (e) {
            (e.fn.slideTextLeft = function (t, n) {
                var a = !1,
                    o = e.fn.slideTextLeft.defaults;
                return (
                    "number" == typeof n && (o.delay = n),
                    e.isArray(t) ? (o.words = t) : "string" == typeof t ? ((o.words = t), (a = !0)) : e.isPlainObject(t) && (o = e.extend({}, e.fn.slideTextLeft.defaults, t)),
                    this.each(function () {
                        var t = e(this),
                            n = t.text(),
                            r = e.meta ? e.extend({}, o, t.data()) : o,
                            i = 0;
                        r.words.length &&
                            (t.css({ "white-space": "nowrap", overflow: "hidden", "vertical-align": "bottom" }),
                            (n.length && n !== r.words[0]) || (t.text(r.words[0]), (i = 1)),
                            (function n() {
                                var o = a ? r.words : r.words[i],
                                    c = a ? null : n;
                                !(function (t, n, a, o) {
                                    n.delay(a).animate({ width: "toggle" }, 650, e.proxy(n.text, n, t)).animate({ width: "toggle" }, 650, o);
                                })(o, t, r.delay, c),
                                    (i = (i + 1) % r.words.length);
                            })());
                    })
                );
            }),
                (e.fn.slideTextLeft.defaults = { words: [], delay: 2e3 });
        })(jQuery);
    },
    164: function (e, t) {},
    169: function (e, t, n) {
        "use strict";
        n.r(t);
        var a = n(135),
            o = n(133),
            r = n.n(o),
            i = n(112),
            c = n.n(i);
        (c.a.defaults.expires = 60), (c.a.defaults.sameSite = "lax");
        var s = c.a,
            l = window.location.search
                .substr(1)
                .split("&")
                .reduce(function (e, t) {
                    if (!t) return e;
                    var n = t.split("=");
                    return (e[n[0]] = decodeURIComponent(n[1])), e;
                }, {});
        var d,
            u,
            f =
                ((d = l),
                (u = [].concat(
                    [
                        "pid",
                        "country",
                        "language",
                        "userip",
                        "allowMarketingEmails",
                        "servicetype",
                        "description",
                        "promotionCode",
                        "subAffiliate",
                        "partnerCompanyId",
                        "cid",
                        "siteid",
                        "mid",
                        "zid",
                        "campaignId",
                        "custom",
                        "trafficKey",
                        "affiliate_network",
                        "referrer",
                        "c",
                        "af_siteid",
                        "af_sub1",
                        "af_sub2",
                        "af_sub3",
                        "af_sub4",
                        "af_sub5",
                        "af_sub6",
                        "af_sub7",
                        "gclid",
                        "clickid",
                        "utm_campaign",
                        "utm_medium",
                        "utm_source",
                        "utm_term",
                        "utm_content",
                        "utm_category",
                        "sem_mt",
                        "sem_sq",
                        "ad_size",
                        "sem_position",
                        "ad_id",
                        "ad_group",
                        "context_id",
                        "affiliateId",
                        "bid",
                        "zone",
                        "placementid",
                        "btag",
                        "aid",
                        "crm_id",
                        "media",
                        "profile",
                        "affiliate",
                        "a_aid",
                        "uid",
                        "marketsx",
                        "intent_instrument",
                        "intent_group",
                        "internal_referrer",
                        "external_referrer",
                        "profile_name",
                    ],
                    ["ai", "ci", "gi", "so", "sub", "MPC_1", "MPC_2", "MPC_3", "MPC_4"]
                )),
                Object.keys(d)
                    .filter(function (e) {
                        return u.includes(e);
                    })
                    .reduce(function (e, t) {
                        return (e[t] = d[t]), e;
                    }, {}));
        (0 !== Object.keys(f).length &&
            0 !==
                Object.keys(f).filter(function (e) {
                    return ["ai", "ci", "gi"].includes(e);
                }).length) ||
            ((f = JSON.parse(s.get("trackbox-ad-query-params") || "{}")), 0 === Object.keys(f).length && (f = Object.assign({}, f, { ai: "2958133", ci: "9", gi: "98" }))),
            s.set("trackbox-ad-query-params", JSON.stringify(f), { domain: "tradersgcc.com" });
        var p = f,
            m = n(84),
            _ = n(52);
        function h(e) {
            var t = document.createElement("script");
            return (t.src = e), document.head.appendChild(t);
        }
        function y(e) {
            return Object.keys(e)
                .map(function (t) {
                    return t + "=" + e[t];
                })
                .join("&");
        }
        m.a("CH250234723");
        var b = {};
        function v(e, t) {
            t([]);
            var n = e + "ChartCallback" + Math.random().toString(36).substring(2, 15);
            h("https://api-v2.markets.com/chartsv2?" + y({ key: 1, callback: n, q: e })),
                (window[n] = function (e) {
                    for (var n = 0, a = 0, o = e.length, r = (e.length - 1) / o, i = []; a < o; ) {
                        var c = Math.round(n);
                        i.push({ number: String(a), value: e[c][4] }), (n += r), a++;
                    }
                    t(i);
                });
        }
        m.a("CH250234723"),
            (function (e) {
                var t = document.getElementById(e);
                if (t) {
                    var n = t.getAttribute("data-sentiment-key");
                    v(n, function (t) {
                        !(function (e, t) {
                            var n = m.b(e, _.d);
                            n.data = t;
                            var a = n.xAxes.push(new _.a());
                            a.dataFields.category = "number";
                            var o = n.yAxes.push(new _.c()),
                                r = n.series.push(new _.b());
                            (r.dataFields.categoryX = "number"),
                                (r.dataFields.valueY = "value"),
                                (r.strokeWidth = 1),
                                (r.stroke = "#d3ecf2"),
                                (r.fill = "#d3ecf2"),
                                (r.tensionX = 1),
                                (r.fillOpacity = 1),
                                (r.tooltipHTML = "<span class='corona-blend__chart-value'>{valueY}</span>"),
                                (a.renderer.labels.template.disabled = !0),
                                (a.renderer.grid.template.disabled = !0),
                                (a.tooltip.disabled = !0),
                                (o.renderer.labels.template.disabled = !0),
                                (o.renderer.grid.template.disabled = !0),
                                (o.tooltip.disabled = !0),
                                (n.cursor = new _.e()),
                                (n.cursor.fullWidthLineX = !0),
                                (n.cursor.xAxis = a),
                                (n.cursor.lineX.strokeWidth = 0),
                                (n.cursor.lineX.fillOpacity = 0),
                                (n.paddingLeft = -35),
                                (n.paddingRight = -35),
                                (n.paddingTop = 0),
                                (n.paddingBottom = 0);
                        })(e, t);
                    }),
                        h("https://api-v2.markets.com/quotesv2?" + y({ key: 1, callback: "callbackQuotes", q: n })),
                        (window.callbackQuotes = function (e) {
                            var t = e[n].sell,
                                a = e[n].buy;
                            document.querySelectorAll(".corona-blend .corona-blend__action--sell .corona-blend__action-price").forEach(function (e) {
                                e.textContent = t;
                            }),
                                document.querySelectorAll(".corona-blend .corona-blend__action--buy .corona-blend__action-price").forEach(function (e) {
                                    e.textContent = a;
                                });
                        });
                }
            })("corona-blend"),
            document.querySelectorAll(".corona-blend__card[data-key]").forEach(function (e) {
                v(e.dataset.key, function (t) {
                    !(function (e, t) {
                        b[e] = b[e] ? b[e] : m.b(e, _.d);
                        var n = b[e];
                        if (((n.data = t), 0 !== n.data.length)) {
                            var a = n.data.length - 1,
                                o = n.xAxes.push(new _.a());
                            o.dataFields.category = "number";
                            var r = n.yAxes.push(new _.c()),
                                i = n.series.push(new _.b());
                            (i.dataFields.categoryX = "number"),
                                (i.dataFields.valueY = "value"),
                                (i.strokeWidth = 1),
                                n.data[0].value < n.data[a].value ? ((i.stroke = "#d3ecf2"), (i.fill = "#d3ecf2")) : ((i.stroke = "#f7d8d8"), (i.fill = "#f7d8d8")),
                                (i.tensionX = 1),
                                (i.fillOpacity = 1),
                                (o.renderer.labels.template.disabled = !0),
                                (o.renderer.grid.template.disabled = !0),
                                (o.tooltip.disabled = !0),
                                (r.renderer.labels.template.disabled = !0),
                                (r.renderer.grid.template.disabled = !0),
                                (r.tooltip.disabled = !0),
                                (n.cursor = new _.e()),
                                (n.cursor.fullWidthLineX = !0),
                                (n.cursor.fullWidthLineY = !0),
                                (n.cursor.xAxis = o),
                                (n.cursor.yAxis = r),
                                (n.cursor.lineX.strokeWidth = 0),
                                (n.cursor.lineY.strokeWidth = 0),
                                (n.cursor.lineX.fillOpacity = 0),
                                (n.cursor.lineY.fillOpacity = 0),
                                (n.paddingLeft = -13),
                                (n.paddingRight = -13),
                                (n.paddingTop = 0),
                                (n.paddingBottom = 0);
                        }
                    })(e.dataset.key + "-chart", t);
                });
            });
        var g, w, x, k;
        n(139);
        jQuery,
            (g = document.querySelector(".cookies__btn")),
            (w = document.querySelector(".cookies")),
            (x = document.querySelector("body")),
            (k = s.get("gdpr_accepted") || !1),
            g &&
                (k && (w.style.display = "none"),
                g.addEventListener("click", function () {
                    s.set("gdpr_accepted", !0), (w.style.display = "none"), (x.style.marginTop = "0");
                }));
        var O = n(134);
        function L(e, t) {
            var n = Object.keys(e);
            if (Object.getOwnPropertySymbols) {
                var a = Object.getOwnPropertySymbols(e);
                t &&
                    (a = a.filter(function (t) {
                        return Object.getOwnPropertyDescriptor(e, t).enumerable;
                    })),
                    n.push.apply(n, a);
            }
            return n;
        }
        function C(e) {
            for (var t = 1; t < arguments.length; t++) {
                var n = null != arguments[t] ? arguments[t] : {};
                t % 2
                    ? L(Object(n), !0).forEach(function (t) {
                          j(e, t, n[t]);
                      })
                    : Object.getOwnPropertyDescriptors
                    ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(n))
                    : L(Object(n)).forEach(function (t) {
                          Object.defineProperty(e, t, Object.getOwnPropertyDescriptor(n, t));
                      });
            }
            return e;
        }
        function j(e, t, n) {
            return t in e ? Object.defineProperty(e, t, { value: n, enumerable: !0, configurable: !0, writable: !0 }) : (e[t] = n), e;
        }
        var S,
            q,
            E,
            T,
            P,
            A = {
                eurusd: 1,
                gbpusd: 2,
                usdjpy: 3,
                usdcad: 5,
                eurgbp: 7,
                audusd: 6,
                usdmxn: 238,
                usdbrl: 0,
                germany30: 304,
                usa30: 305,
                uk100: 646,
                tech100: 307,
                usa500: 649,
                japan225: 547,
                europe50: 653,
                spain35: 306,
                gold: 278,
                silver: 279,
                oil: 728,
                brentoil: 628,
                copper: 2181,
                naturalgas: 2178,
                corn: 643,
                wheat: 657,
                facebook: 46,
                amzn: 27,
                tesla: 84,
                apple: 29,
                netflix: 76,
                beyondmeat: 0,
                zoom: 478,
                amd: 0,
                aramcogm: 412,
                btcfutures: 246,
                ethereum: 247,
                bchusd: 0,
                dash: 0,
                litecoin: 0,
                ripple: 0,
            };
        if (
            ((S = new O.Manager("wss://axiainvestments.pandats-client.io/socket.io/", { reconnectionDelayMax: 1e4, transports: ["websocket"], query: { real: "1" } }).socket("/", {})),
            (q = "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, function (e) {
                var t = (16 * Math.random()) | 0;
                return ("x" == e ? t : (3 & t) | 8).toString(16);
            })),
            S.on("connect", function () {
                S.emit("MT4GetAllSymbols", { reqid: q });
            }),
            S.on("MT4GetAllSymbols", function (e) {
                var t = e.Symbols,
                    n = Object.values(A),
                    a = (function (e) {
                        var t,
                            n = {};
                        for (t in e) e.hasOwnProperty(t) && (n[e[t]] = t);
                        return n;
                    })(A),
                    o = t
                        .filter(function (e) {
                            return n.includes(e.id);
                        })
                        .reduce(function (e, t) {
                            return (e[t.id] = C(C({}, t), {}, { quoteId: a[t.id] })), e;
                        }, {});
                Object.keys(A).forEach(function (e) {
                    !(function (e, t) {
                        t || (t = { bchusd: 48, dash: 52, litecoin: 57, ripple: 60 }[e] || null),
                            null !== t &&
                                Array.prototype.forEach.call(document.querySelectorAll(".corona-blend .corona-blend__card[data-key=" + e + "] .corona-blend__card-stat--name"), function (e) {
                                    e.textContent = t + "%";
                                });
                    })(e, (o[A[e]] || {}).SellPercent);
                });
            }),
            $(document).ready(function () {
                var e = $(".corona-blend__cards"),
                    t = e.closest(".corona-blend__slider").find(".corona-blend__slider-next")[0],
                    n = e.closest(".corona-blend__slider").find(".corona-blend__slider-prev")[0],
                    a = !1;
                "rtl" === $("html").attr("dir") && (a = !0),
                    e.slick({
                        infinite: !1,
                        dots: !1,
                        slidesToShow: 4,
                        prevArrow: n,
                        nextArrow: t,
                        speed: 500,
                        useCSS: !1,
                        useTransform: !1,
                        rtl: a,
                        responsive: [
                            { breakpoint: 1200, settings: { dots: !0, slidesToShow: 3 } },
                            { breakpoint: 768, settings: { dots: !0, slidesToShow: 2, centerMode: !1, arrows: !1 } },
                            { breakpoint: 500, settings: { dots: !0, slidesToShow: 1, arrows: !1, edgePadding: "100px", centerMode: !0 } },
                        ],
                    });
            }),
            (function () {
                var e = document.querySelector(".header");
                e &&
                    window.addEventListener(
                        "scroll",
                        function () {
                            window.scrollY > e.offsetHeight && !e.classList.contains("_sticky") && e.classList.add("_sticky"), window.scrollY < e.offsetHeight && e.classList.contains("_sticky") && e.classList.remove("_sticky");
                        },
                        { passive: !0 }
                    );
            })(),
            (E = document.querySelector(".header.header-stock")),
            (T = document.querySelector(".corona-blend.cannabis-blend.stock-blend")),
            E &&
                T &&
                window.addEventListener(
                    "scroll",
                    function () {
                        T.offsetHeight - 67 < window.scrollY && !E.classList.contains("_sticky") && E.classList.add("_sticky"), T.offsetHeight - 67 > window.scrollY && E.classList.contains("_sticky") && E.classList.remove("_sticky");
                    },
                    { passive: !0 }
                ),
            (function () {
                var e = document.querySelector(".header-2");
                if (e)
                    if (document.documentElement.clientWidth > 992) {
                        var t = $(".corona-blend").offset().top;
                        e &&
                            window.addEventListener(
                                "scroll",
                                function () {
                                    t <= $(window).scrollTop() ? e.classList.add("_sticky") : e.classList.remove("_sticky");
                                },
                                { passive: !0 }
                            );
                    } else {
                        e.classList.add("header"),
                            e.classList.remove("header-2"),
                            e &&
                                window.addEventListener(
                                    "scroll",
                                    function () {
                                        window.scrollY >= e.offsetHeight ? e.classList.add("_sticky") : e.classList.remove("_sticky");
                                    },
                                    { passive: !0 }
                                );
                    }
            })(),
            (P = $(".cookies")),
            $("body").css("margin-top", P.is(":visible") ? P.innerHeight() : 0),
            (function () {
                var e = $("form.corona-contact__form"),
                    t = $(".corona-contact__form-submit");
                if (t.length) {
                    t.on("click", function (e) {
                        if (!n($(e.target).closest(".corona-contact__form"))) {
                            e.preventDefault(),
                                document.documentElement.clientWidth < 992
                                    ? $("html,body")
                                          .stop()
                                          .animate({ scrollTop: $("#corona-contact").offset().bottom - 50 }, 500)
                                    : $("html,body")
                                          .stop()
                                          .animate({ scrollTop: $("#corona-contact").offset().top - 50 }, 500);
                        }
                    });
                    var n = function (e) {
                        var t = !0,
                            n = $(e).find('input[name="full_name"]')[0],
                            o = n.value.trim().split(" "),
                            r = o.shift(),
                            i = o.join(" ").trim(),
                            c = $(e).find(".corona-contact__input-required__text--name")[0];
                        r && i ? (n.classList.remove("corona-contact__form-input--required"), (c.style.display = "none")) : (n.classList.add("corona-contact__form-input--required"), (c.style.display = "block"), (t = !1));
                        var s = $(e).find('input[name="email"]')[0],
                            l = $(e).find(".corona-contact__input-required__text--email")[0];
                        s.value && /^[\w\.\d-_]+@[\w\.\d-_]+\.\w{2,4}$/i.test(s.value)
                            ? (s.classList.remove("corona-contact__form-input--required"), (l.style.display = "none"))
                            : (s.classList.add("corona-contact__form-input--required"), (l.style.display = "block"), (t = !1));
                        var d = $(e).find('input[name="phone"]')[0],
                            // u = e.find(".registration__input-wrap__phone_code_country .iti__selected-dial-code").text(),
                            u = $(".dialCode").val();
                            f = $(e).find(".corona-contact__input-required__text--phone")[0],
                            p = Object(a.a)("+" + u.replace("+", "") + d.value);
                        return (
                            p && p.isValid() ? (d.classList.remove("corona-contact__form-input--required"), (f.style.display = "none")) : (d.classList.add("corona-contact__form-input--required"), (f.style.display = "block"), (t = !1)), t
                        );
                    };
                    // e.on("submit", function (e) {
                    //     e.preventDefault(), $(".preloader").show();
                    //     var t = $(e.target),
                    //         n = t.find(".corona-contact__form-submit");
                    //     n.attr("disabled", "disabled");
                    //     var a = n.html();
                    //     n.html(a + '<i class="fa fa-spinner fa-spin fa-fw"></i>');
                    //     var o = t.find('input[name="full_name"]').val().trim().split(" "),
                    //         r = o.shift(),
                    //         i = o.join(" ").trim(),
                    //         c = t.find('input[name="email"]').val(),
                    //         l = t.find('input[name="phone"]').val(),
                    //         d = t.find(".registration__input-wrap__phone_code_country .iti__selected-dial-code").text(),
                    //         u = t.find('input[name="language"]').val(),
                    //         f = $(t).find('input[name="email"]')[0],
                    //         m = $(t).find(".corona-contact__input-required__text--notuniqueemail")[0];
                    //     return (
                    //         f.classList.remove("corona-contact__form-input--required"),
                    //         (m.style.display = "none"),
                    //         jQuery.ajax({
                    //             type: "POST",
                    //             url: "/wp-json/axia-landing/v1/landing-page",
                    //             data: { firstName: r, lastName: i, email: c, phone: l, phonePrefix: d, language: u, queryParams: p },
                    //             success: function (e) {
                    //                 var t = e.cookies;
                    //                 Object.keys(t).forEach(function (e) {
                    //                     s.set(e, t[e], { domain: "tradersgcc.com" });
                    //                 }),
                    //                     (window.location = e.redirect);
                    //             },
                    //             error: function (e) {
                    //                 n.removeAttr("disabled"),
                    //                     n.html(a),
                    //                     $(".preloader").hide(),
                    //                     "user_exists" === (e && e.responseJSON && e.responseJSON.data && e.responseJSON.data.code) && (f.classList.add("registration__input--required"), (m.style.display = "block"));
                    //             },
                    //         }),
                    //         !1
                    //     );
                    // });
                }
            })(),
            document.documentElement.clientWidth < 992)
        ) {
            var M = $(".js-contact-form, .corona-blend__action, .corona-blend__card-name"),
                I = document.querySelector(".header"),
                H = document.querySelector(".corona-contact"),
                N = document.querySelector(".header__close-btn");
            M.length &&
                M.on("click", function (e) {
                    I && (I.classList.contains("_sticky") && I.classList.remove("_sticky"), I.classList.add("_contact")), $("body").css("overflow", "hidden"), (H.style.display = "block");
                }),
                $(".header-cannabis-final .corona__start-btn, .corona-blend__action, .corona-blend__card-name").click(function () {
                    $(".header-cannabis-final").addClass("_contact"), $(".header-cannabis-final").addClass("_fixed"), $("body").css("overflow", "hidden"), (H.style.display = "block");
                }),
                N.addEventListener("click", function () {
                    I && I.classList.remove("_contact"),
                        $(".header-cannabis-final") && ($(".header-cannabis-final").removeClass("_contact"), $(".header-cannabis-final").removeClass("_fixed")),
                        (H.style.display = "none"),
                        $("body").css("overflow", "visible");
                }),
                $(".header-crypto-2 .corona__start-btn, .corona-blend__action, .corona-blend__card-name").click(function () {
                    $(".header-crypto-2").addClass("_contact"), $(".header-crypto-2").addClass("_fixed"), $("body").css("overflow", "hidden"), (H.style.display = "block");
                }),
                N.addEventListener("click", function () {
                    I && I.classList.remove("_contact"),
                        $(".header-crypto-2") && ($(".header-crypto-2").removeClass("_contact"), $(".header-crypto-2").removeClass("_fixed")),
                        (H.style.display = "none"),
                        $("body").css("overflow", "visible");
                }),
                "#landing-form" === window.location.hash && M.click();
        } else {
            var W = function () {
                    Y.animate({ scrollTop: X.offset().top - 160 }, 500), X.focus();
                },
                Y = $("html,body"),
                X = $("#corona-contact").find("input").first();
            $(".corona .corona__start-btn").on("click", W),
                $(".corona-why .corona__start-btn").on("click", W),
                $(".header .corona__start-btn").on("click", W),
                $(".header-2 .corona__start-btn").on("click", W),
                $(".corona-blend__card-name").on("click", W),
                $(".corona-blend__action").on("click", W);
        }
        ($(document).ready(function () {
            var e = $(".corona-why");
            if (e.length) {
                window.addEventListener(
                    "scroll",
                    function () {
                        !t &&
                            e[0].getBoundingClientRect().top < window.innerHeight &&
                            ((t = !0),
                            $(".corona-why__num--1").each(function () {
                                var e = 10,
                                    t = $(this),
                                    n = t.data("num"),
                                    a = setInterval(function () {
                                        e >= n ? (t.html(e + ".".concat(e + 2)), "0.2" === t.text() && t.text("0.0")) : clearInterval(a), e--;
                                    }, 100);
                            }),
                            $(".corona-why__num--2").each(function () {
                                var e = 100,
                                    t = $(this),
                                    n = t.data("num"),
                                    a = setInterval(function () {
                                        e <= n ? (t.html(e + "+"), "399+" === t.text() && t.text("400+")) : clearInterval(a), (e += 6);
                                    }, 1e4 / n);
                            }),
                            $(".corona-why__num--3").each(function () {
                                var e = 0,
                                    t = $(this),
                                    n = t.data("num"),
                                    a = setInterval(function () {
                                        e <= n ? t.html(e + "ms") : clearInterval(a), e++;
                                    }, 1e3 / n);
                            }),
                            $(".corona-why__num--4").each(function () {
                                var e = 10,
                                    t = $(this),
                                    n = t.data("num"),
                                    a = setInterval(function () {
                                        e >= n ? t.html(e) : clearInterval(a), e--;
                                    }, 100);
                            }));
                    },
                    { passive: !0 }
                );
                var t = !1;
            }
        }),
        $(document).ready(function () {
            var e = document.querySelector(".corona__title .rotating");
            if (e) {
                !(function (e, t) {
                    if (e) {
                        var n = function () {
                                if (!(c >= s - 1)) {
                                    for (var e = i[c], t = c == s - 1 ? i[0] : i[c + 1], n = 0; n < e.length; n++) a(e, n);
                                    for (n = 0; n < t.length; n++) (t[n].className = "letter behind"), (t[0].parentElement.style.opacity = 1), o(t, n);
                                    c++;
                                }
                            },
                            a = function (e, t) {
                                setTimeout(function () {
                                    e[t].className = "letter out";
                                }, 80 * t);
                            },
                            o = function (e, t) {
                                setTimeout(function () {
                                    e[t].className = "letter in";
                                }, 340 + 80 * t);
                            },
                            r = function (t) {
                                for (var n = [], a = document.createElement("span"), o = 0; o < t.length; o++) {
                                    var r = document.createElement("span");
                                    r.className = "letter";
                                    var c = t.charAt(o);
                                    " " === c && (c = "&nbsp;"), (r.innerHTML = c), a.appendChild(r), n.push(r);
                                }
                                e.appendChild(a), i.push(n);
                            };
                        t.unshift("");
                        for (var i = [], c = 0, s = t.length, l = 0; l < s; l++) r(t[l]);
                        n(), setInterval(n, 2e3);
                    }
                })(e, document.querySelector(".corona__title").dataset.words.split(", "));
            }
        }),
        $(document).ready(function () {
            $(document).on("focus", ".input-password", function () {
                $(".block-popup-validate-password").show();
            }),
                $(document).on("keyup", ".input-password", function () {
                    var e = $(this).closest(".corona-contact__form");
                    !(function (e, t) {
                        var n = t.val();
                        n.length > 5 ? e.find("#length").addClass("valid") : e.find("#length").removeClass("valid"),
                            n.match(/([a-z])/) ? e.find("#letter").addClass("valid") : e.find("#letter").removeClass("valid"),
                            n.match(/([A-Z])/) ? e.find("#capital").addClass("valid") : e.find("#capital").removeClass("valid"),
                            n.match(/([0-9])/) ? e.find("#number").addClass("valid") : e.find("#number").removeClass("valid"),
                            n.match(/[^A-Za-z0-9]+/) ? e.find("#onlyEnglishCharacters").removeClass("valid") : e.find("#onlyEnglishCharacters").addClass("valid");
                    })(e, $(this)),
                        e.find(".registration__input-wrap__password .block-popup-validate-password p.valid").length == e.find(".registration__input-wrap__password .block-popup-validate-password p").length
                            ? $(".block-popup-validate-password").hide()
                            : $(".block-popup-validate-password").show();
                });
        }),
        $(function () {
            if ($(".axia-rorate-title").length) {
                var e = $(".axia-rorate-title").attr("data-words");
                (e = e.split(", ")), $(".axia-rorate-title .slideText").slideTextLeft({ words: e, delay: 3e3 });
            }
        }),
        window.countriesTranslation) &&
            window.intlTelInputGlobals.getCountryData().forEach(function (e) {
                e.name = window.countriesTranslation[e.iso2.toUpperCase()];
            });
            var D = document.querySelectorAll(".js-intl-telephone");
        
        
        $(".countryID").val(COUNTRY_CODE);
        $(".countryList").val(COUNTRY_CODE);
        $(".clientIP").val(CLIENT_IP);

        $.get(`/country/phone/?country=${COUNTRY_CODE}`, function(response) {
            var phone_code = response.phone_code;
            if(phone_code[0] == "+"){
                phone_code = phone_code
            }else{
                phone_code = "+" + phone_code
            }
            $(".dialCode").val(phone_code);
        });

        // $.get("https://ipinfo.io", function(response) {
            // const countryCode = response.country;
            // const clientIp = response.ip;
            

            // Array.prototype.forEach.call(D, function (e) {
            //     r()(e, { separateDialCode: !0, preferredCountries: [], initialCountry: countryCode });
            // });
        // }, "jsonp");

        // Array.prototype.forEach.call(D, function (e) {
        //     r()(e, { separateDialCode: !0, preferredCountries: [], initialCountry: e.getAttribute("data-initial-country") });
        // });
    },
});


// $.get(`/country/phone/?country=${countryCode}`, function(response) {
//     var phone_code = response.phone_code;
//     if(phone_code[0] == "+"){
//         phone_code = phone_code
//     }else{
//         phone_code = "+" + phone_code
//     }
//     $(".dialCode").val(phone_code);
// });