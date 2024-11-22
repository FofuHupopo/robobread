import { createEvent, createStore, sample } from "effector";

const changeVisibleError = createEvent<boolean>();


const $errorModalVisible = createStore<boolean>(false);

sample({
    clock: changeVisibleError,
    target: $errorModalVisible
});

export { changeVisibleError, $errorModalVisible };