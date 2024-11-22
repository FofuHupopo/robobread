import {FC, ReactNode} from 'react';
import {Outlet} from "react-router-dom";
import {Categories} from "src/entities/categories";

interface LayoutProps {
    children?: ReactNode,
}

export const LayoutProduct: FC<LayoutProps> = () => {
    return (
        <div className='w-[1080px]  grid grid-cols-layout  h-[1920px]'>
            <div className='pt-[48px] border-r-[2px] border-r-layoutLine bg-layoutColor '>
                <div className='h-[158px] w-[100%] '>
                </div>
                <Categories/>
            </div>
            <main>
                <Outlet/>
            </main>
        </div>
    );
};

