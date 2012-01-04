%global packname  tsDyn
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.7.60
Release:          1%{?dist}
Summary:          Nonlinear time series models with regime switching

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.7-60.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-mgcv R-Matrix R-snow R-mnormt R-foreach R-MASS R-nlme 
Requires:         R-nnet R-tseriesChaos R-tseries R-utils 

BuildRequires:    R-devel tex(latex) R-mgcv R-Matrix R-snow R-mnormt R-foreach R-MASS R-nlme
BuildRequires:    R-nnet R-tseriesChaos R-tseries R-utils 


%description
Implements nonlinear autoregressive (AR) time series models. For
univariate series, a non-parametric approach is available through additive
nonlinear AR. Parametric modeling and testing for regime switching
dynamics is available when the transition is either direct (TAR: threshold
AR) or smooth (STAR: smooth transition AR, LSTAR). For multivariate
series, one can estimate a range of TVAR or threshold cointegration TVECM
models with two or two regimes. Tests can be conducted for TVAR as well as
for TVECM (Hansen and Seo 2002 and Seo 2006).

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
%doc %{rlibdir}/tsDyn/DESCRIPTION
%doc %{rlibdir}/tsDyn/CITATION
%doc %{rlibdir}/tsDyn/doc
%doc %{rlibdir}/tsDyn/html
%{rlibdir}/tsDyn/data
%{rlibdir}/tsDyn/R
%{rlibdir}/tsDyn/NAMESPACE
%{rlibdir}/tsDyn/INDEX
RPM build errors:
%{rlibdir}/tsDyn/ChangeLog
%{rlibdir}/tsDyn/libs
%{rlibdir}/tsDyn/help
%{rlibdir}/tsDyn/Meta

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7.60-1
- initial package for Fedora