import help from "src/assets/help.svg";
import helpBlack from "src/assets/help-black.svg";
import {cn} from "src/lib/utils.ts";
import {useState} from "react";
import {Modal} from "src/shared/ui/modal";
import {useLocation} from "react-router-dom";
import first from 'src/assets/first.svg'
import second from 'src/assets/second.svg'
import third from 'src/assets/third.svg'
import fourth from 'src/assets/fourth.svg'
import close from 'src/assets/close.svg'

const Help = () => {
    const home = useLocation().pathname === '/'
    const [visible, setVisible] = useState(false)
    return (
        <>
            <button
                onClick={() => setVisible(true)}
                className={cn('w-[246px] left-[788px] z-10 top-[84px] absolute flex justify-center items-center h-[84px] rounded-[65px]  text-[28px] font-bold', home ? 'text-white  bg-helpBgHome' : 'text-black  bg-helpBg')}>
                <img src={home ? help : helpBlack} alt='help'/>
                Помощь
            </button>
            <Modal setVisible={setVisible} visible={visible}>
                <div
                    className='px-[70px] flex flex-col relative gap-[66px] pt-[92px] text-textGrey w-[788px] bg-white h-[706px] rounded-[66px] '>
                    <div className='flex  justify-start  items-start h-[72px] '>
                        <img src={first} alt={'first'}/>
                        <div className='pl-[32px] font-bold w-[65%] text-[28px] text-start '>Выберите раздел меню <br /> по
                            вашему желанию
                        </div>
                    </div>
                    <div className='flex  justify-start items-start h-[72px] '>
                        <img src={second} alt={'second'}/>
                        <div className='pl-[32px] font-bold w-[100%] text-[28px] text-start '>Двигайте меню скроллом <br />
                            и выберете желаемый продукт
                        </div>
                    </div>
                    <div className='flex  justify-start items-start h-[108px] '>
                        <img src={third} alt={'third'}/>
                        <div className='pl-[32px] font-bold w-[100%] text-[28px] text-start '>Нажмите "Приготовить"
                            чтобы получить свой свежий только приготовленный заказ
                        </div>
                    </div>
                    <div className='flex  justify-start items-center h-[72px] '>
                        <img src={fourth} alt={'fourth'}/>
                        <div className='pl-[32px] font-bold w-[100%] text-[28px] text-start '>Наслаждайтесь выпечкой
                        </div>
                    </div>
                    <button className='absolute right-[33px] top-[33px]' onClick={() => setVisible(false)}>
                        <img src={close} alt={'close'}/>
                    </button>
                </div>
            </Modal>
        </>
    );
};

export default Help;