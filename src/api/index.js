/**
 * 与后台交互模块
 */
import ajax from './ajax'
/**
 * 上传图片
 */
const MY_URL='http://49.234.51.41:5000'
export const reqUploadPicture = (formData) => ajax(MY_URL+'/api/picture', formData, 'POST')

/**
 * 上传压缩包
 */
export const reqUploadZip = (formData) => ajax(MY_URL+'/api/zip', formData, 'POST')
