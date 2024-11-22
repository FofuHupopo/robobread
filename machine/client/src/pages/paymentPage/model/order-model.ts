import {createEffect} from "effector";
import {API_URL_CLIENT} from "src/shared/api/http/axios-instance.ts";

export type order = {
    id: string,
    amount: number,
    created_at: string,
    paid_at: string | null,
    is_paid: boolean,
    product: number
}


export const createOrderFx = createEffect(async (id: number | undefined) => {
    console.log(id)
    try {
        const res = await fetch(API_URL_CLIENT + `orders/order`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                product: id
            }),
        });
        if (!res.ok) throw new Error("error");
        return await res.json();
    } catch (e) {
        throw new Error("Ошибка при загрузке заказа");
    }
});
