function* fibGenerator(): Generator<number, any, number> {
    let curr: number = 0;
    let next: number = 1;
    yield curr;
    while (true){
        [curr,next] = [next,curr+next];
        yield curr;
    }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */