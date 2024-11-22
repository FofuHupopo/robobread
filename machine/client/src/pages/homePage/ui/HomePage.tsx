import mess from "src/assets/messageHome.png"
import payment from "src/assets/payment.png"
import {Link} from "react-router-dom";
import {useUnit} from "effector-react";
import {$categories} from "src/entities/categories/model/categoties-model.ts";

export const HomePage = () => {
    const categories = useUnit($categories)
    const id = categories ? categories[0].id : 0
    return (
        <div className="bg-home min-w-[1080px] min-h-[1920px] relative">
            <img src={mess} alt='mess' className='pl-[532px] pt-[912px]'/>
            <Link to={`/products/${id}`}>
                <button
                    className='bg-orange rounded-[231px] w-[852px] h-[192px] text-[66px] font-black flex justify-center items-center text-white left-[114px] absolute top-[1419px]'>
                    Посмотреть меню
                </button>
            </Link>
            <img src={payment} alt={'payment'} className='absolute left-[395px] top-[1643px]'/>
        </div>
    );
};
