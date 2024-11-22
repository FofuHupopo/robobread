import {getProductFx} from "src/pages/productPage/model/productPage-model.ts";
import {Link} from "react-router-dom";
import {product} from "src/pages/categoryPage/model/category-model.ts";


type Props = {
    product: product
}

export const ItemProduct = ({product}: Props) => {

    return (
        <Link to={`/product/${product.id}`} onClick={() => getProductFx(product.id)}
              className='w-[312px] mb-[52px] bg-layoutColor rounded-[33px] h-[396px] flex-col justify-start items-center  flex '>
            <div className='font-bold text-[20px] text-center w-[90%] h-[24px] mt-[34px] '>{product.name}</div>
            <div className='mt-[30px]'></div>
            <img className='w-[206px] object-contain h-[158px] overflow-hidden' src={product.image}
                 alt={'image product'}/>
            <div className='h-[29px] text-[24px] font-black mt-[15px]'>{(product.price/100).toFixed(2) + '₽'} </div>
            <button
                className='bg-orange mt-[28px] rounded-[17px] w-[262px] h-[52px] text-[18px] font-bold flex justify-center items-center text-white '
            >
                Приготовить
            </button>
        </Link>
    );
};

