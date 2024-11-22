import {createEffect, createStore, sample} from "effector";
import {API_URL_CLIENT} from "src/shared/api/http/axios-instance.ts";
import {product} from "src/pages/categoryPage/model/category-model.ts";


export const $activeProduct = createStore<product | null>(null);

export const getProductFx = createEffect(async (id: number | undefined) => {
    try {
        const res = await fetch(API_URL_CLIENT + `products/product/${id}`);
        if (!res.ok) throw new Error("error");
        return await res.json();
    } catch (e) {
        throw new Error("Ошибка при загрузке категории");
    }
});
// const $getCategoryStatusFx = status({effect: getCategoryFx});


sample({
    clock: getProductFx.doneData,
    target: $activeProduct
});

// sample({
//     source: $getCategoryStatusFx,
//     filter: (status) => status !== "pending"
// });