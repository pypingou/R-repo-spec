%global packname  mlogitBMA
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Bayesian Model Averaging for Multinomial Logit Models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-BMA R-abind R-maxLik 


BuildRequires:    R-devel tex(latex) R-BMA R-abind R-maxLik



%description
Provides a modified function bic.glm of the BMA package that can be
applied to multinomial logit (MNL) data. The data is converted to binary
logit using the Begg & Gray approximation. The package also contains
functions for maximum likelihood estimation of MNL.

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
%doc %{rlibdir}/mlogitBMA/html
%doc %{rlibdir}/mlogitBMA/DESCRIPTION
%doc %{rlibdir}/mlogitBMA/doc
%{rlibdir}/mlogitBMA/data
%{rlibdir}/mlogitBMA/NAMESPACE
%{rlibdir}/mlogitBMA/R
%{rlibdir}/mlogitBMA/help
%{rlibdir}/mlogitBMA/Meta
%{rlibdir}/mlogitBMA/INDEX

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.3-1
- initial package for Fedora