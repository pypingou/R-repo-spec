%global packname  eRm
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.14.0
Release:          1%{?dist}
Summary:          Extended Rasch Modeling.

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.14-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-splines R-methods R-RaschSampler 

BuildRequires:    R-devel tex(latex) R-splines R-methods R-RaschSampler 

%description
eRm fits Rasch models (RM), linear logistic test models (LLTM), rating
scale model (RSM), linear rating scale models (LRSM), partial credit
models (PCM), and linear partial credit models (LPCM). Missing values are
allowed in the data matrix. Additional features are the ML estimation of
the person parameters, Andersen's LR-test, item-specific Wald test,
Martin-Loef-Test, nonparametric Monte-Carlo Tests, itemfit and personfit
statistics including infit and outfit measures, various ICC and related
plots, automated stepwise item elimination, simulation module for various
binary data matrices. An eRm platform is provided at R-forge (see URL).

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
%doc %{rlibdir}/eRm/doc
%doc %{rlibdir}/eRm/html
%doc %{rlibdir}/eRm/DESCRIPTION
%doc %{rlibdir}/eRm/NEWS
%{rlibdir}/eRm/R
%{rlibdir}/eRm/help
%{rlibdir}/eRm/INDEX
%{rlibdir}/eRm/libs
%{rlibdir}/eRm/NAMESPACE
%{rlibdir}/eRm/Meta
%{rlibdir}/eRm/data

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.14.0-1
- initial package for Fedora