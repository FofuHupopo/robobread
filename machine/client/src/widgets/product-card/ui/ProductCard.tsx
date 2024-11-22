import {product} from "src/pages/categoryPage/model/category-model.ts";
import {PaymentProduct} from "src/features/payment-product/ui/PaymentProduct.tsx";
import arrowLeft from 'src/assets/arrow-left.svg'
import info from 'src/assets/info.svg'
import {Link} from "react-router-dom";
import {changeVisibleContacts} from "src/entities/contacts/model/contact-model.ts";

type Props = {
    product: product
}

export const ProductCard = ({product}: Props) => {
    return (
        <div className='flex  text-center h-full flex-col justify-center items-center'>
            <div className='text-[66px] text-center w-[80%] font-black'>{product.name}</div>
            <div className='flex w-[800px] justify-between mt-[42px] h-[930px] '>
                <img className='w-[504px] rounded-[128px] border-[2px] border-cardProductComposition'  src={product.image} alt={product.name}/>
                <div className='w-[506px] px-[22px] ml-[22px]  bg-cardProductComposition rounded-[54px]'>
                    <div className='text-[28px] text-center pt-[26px] font-black'>Состав:</div>
                    <div className='text-[22px] text-left font-semibold '>{product.composition}</div>
                </div>
            </div>
            <div className='mt-[60px] text-[22px] font-semibold px-[163px]'>
                {product.description}
            </div>
            <div className='bg-layoutLine rounded-[28px] mt-[42px] px-[52px] py-[24px] text-[56px] font-bold'>
                {(product.price/100).toFixed(2) + ' ₽'}
            </div>
            <PaymentProduct product={product}/>
            <div className=' w-full mt-[70px] h-full relative '>
                <div
                    className='border-t-[5px] w-full flex justify-between absolute min-h-[160px] h-[80%] max-h-[233px] bottom-0 border-layoutLine'>
                    <Link to={`/products/${product.category}`}
                          className='flex w-[330px] ml-[46px] mt-[4%] rounded-[30px] h-[84px] justify-center items-center bg-buttonBg'>
                        <img src={arrowLeft} alt={'return'}/>
                        <div className='font-bold text-[28px] '>Назад в меню</div>
                    </Link>
                    <img className='mt-[4%] mr-[46px] cursor-pointer w-[84px] h-[84px]' onClick={()=> changeVisibleContacts(true)} src={info} alt={'info'}/>
                </div>
            </div>
        </div>
    );
};

