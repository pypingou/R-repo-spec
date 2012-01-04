%global packname  rqmcmb2
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.2.1
Release:          1%{?dist}
Summary:          Markov Chain Marginal Bootstrap for Quantile Regression

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0.2-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-quantreg 


BuildRequires:    R-devel tex(latex) R-quantreg



%description
Markov Chain Marginal Bootstrap for Quantile Regression. A resampling
method for inference in quantile regression.  Suitable for modest to large
data sets.

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
%doc %{rlibdir}/rqmcmb2/DESCRIPTION
%doc %{rlibdir}/rqmcmb2/html
%{rlibdir}/rqmcmb2/NAMESPACE
%{rlibdir}/rqmcmb2/Meta
%{rlibdir}/rqmcmb2/INDEX
%{rlibdir}/rqmcmb2/R
%{rlibdir}/rqmcmb2/libs
%{rlibdir}/rqmcmb2/help

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2.1-1
- initial package for Fedora