import { createEvent, createStore, sample } from "effector";

const changeVisibleContacts = createEvent<boolean>();


const $contactsModalVisible = createStore<boolean>(false);

sample({
    clock: changeVisibleContacts,
    target: $contactsModalVisible
});

export { changeVisibleContacts, $contactsModalVisible };