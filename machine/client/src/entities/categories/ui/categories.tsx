import {useUnit} from "effector-react";
import {$categories, getCategoriesFx} from "src/entities/categories/model/categoties-model.ts";
import {Skeleton} from "src/shared/ui/skeleton/ui/Skeleton.tsx";
import {ItemLayoutLink} from "src/shared/ui/item-layout-link";


export const Categories = () => {
    const categories = useUnit($categories);
    const skeletonArray = [...Array(7).keys()].map(i => i + 1);

    const loading =
        useUnit(getCategoriesFx.pending);

    console.log(categories)
    if (loading) return (
        <div className='w-full'>
            {skeletonArray.map(i => <Skeleton key={i} className="bg-gray-300 h-[290px] w-full"></Skeleton>)}
        </div>);
    return (
        <div>
            {categories?.length && categories.map(link => <ItemLayoutLink key={link.id} link={link}/>)}
        </div>
    );
};

