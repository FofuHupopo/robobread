import sbp from 'src/assets/sbp.svg'
// import qr from 'src/assets/qr-test.png'
import {Link} from "react-router-dom";
import info from "src/assets/info.svg";
import success from "src/assets/paySuccesfull.png";
import {changeVisibleContacts} from "src/entities/contacts/model/contact-model.ts";
import { createPayementFx, getQrFx } from '../model/payment-model';
import { createOrderFx } from '../model/order-model';
import { useEffect, useState } from 'react';
import { API_URL_CLIENT } from 'src/shared/api/http/axios-instance';


export const PaymentPage = () => {
    const [qr, setQr] = useState("");
    const [paymentId, setPaymentId] = useState("");
    const [pay, setPay] = useState(false);
    const [price, setPrice] = useState(0);

    useEffect(() => {
        const params = new URLSearchParams(window.location.search);
        //@ts-ignore
        const productId = parseInt(params.get('productId'));
        createOrderFx(productId).then((order) => {
            createPayementFx(order.id).then((payment) => {
                console.log(payment)

                setPaymentId(payment.id)
                setPrice(payment.amount)

                getQrFx(payment.id).then((qr) => {
                    setQr(qr)
                })
            })
        });
    }, []);

    useEffect(() => {
        let intervalId: number;

        const checkPaymentStatus = async () => {
            const response = await fetch(`${API_URL_CLIENT}payment/payment?payment_id=${paymentId}`);
            const data = await response.json();
            if (data.status == 'CONFIRMED' || data.status == 'AUTHORIZED') {
                setPay(true);
                clearInterval(intervalId);
            }
        };

        intervalId = setInterval(checkPaymentStatus, 3000);

        return () => {
            clearInterval(intervalId);
        };
    }, [paymentId]);

    

    return (
        <>
            <div className='flex flex-col h-full items-center'>
                {!pay
                    ?
                    <>
                        <img src={sbp} alt='sbp logo' className='mt-[204px]'/>
                        <div className='font-bold text-center text-[48px] mt-[52px] w-[70%] '>
                            Для оплаты зайдите <br/>
                            в мобильное приложение банка и отсканируйте QR-код
                        </div>
                        <div
                            className='mt-[50px] bg-cardProductComposition justify-center rounded-[80px] flex items-center w-[584px] h-[584px]'>
                            <div dangerouslySetInnerHTML={{ __html: qr }} />
                        </div>
                        <div className='mt-[80px]'>
                            <div className='text-[38px] font-bold text-textGreySecond h-[]'>К оплате:</div>
                            <div className='font-black text-[68px]'>{price / 100},00 ₽</div>
                        </div>
                    </>
                    :
                    <>
                        <div className='text-[48px] mt-[382px] font-bold '>
                            Оплата прошла успешно, <br/>
                            заказ принят
                        </div>
                        <img src={success} alt={'successful'} className='mt-[90px] w-[418px] h-[418px]'  />

                    </>
                }
                <div className=' w-full mt-[100px] h-full relative '>
                    <div
                        className='border-t-[5px] w-full flex justify-between absolute min-h-[170px] h-[80%] max-h-[233px] bottom-0 border-layoutLine'>
                        <Link to={`/`}
                              className='flex w-[430px] ml-[46px] mt-[46px] rounded-[28px] h-[84px] justify-center items-center bg-buttonBg'>
                            <div className='font-bold text-[28px] '>Изменить способ оплаты</div>
                        </Link>
                        <img className='mt-[50px] mr-[46px] cursor-pointer w-[84px] h-[84px]'
                             onClick={() => changeVisibleContacts(true)} src={info} alt={'info'}/>
                    </div>
                </div>
            </div>
        </>
    );
};

