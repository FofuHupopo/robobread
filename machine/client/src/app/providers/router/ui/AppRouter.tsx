import {Suspense} from 'react';
import {Route, Routes} from 'react-router-dom';
import {HomePage} from "src/pages/homePage";
import {LayoutProduct} from "src/layouts/layout-product";
import {Layout} from "src/app/layout/Layout.tsx";
import {CategoryPage} from "src/pages/categoryPage";
import {ProductPage} from "src/pages/productPage";
import {PaymentPage} from "src/pages/paymentPage";
import {CookingPage} from "src/pages/cookingPage";


export const AppRouter = () => {
    return (
        <Suspense fallback={<div></div>}>
            <Routes>
                <Route path="/" element={<Layout/>}>
                    <Route index={true} element={<HomePage/>}/>
                    <Route path='payment' element={<PaymentPage/>}/>
                    <Route path='cooking' element={<CookingPage/>}/>
                    <Route path="products" element={<LayoutProduct/>}>
                        <Route
                            path=":id"
                            element={<CategoryPage/>}
                        />
                    </Route>
                    <Route path="product">
                        <Route
                            path=":id"
                            element={<ProductPage/>}
                        />
                    </Route>

                </Route>
            </Routes>
        </Suspense>
    );
};