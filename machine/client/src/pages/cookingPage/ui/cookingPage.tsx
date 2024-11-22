import {useEffect} from "react";
import {useUnit} from "effector-react";
import {$timeToCook, timeDecrement} from "src/pages/cookingPage/model/model-coookingPage.ts";
import {SvgSelectorStage} from "src/shared/utils/svg-selector-stage.tsx";
import info from "src/assets/info.svg";
import {changeVisibleContacts} from "src/entities/contacts/model/contact-model.ts";


export const CookingPage = () => {
    const time = useUnit($timeToCook)
    let a = 20

    // @ts-ignore
    useEffect(async () => {
        let open = true
        while (a >= 0 && open) {
            console.log('time decrement')
            timeDecrement(a)
            await new Promise(resolve => setTimeout(resolve, 1000))
            a -= 1
        }
        return () => {
            open = false
        }
    }, []);
    return (
        <div className='h-full w-full flex flex-col items-center'>
            <div className='mt-[382px] w-[70%] font-bold text-[48px] '>
                {`До свежего горячего круассана всего ${time} секунд`}
            </div>
            <div className='flex mt-[140px] items-center justify-center'>
                <SvgSelectorStage id={`first-${time >= a ? 'first' : time >= a - (a / 3) ? 'second' : 'third'}`}/>
                <div className='pb-[63px]'  ><SvgSelectorStage id={`line-${time >= a - (a / 3) ? 'first' : 'second'}`}/></div>
                <SvgSelectorStage
                    id={`second-${time >= a - (a / 3) ? 'first' : time >= a - ((a / 3) * 2) ? 'second' : 'third'}`}/>
                <div className='pb-[63px]' ><SvgSelectorStage id={`line-${time >= a - ((a / 3) * 2) ? 'first' : 'second'}`}/></div>
                <SvgSelectorStage id={`third-${time >= a - ((a / 3) * 2) ? 'first' : time > 0 ? 'second' : 'third'}`}/>
            </div>
            <div className=' w-full mt-[100px] h-full relative '>
                <div
                    className='border-t-[5px] w-full flex justify-end absolute min-h-[170px] h-[80%] max-h-[233px] bottom-0 border-layoutLine'>
                    <img className='mt-[50px] mr-[46px] cursor-pointer w-[84px] h-[84px]'  onClick={() => changeVisibleContacts(true)} src={info} alt={'info'}/>
                </div>
            </div>
        </div>
    );
};
