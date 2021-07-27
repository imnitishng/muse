// Create a color map of string tailwind classes to avoid
// deletion by postcss in production build
export const colorsClassMap = {
  '10': 'bg-rankColor-10',
  '20': 'bg-rankColor-20',
  '30': 'bg-rankColor-30',
  '40': 'bg-rankColor-40',
  '50': 'bg-rankColor-50',
  '60': 'bg-rankColor-60',
  '70': 'bg-rankColor-70',
  '80': 'bg-rankColor-80',
  '90': 'bg-rankColor-90',
  '100': 'bg-rankColor-100',
  '110': 'bg-rankColor-110',
  '120': 'bg-rankColor-120',
  '130': 'bg-rankColor-130',
  '140': 'bg-rankColor-140',
  '150': 'bg-rankColor-150',
  '160': 'bg-rankColor-160',
  '170': 'bg-rankColor-170',
  '180': 'bg-rankColor-180',
  '190': 'bg-rankColor-190',
  '200': 'bg-rankColor-200',
}

export const getHost = () => {
  if(process.env.NODE_ENV === 'production')
    return 'http://localhost:1337'
  else
    return 'http://127.0.0.1:8000'
}
