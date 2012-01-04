%global packname  drfit
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.05.95
Release:          1%{?dist}
Summary:          Dose-response data evaluation

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.05-95.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-MASS R-RODBC 

BuildRequires:    R-devel tex(latex) R-stats R-MASS R-RODBC 

%description
drfit provides basic and easy-to-use functions for fitting dose-response
curves to dose-response data, calculating some (eco)toxicological
parameters and plotting the results. Functions that are fitted are the
cumulative density function of the lognormal distribution (probit fit), of
the logistic distribution (logit fit), of the weibull distribution
(weibull fit) and a linear-logistic model ("linlogit" fit), derived from
the latter, which is used to describe data showing stimulation at low
doses (hormesis). In addition, functions checking, plotting and retrieving
dose-response data retrieved from a database accessed via RODBC are

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
%doc %{rlibdir}/drfit/html
%doc %{rlibdir}/drfit/DESCRIPTION
%doc %{rlibdir}/drfit/doc
%{rlibdir}/drfit/Meta
%{rlibdir}/drfit/help
%{rlibdir}/drfit/data
%{rlibdir}/drfit/INDEX
%{rlibdir}/drfit/demo
%{rlibdir}/drfit/R
%{rlibdir}/drfit/NAMESPACE

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.05.95-1
- initial package for Fedora