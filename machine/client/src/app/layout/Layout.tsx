import {useGate} from "effector-react";
import {Outlet} from "react-router-dom";
import Help from "src/entities/help/ui/Help";
import {appStartedGate} from "src/app/layout/mode/layout-model.ts";

export const Layout = () => {
    useGate(appStartedGate)
    return (
        <div className='w-[1080px]  text-center relative  h-[1920px]'>
            <Help/>
            <main className=' w-[1080px] h-[1920px] border-[1px] border-black'>
                <Outlet/>
            </main>
        </div>
    );
};

