%global packname  vars
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.9
Release:          1%{?dist}
Summary:          VAR Modelling

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.4-9.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS R-strucchange R-urca R-lmtest R-sandwich 

BuildRequires:    R-devel tex(latex) R-MASS R-strucchange R-urca R-lmtest R-sandwich 

%description
Estimation, lag selection, diagnostic testing, forecasting, causality
analysis, forecast error variance decomposition and impulse response
functions of VAR models and estimation of SVAR/SVEC models.

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
%changelog
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.9-1
- initial package for Fedora