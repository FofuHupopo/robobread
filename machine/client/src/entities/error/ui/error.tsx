import {Modal} from "src/shared/ui/modal";
import close from "src/assets/close.svg";
import error from "src/assets/error.png";
import {$errorModalVisible, changeVisibleError} from "src/entities/error/model/error-model.ts";
import {Link} from "react-router-dom";
import {useUnit} from "effector-react";

export const Error = () => {
    const visible = useUnit($errorModalVisible)
    return (
        <Modal visible={visible} setVisible={changeVisibleError}>
            <div
                className='w-[788px] relative font-bold text-contactColor flex flex-col items-center h-[754px] bg-white rounded-[66px] '>
                <div className='flex flex-col justify-center items-center pt-[72px]'>
                    <img src={error} alt='error' className='w-[260px] h-[260px] '/>
                    <div className='text-[48px] font-bold mt-[30px]'>
                        Не удалось загрузить
                    </div>
                    <div className='font-semibold font-contactColor text-center w-[90%] text-[28px] mt-[24px]'>
                        При загрузке мы столкнулись с проблемой. <br/> Не переживайте, для продолжения нажмите
                        “Повторить” или
                        вернитесь на главный экран.
                    </div>
                    <div className='mt-[40px] flex '>
                        <button
                            className='w-[337px] flex h-[84px]  text-[28px] text-black border-[4px] border-buttonBg rounded-[28px]'>
                            <Link to={''} className='flex w-full justify-center items-center h-full'>
                                <svg width="48" height="48" viewBox="0 0 48 48" fill="none"
                                     xmlns="http://www.w3.org/2000/svg">
                                    <path fillRule="evenodd" clipRule="evenodd"
                                          d="M27.6371 9.33475C25.4878 7.55769 22.5122 7.55769 20.3629 9.33475L9.59078 18.2412C8.6085 19.0534 8 20.3365 8 21.7345V37.7498C8 39.1106 9.00886 40.002 10 40.002H14C15.1046 40.002 16 39.1065 16 38.002V31.3715C16 28.0355 18.5729 25.1194 22 25.1194H26C29.4271 25.1194 32 28.0355 32 31.3715V38.002C32 39.1065 32.8954 40.002 34 40.002H38C38.9911 40.002 40 39.1106 40 37.7498V21.7345C40 20.3365 39.3915 19.0534 38.4092 18.2412L27.6371 9.33475ZM30.1859 6.252L40.9581 15.1585C42.8988 16.7631 44 19.1961 44 21.7345V37.7498C44 41.0858 41.4271 44.002 38 44.002H34C30.6863 44.002 28 41.3157 28 38.002V31.3715C28 30.0108 26.9911 29.1194 26 29.1194H22C21.0089 29.1194 20 30.0108 20 31.3715V38.002C20 41.3157 17.3137 44.002 14 44.002H10C6.57287 44.002 4 41.0858 4 37.7498V21.7345C4 19.1961 5.10118 16.7631 7.04193 15.1585L17.8141 6.25199C21.4425 3.25194 26.5575 3.25194 30.1859 6.252Z"
                                          fill="#434343"/>
                                </svg>
                                <div className='ml-[12px]'>На главную</div>
                            </Link>
                        </button>
                        <button
                            className='w-[337px] flex text-[28px] ml-[22px] h-[84px] bg-orange text-white rounded-[28px] '>
                            <Link to={''} className='flex w-full justify-center items-center h-full'>
                                <svg width="48" height="48" viewBox="0 0 48 48" fill="none"
                                     xmlns="http://www.w3.org/2000/svg">
                                    <g clipPath="url(#clip0_872_5057)">
                                        <path
                                            d="M40 21.9994C39.5109 18.4799 37.8781 15.2187 35.3533 12.7184C32.8284 10.2181 29.5515 8.61725 26.0273 8.16252C22.5032 7.70779 18.9272 8.42438 15.8504 10.2019C12.7736 11.9794 10.3665 14.7193 9 17.9994M8 9.99941V17.9994H16"
                                            stroke="white" strokeWidth="4" strokeLinecap="round"
                                            strokeLinejoin="round"/>
                                        <path
                                            d="M8 26C8.48912 29.5196 10.1219 32.7807 12.6467 35.281C15.1716 37.7813 18.4485 39.3822 21.9727 39.8369C25.4968 40.2916 29.0728 39.575 32.1496 37.7975C35.2264 36.02 37.6335 33.2801 39 30M40 38V30H32"
                                            stroke="white" strokeWidth="4" strokeLinecap="round"
                                            strokeLinejoin="round"/>
                                    </g>
                                    <defs>
                                        <clipPath id="clip0_872_5057">
                                            <rect width="48" height="48" fill="white"/>
                                        </clipPath>
                                    </defs>
                                </svg>
                                <div className='ml-[12px]'>Повторить</div>
                            </Link>
                        </button>
                    </div>
                </div>
                <button className='absolute right-[33px] top-[33px]' onClick={() => changeVisibleError(false)}>
                    <img src={close} alt={'close'}/>
                </button>
            </div>
        </Modal>
    );
};

