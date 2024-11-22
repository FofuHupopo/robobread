import {useUnit} from "effector-react";
import {$activeProduct} from "src/pages/productPage/model/productPage-model.ts";
import {ProductCard} from "src/widgets/product-card/ui/ProductCard.tsx";


export const ProductPage = () => {
    const product = useUnit($activeProduct)

    return (
        <div className='w-[1080px]  h-[1920px]'>
            {product
                &&
                <div className='pt-[220px] h-[1920px] w-full'>
                    <ProductCard product={product}/>
                </div>
            }
        </div>
    );
};
