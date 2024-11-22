import {useUnit} from "effector-react/compat";

import {$categories} from "src/entities/categories/model/categoties-model.ts";
import {ItemProduct} from "src/shared/ui/item-product";
import {$activeCategoryProducts, getCategoryFx} from "src/pages/categoryPage/model/category-model.ts";

export const CategoryPage = () => {
    const products = useUnit($activeCategoryProducts)
    const categories = useUnit($categories)
    const loading =
        useUnit(getCategoryFx.pending);
    if (loading) return (
        <div className='w-full'>
            load
            {/*{skeletonArray.map(i => <Skeleton key={i} className="bg-gray-300 h-[290px] w-full"></Skeleton>)}*/}
        </div>);
    let name
    if (products) {
        name = categories?.find(c => c.id === products[0].category)?.name
    } else name = 'Категория'
    return (
        <div className='pt-[220px] w-full flex flex-col items-center'>
            <div className='text-[66px] mb-[42px] font-black '>{name}</div>
            <div className='grid grid-cols-2  self-auto justify-self-stretch items-stretch w-full px-[30px] '>
                {products && products.map(product => <ItemProduct key={product.id} product={product}/>)}
            </div>
        </div>)
        ;
};

