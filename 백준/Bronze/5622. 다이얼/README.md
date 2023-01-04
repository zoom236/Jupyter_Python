# [Bronze II] 다이얼 - 5622 

[문제 링크](https://www.acmicpc.net/problem/5622) 

### 성능 요약

메모리: 30616 KB, 시간: 32 ms

### 분류

구현(implementation)

### 문제 설명

<p>상근이의 할머니는 아래 그림과 같이 오래된 다이얼 전화기를 사용한다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/9c88dd24-3a4c-4a09-bc50-e6496958214d/-/preview/" style="width: 267px; height: 265px;"></p>

<p>전화를 걸고 싶은 번호가 있다면, 숫자를 하나를 누른 다음에 금속 핀이 있는 곳 까지 시계방향으로 돌려야 한다. 숫자를 하나 누르면 다이얼이 처음 위치로 돌아가고, 다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 한다.</p>

<p>숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.</p>

<p>상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다. 즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다. 예를 들어, UNUCIC는 868242와 같다.</p>

<p>할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 알파벳 대문자로 이루어진 단어가 주어진다. 단어의 길이는 2보다 크거나 같고, 15보다 작거나 같다.</p>

### 출력 

 <p>첫째 줄에 다이얼을 걸기 위해서 필요한 최소 시간을 출력한다.</p>

### 해설
<p> tele의 갯수만큼 for문을 돌리고 dial 요소에 번호를 부여한다. </p>
<p> tele주소의 값이 dial요소에 들어가 있으면 dial 요소의 인덱스 번호 + 3 한 값을 time에 더하여 time에 대입한다. </p>
<p> for문이 다 돌고 난 후 마지막 time 값 출력하여 시간을 찾는다. </p>

### 다른 풀이 
<p>alpabet_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']</p>
<p>word = input()</p>

<p>time = 0</p>
<p>for unit in alpabet_list :  </p>
<p>    for i in unit:  # alpabet 리스트에서 각 요소를 꺼내서 한글자씩 분리</p>
<p>        for x in word :  # 입력받은 문자를 하나씩 분리</p>
<p>            if i == x :  # 두 알파벳이 같으면</p>
<p>                time += alpabet_list.index(unit) +3  # time = time + index +3</p>
<p>print(time)</p>
<p> 2중 for문 의미 : 알파벳 리스트 원소를 각각의 알파벳으로 분리하여 변수 i에 선언</p>
<p> 3중 for문 의미 : 입력받은 문자를 하나씩 분리 하여 변수 x에 선언 </p>
