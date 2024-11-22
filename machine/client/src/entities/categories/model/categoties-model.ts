import {createEffect, createStore, sample} from "effector";
import {status} from "patronum/status";
import {API_URL_CLIENT} from "src/shared/api/http/axios-instance.ts";
import {appStartedGate} from "src/app/layout/mode/layout-model.ts";
import {getCategoryFx} from "src/pages/categoryPage/model/category-model.ts";

export type category = {
    image: string
    id: number
    name: string
}


export const $categories = createStore<category[] | null>(null);

export const getCategoriesFx = createEffect(async () => {
    try {
        const res = await fetch(API_URL_CLIENT + "products/category");
        if (!res.ok) throw new Error("error");
        return await res.json();
    } catch (e) {
        throw new Error("Ошибка при загрузке категорий");
    }
});

const $getCategoriesStatusFx = status({effect: getCategoriesFx});

sample({
    clock: appStartedGate.open,
    source: $getCategoriesStatusFx,
    filter: (status) => status !== "pending",
    target: getCategoriesFx
});


sample({
    // @ts-ignore
    clock: getCategoriesFx.doneData,
    target: $categories
});


sample({
    // @ts-ignore
    source: {category: $categories},
    clock: getCategoriesFx.doneData,
    fn: ({category}) => (category ? category[0].id : undefined),
    target: getCategoryFx
});

