import s from './Button.module.css';

export default function Button({ variant = 'teal', className = '', loading = false, children, ...props }) {
  const variantClass =
    variant === 'green' ? s.green :
      variant === 'orange' ? s.orange :
        variant === 'aqua' ? s.aqua :
          variant === 'ghost' ? s.ghost :
            s.teal;

  return (
    <button
      {...props}
      className={[s.btn, variantClass, loading ? s.loading : '', className].join(' ')}
      disabled={props.disabled || loading}
    >
      {loading ? (
        <span className={s.spinner} />
      ) : children}
    </button>
  );
}
