from pathlib import Path
import wave, hashlib, math, json
from array import array
p=Path('artists/01-omah-lay/audio/get-layd')
rows=[]
for name in ['lo lo.wav','you.wav','Bad influence.wav','ye ye ye.wav']:
    f=p/name
    h=hashlib.sha256(f.read_bytes()).hexdigest()
    with wave.open(str(f),'rb') as w:
        ch,bw,rate,n,comp=w.getnchannels(),w.getsampwidth(),w.getframerate(),w.getnframes(),w.getcomptype()
        bins=[]; decoded=0; peak=0
        while True:
            raw=w.readframes(round(rate*0.1))
            if not raw: break
            if bw!=2 or comp!='NONE': raise ValueError(f'{name}: unsupported PCM')
            a=array('h');a.frombytes(raw)
            decoded+=len(a)//ch
            peak=max(peak,max(map(abs,a),default=0))
            bins.append(math.sqrt(sum(x*x for x in a)/len(a))/32768)
    active=[i for i,x in enumerate(bins) if x>0.002]
    start=round(active[0]*0.1,2) if active else None
    end=round(min(n/rate,(active[-1]+1)*0.1),2) if active else None
    rise=[0]+[max(0,bins[i]-bins[i-1]) for i in range(1,len(bins))]
    candidates=[]
    for lag in range(3,13):
        num=sum(rise[i]*rise[i-lag] for i in range(lag,len(rise)))
        den=math.sqrt(sum(x*x for x in rise[lag:])*sum(x*x for x in rise[:-lag]))
        candidates.append({'bpm_equivalent':round(600/lag,1),'correlation':round(num/den if den else 0,3)})
    rows.append({'file':name,'sha256':h,'bytes':f.stat().st_size,'channels':ch,'bits':bw*8,'sample_rate_hz':rate,'frames':n,'decoded_frames':decoded,'duration_seconds':round(n/rate,3),'signal_start_seconds_approx':start,'signal_end_seconds_approx':end,'leading_low_signal_seconds_approx':start,'trailing_low_signal_seconds_approx':round(n/rate-end,2) if end is not None else None,'peak_fraction_full_scale':round(peak/32768,4),'envelope_pulse_candidates':sorted(candidates,key=lambda x:x['correlation'],reverse=True)[:3]})
out=p/'wav-intake.json'
out.write_text(json.dumps({'method':'std-lib PCM decode; 100ms whole-mix RMS threshold 0.002; envelope rise correlation gives unverified pulse candidates','songs':rows},indent=2)+'\n',encoding='utf-8')
for r in rows: print(r['file'],r['duration_seconds'],r['signal_start_seconds_approx'],r['signal_end_seconds_approx'],r['sha256'])
