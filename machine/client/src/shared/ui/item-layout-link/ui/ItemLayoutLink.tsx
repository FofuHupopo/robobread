import {Link, useLocation} from "react-router-dom";
import {cn} from "src/lib/utils.ts";
import {category} from "src/entities/categories/model/categoties-model.ts";
import {getCategoryFx} from "src/pages/categoryPage/model/category-model.ts";

export type Props = {
    link: category
}

export const ItemLayoutLink = ({link}: Props) => {
    const name = Number(useLocation().pathname.replace('/products/', ''))
    return (
        <Link onClick={() => getCategoryFx(link.id)}
              className={cn('w-full h-[120px] flex items-center', name === link.id && 'bg-selectCategory')}
              to={'' + link.id}>
            <img className='ml-[25px] h-[86px] w-[86px]' src={link.image} alt={link.name}/>
            <div className='text-[28px] ml-[22px] font-bold'> {link.name} </div>
        </Link>
    );
};
