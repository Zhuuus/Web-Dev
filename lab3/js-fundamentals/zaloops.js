//let i = 3;

while (i) {
  alert( i-- );
} //1

//let i = 0;
while (++i < 5) alert( i ); //1 to 4

//let i = 0;
while (i++ < 5) alert( i ); //1 to 5

for (let i = 0; i < 5; ++i) alert( i ); //0 to 4

for (let i = 0; i < 5; i++) alert( i ); //0 to 4

for (let i = 2; i <= 10; i++) {
    if (i % 2 == 0) {
      alert( i );
    }
  } //nums from 2 to 10

let i = 0;
while(i < 3){
    alert( `number ${i}!` );
    i++;
} //for to while

let num;

do {
  num = prompt("num > 100?", 0);
} while (num <= 100 && num);

let n = 10;

nextPrime:
for (let i = 2; i <= n; i++) { // for each i...

  for (let j = 2; j < i; j++) { // look for a divisor..
    if (i % j == 0) continue nextPrime; // not a prime, go next i
  }

  alert( i ); // a prime
}