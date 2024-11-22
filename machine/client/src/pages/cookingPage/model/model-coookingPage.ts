import {createEvent, createStore, sample} from "effector";


export const $timeToCook = createStore<number>(0);

export const timeDecrement = createEvent<number>()


sample({
    clock: timeDecrement,
    target: $timeToCook
})

// sample({
//     source: $getCategoryStatusFx,
//     filter: (status) => status !== "pending"
// });