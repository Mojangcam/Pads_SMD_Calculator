# Pads_SMD_Calculator

## 사용방법

1. pads.exe파일을 다운로드 받아서 실행
2. 값을 입력하는 곳에 값들을 입력하면 아래에 value가 나옵니다.
3. min size와 max size 를 입력하면 foot size가 나오는데 foot size가 나온 상태에서 foot size 입력하는 곳에 빈칸으로 두어도 foot size value가 자동으로 들어가 계산이 됩니다.
4. foot size가 빈칸이고, row pitch와 pin pitch를 입력했을때 이 전에 foot size를 계산했다면 그대로 가져와 계산합니다.
5. 단위는 mm를 사용합니다.

## Value list
1. foot_size = round((foot_size_min + foot_size_max) / 2) 최솟값과 최댓값을 더하여 2로 나눈값을 반올림 한 값
2. length = foot_size + 1.1 발 사이즈에 1.1을 더한 값
3. row_pitch_value = row_pitch + 1.4 로우 피치에 1.4를 더한 값
4. pad_width<pre>pin pitch가 0.5미만일때 0.2
               pin pitch가 0.5일때 0.3
               pin pitch가 0.65일때 0.35
               pin pitch가 0.8일때 0.5
               pin pitch가 1.0이상일때 0.65</pre>
