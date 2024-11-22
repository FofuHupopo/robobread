import {createEffect, createStore } from "effector";
import {API_URL_CLIENT} from "src/shared/api/http/axios-instance.ts";

export type payment = {
  id: string,
  amount: number,
  order_id: string,
  description: string,
  success: boolean,
  status: string,
  payment_id: string,
  error_code: string,
  payment_url: string,
  message: string,
  details: string,
}


export const $currentQrCodeSvg = createStore<string | null>(null);


export const createPayementFx = createEffect(async (id: string | undefined) => {
    console.log(id)
    try {
        const res = await fetch(API_URL_CLIENT + `payment/payment`, {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              order_id: id
            }),
        });
        if (!res.ok) throw new Error("error");
        return await res.json();
    } catch (e) {
        throw new Error("Ошибка при загрузке оплаты");
    }
});


export const getQrFx = createEffect(async (id: string | undefined) => {
  console.log(id)
  try {
      const res = await fetch(API_URL_CLIENT + `payment/payment/qr?payment_id=${id}`, {
          method: "GET",
      });
      if (!res.ok) throw new Error("error");
      return await res.text();
  } catch (e) {
      throw new Error("Ошибка при загрузке qr кода");
  }
});


// sample({
//   // @ts-ignore
//   clock: createOrderFx.doneData,
//   fn: (order: order) => (order.id),
//   target: createPayementFx
// })


// sample({
//   // @ts-ignore
//   clock: createPayementFx.doneData,
//   fn: (payment: payment) => (payment.id),
//   target: getQrFx
// })


// sample({
//   clock: getQrFx.doneData,
//   target: $currentQrCodeSvg
// });
