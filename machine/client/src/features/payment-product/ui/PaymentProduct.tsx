import sbp from 'src/assets/sbp.svg'
import card from 'src/assets/card.svg'
import nal from 'src/assets/nal.svg'
import {Link} from "react-router-dom";
import { product } from 'src/pages/categoryPage/model/category-model';

type Props = {
    product: product
}

export const PaymentProduct = ({product}: Props) => {
    return (
        <div className='mt-[6%]  text-center'>
            <div className='font-black text-[48px] text-center'>Оплатить через</div>
            <div>
                <div className='mt-[42px] gap-[22px] flex px-[50px]'>
                    <Link
                        to={`/payment?productId=${product.id}`}
                        className=' bg-cardProductComposition rounded-[54px] w-[315px] h-[222px] flex justify-center items-center  '>
                        <img src={sbp} alt='sbp'/>
                    </Link>
                    <div
                        className=' bg-cardProductComposition flex-col rounded-[54px] w-[315px] h-[222px] flex justify-center items-center  '>
                        <img src={card} alt='card'/>
                        <div className='text-[22px] font-black'>
                            Банковская карта
                        </div>
                    </div>
                    <div
                        className=' bg-cardProductComposition flex-col rounded-[54px] w-[315px] h-[222px] flex justify-center items-center  '>
                        <img src={nal} alt='nal'/>
                        <div className='text-[22px] font-black'>
                            Наличные деньги
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

