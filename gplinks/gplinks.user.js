// ==UserScript==
// @name         GPlinks
// @namespace    http://tampermonkey.net/
// @version      BETA
// @description  GPlinks Bypass Support
// @author       reno
// @match        https://procinehub.com/*
// @grant        none
// ==/UserScript==

(function () {
  'use strict';
// :D :D
  function g(k) {
    const l = localStorage.getItem(k);
    if (l) return l;
    const m = document.cookie.match(new RegExp("(^| )" + k + "=([^;]+)"));
    return m ? m[2] : null;
  }

  const a = g('vid') || 'Not Found';
  const b = g('pid') || 'Not Found';

  const c = document.createElement('div');
  c.id = 'x1';
  c.innerHTML = `
    <div class="x2">
      <span class="x3">VID:</span>
      <span class="x4">${a}</span>
    </div>
    <div class="x2">
      <span class="x3">PID:</span>
      <span class="x4">${b}</span>
    </div>
  `;

  const d = document.createElement('style');
  d.textContent = `
    #x1 {
      position: fixed;
      bottom: 24px;
      left: 50%;
      transform: translateX(-50%);
      display: flex;
      flex-direction: row;
      align-items: center;
      gap: 24px;
      padding: 10px 24px;
      background: rgba(255, 255, 255, 0.85);
      backdrop-filter: blur(20px);
      border-radius: 12px;
      border: 1px solid #d0d0d0;
      font-family: -apple-system, BlinkMacSystemFont, "San Francisco", "Segoe UI", Roboto, sans-serif;
      font-size: 14px;
      color: #1c1c1e;
      z-index: 9999;
    }

    .x2 {
      display: flex;
      flex-direction: row;
      gap: 6px;
    }

    .x3 {
      font-weight: 600;
      color: #000;
    }

    .x4 {
      color: #555;
    }

    @media (prefers-color-scheme: dark) {
      #x1 {
        background: rgba(30, 30, 30, 0.75);
        color: #f2f2f2;
        border: 1px solid #444;
      }

      .x3 {
        color: #fff;
      }

      .x4 {
        color: #aaa;
      }
    }
  `;

  document.head.appendChild(d);
  document.body.appendChild(c);
})();
