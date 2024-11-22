import {createEffect, createStore, sample} from "effector";
import {API_URL_CLIENT} from "src/shared/api/http/axios-instance.ts";

export type product = {
    category: number
    composition: string,
    description: string
    id: number
    image: string
    name: string
    price: number
}

export const $activeCategoryProducts = createStore<product[] | null>(null);

export const getCategoryFx = createEffect(async (id: number | undefined) => {
    console.log(id)
    try {
        const res = await fetch(API_URL_CLIENT + `products/product?category_id=${id}`);
        if (!res.ok) throw new Error("error");
        return await res.json();
    } catch (e) {
        throw new Error("Ошибка при загрузке категории");
    }
});
// const $getCategoryStatusFx = status({effect: getCategoryFx});


sample({
    clock: getCategoryFx.doneData,
    target: $activeCategoryProducts
});

// sample({
//     source: $getCategoryStatusFx,
//     filter: (status) => status !== "pending"
// });