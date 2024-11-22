import {Modal} from "src/shared/ui/modal";
import {useUnit} from "effector-react";
import {$contactsModalVisible, changeVisibleContacts} from "src/entities/contacts/model/contact-model.ts";
import close from "src/assets/close.svg";

export const Contacts = () => {
    const visible = useUnit($contactsModalVisible)
    return (
        <Modal visible={visible} setVisible={changeVisibleContacts} >
            <div className='w-[768px] relative font-bold text-contactColor flex flex-col items-center h-[570px] bg-white rounded-[66px] '>
                <div className='text-[48px] pb-[40px] pt-[92px] font-bold'>
                    Контакты для связи
                </div>
                <div
                    className='flex w-[696px] text-[38px] rounded-[30px] px-[110px] bg-cardProductComposition py-[33px] '>
                    <svg className='mr-[22px]' width="66" height="67" viewBox="0 0 66 67" fill="none"
                         xmlns="http://www.w3.org/2000/svg">
                        <path
                            d="M56.5411 48.771C56.5411 49.6237 56.3516 50.5 55.9489 51.3527C55.5463 52.2054 55.0252 53.0108 54.3383 53.7687C53.1777 55.0478 51.8986 55.9715 50.4538 56.5637C49.0326 57.1558 47.4931 57.4637 45.835 57.4637C43.4191 57.4637 40.8373 56.8953 38.1134 55.7346C35.3895 54.574 32.6656 53.0108 29.9654 51.0448C27.2416 49.0552 24.6598 46.8524 22.1965 44.4128C19.7568 41.9494 17.554 39.3676 15.5881 36.6674C13.6458 33.9672 12.0825 31.267 10.9456 28.5905C9.8087 25.8903 9.24023 23.3086 9.24023 20.8452C9.24023 19.2346 9.52447 17.695 10.0929 16.2738C10.6614 14.829 11.5615 13.5026 12.8168 12.3183C14.3327 10.8261 15.9907 10.0918 17.7435 10.0918C18.4067 10.0918 19.0699 10.2339 19.6621 10.5181C20.2779 10.8024 20.8227 11.2287 21.249 11.8446L26.7442 19.5899C27.1705 20.182 27.4784 20.7268 27.6916 21.2479C27.9048 21.7453 28.0232 22.2427 28.0232 22.6927C28.0232 23.2612 27.8574 23.8297 27.5258 24.3744C27.2179 24.9192 26.7678 25.4877 26.1994 26.0561L24.3992 27.9273C24.1387 28.1879 24.0203 28.4958 24.0203 28.8748C24.0203 29.0643 24.044 29.2301 24.0913 29.4195C24.1624 29.609 24.2334 29.7511 24.2808 29.8933C24.7072 30.6749 25.4414 31.6934 26.4836 32.9251C27.5495 34.1567 28.6864 35.4121 29.9181 36.6674C31.1971 37.9228 32.4288 39.0834 33.6841 40.1493C34.9158 41.1915 35.9343 41.902 36.7396 42.3284C36.8581 42.3758 37.0002 42.4468 37.166 42.5179C37.3555 42.5889 37.545 42.6126 37.7581 42.6126C38.1608 42.6126 38.4687 42.4705 38.7293 42.21L40.5294 40.4335C41.1215 39.8414 41.69 39.3913 42.2348 39.1071C42.7796 38.7755 43.3243 38.6097 43.9165 38.6097C44.3665 38.6097 44.8402 38.7044 45.3613 38.9176C45.8824 39.1308 46.4272 39.4387 47.0193 39.8414L54.8594 45.4076C55.4752 45.8339 55.9016 46.3313 56.1621 46.9235C56.399 47.5156 56.5411 48.1078 56.5411 48.771Z"
                            stroke="#434343" strokeWidth="4.17311" strokeMiterlimit="10"/>
                    </svg>
                    + 7-999-000-00-00
                </div>
                <div
                    className='flex w-[696px]  text-[38px] rounded-[30px] px-[130px] bg-cardProductComposition mt-[22px] py-[33px] '>
                    <svg className='mr-[22px]' width="66" height="67" viewBox="0 0 66 67" fill="none"
                         xmlns="http://www.w3.org/2000/svg">
                        <g clipPath="url(#clip0_825_4078)">
                            <path
                                d="M8.25 19.6719C8.25 18.2132 8.82946 16.8142 9.86091 15.7828C10.8924 14.7513 12.2913 14.1719 13.75 14.1719H52.25C53.7087 14.1719 55.1076 14.7513 56.1391 15.7828C57.1705 16.8142 57.75 18.2132 57.75 19.6719V47.1719C57.75 48.6306 57.1705 50.0295 56.1391 51.061C55.1076 52.0924 53.7087 52.6719 52.25 52.6719H13.75C12.2913 52.6719 10.8924 52.0924 9.86091 51.061C8.82946 50.0295 8.25 48.6306 8.25 47.1719V19.6719Z"
                                stroke="#434343" strokeWidth="4.17311" strokeLinecap="round" strokeLinejoin="round"/>
                            <path d="M8.25 19.6709L33 36.1709L57.75 19.6709" stroke="#434343" strokeWidth="4.17311"
                                  strokeLinecap="round" strokeLinejoin="round"/>
                        </g>
                        <defs>
                            <clipPath id="clip0_825_4078">
                                <rect width="66" height="66" fill="white" transform="translate(0 0.421875)"/>
                            </clipPath>
                        </defs>
                    </svg>
                    hleborob@hello.ru
                </div>
                <button className='absolute right-[33px] top-[33px]' onClick={() => changeVisibleContacts(false)}>
                    <img src={close} alt={'close'}/>
                </button>
            </div>
        </Modal>
    );
};

