function filter(arr: number[], fn: (n: number, i: number) => any): number[] {
    let currentIndex = 0
    for (let i = 0; i < arr.length; i++){
        if (fn(arr[i],i)){
            if (i !== currentIndex){
                let temp = arr[currentIndex]
                arr[currentIndex] = arr[i]
                arr[i] = temp
            }
            currentIndex ++
        }
    }
    return arr.slice(0,currentIndex)
};