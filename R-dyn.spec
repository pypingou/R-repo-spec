%global packname  dyn
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.8
Release:          1%{?dist}
Summary:          Time Series Regression

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-8.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-zoo 

BuildRequires:    R-devel tex(latex) R-zoo 

%description
Time series regression.  The dyn class interfaces ts, irts, its, zoo and
zooreg time series classes to lm, glm, loess, quantreg::rq, MASS::rlm,
MCMCpack::MCMCregress, quantreg::rq, randomForest::randomForest and other
regression functions allowing those functions to be used with time series
including specifications that may contain lags, diffs and missing values.

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
%doc %{rlibdir}/dyn/NEWS
%doc %{rlibdir}/dyn/DESCRIPTION
%doc %{rlibdir}/dyn/html
%doc %{rlibdir}/dyn/COPYING
%{rlibdir}/dyn/data
%{rlibdir}/dyn/Meta
%{rlibdir}/dyn/conformance-notes.txt
%{rlibdir}/dyn/THANKS
%{rlibdir}/dyn/WISHLIST
%{rlibdir}/dyn/README
%{rlibdir}/dyn/INDEX
%{rlibdir}/dyn/R
%{rlibdir}/dyn/demo
%{rlibdir}/dyn/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.8-1
- initial package for Fedora