// *Determinar si un número es par o impar.
// const parImpar = (num) => {
//     if(num % 2 === 0)return `el ${num} es par`
//     return `el ${num} es impar`
// }

// console.table(parImpar(564))

/*******************************************************/

//* Calcular el factorial de un número.

// const factorial = (num) => {
//     if(num <= 1) return 1
//     return num * factorial(num - 1)
// }

// console.log(factorial(8))

/*******************************************************/

// *Crear un arreglo de números y encontrar el número mayor.

// const mayor = (arr) => {
//     let orden = arr.sort((a,b) =>  a - b)
//     return `${orden[orden.length - 1]} es el mayor`
// }

// console.log(mayor([2,5,8,7,4,1,10,1,5]))


/*******************************************************/

// const invertir = (text) => {
//     let reverce = text.split('').reverse().join('');
//     return reverce
    
// }
// console.log(invertir('menu'))


/*******************************************************/

//* Crear un bucle que imprima los números del 1 al 10.
// con while
// const coontador = (num) => {
//     while(num < 10){
//         num = num + 1;
//         console.log(num) 
//     }
// }   
// console.log(coontador(0))

/*******************************************************/
// const areatriangulo = (base, altura) => {
//     return base * altura / 2
// }

// console.log(areatriangulo(10,20))

/*******************************************************/
// *Crear una función que reciba dos números y devuelva el mayor de ellos.

// const mayor = (num1, num2) => {
//     if(num1 > num2) return num1
//     return num2
// }
// console.log(mayor(55,10))

/*******************************************************/
// *Crear una función que reciba un arreglo de números y devuelva la suma de los números pares.

// *sin metodos
// const sumaPares = (arr) => {
//     let suma = 0
//     for(let ele of arr){
//         if(ele % 2 == 0){
//             suma += ele
//         }
//     }
//     return suma
// } 

// console.log(sumaPares([1,2,3,5,6,7,8,9,10]))

//* con metodos

// const sumaPares = (arr) => {
//   let filtro = arr.filter(ele => ele % 2 === 0)
//   return filtro.reduce((a,b) => a + b,0)
// } 

// console.log(sumaPares([1,2,3,4,5,6]))


/*******************************************************/
//* Crear una función que reciba un arreglo de palabras y devuelva la palabra más larga.

// const masLarga = (arr) => {
//     let ordenar = arr.sort((a,b) => a.length > b.length ? 1 : -1)
//     return ordenar[ordenar.length - 1]
// }
// console.log(masLarga(['uno','alexander','mar','dos']))
/*******************************************************/
// *Crear una función que reciba una cadena de texto y devuelva la misma cadena con todas las palarbas en mayuscula

// const Mayus = (arr) => {
//     return arr.map(i => i.toUpperCase())
// }
// console.log(Mayus(['alexander','moto', 'deportar']))


/*******************************************************/
// Crear una función que reciba un arreglo de números y devuelva un nuevo arreglo con los números ordenados de forma ascendente.

//* con metodos

// const ordenados = (arr) => {
//     return arr.sort((a, b) => b - a)
// }
// console.log(ordenados([5,1,4,7,8,2,10]))

//* sin metodos

// const ordenados = arr => {
//     const l = arr.length;
//     for (let i = 0; i < l; i++ ) {
//       for (let j = 0; j < l - 1 - i; j++ ) {
//         if ( arr[ j ] < arr[ j + 1 ] ) {
//           [ arr[ j ], arr[ j + 1 ] ] = [ arr[ j + 1 ], arr[ j ] ];
//         }
//       }
//     }
  
//     return arr;
//   };

// console.log(ordenados([5,6,4,8,7,10,4,1,2]))


/*******************************************************/
//* Crear una función que reciba un objeto y devuelva un arreglo con los valores del objeto.

// const objetoToArr = obj => {
//     let arr = []
//     for(let i in obj){
//         arr.push(obj[i])
//     }
//     return arr
// }
// console.log(objetoToArr({
//     'nombre': 'alexander',
//     'edad': 18,
//     'pais': 'colombia'
// }))
 

/*******************************************************/
//* Crear una función que reciba una cadena de texto y devuelva la misma cadena con las palabras en orden inverso.

// const reverse = text => {
//     let convertToArr = text.split(' ');
//     let reverse = convertToArr.reverse();
//     let convertToString = reverse.join(' ');
//     return convertToString
// }
// console.log(reverse('hola mundo'))

/*******************************************************/
// *Crear una función que reciba un arreglo de números y devuelva la suma de todos los números en posiciones impares.

// const sumaPosiciones = arr => {
//     let suma = 0
//     for(let num of arr) {
//         if(arr.indexOf(num) % 2 === 0){
//             suma += num
//         }
//     }
//     return suma
// }
// console.log(sumaPosiciones([1,2,3,4,56,7,8,9,1]))

/*******************************************************/

//* Crear una función que reciba un arreglo de números y devuelva el promedio de dichos números.

// const promedio = arr => {
//     let suma = 0;
//     for(let ele of arr){
//         suma += ele
//     }
//     let promedio = suma / arr.length
//     return promedio.toFixed(2)
// }
// console.log(promedio([1,2,3,45,6,78,9]))

/*******************************************************/
// *Crear una función que reciba un arreglo de objetos y devuelva la suma de las propiedades numéricas de dichos objetos.
//  const sumaValores = obj => {
//     let suma = 0; 
//     for(let ele of obj){
//         suma += ele.cuenta
//     }
//     return `el valor total de las cuentas son: ${suma}`

//  }
//  console.log(sumaValores([
//     {
//       nombre: 'alexander',
//       edad: 19,
//       cuenta: 2000000
//     },

//     {
//       nombre: 'alexander',
//       edad: 29,
//       cuenta: 5000000
//     },

//     {
//       nombre: 'alexander',
//       edad: 49,
//       cuenta: 8400000
//     }
//  ]))

/*******************************************************/
// Crear una función que reciba una cadena de texto y una palabra y devuelva si la repite o no.

// const repite = (text, word) => {

//     if(text.includes(word)) return `el tecto si contiene la palabra ${word}`
//     return `el tecto no contiene la palabra ${word}`

// }
// console.log(repite('los sustantivos son aquellos que nombren animales personas u objetos', 'personas'))

/*******************************************************/
//* Crear una función que reciba un arreglo de números y devuelva un nuevo arreglo sin duplicados.

// const duplicados = arr => {
//     let convertSet = new Set (arr)
//     let result = [...convertSet]
//     return result
// }
// console.log(duplicados([1,2,3,6,4,5,5,6,7,8,8]))


/*******************************************************/
// *Crear una función que reciba un arreglo de objetos con propiedades "nombre" y "edad", y devuelva el objeto con la persona de mayor edad.

// const mayor = arr => {
//    let ordenar =  arr.sort((a,b) => b.edad - a.edad)
//    return ordenar[0]
// }
// console.log(mayor([
//     {
//       nombre: 'alexander',
//       edad: 19,
//       pais: 'colombia'
//     },

//     {
//       nombre: 'daniel',
//       edad: 27,
//       pais: 'costa rica'
//     },

//     {
//       nombre: 'natalia',
//       edad: 41,
//       pais: 'colombiana'
//     },
//     {
//       nombre: 'maria',
//       edad: 22,
//       pais: 'estados unidos'
//     },

    
// ]))

/*******************************************************/
//* Crear una función que reciba un arreglo de números y devuelva la mediana de dichos números.

// const media = arr => {
//   let suma = 0;
//   for(let ele of arr){
//     suma += ele
//   }
//   return suma / arr.length
// }
// console.log(media([1,2,3,4,5,6,7,8]))
/*******************************************************/


    // Implementar una función que aumente el valor recibido en 5 hasta un límite de 8 veces.
    // Retornar el valor final.
    // Utilizar el bucle Do-While.
    // Tu código:
 
    function continueStatement(num) {
        // Iterar en un bucle aumentando en 2 el número recibido hasta un límite de 10 veces.
        // Guardar cada nuevo valor en un array y retornarlo.
        // Cuando el número de iteraciones alcance el valor 5, no se suma ese caso y
        // se continua con la siguiente iteración.
        // [PISTA]: utiliza el statement 'continue'.
        let conta = 1
        let arr = []
        while (conta < 11){
           
            num = num + 2
            if (conta === 6){
                arr.pop(num)
            }
              arr.push(num)
              conta++
        }
        return arr
     }
     console.log(continueStatement(2))

