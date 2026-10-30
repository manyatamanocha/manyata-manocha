const assert = require('node:assert/strict');
const vm = require('node:vm');
const fs = require('node:fs');
const code = fs.readFileSync(require('node:path').join(__dirname, '../peek-animation.js'), 'utf8');
async function setup({hidden=false, reduced=false, inView=true, failed=false}={}) {
  const events={}, winEvents={}, calls=[];
  let observer, motionChange;
  const hero={getBoundingClientRect:()=>({top:inView?0:1500,bottom:inView?700:2200})};
  function animate(target, keys, opts) {
    const a={target,keys,opts,state:'running',cancel(){this.state='cancelled'},pause(){this.state='paused'},play(){this.state='running'},finish(){this.onfinish?.()}};
    calls.push(a);return a;
  }
  const arm={animate:(k,o)=>animate('arm',k,o)};
  const imgs=[0,1].map(()=>({naturalWidth:failed?0:917,decode:()=>failed?Promise.reject():Promise.resolve()}));
  const mascot={dataset:{},classList:{add(){},remove(){}},closest:()=>hero,querySelector:()=>arm,querySelectorAll:()=>imgs,addEventListener:(k,v)=>events[k]=v,animate:(k,o)=>animate('body',k,o)};
  const doc={hidden,getElementById:()=>mascot,addEventListener:(k,v)=>events[k]=v};
  const motion={matches:reduced,addEventListener:(_,fn)=>motionChange=fn};
  class IO {constructor(cb){observer=cb} observe(el){assert.equal(el,hero,'Observe stationary hero, never transformed mascot')}}
  const win={innerHeight:900,matchMedia:()=>motion,addEventListener:(k,v)=>winEvents[k]=v,IntersectionObserver:IO};
  vm.runInNewContext(code,{document:doc,window:win,IntersectionObserver:IO,Promise,Array,Error});
  await new Promise(setImmediate);
  return {calls,events,doc,mascot,motion,motionChange,observe:(v)=>observer([{isIntersecting:v}]),winEvents};
}
(async()=>{
  let x=await setup();
  assert.equal(x.calls.length,1,'Entrance starts without click');
  assert.equal(x.calls[0].target,'body');
  x.calls[0].finish();
  assert.equal(x.calls[1].target,'arm','Wave affects only arm');
  x.calls[1].finish();assert.equal(x.mascot.dataset.phase,'resting');
  x.events.click();assert.equal(x.calls[2].target,'arm','Click only replays wave');
  x.events.click();assert.equal(x.calls.length,3,'Rapid clicks cannot stack waves');
  x=await setup({hidden:true});assert.equal(x.calls.length,0);
  x.doc.hidden=false;x.events.visibilitychange();assert.equal(x.calls.length,1,'Hidden-tab startup resumes automatically');
  x.observe(false);assert.equal(x.calls[0].state,'paused');
  x.observe(true);assert.equal(x.calls[0].state,'running','Offscreen entrance resumes instead of being discarded');
  x=await setup({inView:false});assert.equal(x.calls.length,0);
  x.observe(true);assert.equal(x.calls.length,1,'First scroll into view starts greeting');
  x=await setup({reduced:true});assert.equal(x.calls.length,0);assert.equal(x.mascot.dataset.phase,'resting');
  x=await setup();x.motion.matches=true;x.motionChange();assert.equal(x.calls[0].state,'cancelled');
  x.calls[0].finish();assert.equal(x.calls.length,1,'Cancelled entrance cannot launch wave');
  x=await setup({failed:true});assert.equal(x.calls.length,0);assert.equal(x.mascot.dataset.phase,'resting');
  console.log('PASS: autoplay, independent arm, rest/replay, rapid clicks, hidden tab, offscreen pause/resume, reduced motion, image failure');
})().catch(e=>{console.error(e);process.exitCode=1});
