let arr = [3,1,2,5,4,7,6,9,8]

for(let i = 0; i < arr.length; i++){
    if(arr[0] > arr[1]){
        let aux = arr[1]
        arr[0] = arr[1];
        arr[0]= aux; 
    }
    console.log(arr[i])
} 