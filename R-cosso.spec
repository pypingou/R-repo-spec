%global packname  cosso
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          COSSO, adaptive COSSO, variable selection for nonparametric smoothing spline models.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-quadprog R-gss 


BuildRequires:    R-devel tex(latex) R-quadprog R-gss



%description
COSSO is the short term for Component Selection and Smoothing Operator. It
is a new regularization method for multivariate function estimation and
component. The COSSO imposes a soft-thresholding penalty operator on
function components in the framework of reproducing kernel Hilbert space
(RKHS) to achieve sparsity. In a sense, the COSSO generalizes the LASSO
(Tibshirani 1996) for variable selection in linear models to nonparametric
regression models. Details about the procedures are given in the papers by
Lin and Zhang (2006) and Zhang and Lin (2006).

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/cosso/html
%doc %{rlibdir}/cosso/DESCRIPTION
%{rlibdir}/cosso/help
%{rlibdir}/cosso/data
%{rlibdir}/cosso/Meta
%{rlibdir}/cosso/R
%{rlibdir}/cosso/INDEX
%{rlibdir}/cosso/NAMESPACE

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora